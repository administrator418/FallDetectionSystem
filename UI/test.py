import os
import sys
from PySide6.QtWidgets import QApplication

dpi = QApplication(sys.argv).primaryScreen().logicalDotsPerInch()
print(str(int(dpi)))
