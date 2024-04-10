from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["PySide6", "os", "sys"],
    "iconfile": "UI/icon.icns",
}

setup(
    app=APP,
    name="跌倒检测系统",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
