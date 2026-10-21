# Huawei Lite Wearable Development Troubleshooting

### 1. `c.getHosSdkVersion().getApiVersion() is not a function` in Hvigor
- **Symptom**: DevEco Studio / Hvigor fails during project task service initialization with `TypeError: c.getHosSdkVersion().getApiVersion() is not a function`.
- **Root Cause**: `hvigor-ohos-plugin` expects a HarmonyOS phone SDK structure when `DEVECO_SDK_HOME` is set, but OpenHarmony SDK only contains `openharmony` instead of `hms`.
- **Fix**: In `C:\Program Files\Huawei\DevEco Studio\tools\hvigor\hvigor-ohos-plugin\src\tasks\service\project-task-service.js`, patch the version extraction check:
  ```javascript
  const hosVer = (c && c.getHosSdkVersion && typeof c.getHosSdkVersion().getApiVersion === 'function') 
    ? c.getHosSdkVersion().getApiVersion() 
    : (c.getOhosSdkVersion ? c.getOhosSdkVersion().getApiVersion() : 23);
  ```

---

### 2. Sideload Error Code 105 (`SIGNATURE_MISMATCH` / `NO_MATCHING_DEVICE`)
- **Symptom**: DevEco Assistant reports `errorCode 105` or installation fails immediately upon receiving the package.
- **Root Cause**:
  1. The inner binary was left unsigned or signed with a profile that only listed the phone's UDID, not the watch's UDID.
  2. The watch UDID was omitted during automatic AGC signing in DevEco Studio.
- **Fix**: Re-generate the `.p7b` provision profile in DevEco Studio or AGC with both phone UDID and Watch UDID, and run the dual-layer `package_and_sign.py` script.

---

### 3. Bluetooth Transfer Stalls at 0% or Disconnects
- **Symptom**: DevEco Assistant logs show `get hap file progress` stopping halfway or phone screen locks and drops Bluetooth connection.
- **Fix**:
  - Run the `keep_phone_awake.py` daemon via ADB to keep the phone screen active during transmission:
    ```bash
    python keep_phone_awake.py
    ```
  - Ensure Huawei Health / DevEco Assistant has "Battery Optimization: Unrestricted" enabled.

---

### 4. Trapped in App / Back Swipe Ineffective
- **Symptom**: Swiping right on the watch does nothing, or application cannot be exited.
- **Root Cause**: `router.replace` cleared the root page from the navigation stack, and the top-level container did not implement `onswipe`.
- **Fix**:
  1. Avoid using `router.replace` on initial launch; place the main entry screen as the first item in `config.json` `"pages"`.
  2. Attach `onswipe="handleSwipe"` on `<stack>` and call `app.terminate()` on horizontal swipes on the main page.
