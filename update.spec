# -*- mode: python -*-

block_cipher = None


a = Analysis(['update.py'],
             pathex=['F:\\PycharmProjects\\pp_ocr_py34'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='update',
          debug=False,
          strip=False,
          upx=True,
          console=False )
