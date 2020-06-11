from practice import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        #self.actionClose.triggered.connect(self.close)
        #self.num1.clicked.connect(self.openMsg)


'''
    def openMsg(self):
        file = QFileDialog.getOpenFileName(self, "选择文件", "/Users", 'All Files (*);;Text Files (*.txt)')
        #self.statusBar.showMessage(file)
        print(0)
'''


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.show()

    sys.exit(app.exec_())



