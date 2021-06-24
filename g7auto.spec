# -*- mode: python ; coding: utf-8 -*-
import sys
import platform

block_cipher = None
cwd = os.getcwd().replace("\\", "/")
ver = f"{sys.version_info.major}.{sys.version_info.minor}"


a = Analysis([f'{cwd}/g7auto/g7ui.py'],
             pathex=[f'{cwd}/src', cwd],
             binaries=[],
             datas=[],
             hiddenimports=[''],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='g7auto',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )