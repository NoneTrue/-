@echo off
setlocal
cd /d "%~dp0"
if defined CHANGEVISION_PYTHON (
  "%CHANGEVISION_PYTHON%" -m PyInstaller --noconfirm ChangeVision2026.spec
) else (
  py -3.11 -m PyInstaller --noconfirm ChangeVision2026.spec
)
if errorlevel 1 exit /b 1
if defined CHANGEVISION_PYTHON (
  "%CHANGEVISION_PYTHON%" package_runtime.py dist\ChangeVision2026 --include-otb
) else (
  py -3.11 package_runtime.py dist\ChangeVision2026 --include-otb
)
exit /b %errorlevel%
