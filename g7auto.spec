# -*- mode: python ; coding: utf-8 -*-

import sys
from kivy_deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal,hookspath
from PyInstaller.utils.hooks import collect_submodules
cwd = os.getcwd().replace("\\", "/")
ver = f"{sys.version_info.major}.{sys.version_info.minor}"

block_cipher = None

excludekivy = get_deps_minimal(video=None, audio=None,spelling=None,camera=None)['excludes']

data = [(f'{cwd}/g7auto/data/bg.png', 'data'),
        (f'{cwd}/g7auto/data/chromedriver.exe', '.')
       ]

a = Analysis([f'{cwd}/g7auto/g7ui.py'],
            pathex=[f'{cwd}/g7auto/'],
            binaries=[],
            datas=data,
            hiddenimports=['six','packaging','packaging.version','packaging.specifiers','configparser'], #collect_submodules('kivy.garden'),
            hookspath=[],
            runtime_hooks=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            excludes = excludekivy,
	    noarchive=False)

    
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)


exe = EXE(pyz,Tree(f'{cwd}/g7auto/'),
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        icon='icon.ico',
        name='G7Auto',
        debug=False,
        strip=False,
        upx=True,
        console=False )

	
coll = COLLECT(exe, Tree(f'{cwd}/g7auto/'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='G7Autop')