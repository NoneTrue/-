from pathlib import Path
import sys,json
if sys.version_info[:3] != (3,11,9):
    raise SystemExit('Build requires Python 3.11.9 exactly; no other interpreter is allowed.')
from PyInstaller.utils.hooks import collect_data_files,collect_dynamic_libs,collect_submodules
root=Path(SPECPATH)
datas=[];binaries=[];hidden=[]
for package in ('rasterio','pyproj'):
    datas+=collect_data_files(package)
    binaries+=collect_dynamic_libs(package)
hidden+=collect_submodules('rasterio',filter=lambda name: '.tests' not in name)
icon=root/'runtime'/'icons'/'ChangeVision2026_HQ.ico'
a=Analysis([str(root/'main.py')],pathex=[str(root)],binaries=binaries,datas=datas,
           hiddenimports=hidden+['runtime_diagnostics'],hookspath=[],runtime_hooks=[],
           excludes=['torch','kornia','kornia_rs','ultralytics','arcpy','qgis','osgeo','PyQt5','PyQt6','PySide2',
                     'pandas','matplotlib','IPython','notebook','numba','xarray','dask','distributed',
                     'bokeh','plotly','sympy','pygame'],noarchive=False)
base=Path(sys.base_prefix).resolve();site=base/'Lib'/'site-packages'
approved={}
for folder in [site/'PySide6',site/'rasterio.libs',site/'pyproj.libs',site/'shapely.libs',
               site/'numpy.libs',site/'scipy.libs',base/'DLLs',base]:
    for p in folder.glob('*.dll'):approved.setdefault(p.name.lower(),p)
filtered=[];changes=[]
for dest,source,kind in a.binaries:
    p=Path(source).resolve()
    if not p.is_relative_to(base):
        replacement=approved.get(p.name.lower())
        changes.append(dict(destination=dest,external_source=str(p),replacement=str(replacement) if replacement else None))
        if replacement:filtered.append((dest,str(replacement),kind))
    else:filtered.append((dest,source,kind))
a.binaries=filtered
(root/'validation'/'build_dependency_resolution_upgrade.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,[],exclude_binaries=True,name='ChangeVision2026_Upgrade',debug=False,
        bootloader_ignore_signals=False,strip=False,upx=False,console=False,
        icon=str(icon) if icon.is_file() else None)
COLLECT(exe,a.binaries,a.datas,strip=False,upx=False,name='ChangeVision2026_Upgrade')
