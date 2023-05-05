# -*- coding: utf-8 -*-
import sys
import qtawesome
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class ModifyUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 373)

        # 最小化
        self.minimize_button = QtWidgets.QPushButton(Dialog)
        self.minimize_button.setGeometry(QtCore.QRect(90, 20, 31, 21))
        self.minimize_button.setObjectName("minimizeButton")

        # 其他
        self.other_button = QtWidgets.QPushButton(Dialog)
        self.other_button.setGeometry(QtCore.QRect(50, 20, 31, 21))
        self.other_button.setObjectName("other_button")

        # 关闭
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.close_button.setObjectName("closeButton")


        self.gridLayoutWidget_1 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_1.setGeometry(QtCore.QRect(0, 80, 341, 191))
        self.gridLayoutWidget_1.setObjectName("gridLayoutWidget_2")

        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_1)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setSpacing(0)
        self.gridLayout_1.setObjectName("gridLayout_2")

        self.layoutWidget_1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_1.setGeometry(QtCore.QRect(0, 330, 341, 41))
        self.layoutWidget_1.setObjectName("layoutWidget_1")

        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.layoutWidget_1)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")


        # 更改 标题
        self.modify_title = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.modify_title.setObjectName("modify_title")
        self.gridLayout_1.addWidget(self.modify_title, 0, 0, 1, 2)
        # 查找 标题
        self.search_title = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.search_title.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.search_title.setMouseTracking(False)
        self.search_title.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.search_title.setObjectName("search_title")
        self.gridLayout_1.addWidget(self.search_title, 3, 0, 1, 2)

        # 更改年龄 标题
        self.modify_age_button = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.modify_age_button.setObjectName("modify_age")
        self.gridLayout_1.addWidget(self.modify_age_button, 7, 0, 1, 1)
        # 更改性别 标题
        self.modify_sex_button = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.modify_sex_button.setObjectName("modify_sex")
        self.gridLayout_1.addWidget(self.modify_sex_button, 8, 0, 1, 1)
        # 更多信息 标题
        self.modify_more_button = QtWidgets.QPushButton(self.gridLayoutWidget_1)
        self.modify_more_button.setObjectName("modify_more")
        self.gridLayout_1.addWidget(self.modify_more_button, 9, 0, 1, 1)


        # 姓名 输入搜索框
        self.name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout_1.addWidget(self.name_lineEdit, 2, 0, 1, 2)
        # 年龄 输入框
        self.age_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.age_lineEdit.setObjectName("age_lineEdit")
        self.gridLayout_1.addWidget(self.age_lineEdit, 7, 1, 1, 1)
        # 性别 输入框
        self.sex_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.sex_lineEdit.setObjectName("sex_lineEdit")
        self.gridLayout_1.addWidget(self.sex_lineEdit, 8, 1, 1, 1)
        # 更多信息 输入框
        self.more_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_1)
        self.more_lineEdit.setObjectName("more_lineEdit")
        self.gridLayout_1.addWidget(self.more_lineEdit, 9, 1, 1, 1)


        # 确定 按钮
        self.confirm_button = QtWidgets.QPushButton(self.layoutWidget_1)
        self.confirm_button.setMinimumSize(QtCore.QSize(20, 0))
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_1.addWidget(self.confirm_button)
        # 取消 按钮
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget_1)
        self.cancel_button.setMinimumSize(QtCore.QSize(20, 0))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_1.addWidget(self.cancel_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.minimize_button.setText(_translate("Dialog", ""))
        self.other_button.setText(_translate("Dialog", ""))
        self.close_button.setText(_translate("Dialog", ""))

        self.modify_more_button.setText(_translate("Dialog", " 更改更多信息 "))
        self.modify_age_button.setText(_translate("Dialog", " 更改年龄 "))
        self.modify_sex_button.setText(_translate("Dialog", " 更改性别 "))
        self.modify_title.setText(_translate("Dialog", "更改信息"))
        self.search_title.setText(_translate("Dialog", "查找"))
        self.confirm_button.setText(_translate("Dialog", "修改"))
        self.cancel_button.setText(_translate("Dialog", "退出"))

        # ------------------------------------ #
        # 控制按钮样式
        self.minimize_button.setFixedSize(30, 30)  # 设置关闭按钮的大小
        self.other_button.setFixedSize(30, 30)  # 设置按钮大小
        self.close_button.setFixedSize(30, 30)  # 设置最小化按钮大小

        # 设置按钮部件的QSS样式
        # 默认为淡色，鼠标悬浮时为深色
        self.close_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.other_button.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')
        self.minimize_button.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:15px;}QPushButton:hover{background:green;}''')

        # ------------------------------------ #
        # 整体样式
        Dialog.setWindowOpacity(0.9)
        Dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pe = QPalette()
        Dialog.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)
        Dialog.setPalette(pe)

        # ------------------------------------ #
        # 图标样式
        spin_icon = qtawesome.icon('fa5s.folder-open', color='black')
        Dialog.setWindowIcon(spin_icon)

        # ------------------------------------ #
        self.gridLayoutWidget_1.setStyleSheet('''
                QPushButton{
                    border:none;
                    color:white;
                    padding-left:5px;
                    height:50px;
                    font-size:20px;
                    font-weight:500;
                    padding-right:10px;
                    font-family: "Helvetica Neue";
                }
                QLabel{ 
                    font-size:20px;
                    font-weight:600;color:white;
                    font-family: "Helvetica Neue";
                }''')

        self.modify_title.setStyleSheet('''
                QPushButton{
                    border:none;
                    border-bottom:2px solid white;
                    font-size:28px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } ''')

        self.search_title.setStyleSheet('''
                QPushButton{font-size:28px;}
                QPushButton:hover{
                    color:black;
                    border:0px solid #F3F3F5;
                    border-radius:0px;
                    background:LightGray;
                } ''')


        # ------------------------------------ #
        # 输入栏样式
        lineText = [self.name_lineEdit, self.age_lineEdit, self.sex_lineEdit, self.more_lineEdit]
        line = 0
        for lineEdit in lineText:
            lineEdit.setStyleSheet('''
                QLineEdit{
                    border:2px solid gray;
                    font-size:13px;
                    font-weight:700;
                    font-family: "Helvetica Neue";
                    border-radius:12px;
                    height:25px;
                }''')
            lineEdit.setPlaceholderText(str(line))
            if 1 <= line <= 3:
                lineEdit.setPlaceholderText('********')
            line = line + 1
            lineEdit.setAlignment(Qt.AlignCenter)  # 居中放置
        self.name_lineEdit.setPlaceholderText('输入待修改者姓名，点击查找')


        # ------------------------------------ #
        # 确定 退出按钮样式
        controlButton = [self.confirm_button, self.cancel_button]
        for button in controlButton:
            button.setStyleSheet(''' 
                QPushButton{
                    color:black;
                    border:none;
                    border-bottom:2px solid white;
                    font-size:28px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                } 
                QPushButton:hover{
                    color:white;
                    border:0px solid #F3F3F5;
                    border-radius:0px;
                    background:LightGray;
                } ''')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = ModifyUi()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())