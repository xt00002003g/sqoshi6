import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit

from Bot import ShoppingBot


def remove_item_qlist(given_qlist):
    listItems = given_qlist.selectedItems()
    if not listItems: return
    for item in listItems:
        given_qlist.takeItem(given_qlist.row(item))


def qlist_to_list(listWidget):
    return [str(listWidget.item(i).text()) for i in range(listWidget.count())]


class Ui_MainWindow(PyQt5.QtCore.QObject):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionReset_preferences = QtWidgets.QAction(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.del_account_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_account_btn = QtWidgets.QPushButton(self.centralwidget)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.accounts_list = QtWidgets.QListWidget(self.centralwidget)
        self.set_max_price_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_category_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_category_btn = QtWidgets.QPushButton(self.centralwidget)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.categories_list = QtWidgets.QListWidget(self.centralwidget)
        self.del_brand_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_brand_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.brands_list = QtWidgets.QListWidget(self.centralwidget)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.sizes_list = QtWidgets.QListWidget(self.centralwidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.menuMenu = QtWidgets.QMenu(self.menubar)

    def get_text(self):
        text, okPressed = QInputDialog.getText(QInputDialog(), "Get text", "Size:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text

    def get_integer(self):
        i, okPressed = QInputDialog.getInt(QInputDialog(), "Get integer", "Price:")
        if okPressed:
            return i

    def start_bot(self):
        print('Creating Bot object start ')
        # TODO : TypeError: 'QListWidget' object is not iterable
        ShoppingBot("piotrpopisgames@gmail.com", 'testertest', qlist_to_list(self.sizes_list),
                    qlist_to_list(self.brands_list), self.textEdit.toPlainText(), self.lcdNumber.intValue())

    def stop_bot(self):
        print('Stopping bot')

    def add_size(self):
        self.sizes_list.addItem(self.get_text())
        print('Adding size')

    def add_brand(self):
        self.brands_list.addItem(self.get_text())
        print('Adding brand')

    def add_category(self):
        self.categories_list.addItem(self.get_text())
        print('Adding category')

    # TODO IMPLEMENT
    def add_account(self):
        print('Adding account')

    def set_max_price(self):
        self.lcdNumber.display(str(self.get_integer()))

    def del_size(self):
        remove_item_qlist(self.sizes_list)

    def del_brand(self):
        remove_item_qlist(self.brands_list)

    def del_category(self):
        remove_item_qlist(self.categories_list)

    def del_account(self):
        if len(self.accounts_list) > 1:
            remove_item_qlist(self.accounts_list)
        else:
            pass

    def setupUi(self, MainWindow, login, password):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 548)
        self.start_btn.setGeometry(QtCore.QRect(630, 400, 141, 41))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start_bot)
        self.stop_btn.setGeometry(QtCore.QRect(800, 400, 141, 41))
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.clicked.connect(self.stop_bot)
        self.dateTimeEdit.setGeometry(QtCore.QRect(440, 340, 171, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lcdNumber.setGeometry(QtCore.QRect(650, 210, 101, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar.setGeometry(QtCore.QRect(30, 470, 921, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2.setGeometry(QtCore.QRect(20, 10, 921, 21))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.sizes_list.setGeometry(QtCore.QRect(20, 80, 241, 91))
        self.sizes_list.setObjectName("sizes_list")
        self.textEdit.setGeometry(QtCore.QRect(440, 210, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_4.setGeometry(QtCore.QRect(450, 190, 101, 17))
        self.label_4.setObjectName("label_4")
        self.label_5.setGeometry(QtCore.QRect(660, 190, 141, 17))
        self.label_5.setObjectName("label_5")
        self.checkBox.setGeometry(QtCore.QRect(620, 270, 91, 31))
        self.checkBox.setObjectName("checkBox")
        self.textEdit_3.setGeometry(QtCore.QRect(440, 270, 171, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6.setGeometry(QtCore.QRect(450, 250, 101, 17))
        self.label_6.setObjectName("label_6")
        self.label_7.setGeometry(QtCore.QRect(30, 60, 121, 17))
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(30, 190, 121, 17))
        self.label_8.setObjectName("label_8")
        self.brands_list.setGeometry(QtCore.QRect(20, 210, 241, 91))
        self.brands_list.setObjectName("brands_list")
        self.add_size_btn.setGeometry(QtCore.QRect(270, 80, 141, 41))
        self.add_size_btn.setObjectName("add_size_btn")
        self.add_size_btn.clicked.connect(self.add_size)
        self.del_size_btn.setGeometry(QtCore.QRect(270, 130, 141, 41))
        self.del_size_btn.setObjectName("del_size_btn")
        self.del_size_btn.clicked.connect(self.del_size)
        self.add_brand_btn.setGeometry(QtCore.QRect(270, 210, 141, 41))
        self.add_brand_btn.setObjectName("add_brand_btn")
        self.add_brand_btn.clicked.connect(self.add_brand)
        self.del_brand_btn.setGeometry(QtCore.QRect(270, 260, 141, 41))
        self.del_brand_btn.setObjectName("del_brand_btn")
        self.categories_list.setGeometry(QtCore.QRect(20, 340, 241, 91))
        self.categories_list.setObjectName("categories_list")
        self.label_9.setGeometry(QtCore.QRect(30, 320, 121, 17))
        self.label_9.setObjectName("label_9")
        self.add_category_btn.setGeometry(QtCore.QRect(270, 340, 141, 41))
        self.add_category_btn.setObjectName("add_category_btn")
        self.add_category_btn.clicked.connect(self.add_category)
        self.del_category_btn.setGeometry(QtCore.QRect(270, 390, 141, 41))
        self.del_category_btn.setObjectName("del_category_btn")
        self.set_max_price_btn.setGeometry(QtCore.QRect(760, 210, 71, 31))
        self.set_max_price_btn.setObjectName("set_max_price_btn")
        self.set_max_price_btn.clicked.connect(self.set_max_price)
        self.accounts_list.setGeometry(QtCore.QRect(440, 80, 241, 91))
        self.accounts_list.setObjectName("accounts_list")
        self.accounts_list.addItem(login)
        self.label_10.setGeometry(QtCore.QRect(450, 60, 121, 17))
        self.label_10.setObjectName("label_10")
        self.add_account_btn.setGeometry(QtCore.QRect(690, 80, 141, 41))
        self.add_account_btn.setObjectName("add_account_btn")
        self.add_account_btn.clicked.connect(self.add_account)
        self.del_account_btn.setGeometry(QtCore.QRect(690, 130, 141, 41))
        self.del_account_btn.setObjectName("del_account_btn")
        self.checkBox_2.setGeometry(QtCore.QRect(620, 340, 91, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionReset_preferences.setObjectName("actionReset_preferences")
        self.actionInfo.setObjectName("actionInfo")
        self.actionDonate.setObjectName("actionDonate")
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionReset_preferences)
        self.menuMenu.addAction(self.actionInfo)
        self.menuMenu.addAction(self.actionDonate)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Campaign ID"))
        self.label_5.setText(_translate("MainWindow", "Max Price( Per Item)"))
        self.checkBox.setText(_translate("MainWindow", "Send Mail"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.label_7.setText(_translate("MainWindow", "Sizes"))
        self.label_8.setText(_translate("MainWindow", "Brands"))
        self.add_size_btn.setText(_translate("MainWindow", "Add"))
        self.del_size_btn.setText(_translate("MainWindow", "Delete"))
        self.add_brand_btn.setText(_translate("MainWindow", "Add"))
        self.del_brand_btn.setText(_translate("MainWindow", "Delete"))
        self.label_9.setText(_translate("MainWindow", "Categories"))
        self.add_category_btn.setText(_translate("MainWindow", "Add"))
        self.del_category_btn.setText(_translate("MainWindow", "Delete"))
        self.set_max_price_btn.setText(_translate("MainWindow", "Set"))
        self.label_10.setText(_translate("MainWindow", "Accounts"))
        self.add_account_btn.setText(_translate("MainWindow", "Add"))
        self.del_account_btn.setText(_translate("MainWindow", "Delete"))
        self.checkBox_2.setText(_translate("MainWindow", "Date"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionReset_preferences.setText(_translate("MainWindow", "Reset preferences"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionDonate.setText(_translate("MainWindow", "Donate"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, 'franek0', 'haslo')
    MainWindow.show()
    sys.exit(app.exec_())
