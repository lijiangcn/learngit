import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class mainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(mainWindow,self).__init__(parent)
        self.resize(800,500)
        #实例化建状态栏
        self.status=self.statusBar()
        #4000 is the duration of message
        self.status.showMessage('this is a remark',4000)
        self.setWindowTitle('example of pyqt')
        baseWidget=QWidget()
        self.setCentralWidget(baseWidget)
        btnClose=QPushButton(baseWidget)
        btnClose.setText('close')
        btnClose.setGeometry(100,90,75,23)
        btnClose.clicked.connect(self.onButtonClick)

    def center(self):
        #get the size of screen
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        #move the window to the center of the screen
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
 
    def onButtonClick(self):
        sender=self.sender()
        print(sender.text+'pressed')
        qApp=QApplication.instance()
        qApp.quit()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=mainWindow()
    form.center()
    form.show()
    sys.exit(app.exec())
    
