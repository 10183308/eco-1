# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Wed Jul 16 14:10:11 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(317, 412)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.gen_showconsole = QtGui.QCheckBox(self.groupBox_2)
        self.gen_showconsole.setObjectName(_fromUtf8("gen_showconsole"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.gen_showconsole)
        self.gen_showparsestatus = QtGui.QCheckBox(self.groupBox_2)
        self.gen_showparsestatus.setChecked(True)
        self.gen_showparsestatus.setObjectName(_fromUtf8("gen_showparsestatus"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.gen_showparsestatus)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.app_fontfamily = QtGui.QFontComboBox(self.groupBox_4)
        self.app_fontfamily.setFontFilters(QtGui.QFontComboBox.MonospacedFonts)
        self.app_fontfamily.setObjectName(_fromUtf8("app_fontfamily"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.app_fontfamily)
        self.app_fontsize = QtGui.QSpinBox(self.groupBox_4)
        self.app_fontsize.setObjectName(_fromUtf8("app_fontsize"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.app_fontsize)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.app_theme = QtGui.QComboBox(self.groupBox_3)
        self.app_theme.setObjectName(_fromUtf8("app_theme"))
        self.app_theme.addItem(_fromUtf8(""))
        self.app_theme.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.app_theme)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.app_custom = QtGui.QGroupBox(self.tab_2)
        self.app_custom.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.app_custom.setFlat(False)
        self.app_custom.setCheckable(True)
        self.app_custom.setChecked(False)
        self.app_custom.setObjectName(_fromUtf8("app_custom"))
        self.formLayout = QtGui.QFormLayout(self.app_custom)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.app_custom)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.app_foreground = QtGui.QPushButton(self.app_custom)
        self.app_foreground.setAutoFillBackground(False)
        self.app_foreground.setStyleSheet(_fromUtf8("background-color:  rgb(72, 72, 72)"))
        self.app_foreground.setText(_fromUtf8(""))
        self.app_foreground.setObjectName(_fromUtf8("app_foreground"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.app_foreground)
        self.label_2 = QtGui.QLabel(self.app_custom)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.app_background = QtGui.QPushButton(self.app_custom)
        self.app_background.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255)"))
        self.app_background.setText(_fromUtf8(""))
        self.app_background.setObjectName(_fromUtf8("app_background"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.app_background)
        self.verticalLayout.addWidget(self.app_custom)
        self.verticalLayout.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Startup", None))
        self.gen_showconsole.setText(_translate("MainWindow", "Show console", None))
        self.gen_showparsestatus.setText(_translate("MainWindow", "Show Parsing status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Font", None))
        self.label_3.setText(_translate("MainWindow", "Family", None))
        self.label_4.setText(_translate("MainWindow", "Size", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Theme", None))
        self.app_theme.setItemText(0, _translate("MainWindow", "Light (Default)", None))
        self.app_theme.setItemText(1, _translate("MainWindow", "Dark", None))
        self.app_custom.setTitle(_translate("MainWindow", "Custom", None))
        self.label.setText(_translate("MainWindow", "Foreground:", None))
        self.label_2.setText(_translate("MainWindow", "Background:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Appearance", None))

