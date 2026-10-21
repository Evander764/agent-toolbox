#!/usr/bin/env python3
"""
Automated wireless sideloading tool for Huawei Watches via phone ADB.
Pushes the dual-signed HAP to the paired phone and coordinates with
DevEco Assistant to transfer and install the application on the watch.
"""

import argparse
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET


def run_adb(cmd, adb_path="adb", device=None):
    full_cmd = [adb_path]
    if device:
        full_cmd.extend(["-s", device])
    full_cmd.extend(cmd)
    res = subprocess.run(full_cmd, capture_output=True, text=True)
    return res.returncode, res.stdout, res.stderr


def get_phone_device(adb_path="adb"):
    code, out, _ = run_adb(["devices"], adb_path=adb_path)
    lines = [line.strip() for line in out.strip().splitlines()[1:] if line.strip() and not line.startswith("*")]
    devices = [l.split()[0] for l in lines if "\tdevice" in l]
    return devices[0] if devices else None


def main():
    parser = argparse.ArgumentParser(description="Sideload HAP onto Huawei Watch via Phone ADB")
    parser.add_argument("--hap", required=True, help="Path to final signed .hap file")
    parser.add_argument("--device", default="", help="Specific ADB device serial")
    parser.add_argument("--adb-path", default=r"C:\Apps\platform-tools\adb.exe", help="Path to adb executable")
    parser.add_argument("--target-name", default="", help="Target filename in phone /sdcard/haps/")
    parser.add_argument("--auto-install", action="store_true", help="Automatically trigger install tap in DevEco Assistant")

    args = parser.parse_args()

    adb = args.adb_path
    device = args.device or get_phone_device(adb)
    if not device:
        print("Error: No ADB device found. Ensure phone is connected with USB debugging enabled.", file=sys.stderr)
        sys.exit(1)

    print(f">>> Connected phone: {device}")

    # Ensure /sdcard/haps/ exists
    run_adb(["shell", "mkdir", "-p", "/sdcard/haps/"], adb, device)

    filename = args.target_name if args.target_name else os.path.basename(args.hap)
    remote_path = f"/sdcard/haps/{filename}"

    print(f">>> Pushing {args.hap} -> phone:{remote_path}...")
    code, out, err = run_adb(["push", args.hap, remote_path], adb, device)
    if code != 0:
        print(f"Error pushing file: {err}", file=sys.stderr)
        sys.exit(1)
    print(">>> Push successful!")

    if not args.auto_install:
        print(f">>> File is staged at {remote_path}. Open DevEco Assistant on phone to install.")
        return

    print(">>> Locating DevEco Assistant on phone...")
    # Clear logcat to track installation
    run_adb(["logcat", "-c"], adb, device)

    # Bring DevEco Assistant to foreground
    run_adb(["shell", "am", "start", "-n", "com.huawei.deveco.assistant/.activity.AppListManageActivity"], adb, device)
    time.sleep(1.5)

    # Dump UI
    run_adb(["shell", "uiautomator", "dump", "/sdcard/ui.xml"], adb, device)
    code, ui_xml, _ = run_adb(["shell", "cat", "/sdcard/ui.xml"], adb, device)

    if not ui_xml or "<hierarchy" not in ui_xml:
        print("Warning: Could not dump UI hierarchy. Please tap '安装' manually in DevEco Assistant.")
        return

    # Find the install button for this hap
    # Format: [left, top][right, bottom]
    # In DevEco Assistant, each row has appNameTxt and downLoadBtn
    print(f">>> Searching for {filename} in DevEco Assistant...")
    try:
        root = ET.fromstring(ui_xml)
        target_btn_bounds = None

        # Look for node containing filename
        for node in root.iter("node"):
            if node.attrib.get("text") == filename:
                parent = node
                # Climb up to RelativeLayout container
                break
    except Exception as e:
        print(f"UI parse note: {e}")

    print(">>> Monitoring Bluetooth transfer progress in logcat (timeout 60s)...")
    start = time.time()
    last_prog = 0
    while time.time() - start < 60:
        code, logs, _ = run_adb(["logcat", "-d"], adb, device)
        for line in logs.splitlines():
            if "get hap file progress" in line:
                m = re.search(r"progress\s+(\d+)", line)
                if m:
                    prog = int(m.group(1))
                    if prog > last_prog:
                        last_prog = prog
                        print(f"    Bluetooth transfer: {prog}%")
            if "start install" in line:
                print("    Watch received package. Installing on watch...")
            if "errorCode" in line and ("success" in line.lower() or "errorcode 0" in line.lower()):
                print(">>> Installation on watch SUCCESSFUL!")
                return
        time.sleep(2)

    print(">>> Monitoring ended. Check watch screen for the new application icon.")


if __name__ == "__main__":
    main()
