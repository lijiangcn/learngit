import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget,QMainWindow
from PyQt5.QtGui import QIcon

class mainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(mainWindow,self).__init__(parent)
        self.resize(400,200)
        #实例化建状态栏
        self.status=self.statusBar()
        #4000 is the duration of message
        self.status.showMessage('this is a remark',4000)
        self.setWindowTitle('example of pyqt')

    def center(self):
        #get the size of screen
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        #move the window to the center of the screen
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=mainWindow()
    form.center()
    form.show()
    sys.exit(app.exec())
    
