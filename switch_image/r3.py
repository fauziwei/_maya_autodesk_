import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)


        img_fold = "C:/my_contacts"

        for img in os.listdir(img_fold):
            img_path = os.path.join(img_fold, img)

            pixmap = QtGui.QPixmap(img_path)
            lbl = QtGui.QLabel(self)
            lbl.setPixmap(pixmap)

            hbox.addWidget(lbl)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Image viewer')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()