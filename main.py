import sys

from helpers import isConsoleApplication
from console import ConsoleApplication
from gui import GUIApplication

__IS_CONSOLE_APP = isConsoleApplication()

if __IS_CONSOLE_APP:
    ConsoleApplication()
else:
    GUIApplication()


sys.exit(0)