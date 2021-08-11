import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes
import mysql.connector
from tabulate import tabulate
from time import sleep
  
 # set taskbar icon as same as window icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #---variables---
        self.count = 0

        #---window configs---
        self.setWindowTitle("Python Web")
        self.setGeometry(250, 150, 850, 550)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("images/logo2.png"))
        self.setIconSize(QSize(100, 100))
        self.offset = None
        print("app started")
        self.winDesign()
        self.widgets()
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

#---------------------------------------------------------------------------------------------------------

    def winDesign(self):
        self.bg = QLabel(self)
        self.bg.setGeometry(13, 15, 824, 520)
        self.bg.setStyleSheet(
            "background-color: #F1C40F; border: 2px solid rgb(255, 255, 255); border-radius: 6px; border-style: dashed;")
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(130, 130, 130))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.bg.setGraphicsEffect(self.blur_effect)

        self.title = QLabel(self)
        self.title.setGeometry(320, 17, 278, 43)
        self.title.setText('BOOKS REGISTRY')
        self.title.setFont(QFont('Hikou Rough', 20))
        self.title.setStyleSheet(
            "QLabel""{""color: #FFFFFF;""}")

        self.close = QToolButton(self)
        self.close.setGeometry(803, 24, 25, 25)
        self.close.clicked.connect(lambda: self.quit())
        self.close.setIcon(QIcon('images/closeOff.png'))
        self.close.setIconSize(QSize(25, 25))
        self.close.setStyleSheet(
            "QToolButton""{""background-color: rgba(0, 0, 0, 0.0); border-radius: 0px;""}")

