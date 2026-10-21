# Huawei Lite Wearable Dual-Layer Signing & Provisioning Guide

## Why Dual-Layer Signing is Required
For standard HarmonyOS phone/tablet apps, signing the outer `.hap` archive is sufficient. However, for **OpenHarmony Lite Wearable devices** (such as HUAWEI WATCH FIT 5, GT series), the firmware runtime expects a **dual-layer signature**:

1. **Inner Binary (`entry-default-signed.bin`)**: The compiled LiteOS JS bytecode bundle. It must be signed using `hap-sign-tool.jar` in `inForm=bin` mode.
2. **Outer Package (`final_signed.hap`)**: A ZIP archive containing the signed binary, profile, and assets. It must be signed in `inForm=zip` mode.

If either layer is unsigned or signed with a profile that lacks the watch UDID, the watch installer rejects the package with error codes (e.g., signature verification failed or signature mismatch).

---

## Required Provisioning Assets
All files typically reside under `C:\Users\<User>\.ohos\config\`:

1. **Keystore (`.p12`)**: Contains the private development signing key (e.g. `fit5-water_...p12`).
2. **Certificate (`.cer`)**: Development certificate corresponding to the key.
3. **Provision Profile (`.p7b`)**: AGC debug profile (`auto_debug_<bundleName>_watch.p7b`).
   - **CRITICAL**: The profile's `device-list` MUST contain the **Watch UDID** (64-character hex string).
   - Finding Watch UDID: On the watch, go to **Settings > About > Device Info**, or check via paired phone Health app / DevEco Assistant.

---

## Dual-Signing Command Sequence

### Step 1: Sign the Inner `.bin`
```bash
java -jar "hap-sign-tool.jar" sign-app \
  -mode localSign \
  -keyAlias debugKey \
  -keyPwd <password> \
  -appCertFile <path_to_cer> \
  -profileFile <path_to_p7b> \
  -profileSigned 1 \
  -inFile "entry/build/default/outputs/default/bin/entry-default-unsigned.bin" \
  -signAlg SHA256withECDSA \
  -keystoreFile <path_to_p12> \
  -keystorePwd <password> \
  -outFile "entry/build/default/outputs/default/bin/entry-default-signed.bin" \
  -inForm bin
```

### Step 2: Package into Stored ZIP
Package `entry-default-signed.bin` into `temp_unsigned.hap` with `ZIP_STORED` (no compression).

### Step 3: Sign the Outer `.hap`
```bash
java -jar "hap-sign-tool.jar" sign-app \
  -mode localSign \
  -keyAlias debugKey \
  -keyPwd <password> \
  -appCertFile <path_to_cer> \
  -profileFile <path_to_p7b> \
  -profileSigned 1 \
  -inFile "temp_unsigned.hap" \
  -signAlg SHA256withECDSA \
  -keystoreFile <path_to_p12> \
  -keystorePwd <password> \
  -outFile "final_signed.hap"
```

### Step 4: Binary Verification
Inspect both the outer HAP bytes and inner binary bytes to ensure the target device UDID string is physically present in both certificate chains.
