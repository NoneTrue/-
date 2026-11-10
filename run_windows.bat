@echo off
setlocal
cd /d "%~dp0"
if defined CHANGEVISION_PYTHON (
  "%CHANGEVISION_PYTHON%" main.py
) else (
  py -3.11 -c "import sys; assert sys.version_info[:3] == (3, 11, 9)" >nul 2>&1
  if errorlevel 1 (
    python -c "import sys; assert sys.version_info[:3] == (3, 11, 9)" >nul 2>&1
    if errorlevel 1 (
      echo Python 3.11 is required. Set CHANGEVISION_PYTHON to its executable.
      pause
      exit /b 1
    )
    python main.py
  ) else (
    py -3.11 main.py
  )
)
if errorlevel 1 pause