#----------------------------------------------------------------------------------------------------------

    def widgets(self):
        # self.searchWidgetTitleCover = QPushButton(self)
        # self.searchWidgetTitleCover.clicked.connect(lambda: self.searchWidgetsPg())
        # self.searchWidgetTitleCover.setText('SEARCH:')
        # self.searchWidgetTitleCover.setFont(QFont('Hikou Rough', 14))
        # self.searchWidgetTitleCover.setGeometry(275, 68, 148, 39)
        # self.searchWidgetTitleCover.setStyleSheet(
        #     "background-color: #ECBD00; \
        #     color: #FFDBDB; \
        #     border-top: 2px solid rgb(222, 178, 0); \
        #     border-left: 2px solid rgb(222, 178, 0); \
        #     border-right: 2px solid rgb(222, 178, 0); \
        #     border-top-left-radius: 6px; \
        #     border-top-right-radius: 6px;")

        self.addWidgetCover = QLabel(self)
        self.addWidgetCover.setGeometry(33, 105, 390, 103)
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(234, 187, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.addWidgetCover.setGraphicsEffect(self.blur_effect)
        self.addWidgetCover.setStyleSheet(
            "background-color: #F1C40F; \
            border: 2px solid rgb(255, 220, 79); \
            border-bottom-left-radius: 6px; \
            border-bottom-right-radius: 6px;")

        self.addWidgetTitleCover = QPushButton(self)
        self.addWidgetTitleCover.setText('ADD TO REGISTRY:')
        self.addWidgetTitleCover.setFont(QFont('Hikou Rough', 14))
        self.addWidgetTitleCover.clicked.connect(lambda: self.addWidgetsPg())
        self.addWidgetTitleCover.setGeometry(33, 68, 240, 39)
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(234, 187, 0))
        self.blur_effect.setYOffset(-5)
        self.blur_effect.setXOffset(0)
        self.addWidgetTitleCover.setGraphicsEffect(self.blur_effect)
        self.addWidgetTitleCover.setStyleSheet(
            "background-color: #F1C40F; \
            color: #FFFFFF; border-top: 2px solid rgb(255, 220, 79); \
            border-left: 2px solid rgb(255, 220, 79); \
            border-right: 2px solid rgb(255, 220, 79); \
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")

        self.searchWidgetTitleCover = QPushButton(self)
        self.searchWidgetTitleCover.clicked.connect(lambda: self.searchWidgetsPg())
        self.searchWidgetTitleCover.setText('SEARCH:')
        self.searchWidgetTitleCover.setFont(QFont('Hikou Rough', 14))
        self.searchWidgetTitleCover.setGeometry(273, 68, 150, 39)
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(234, 187, 0))
        self.blur_effect.setYOffset(-5)
        self.blur_effect.setXOffset(0)
        self.searchWidgetTitleCover.setGraphicsEffect(self.blur_effect)
        self.searchWidgetTitleCover.setStyleSheet(
            "background-color: #ECBD00; \
            color: #FFDBDB; \
            border-top: 2px solid rgb(222, 178, 0); \
            border-left: 2px solid rgb(222, 178, 0); \
            border-right: 2px solid rgb(222, 178, 0); \
            border-bottom: 2px solid rgb(255, 220, 79);\
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")
        
        self.counter = QLabel(self)
        self.counter.setGeometry(324, 180, 98, 22)
        self.counter.setText('0 ENTRIES')
        self.counter.setFont(QFont('Hikou Rough', 14))
        self.counter.setStyleSheet(
            "QLabel""{""color: #FFDBDB;""}")

        self.idTxt = QLabel(self)
        self.idTxt.setGeometry(38, 115, 25, 22)
        self.idTxt.setText('ID:')
        self.idTxt.setFont(QFont('Hikou Rough', 12))
        self.idTxt.setStyleSheet(
            "QLabel""{""color: #FF0000;""}")
        
        self.idField = QLineEdit(self)
        self.idField.setGeometry(59, 111, 102, 28)
        self.onlyInt = QIntValidator()
        self.idField.setValidator(self.onlyInt)
        self.idField.setFont(QFont('Halvar Breit Rg', 9))
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(13)
        self.blur_effect.setColor(QColor(208, 166, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.idField.setGraphicsEffect(self.blur_effect)
        self.idField.setStyleSheet(
            "QLineEdit""{""background-color: #FFCC00; \
            border-radius: 4px; \
            border: 2px solid white; \
            border-style: dashed;""}")

        self.nmTxt = QLabel(self)
        self.nmTxt.setGeometry(175, 115, 60, 22)
        self.nmTxt.setText('NAME:')
        self.nmTxt.setFont(QFont('Hikou Rough', 12))
        self.nmTxt.setStyleSheet(
            "QLabel""{""color: #FF0000;""}")
        
        self.nmField = QLineEdit(self)
        self.nmField.setGeometry(226, 111, 193, 28)
        self.nmField.setFont(QFont('Halvar Breit Rg', 9))
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(13)
        self.blur_effect.setColor(QColor(208, 166, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.nmField.setGraphicsEffect(self.blur_effect)
        self.nmField.setStyleSheet(
            "QLineEdit""{""background-color: #FFCC00; \
            border-radius: 4px; \
            border: 2px solid white; \
            border-style: dashed;""}")

        self.authorTxt = QLabel(self)
        self.authorTxt.setGeometry(38, 151, 66, 22)
        self.authorTxt.setText('AUTHOR:')
        self.authorTxt.setFont(QFont('Hikou Rough', 12))
        self.authorTxt.setStyleSheet(
            "QLabel""{""color: #FF0000;""}")
        
        # self.authorField = QLineEdit(self)
        # self.authorField = QComboBox(self, editable = True, insertPolicy = QComboBox.InsertAtTop)
        self.authorField = QComboBox(self, editable = True)
        self.authorField.setGeometry(106, 145, 141, 28)
        self.authorField.setFont(QFont('Halvar Breit Rg', 9))
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(13)
        self.blur_effect.setColor(QColor(208, 166, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.authorField.setGraphicsEffect(self.blur_effect)
        self.authorField.setStyleSheet(
            "QComboBox""{""background-color: #FFCC00; \
            border-radius: 4px; \
            border: 2px solid white; \
            border-style: dashed;""}" \
                
            "QComboBox QAbstractItemView""{""background-color: #FFCC00; \
            border-left: 2px solid white; \
            border-right: 2px solid white; \
            border-bottom: 2px solid white; \
            selection-background-color: #F3C200; \
            border-bottom-left-radius: 5px; \
            border-bottom-right-radius: 5px; \
            border-style: dashed;""}")
        self.authorField.findChild(QFrame).setWindowFlags(Qt.Popup | Qt.NoDropShadowWindowHint) #removes shadow of the dropdown box
        
        self.priceTxt = QLabel(self)
        self.priceTxt.setGeometry(256, 151, 60, 22)
        self.priceTxt.setText('PRICE:')
        self.priceTxt.setFont(QFont('Hikou Rough', 12))
        self.priceTxt.setStyleSheet(
            "QLabel""{""color: #FF0000;""}")
        
        self.priceField = QLineEdit(self)
        self.priceField.setGeometry(307, 145, 111, 28)
        self.onlyInt = QIntValidator()
        self.priceField.setValidator(self.onlyInt)
        self.priceField.setFont(QFont('Halvar Breit Rg', 9))
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(13)
        self.blur_effect.setColor(QColor(208, 166, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.priceField.setGraphicsEffect(self.blur_effect)
        self.priceField.setStyleSheet(
            "QLineEdit""{""background-color: #FFCC00; \
            border-radius: 4px; \
            border: 2px solid white; \
            border-style: dashed;""}")

        self.addBtn = QToolButton(self)
        self.addBtn.setGeometry(213, 175, 40, 28)
        self.addBtn.clicked.connect(lambda: self.addItem())
        self.addBtn.setIcon(QIcon('images/add.png'))
        self.addBtn.setIconSize(QSize(21, 21))
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(229, 182, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.addBtn.setGraphicsEffect(self.blur_effect)
        self.addBtn.setStyleSheet(
            "QToolButton""{""background-color: #00FFCC00; \
            border-radius: 6px;""}")

        self.displayAr = QLabel(self)
        self.displayAr.setGeometry(33, 219, 390, 292)
        self.blur_effect = QGraphicsDropShadowEffect()
        self.blur_effect.setBlurRadius(15)
        self.blur_effect.setColor(QColor(234, 187, 0))
        self.blur_effect.setYOffset(0)
        self.blur_effect.setXOffset(0)
        self.displayAr.setGraphicsEffect(self.blur_effect)
        self.displayAr.setStyleSheet(
            "background-color: #F1C40F; \
            border: 2px solid rgb(255, 220, 79); \
            border-radius: 6px;")

        self.addWidgets_Visibility(True)
        self.srchWidgets_Visibility(False)
        

        #---ENTRIES COUNT UPDATER---
        base = mysql.connector.connect(host='localhost', user='root', passwd='server.prj_8378', database='bookReg')
        pointr = base.cursor()
        pointr.execute('SELECT COUNT(*) FROM books;')
        fixture_count = pointr.fetchone()[0]
        self.counter.setText(f'{fixture_count} ENTRIES')
        base.close()
        pointr.close()
        

    def searchWidgetsPg(self):
        
        self.addWidgetTitleCover.clicked.connect(lambda: self.addWidgetsPg())

        self.addWidgetTitleCover.setStyleSheet(
            "background-color: #ECBD00; \
            color: #FFDBDB; \
            border-top: 2px solid rgb(222, 178, 0); \
            border-left: 2px solid rgb(222, 178, 0); \
            border-right: 2px solid rgb(222, 178, 0); \
            border-bottom: 2px solid rgb(255, 220, 79);\
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")

        self.searchWidgetTitleCover.setStyleSheet(
            "background-color: #F1C40F; \
            color: #FFFFFF; \
            border-top: 2px solid rgb(255, 220, 79); \
            border-left: 2px solid rgb(255, 220, 79); \
            border-right: 2px solid rgb(255, 220, 79); \
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")

        self.srchWidgets_Visibility(True)
        self.addWidgets_Visibility(False)

    def addWidgetsPg(self):

        self.srchWidgets_Visibility(False)
        
        self.searchWidgetTitleCover.clicked.connect(lambda: self.searchWidgetsPg())

        self.searchWidgetTitleCover.setStyleSheet(
            "background-color: #ECBD00; \
            color: #FFDBDB; \
            border-top: 2px solid rgb(222, 178, 0); \
            border-left: 2px solid rgb(222, 178, 0); \
            border-right: 2px solid rgb(222, 178, 0); \
            border-bottom: 2px solid rgb(255, 220, 79);\
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")

        self.addWidgetTitleCover.setStyleSheet(
            "background-color: #F1C40F; \
            color: #FFFFFF; border-top: 2px solid rgb(255, 220, 79); \
            border-left: 2px solid rgb(255, 220, 79); \
            border-right: 2px solid rgb(255, 220, 79); \
            border-top-left-radius: 6px; \
            border-top-right-radius: 6px;")

        self.addWidgets_Visibility(True)






















    def addItem(self):
        base = mysql.connector.connect(host='localhost', user='root', passwd='server.prj_8378', database='bookReg')

        idInp = self.idField.text()
        nmInp = self.nmField.text()
        authorInp = self.authorField.currentText()
        priceInp = self.priceField.text()
        
        if nmInp == '' or authorInp == '':
            pass
        else:  
            pointr = base.cursor()
            query = "INSERT INTO books (id, name, author, price) VALUES (%s, %s, %s, %s)"
            value = (idInp, nmInp, authorInp, priceInp)
    
            pointr.execute(query, value)
            base.commit()

            self.idField.clear()
            self.nmField.clear()
            self.authorField.addItem(authorInp)
            self.authorField.clearEditText()
            self.priceField.clear()

            self.count += 1
            pointr.execute('SELECT COUNT(*) FROM books;')
            fixture_count = pointr.fetchone()[0]
            self.counter.setText(f'{fixture_count} ENTRIES')

            self.addBtn.setIcon(QIcon('images/check.png'))
            self.addBtn.setIconSize(QSize(21, 21))

            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            self.addBtn.setIcon(QIcon('images/add.png'))
            self.addBtn.setIconSize(QSize(21, 21))

        base.close()
        pointr.close()


    def addWidgets_Visibility(self, boolVal):
        self.counter.setVisible(boolVal)
        self.idTxt.setVisible(boolVal)
        self.idField.setVisible(boolVal)
        self.nmTxt.setVisible(boolVal)
        self.nmField.setVisible(boolVal)
        self.authorTxt.setVisible(boolVal)
        self.authorField.setVisible(boolVal)
        self.priceTxt.setVisible(boolVal)
        self.priceField.setVisible(boolVal)
        self.addBtn.setVisible(boolVal)

    def srchWidgets_Visibility(self, boolVal):
        self.displayAr.setVisible(boolVal)        





















    # def clickme2(self):
    #     base = mysql.connector.connect(host='localhost', user='root', passwd='server.prj_8378', database='bookReg')

    #     pointr = base.cursor()
    #     pointr.execute("SELECT * FROM books")

    #     idval = self.idSrField.text()
    #     print(idval)

    #     for i in pointr:
    #         if int(i[0]) == int(idval):
    #             print('yes')
    #             res = str(i)
    #             self.display.setText(res)
    #         else:
    #             print('No')
    #     print('successfully exected clicme2...')

    def clickme(self):
        print('add clicked')

    def quit(self):
        print("app closed")
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())