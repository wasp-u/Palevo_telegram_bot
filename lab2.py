import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from numpy import *

class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.name = QLabel("ПІБ")
        self.number = QLabel("Номер")
        self.group = QLabel("Група")
        StartWindow.namew = QLineEdit()
        StartWindow.namew.setPlaceholderText("Osadchiy Yuriy")
        StartWindow.numberw = QLineEdit()
        StartWindow.numberw.setPlaceholderText("18")
        StartWindow.groupw = QLineEdit()
        StartWindow.groupw.setPlaceholderText("ІО-64")

        self.next = QPushButton("Next")
        self.next.setAutoDefault(True)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.name,0,0)
        self.grid.addWidget(self.number,1,0)
        self.grid.addWidget(self.group,2,0)
        self.grid.addWidget(StartWindow.namew,0,1,1,2)
        self.grid.addWidget(StartWindow.numberw,1,1,1,2)
        self.grid.addWidget(StartWindow.groupw,2,1)
        self.grid.addWidget(self.next,2,2)

        self.setLayout(self.grid)

        self.next.clicked.connect(self.showEvent)

        self.resize(300, 200)
        self.center()
        self.setWindowTitle('Start Window')


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showEvent(self):
        self.setVisible(False)
        self.mw = MainWindow()
        self.mw.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.nextwindow = QPushButton("START")
        self.nextwindow.setAutoDefault(True)
        self.name = QLabel("ПІБ: " + StartWindow.namew.text())
        self.group = QLabel("Група: " + StartWindow.groupw.text())
        self.number = QLabel("Номер: "+ StartWindow.numberw.text())
        self.var = QLabel("Варіант: " + str((int(StartWindow.numberw.text())+(int(StartWindow.groupw.text().split("-")[1])%60))%30+1))

        self.grid = QGridLayout()
        self.grid.setSpacing(5)

        self.grid.addWidget(self.name,0,0)
        self.grid.addWidget(self.number,2,0)
        self.grid.addWidget(self.group,1,0)
        self.grid.addWidget(self.var,3,0)
        self.grid.addWidget(self.nextwindow,4,0)

        self.setLayout(self.grid)

        self.nextwindow.clicked.connect(self.showEvent)

        self.resize(300, 200)
        self.center()
        self.setWindowTitle('MainWIndow')

    def showEvent(self):
        self.setVisible(False)
        self.sw = SecondWindow()
        self.sw.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class myListWidget(QListWidget) :
    def Clicked(self,item) :
        if item.text() in SecondWindow.s:
            pass
        else:
            SecondWindow.s.append(item.text())
            SecondWindow.listSet.addItem(item.text())

    def removeSel(self,item):
        SecondWindow.s.remove(item.text())
        SecondWindow.listSet.clear()
        SecondWindow.listSet.addItems(SecondWindow.s)


