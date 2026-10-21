# Huawei Watch App Builder Skill

A production-ready skill and automation pipeline for building, dual-layer signing, and sideloading applications on **HUAWEI WATCH FIT 5**, **HUAWEI WATCH FIT 3/4**, and **HUAWEI WATCH GT** series running OpenHarmony / HarmonyOS LiteOS.

## What's Included
- `SKILL.md`: Main instructions and rules for AI agents and developers.
- `scripts/assemble_hap.ps1`: Headless CLI compilation using DevEco Studio SDK and Hvigor.
- `scripts/package_and_sign.py`: Automated dual-layer signing of inner `.bin` and outer `.hap` with Watch UDID verification.
- `scripts/sideload_hap.py`: ADB-driven wireless sideloading pipeline via connected phone and DevEco Assistant.
- `scripts/keep_phone_awake.py`: Keep-awake daemon to prevent Bluetooth connection drops during sideloading.
- `references/lite_wearable_guide.md`: Touch event bubbling rules, crown navigation, and CSS restrictions.
- `references/signing_and_provisioning.md`: Provisioning profile, keystore, and UDID setup.
- `references/troubleshooting.md`: Solutions for common errors (Error 105, Hvigor crashes, gesture traps).
- `templates/config.json`: Standardized Lite Wearable module manifest.

## Usage
Refer to `SKILL.md` for step-by-step instructions.
