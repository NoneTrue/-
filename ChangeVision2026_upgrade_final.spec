from pathlib import Path
import sys, json

if sys.version_info[:3] != (3, 11, 9):
    raise SystemExit('Build requires Python 3.11.9 exactly; no other interpreter is allowed.')

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules

root = Path(SPECPATH)
datas = []
binaries = []
hidden = []
for package in ('rasterio', 'pyproj'):
    datas += collect_data_files(package)
    binaries += collect_dynamic_libs(package)
hidden += collect_submodules('rasterio', filter=lambda name: '.tests' not in name)
hidden += ['runtime_diagnostics', 'image_location']
icon = root / 'runtime' / 'icons' / 'ChangeVision2026_HQ.ico'
analysis = Analysis(
    [str(root / 'main.py')], pathex=[str(root)], binaries=binaries, datas=datas,
    hiddenimports=hidden, hookspath=[], runtime_hooks=[],
    excludes=['torch', 'kornia', 'kornia_rs', 'ultralytics', 'arcpy', 'qgis', 'osgeo',
              'PyQt5', 'PyQt6', 'PySide2', 'pandas', 'matplotlib', 'IPython',
              'notebook', 'numba', 'xarray', 'dask', 'distributed', 'bokeh',
              'plotly', 'sympy', 'pygame'], noarchive=False)

base = Path(sys.base_prefix).resolve()
site = base / 'Lib' / 'site-packages'
approved = {}
for folder in [site / 'PySide6', site / 'rasterio.libs', site / 'pyproj.libs',
               site / 'shapely.libs', site / 'numpy.libs', site / 'scipy.libs',
               base / 'DLLs', base]:
    for path in folder.glob('*.dll'):
        approved.setdefault(path.name.lower(), path)
filtered = []
changes = []
for destination, source, kind in analysis.binaries:
    path = Path(source).resolve()
    if not path.is_relative_to(base):
        replacement = approved.get(path.name.lower())
        changes.append(dict(destination=destination, external_source=str(path),
                            replacement=str(replacement) if replacement else None))
        if replacement:
            filtered.append((destination, str(replacement), kind))
    else:
        filtered.append((destination, source, kind))
analysis.binaries = filtered
(root / 'validation' / 'build_dependency_resolution_final.json').write_text(
    json.dumps(changes, indent=2), encoding='utf-8')

pyz = PYZ(analysis.pure)
exe = EXE(pyz, analysis.scripts, [], exclude_binaries=True,
          name='ChangeVision2026_Upgrade_Final', debug=False,
          bootloader_ignore_signals=False, strip=False, upx=False, console=False,
          icon=str(icon) if icon.is_file() else None)
COLLECT(exe, analysis.binaries, analysis.datas, strip=False, upx=False,
        name='ChangeVision2026_Upgrade_Final')
