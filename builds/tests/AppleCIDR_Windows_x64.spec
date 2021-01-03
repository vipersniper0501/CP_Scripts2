# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['GUIs\\ScriptRunnerPyQt5_GUI\\ScriptGUIrunner.py'],
             pathex=['C:\\Users\\Michael\\Desktop\\Coding_Projects\\CyberScripts_2'],
             binaries=[],
             datas=[('./GUIs/ScriptRunnerPyQt5_GUI/resources.qrc', '.'), ('./GUIs/ScriptRunnerPyQt5_GUI/resources_rc.py', '.'), ('./GUIs/ScriptRunnerPyQt5_GUI/scripFunc', 'scripFunc/'), ('./GUIs/ScriptRunnerPyQt5_GUI/PyUIs', 'PyUIs/'), ('./GUIs/ScriptRunnerPyQt5_GUI/images', 'images/'), ('./GUIs/ScriptRunnerPyQt5_GUI/configurations', 'configurations/')],
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
          name='AppleCIDR_Windows_x64',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , version='GUIs\\ScriptRunnerPyQt5_GUI\\VERSION', uac_admin=True, icon='GUIs\\ScriptRunnerPyQt5_GUI\\images\\cup2.ico')
