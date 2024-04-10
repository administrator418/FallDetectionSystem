import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["UI/icon.ico", "UI/themes/"]

# TARGET
target = Executable(
    script="UI/main.py",
    icon="UI/icon.ico"
)

# SETUP CX FREEZE
setup(
    name="PyDracula",
    version="0.0",
    description="跌倒检测系统",
    author="jayden",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)
