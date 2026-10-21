#!/usr/bin/env python3
"""
Dual-layer signing pipeline for Huawei Lite Wearable HAPs.
In Huawei LiteOS / HarmonyOS Lite Wearables (Watch Fit 5, Watch GT, Band):
The HAP must have both its inner .bin and the outer .hap signed with the device UDID.
"""

import argparse
import os
import subprocess
import sys
import zipfile


def sign_file(sign_tool, java_exe, in_file, out_file, cert_file, keystore_file, profile_file, keystore_pwd, in_form="zip"):
    cmd = [
        java_exe, "-jar", sign_tool, "sign-app",
        "-mode", "localSign",
        "-keyAlias", "debugKey",
        "-keyPwd", keystore_pwd,
        "-appCertFile", cert_file,
        "-profileFile", profile_file,
        "-profileSigned", "1",
        "-inFile", in_file,
        "-signAlg", "SHA256withECDSA",
        "-keystoreFile", keystore_file,
        "-keystorePwd", keystore_pwd,
        "-outFile", out_file,
        "-inForm", in_form
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error signing {in_file}:", file=sys.stderr)
        print(res.stdout, file=sys.stderr)
        print(res.stderr, file=sys.stderr)
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Dual-sign Huawei Lite Wearable HAP")
    parser.add_argument("--project-dir", required=True, help="Root directory of the watch project")
    parser.add_argument("--profile", required=True, help="Path to auto_debug_*.p7b provision profile")
    parser.add_argument("--cert", required=True, help="Path to .cer certificate file")
    parser.add_argument("--keystore", required=True, help="Path to .p12 keystore file")
    parser.add_argument("--password", required=True, help="Keystore / key password")
    parser.add_argument("--watch-udid", default="", help="Optional watch UDID to verify in signature")
    parser.add_argument("--output", default="", help="Path for the final signed HAP")
    parser.add_argument("--studio-path", default=r"C:\Program Files\Huawei\DevEco Studio", help="DevEco Studio installation path")

    args = parser.parse_args()

    base_out = os.path.join(args.project_dir, "entry", "build", "default", "outputs", "default")
    bin_unsigned = os.path.join(base_out, "bin", "entry-default-unsigned.bin")
    bin_signed = os.path.join(base_out, "bin", "entry-default-signed.bin")
    temp_hap = os.path.join(base_out, "temp_unsigned.hap")
    final_hap = args.output if args.output else os.path.join(base_out, "final_signed.hap")

    sign_tool = os.path.join(args.studio_path, "sdk", "default", "openharmony", "toolchains", "lib", "hap-sign-tool.jar")
    java_exe = os.path.join(args.studio_path, "jbr", "bin", "java.exe")

    if not os.path.exists(bin_unsigned):
        print(f"Error: Unsigned inner bin not found at: {bin_unsigned}", file=sys.stderr)
        sys.exit(1)

    print(">>> 1/3: Signing inner bin...")
    if not sign_file(sign_tool, java_exe, bin_unsigned, bin_signed, args.cert, args.keystore, args.profile, args.password, in_form="bin"):
        sys.exit(1)

    print(">>> 2/3: Packaging inner bin into HAP archive...")
    if os.path.exists(temp_hap):
        os.remove(temp_hap)
    with zipfile.ZipFile(temp_hap, 'w', zipfile.ZIP_STORED) as z:
        z.write(bin_signed, "entry-default-signed.bin")

    print(f">>> 3/3: Signing outer HAP -> {final_hap}...")
    if os.path.exists(final_hap):
        os.remove(final_hap)
    if not sign_file(sign_tool, java_exe, temp_hap, final_hap, args.cert, args.keystore, args.profile, args.password, in_form="zip"):
        sys.exit(1)

    print(f">>> Signing complete! Final HAP: {final_hap} ({os.path.getsize(final_hap)} bytes)")

    if args.watch_udid:
        udid_bytes = args.watch_udid.strip().encode("utf-8")
        with open(final_hap, "rb") as f:
            outer_data = f.read()
        with zipfile.ZipFile(final_hap, "r") as z:
            inner_data = z.read("entry-default-signed.bin")

        in_outer = udid_bytes in outer_data
        in_inner = udid_bytes in inner_data
        print(f">>> UDID Verification ({args.watch_udid}):")
        print(f"    - Included in outer HAP: {in_outer}")
        print(f"    - Included in inner BIN: {in_inner}")
        if not (in_outer and in_inner):
            print("WARNING: UDID was not found in both signature blocks! App may fail to install on watch.", file=sys.stderr)
            sys.exit(2)


if __name__ == "__main__":
    main()
