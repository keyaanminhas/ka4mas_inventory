# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main1.py'],
             pathex=['C:\\Users\\ka4ma\\Documents\\python3\\tonitoon customer'],
             binaries=[('chromedriver.exe', 'chromedriver.exe')],
             datas=[('time.txt', 'time.txt')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='main1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\ka4ma\\Documents\\python3\\kogo.ico')
