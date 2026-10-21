---
name: huawei-watch-app-builder
description: >-
  Complete development, UI/UX architecture, dual-layer signing, and automated wireless
  sideloading workflow for Huawei Lite Wearables (HUAWEI WATCH FIT 5, FIT 3/4, WATCH GT series).
  Use when the user asks to create, modify, fix touch/scroll/gesture bugs, compile, sign, or install
  watch applications (HAPs) on a Huawei smart watch.
---

# Huawei Watch App Builder (Lite Wearables)

## Overview
This skill provides an end-to-end engineering guide, automated toolchain, and troubleshooting runbook for creating, refactoring, dual-layer signing, and sideloading Lite Wearable applications (`liteWearable`) on Huawei smart watches (such as **HUAWEI WATCH FIT 5**, **FIT 3/4**, and **WATCH GT** series).

---

## Quick Reference & Tool Index

| Script / Reference | Purpose |
| :--- | :--- |
| [`scripts/assemble_hap.ps1`](./scripts/assemble_hap.ps1) | CLI compilation of unsigned `.hap` without launching DevEco Studio GUI. |
| [`scripts/package_and_sign.py`](./scripts/package_and_sign.py) | Dual-layer signing tool (signs inner `.bin` + outer `.hap` with Watch UDID). |
| [`scripts/sideload_hap.py`](./scripts/sideload_hap.py) | ADB push to paired phone + automated installation via DevEco Assistant. |
| [`scripts/keep_phone_awake.py`](./scripts/keep_phone_awake.py) | Daemon to prevent phone screen sleep during Bluetooth transfer. |
| [`references/lite_wearable_guide.md`](./references/lite_wearable_guide.md) | Component behaviors, touch/click rules, rotary crown mechanics. |
| [`references/signing_and_provisioning.md`](./references/signing_and_provisioning.md) | In-depth AGC provision profiles, keystores, and certificate setup. |
| [`references/troubleshooting.md`](./references/troubleshooting.md) | Solutions for Error 105, Hvigor TypeError, scroll freezing, and gesture lock. |

---

## 4 Golden Rules for Watch UI/UX Design

1. **Click Events**:
   - **Never** attach `onclick` to `<list-item>` or raw `<text>`. The LiteOS engine consumes item touches for list physics and drops click events.
   - **Always** attach `onclick` to a container `<div>` with explicit dimensions (`width ≥ 80px`, `height ≥ 40px`).

2. **Rotary Crown & Vertical Scrolling**:
   - **Prefer `<swiper vertical="true">` over `<list>`**.
   - `<swiper vertical="true">` natively responds to the physical rotating crown and finger swipe gestures with zero configuration, whereas `<list>` frequently freezes due to layout overflow or unsupported margin attributes.

3. **Edge Gestures (`onswipe`)**:
   - The root element on every page must be `<stack class="container" onswipe="handleSwipe">`.
   - On the main screen: `e.direction === 'right' || e.direction === 'left'` calls `app.terminate()` to exit.
   - On subpages: `e.direction === 'right'` calls `router.back()`.

4. **Screen Constraints**:
   - Target layout: 408 × 480 px.
   - Avoid unsupported CSS attributes like `font-weight`, `line-height`, `box-shadow`, or margins on `<list-item>`.

---

## Step-by-Step Production Workflow

### Step 1: Scaffold & Implement
- Configure `entry/src/main/config.json`:
  - `deviceType`: `["liteWearable"]`
  - `window.designWidth`: `408`
  - Required permissions: `ohos.permission.ACCELEROMETER`, `ohos.permission.VIBRATE`
- Place the primary entry page as the first item in the `"pages"` array to prevent redirect flashes or empty back-stacks.

### Step 2: Build Unsigned HAP (CLI)
Run the automated build script in PowerShell:
```powershell
& "scripts/assemble_hap.ps1" -ProjectPath "c:\Apps\MyWatchApp"
```

### Step 3: Dual-Layer Signature
Lite Wearables require **both** the inner compiled binary (`entry-default-signed.bin`) and the outer archive (`final_signed.hap`) to be signed with a profile containing the target watch's UDID:
```bash
python scripts/package_and_sign.py \
  --project-dir "c:\Apps\MyWatchApp" \
  --profile "C:\Users\<User>\.ohos\config\auto_debug_<bundle>_watch.p7b" \
  --cert "C:\Users\<User>\.ohos\config\<name>.cer" \
  --keystore "C:\Users\<User>\.ohos\config\<name>.p12" \
  --password "<password>" \
  --watch-udid "<WATCH_UDID_HEX>" \
  --output "c:\Apps\MyWatchApp\entry\build\default\outputs\default\final_signed.hap"
```

### Step 4: Wireless Sideload via Phone ADB
1. Ensure the keep-awake daemon is active:
   ```bash
   python scripts/keep_phone_awake.py
   ```
2. Push and install via DevEco Assistant:
   ```bash
   python scripts/sideload_hap.py \
     --hap "c:\Apps\MyWatchApp\entry\build\default\outputs\default\final_signed.hap" \
     --target-name "my-watch-app.hap" \
     --auto-install
   ```
3. Monitor logcat for `get hap file progress` and watch installation confirmation (`errorCode: 0`).
