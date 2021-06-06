#example of Qlabel
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap,QPalette
import sys

class mywindow(QWidget):
    def __init__(self):
        super(mywindow,self).__init__()
        self.resize(400,300)

        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        label1.setText('this is a text label')
        #背景填充使能
        label1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>welcome to python<a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('this is a picture label')
        label3.setPixmap(QPixmap("/home/lee/Pictures/3.jpg"))

        label4.setText("<A href='www.baidu.com'>walcome baidu<a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('this is a hyperlink')

        #layout
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addStretch()

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(True)
        label4.linkActivated.connect(self.link_clicked)

        #label2.linkHovered.connected(self.link_hovered)
        #label1.setTextInteractionaFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("qlabel example")

    #def link_hovered(self):
        #print('the first')
    

    def link_clicked(self):
        print('the second')


if __name__=='__main__':
    app=QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec_())