#!/usr/bin/env python3
"""
Lightweight keep-awake daemon for connected phone via ADB.
Prevents the phone screen from sleeping so that Bluetooth transfers
to the paired Huawei Watch are not throttled or disconnected.
"""

import subprocess
import time
import sys


def main():
    adb = r"C:\Apps\platform-tools\adb.exe"
    print(">>> Starting ADB phone keep-awake daemon (pings every 25s)...")
    while True:
        try:
            # Send wake key if screen is off, or send keyevent to reset screen timer
            subprocess.run([adb, "shell", "input", "keyevent", "KEYCODE_WAKEUP"], capture_output=True)
            subprocess.run([adb, "shell", "svc", "power", "stayon", "usb"], capture_output=True)
        except Exception as e:
            print(f"keep-awake exception: {e}", file=sys.stderr)
        time.sleep(25)


if __name__ == "__main__":
    main()