class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        SecondWindow.setA = list()
        SecondWindow.s = list()
        SecondWindow.setB = list()
        widget = QWidget()

        self.radio1 = QRadioButton('set A')
        self.radio2 = QRadioButton('set B')
        self.clear = QPushButton("Clear")
        self.add = QPushButton("Add")
        self.add.setFlat(True)
        self.clear.setFlat(True)
        self.clear.setStyleSheet("QWidget { background-color: #4c88ff}")
         #box
        gridbox = QGridLayout()
        gridbox.addWidget(self.radio1,0,0)
        gridbox.addWidget(self.radio2,0,1)
        gridbox.addWidget(self.clear,0,3)
        gridbox.addWidget(self.add,0,2)

        box = QGroupBox("Оберіть множину",widget)
        box.setLayout(gridbox)
        box.setStyleSheet("QWidget { background-color: #ffc60c}")
         #box

        bg = "#353638"
        appearance = self.palette()
        appearance.setColor(QPalette.Active, QPalette.Window,
                     QColor(bg))
        appearance.setColor(QPalette.Inactive, QPalette.Window,
                     QColor(bg))
        self.setPalette(appearance)

        self.tabWidget1 = QWidget(self)
        self.tabWidget1.setStyleSheet("QWidget { background-color: #4c88ff }")
        self.tabWidget2 = ThirdWindow()
        self.tabWidget2.setStyleSheet("QWidget { background-color: #dfdfdf }")
        self.tabWidget3 = FourthWindow()
        self.tabWidget3.setStyleSheet("QWidget { background-color: #ffcdcd }")

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tabWidget1,'window &2')
        self.tabs.addTab(self.tabWidget2,'window &3')
        self.tabs.addTab(self.tabWidget3,'window &4')

        self.save = QPushButton("Save")
        self.save.setFlat(True)
        self.load = QPushButton("Load")
        self.load.setFlat(True)


        self.man = QLabel("Man:")
        self.woman = QLabel("Woman:")
        self.set = QLabel("Your set:")

        self.listMan = myListWidget()
        self.listWoman = myListWidget()
        SecondWindow.listSet = myListWidget()

        self.ManNames = ['lol','kek','cheburek']
        for Item in self.ManNames:
            self.listMan.addItem(Item)
        self.listMan.itemClicked.connect(self.listMan.Clicked)

        self.listSet.itemClicked.connect(self.listSet.removeSel)

        self.WomanNames = ['Анна','Анастасия','Алёна','Елена','Андрюха']
        for Item in self.WomanNames:
            self.listWoman.addItem(Item)
        self.listWoman.itemClicked.connect(self.listMan.Clicked)

        self.grid = QGridLayout(self.tabWidget1)
        self.grid.setSpacing(5)

        self.grid.addWidget(self.man,1,0)
        self.grid.addWidget(self.woman,1,1)
        self.grid.addWidget(self.set,1,2,1,2)
        self.grid.addWidget(SecondWindow.listSet,2,2,1,2)
        self.grid.addWidget(self.listMan,2.5,0)
        self.grid.addWidget(self.listWoman,2,1)
        self.grid.addWidget(self.save,3,2)
        self.grid.addWidget(self.load,3,3)
        self.grid.addWidget(box,0,0,1,4)
        self.tabWidget1.setLayout(self.grid)

        self.maingrid = QGridLayout()
        self.maingrid.setSpacing(5)
        self.maingrid.addWidget(self.tabs,0,0)

        self.setLayout(self.maingrid)

        self.add.clicked.connect(self.addEvent)
        self.clear.clicked.connect(self.clearSet)

        self.resize(700, 500)
        self.center()
        self.setWindowTitle('MainWIndow')


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def addEvent(self):
        if self.radio1.isChecked():
            try:
                SecondWindow.setA.clear()
                SecondWindow.setA = copy(SecondWindow.s)
                ThirdWindow.setA.addItems(SecondWindow.s)
            except:
                print('error')
        if self.radio2.isChecked():
            try:
                SecondWindow.setB.clear()
                SecondWindow.setB = copy(SecondWindow.s)
                ThirdWindow.setB.addItems(SecondWindow.s)
            except:
                print('error')

    def clearSet(self):
        SecondWindow.listSet.clear()
        SecondWindow.s.clear()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.aSb = QPushButton("aSb")
        self.aSb.setFlat(True)
        self.aSb.clicked.connect(self.showGraphS)
        self.aRb = QPushButton("aRb")
        self.aRb.setFlat(True)
        self.aRb.clicked.connect(self.showGraphR)
        ThirdWindow.setA = QListWidget()
        ThirdWindow.setB = QListWidget()

        self.setALabel = QLabel('Set A:')
        self.setBLabel = QLabel('Set B:')

        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.grid.addWidget(self.setALabel,0,0)
        self.grid.addWidget(self.setBLabel,0,1)
        self.grid.addWidget(ThirdWindow.setA,1,0)
        self.grid.addWidget(ThirdWindow.setB,1,1)
        self.grid.addWidget(self.aSb,0,2)
        self.grid.addWidget(self.aRb,0,3)


        self.setLayout(self.grid)

    def showGraphS(self):
        self.matrixS = QTableWidget(len(SecondWindow.setB),len(SecondWindow.setA))
        self.grid.addWidget(self.matrixS,2,0,1,7)
        r = random.randint(0,len(SecondWindow.setA))

        for i in range(len(SecondWindow.setA)):
            self.matrixS.setHorizontalHeaderItem(i,QTableWidgetItem(SecondWindow.setA[i]))
        for j in range(len(SecondWindow.setB)):
            self.matrixS.setVerticalHeaderItem(j,QTableWidgetItem(SecondWindow.setB[j]))
        for i in range(len(SecondWindow.setA)):
            for j in range(len(SecondWindow.setB)):
                if random.randint(0,4) == 1:
                    self.matrixS.setItem(j,i,QTableWidgetItem('1'))
                else: self.matrixS.setItem(j,i,QTableWidgetItem('0'))

    def showGraphR(self):
        self.matrixR = QTableWidget(len(SecondWindow.setB),len(SecondWindow.setA))
        self.grid.addWidget(self.matrixR,1,2,1,5)
        r = random.randint(0,len(SecondWindow.setA))

        for i in range(len(SecondWindow.setA)):
            self.matrixR.setHorizontalHeaderItem(i,QTableWidgetItem(SecondWindow.setA[i]))
        for j in range(len(SecondWindow.setB)):
            self.matrixR.setVerticalHeaderItem(j,QTableWidgetItem(SecondWindow.setB[j]))
        for i in range(len(SecondWindow.setA)):
            for j in range(len(SecondWindow.setB)):
                if random.randint(0,4) == 1:
                    self.matrixR.setItem(j,i,QTableWidgetItem('1'))
                else: self.matrixR.setItem(j,i,QTableWidgetItem('0'))


class FourthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.grid = QGridLayout()
        self.grid.setSpacing(5)


        self.setLayout(self.grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SecondWindow()
    w.show()
    sys.exit(app.exec_())
