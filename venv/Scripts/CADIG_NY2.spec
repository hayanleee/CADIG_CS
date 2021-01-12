# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Python\\NY_pyside2\\CADIG_NY2.py'],
             pathex=['D:\\Python\\NY_pyside2\\dll', 'D:\\Python\\NY_pyside2\\venv\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='CADIG_NY2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\Python\\NY_pyside2\\image\\logo_ico2.ico')
