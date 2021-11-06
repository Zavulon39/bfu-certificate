from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from src.manager.data import DataManager
from src.manager.screen import ScreenManager
from docxtpl import DocxTemplate
from ..types import Certificate


class DetailScreen(QtWidgets.QWidget):
    """ Экран детального обзора заявки """

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("Form")
        self.resize(972, 531)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.student_name = QtWidgets.QLineEdit(self)
        self.student_name.setGeometry(QtCore.QRect(150, 80, 351, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.student_name.setFont(font)
        self.student_name.setStyleSheet("padding: 0 2.5px;\n"
                                        "outline: none;\n"
                                        " border: 1px solid rgb(183, 183, 183);")
        self.student_name.setObjectName("student_name")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.h1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.h1.setFont(font)
        self.h1.setObjectName("h1")
        self.horizontalLayout.addWidget(self.h1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.status_img = QtWidgets.QLabel(self)
        self.status_img.setGeometry(QtCore.QRect(130, 370, 31, 31))
        self.status_img.setText("")
        self.status_img.setPixmap(QtGui.QPixmap(".\\assets/img/success.png"))
        self.status_img.setScaledContents(True)
        self.status_img.setObjectName("status_img")
        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setGeometry(QtCore.QRect(30, 480, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton {\n"
                                    "    background: #2BBBAD;\n"
                                    "        color: #fff;\n"
                                    "     width: 100px;\n"
                                    "    border-radius: 6px;\n"
                                    "    padding: 4px;\n"
                                    "}\n"
                                    "          \n"
                                    "QPushButton:hover {\n"
                                    "    background: #26ad9f;\n"
                                    " }")
        self.save_btn.setObjectName("save_btn")
        self.quit_btn = QtWidgets.QPushButton(self)
        self.quit_btn.setGeometry(QtCore.QRect(160, 480, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("QPushButton {\n"
                                    "                                        background: #c62828;\n"
                                    "                                            color: #fff;\n"
                                    "                                         width: 100px;\n"
                                    "                                        border-radius: 6px;\n"
                                    "                                        padding: 4px;\n"
                                    "                                    }\n"
                                    "                                                                       QPushButton:hover {\n"
                                    "                                        background: #b71c1c;\n"
                                    "                                    }")
        self.quit_btn.setObjectName("quit_btn")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.course = QtWidgets.QLineEdit(self)
        self.course.setGeometry(QtCore.QRect(120, 150, 381, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.course.setFont(font)
        self.course.setStyleSheet("padding: 0 2.5px;\n"
                                  "outline: none;\n"
                                  " border: 1px solid rgb(183, 183, 183);")
        self.course.setObjectName("course")
        self.base = QtWidgets.QLineEdit(self)
        self.base.setGeometry(QtCore.QRect(220, 190, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.base.setFont(font)
        self.base.setStyleSheet("padding: 0 2.5px;\n"
                                "outline: none;\n"
                                " border: 1px solid rgb(183, 183, 183);")
        self.base.setObjectName("base")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.direction = QtWidgets.QLineEdit(self)
        self.direction.setGeometry(QtCore.QRect(190, 230, 311, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.direction.setFont(font)
        self.direction.setStyleSheet("padding: 0 2.5px;\n"
                                     "outline: none;\n"
                                     " border: 1px solid rgb(183, 183, 183);")
        self.direction.setText("")
        self.direction.setObjectName("direction")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(30, 230, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.birthday = QtWidgets.QDateEdit(self)
        self.birthday.setGeometry(QtCore.QRect(200, 110, 301, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.birthday.setFont(font)
        self.birthday.setObjectName("birthday")
        self.start_date = QtWidgets.QDateEdit(self)
        self.start_date.setGeometry(QtCore.QRect(220, 270, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.start_date.setFont(font)
        self.start_date.setObjectName("start_date")
        self.end_date = QtWidgets.QDateEdit(self)
        self.end_date.setGeometry(QtCore.QRect(220, 310, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.end_date.setFont(font)
        self.end_date.setObjectName("end_date_2")
        self.res = QtWidgets.QTextBrowser(self)
        self.res.setGeometry(QtCore.QRect(540, 70, 411, 421))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.res.setFont(font)
        self.res.setObjectName("res")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Заявка от:"))
        self.student_name.setPlaceholderText(_translate("Form", "Введите ФИО студента..."))
        self.label_2.setText(_translate("Form", "Начало обучения:"))
        self.label_3.setText(_translate("Form", "Конец обучения:"))
        self.h1.setText(_translate("Form", "Заявка № 1"))
        self.label_4.setText(_translate("Form", "Статус:"))
        self.save_btn.setText(_translate("Form", "Сохранить"))
        self.quit_btn.setText(_translate("Form", "Вернуться"))
        self.label_5.setText(_translate("Form", "Курс:"))
        self.course.setPlaceholderText(_translate("Form", "Введите курс студента (c формой обчения)"))
        self.base.setPlaceholderText(_translate("Form", "Платная / Бюджетная"))
        self.label_6.setText(_translate("Form", "Основа обучения:"))
        self.direction.setPlaceholderText(_translate("Form", "Введите направление"))
        self.label_7.setText(_translate("Form", "Направление:"))
        self.label_8.setText(_translate("Form", "Дата рождения:"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.init_logic()

    def init_logic(self):
        """ Бизнес-логика """
        from .certificate_list import CertificateListScreen

        certificate = DataManager().certificate_detail

        self.h1.setText(f"Заявка № {certificate.id}")
        self.student_name.setText(certificate.name)
        self.start_date.setDate(certificate.from_date)
        self.end_date.setDate(certificate.to_date)
        self.birthday.setDate(certificate.birthday)
        self.course.setText(certificate.course)
        self.base.setText(certificate.base)
        self.direction.setText(certificate.direction)

        self.status_img.setPixmap(QtGui.QPixmap(
            "./assets/img/success.png"
            if certificate.is_checked else
            "./assets/img/error.png"
        ))

        self.student_name.textChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.direction.textChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.course.textChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.base.textChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.birthday.dateChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.start_date.dateChanged.connect(lambda: self.change_handler(certificate.enrolment_order))
        self.end_date.dateChanged.connect(lambda: self.change_handler(certificate.enrolment_order))

        self.change_handler(certificate.enrolment_order)

        self.quit_btn.clicked.connect(lambda: ScreenManager.set_screen(CertificateListScreen(ScreenManager.get_ui()), self))
        self.save_btn.clicked.connect(self.save_file)

    def save_file(self):
        """ Обработчик нажатия на кнопку сохранения справки """
        doc = DocxTemplate('assets/certificate.docx')
        name = self.student_name.text()

        doc.render({
            'now': date.today(),
            'enrolment_order': DataManager().certificate_detail.enrolment_order,
            'name': name,
            'birthday': self.birthday.text(),
            'course': self.course.text(),
            'base': self.base.text(),
            'direction': self.direction.text(),
            'from_date': self.start_date.text(),
            'to_date': self.end_date.text(),
        })
        doc.save(f'{name}.docx')

    def change_handler(self, enrolment_order: str):
        """ Обработчик изменения любого поля """

        name = self.student_name.text()
        birthday = self.birthday.text()
        course = self.course.text()
        base = self.base.text()
        direction = self.direction.text()
        from_date = self.start_date.text()
        to_date = self.end_date.text()

        self.res.setText("""{}, {} года рождения, является  студентом(кой) ФГАОУ ВО «БФУ им. И. Канта» {} формы обучения по основным образовательным программам на {}, специальность/направление «{}»

Зачислен(а)  {}
Начало обучения: {}
Предполагаемая дата окончания обучения:
 {} г.
                """.format(
            name,
            birthday,
            course,
            base,
            direction,
            enrolment_order,
            from_date,
            to_date
        ))

        message = QtWidgets.QMessageBox(self)
        message.setWindowTitle('Успех!')
        message.setText('Справка сохранилась в директорию, где находиться приложение')
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        message.setFont(font)
        message.exec_()
