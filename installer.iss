#define AppName "ChangeVision2026"
#define AppVersion "2026.09.06"
#define BuildDir "dist\ChangeVision2026"
[Setup]
AppId={{9E9492C0-DA33-41DC-90E5-053DD6FC62BA}
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={autopf}\ChangeVision2026
DefaultGroupName=ChangeVision2026
OutputDir=installer_output
OutputBaseFilename=ChangeVision2026_Setup
SetupIconFile=runtime\icons\ChangeVision2026_HQ.ico
UninstallDisplayIcon={app}\runtime\icons\ChangeVision2026_HQ.ico
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
Compression=lzma2
SolidCompression=yes
[Files]
Source: "{#BuildDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; Flags: unchecked
[Icons]
Name: "{group}\ChangeVision2026"; Filename: "{app}\ChangeVision2026.exe"; WorkingDir: "{app}"; IconFilename: "{app}\runtime\icons\ChangeVision2026_HQ.ico"; AppUserModelID: "ChangeVision2026.Analysis"
Name: "{autodesktop}\ChangeVision2026"; Filename: "{app}\ChangeVision2026.exe"; WorkingDir: "{app}"; IconFilename: "{app}\runtime\icons\ChangeVision2026_HQ.ico"; AppUserModelID: "ChangeVision2026.Analysis"; Tasks: desktopicon
