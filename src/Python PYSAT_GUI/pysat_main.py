from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)

    def runningFunctions(self, MainWindow):
        emp1 = pysat_ui()
        emp1.mainframe(MainWindow)
        emp1.menu_item_shortcuts()
        emp1.menu_item_functions(MainWindow)
        emp1.ok(MainWindow)


    def new(self):
        # TODO create a new window to work in. The old window does not disappear
        window = Main(self)
        window.show()


    def exit(self):
        # TODO close the current window
        self.close()

def main():
    app = QApplication(sys.argv)

    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(1.3)

    main_window = Main()
    main_window.show()
    splash.finish(main_window)
    app.exec_()

if __name__ == "__main__":
    main()