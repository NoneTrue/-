#define AppName "ChangeVision2026 Upgrade Final"
#define AppVersion "2026.11.07"
#define BuildDir "dist\ChangeVision2026_Upgrade_Final"
[Setup]
AppId={{12A0784D-913B-4A53-9290-0CDAE61BD81E}
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={%LOCALAPPDATA}\Programs\ChangeVision2026_Upgrade_Final
DefaultGroupName={#AppName}
OutputDir=installer_output
OutputBaseFilename=ChangeVision2026_Upgrade_Final_Setup
SetupIconFile=runtime\icons\ChangeVision2026_HQ.ico
UninstallDisplayIcon={app}\runtime\icons\ChangeVision2026_HQ.ico
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
[Files]
Source: "{#BuildDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; Flags: unchecked
[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\ChangeVision2026_Upgrade_Final.exe"; WorkingDir: "{app}"; IconFilename: "{app}\runtime\icons\ChangeVision2026_HQ.ico"; AppUserModelID: "ChangeVision2026.Analysis"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\ChangeVision2026_Upgrade_Final.exe"; WorkingDir: "{app}"; IconFilename: "{app}\runtime\icons\ChangeVision2026_HQ.ico"; AppUserModelID: "ChangeVision2026.Analysis"; Tasks: desktopicon
