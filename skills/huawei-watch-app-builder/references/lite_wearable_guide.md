# Huawei Lite Wearable (LiteOS / HarmonyOS) Development Guide

This guide compiles essential architectural rules, UI component behaviors, and critical touch/gesture patterns for developing lightweight watch applications on devices such as **HUAWEI WATCH FIT 5**, **HUAWEI WATCH FIT 3/4**, and **HUAWEI WATCH GT**.

---

## 1. Hardware & Resolution Profile
- **Target Architecture**: `liteWearable` (OpenHarmony JS UI runtime on LiteOS).
- **Display Resolution**: 408 × 480 px (AMOLED rectangular).
- **Design Width in config.json**: `"designWidth": 408`.
- **Primary Input Channels**:
  - Capacitive multi-touch screen.
  - Screen edge swipe gestures (left/right/up/down).
  - Physical rotating digital crown (hardware rotary encoder).
  - PPG / Accelerometer / Gyroscope / Wear-detection sensors.

---

## 2. Touch & Gesture Best Practices (Critical Pitfalls)

### A. Click Event Dispatching (`onclick`)
- **NEVER put `onclick` on `<list-item>`**: In LiteOS C++ engine, `UIListItem` consumes touches for list velocity physics and drops JS click events. Clicks on `<list-item>` are completely ignored.
- **NEVER put `onclick` on standalone `<text>`**: Text elements have minimal bounding boxes, miss clicks near rounded bezels, and frequently drop events.
- **ALWAYS wrap clickable areas in `<div onclick="...">`**:
  ```html
  <!-- CORRECT -->
  <div class="card-btn" onclick="onSelect">
    <text class="btn-text">确定</text>
  </div>
  ```
- **Minimum Touch Target**: Maintain at least `80px × 40px` (or `44px` height) with padding `8px-12px` to guarantee easy finger activation.

### B. Lists vs. Swiper (Crown & Scroll Reliability)
- **Why `<list>` frequently freezes**:
  - In LiteOS flex layout, if a `<list>` height combined with headers exceeds 480px, the scrollable range evaluates to 0.
  - LiteOS `<list-item>` does **NOT** support CSS `margin` or `padding`. Adding margins corrupts item offset calculations.
  - Digital crown focus (`list.focus()`) is fragile and easily lost.
- **Why `<swiper vertical="true">` is the recommended standard**:
  - Full-screen or paginated cards glide smoothly with zero scroll-trap issues.
  - **Native Rotary Crown Support**: LiteOS `<swiper>` automatically responds to crown turns, advancing pages with tactile detents.
  - Structure:
    ```html
    <swiper class="main-swiper" vertical="true" index="{{pageIndex}}" onchange="onSwiperChange">
      <div class="card">...</div>
      <div class="card">...</div>
    </swiper>
    ```

### C. Edge Swipes & Exiting (`onswipe`)
- Huawei watches rely on edge swipes for navigation. If not handled, users can get trapped inside the application.
- Bind `onswipe="handleSwipe"` on the root container (`<stack>` or `<div>`):
  ```javascript
  handleSwipe(e) {
    if (e && e.direction === 'right') {
      // Subpage -> Return to previous screen
      router.back();
    }
  }
  ```
  On the **root/main page**:
  ```javascript
  handleSwipe(e) {
    if (e && (e.direction === 'right' || e.direction === 'left')) {
      // Main page -> Cleanly exit back to watch face
      app.terminate();
    }
  }
  ```

---

## 3. CSS Style Engine Restrictions
LiteOS uses a compact CSS parser. Unsupported attributes will trigger compiler warnings or layout clipping:
- **Do NOT use**: `font-weight`, `line-height`, `box-shadow`, `calc()`, `margin` on `<list-item>`.
- **Typography**: Size fonts strictly using `font-size: 20px;` (large), `font-size: 28px;` (titles), `font-size: 16px;` (hints).
- **Colors**: Use 6-character hex (`#101114`, `#e6a23c`, `#22c55e`). Avoid named web colors.

---

## 4. Hardware Sensors & System Services

### A. Wear Detection (`@system.sensor`)
```javascript
import sensor from '@system.sensor';

sensor.subscribeOnBodyState({
  success: function(ret) {
    // ret.value === true (on wrist) / false (removed)
    console.info('On-body state: ' + ret.value);
  }
});
```

### B. Haptic Feedback (`@system.vibrator`)
Always pair major user touches and crown changes with haptic feedback:
```javascript
import vibrator from '@system.vibrator';

vibrator.vibrate({ mode: 'short' }); // short (button tick) or 'long' (alert)
```

### C. Persistent Storage (`@system.storage`)
```javascript
import storage from '@system.storage';

storage.get({
  key: 'my_app_state',
  default: '',
  success: (data) => { /* JSON.parse(data) */ }
});
```
