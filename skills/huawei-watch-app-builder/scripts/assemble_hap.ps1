# Assemble an unsigned OpenHarmony / HarmonyOS Lite Wearable HAP via CLI
param(
  [string]$ProjectPath = ".",
  [string]$StudioPath = "C:\Program Files\Huawei\DevEco Studio"
)

$ErrorActionPreference = "Stop"
$ResolvedProject = Resolve-Path $ProjectPath
Set-Location $ResolvedProject

Write-Host ">>> Building Lite Wearable HAP in: $ResolvedProject"

# Set DevEco build toolchain paths
$env:JAVA_HOME = Join-Path $StudioPath "jbr"
$env:DEVECO_SDK_HOME = Join-Path $StudioPath "sdk"
$env:NODE_HOME = Join-Path $StudioPath "tools\node"
$env:Path = "$(Join-Path $env:JAVA_HOME 'bin');$env:NODE_HOME;$(Join-Path $StudioPath 'tools\ohpm\bin');$(Join-Path $StudioPath 'tools\hvigor\bin');$env:Path"

if (-not (Test-Path "local.properties")) {
  "sdk.dir=$($env:DEVECO_SDK_HOME -replace '\\', '\\')" | Set-Content local.properties -Encoding ASCII
}

# Install dependencies if oh-package.json5 exists
if (Test-Path "oh-package.json5") {
  Write-Host ">>> Running ohpm install..."
  & (Join-Path $StudioPath "tools\ohpm\bin\ohpm.bat") install --all
  if ($LASTEXITCODE -ne 0) { throw "ohpm install failed" }
}

# Run hvigor assembleHap
Write-Host ">>> Running hvigorw assembleHap..."
& (Join-Path $StudioPath "tools\hvigor\bin\hvigorw.bat") --mode module -p product=default -p buildMode=debug assembleHap --no-daemon
if ($LASTEXITCODE -ne 0) { throw "hvigor assembleHap failed" }

$unsignedHap = Join-Path $ResolvedProject "entry\build\default\outputs\default\entry-default-unsigned.hap"
if (-not (Test-Path $unsignedHap)) {
  throw "Build finished but unsigned HAP not found at: $unsignedHap"
}

$hapItem = Get-Item $unsignedHap
Write-Host ">>> Build successful! Output: $($hapItem.FullName) ($($hapItem.Length) bytes)"
