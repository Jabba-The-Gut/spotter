import sys

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from fbs_runtime.application_context.PyQt5 import ApplicationContext


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        """
        Initialize gui relevant settings
        :return: none
        """
        self.resize(500, 500)  # set size
        self.center()
        self.setWindowTitle("spotter")
        self.show()

    def center(self):
        """
        Initialize the main window
        :return:  none
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
