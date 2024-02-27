# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfparserdb.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)
import res_rc

class Ui_PDFParserDB(object):
    def setupUi(self, PDFParserDB):
        if not PDFParserDB.objectName():
            PDFParserDB.setObjectName(u"PDFParserDB")
        PDFParserDB.resize(275, 376)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PDFParserDB.sizePolicy().hasHeightForWidth())
        PDFParserDB.setSizePolicy(sizePolicy)
        PDFParserDB.setMinimumSize(QSize(275, 376))
        PDFParserDB.setMaximumSize(QSize(275, 376))
        PDFParserDB.setStyleSheet(u"font-family: Times New Roman;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.427447 rgba(255, 92, 92, 235), stop:1 rgba(255, 179, 179, 255));\n"
"")
        PDFParserDB.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.actionParsing = QAction(PDFParserDB)
        self.actionParsing.setObjectName(u"actionParsing")
        self.actionDBSetting = QAction(PDFParserDB)
        self.actionDBSetting.setObjectName(u"actionDBSetting")
        self.actionDBSetting.setCheckable(True)
        self.centralwidget = QWidget(PDFParserDB)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.log = QListView(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(10, 210, 251, 161))
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.button_go = QPushButton(self.centralwidget)
        self.button_go.setObjectName(u"button_go")
        self.button_go.setGeometry(QRect(10, 170, 101, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 243, 156))
        self.verticalLayout_menu = QVBoxLayout(self.widget)
        self.verticalLayout_menu.setObjectName(u"verticalLayout_menu")
        self.verticalLayout_menu.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_host = QHBoxLayout()
        self.horizontalLayout_host.setObjectName(u"horizontalLayout_host")
        self.label_host = QLabel(self.widget)
        self.label_host.setObjectName(u"label_host")
        self.label_host.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.horizontalLayout_host.addWidget(self.label_host)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_host.addWidget(self.lineEdit)


        self.verticalLayout_menu.addLayout(self.horizontalLayout_host)

        self.horizontalLayout_nameDB = QHBoxLayout()
        self.horizontalLayout_nameDB.setObjectName(u"horizontalLayout_nameDB")
        self.label_nameBD = QLabel(self.widget)
        self.label_nameBD.setObjectName(u"label_nameBD")
        self.label_nameBD.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.horizontalLayout_nameDB.addWidget(self.label_nameBD)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_nameDB.addWidget(self.lineEdit_2)


        self.verticalLayout_menu.addLayout(self.horizontalLayout_nameDB)

        self.horizontalLayout_login = QHBoxLayout()
        self.horizontalLayout_login.setObjectName(u"horizontalLayout_login")
        self.label_login = QLabel(self.widget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.horizontalLayout_login.addWidget(self.label_login)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_login.addWidget(self.lineEdit_3)


        self.verticalLayout_menu.addLayout(self.horizontalLayout_login)

        self.horizontalFrame_password = QFrame(self.widget)
        self.horizontalFrame_password.setObjectName(u"horizontalFrame_password")
        self.horizontalFrame_password.setStyleSheet(u"QFrame {\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    margin-right: 0;\n"
"}")
        self.password = QHBoxLayout(self.horizontalFrame_password)
        self.password.setObjectName(u"password")
        self.label_password = QLabel(self.horizontalFrame_password)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.password.addWidget(self.label_password)

        self.enter_password = QLineEdit(self.horizontalFrame_password)
        self.enter_password.setObjectName(u"enter_password")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enter_password.sizePolicy().hasHeightForWidth())
        self.enter_password.setSizePolicy(sizePolicy1)
        self.enter_password.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 10pt;\n"
"}")

        self.password.addWidget(self.enter_password)

        self.pushButton = QPushButton(self.horizontalFrame_password)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/PDFParcerDB/icons/visible.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/PDFParcerDB/icons/invisible.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(True)

        self.password.addWidget(self.pushButton)


        self.verticalLayout_menu.addWidget(self.horizontalFrame_password)

        self.horizontalLayout_way_to_file = QHBoxLayout()
        self.horizontalLayout_way_to_file.setObjectName(u"horizontalLayout_way_to_file")
        self.label_way_to_file = QLabel(self.widget)
        self.label_way_to_file.setObjectName(u"label_way_to_file")
        self.label_way_to_file.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.horizontalLayout_way_to_file.addWidget(self.label_way_to_file)

        self.vybor_PDF = QHBoxLayout()
        self.vybor_PDF.setObjectName(u"vybor_PDF")
        self.way_to_file = QLineEdit(self.widget)
        self.way_to_file.setObjectName(u"way_to_file")

        self.vybor_PDF.addWidget(self.way_to_file)

        self.browse = QToolButton(self.widget)
        self.browse.setObjectName(u"browse")
        self.browse.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")

        self.vybor_PDF.addWidget(self.browse)


        self.horizontalLayout_way_to_file.addLayout(self.vybor_PDF)


        self.verticalLayout_menu.addLayout(self.horizontalLayout_way_to_file)

        PDFParserDB.setCentralWidget(self.centralwidget)

        self.retranslateUi(PDFParserDB)

        QMetaObject.connectSlotsByName(PDFParserDB)
    # setupUi

    def retranslateUi(self, PDFParserDB):
        PDFParserDB.setWindowTitle(QCoreApplication.translate("PDFParserDB", u"PDFParserDB", u"PDFParserDB"))
#if QT_CONFIG(tooltip)
        PDFParserDB.setToolTip(QCoreApplication.translate("PDFParserDB", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionParsing.setText(QCoreApplication.translate("PDFParserDB", u"Parsing", None))
        self.actionDBSetting.setText(QCoreApplication.translate("PDFParserDB", u"DBSetting", None))
        self.button_go.setText(QCoreApplication.translate("PDFParserDB", u"Go!", None))
        self.label_host.setText(QCoreApplication.translate("PDFParserDB", u"Host", None))
        self.label_nameBD.setText(QCoreApplication.translate("PDFParserDB", u"NameDB", None))
        self.label_login.setText(QCoreApplication.translate("PDFParserDB", u"Login", None))
        self.label_password.setText(QCoreApplication.translate("PDFParserDB", u"Password", None))
        self.enter_password.setText("")
        self.pushButton.setText("")
        self.label_way_to_file.setText(QCoreApplication.translate("PDFParserDB", u"Way to file:", None))
        self.browse.setText(QCoreApplication.translate("PDFParserDB", u"Browse", None))
    # retranslateUi

