from datetime import date
from docx.opc.exceptions import PackageNotFoundError
from docxtpl import DocxTemplate
from PyQt5 import QtCore, QtGui, QtWidgets
from src.manager.data import DataManager
from src.manager.screen import ScreenManager
from ..types import Certificate


class CertificateListScreen(QtWidgets.QWidget):
    """ Экран с выводом всех заявок """

    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("Form")
        self.resize(972, 531)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(15, 121, 941, 331))
        self.tableWidget.setMinimumSize(QtCore.QSize(941, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.is_checked = QtWidgets.QCheckBox('Распечатана', self)
        self.is_checked.setGeometry(QtCore.QRect(581, 81, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        item.setFont(font)
        self.is_checked.setFont(font)
        self.search_btn = QtWidgets.QPushButton(self)
        self.search_btn.setGeometry(QtCore.QRect(711, 81, 111, 31))
        self.search_btn.setText('Поиск')
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet("QPushButton {\n"
                                    "    background: #f9a825;\n"
                                    "        color: #fff;\n"
                                    "     width: 100px;\n"
                                    "    border-radius: 6px;\n"
                                    "    padding: 4px;\n"
                                    "}\n"
                                    "          \n"
                                    "QPushButton:hover {\n"
                                    "    background: #f57f17;\n"
                                    " }")
        self.search_btn.setObjectName("search_btn")
        self.clear_filters = QtWidgets.QPushButton(self)
        self.clear_filters.setGeometry(QtCore.QRect(831, 81, 111, 31))
        self.clear_filters.setText('Сбросить')
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.clear_filters.setFont(font)
        self.clear_filters.setStyleSheet("QPushButton {\n"
                                      "    background: #c62828;\n"
                                      "        color: #fff;\n"
                                      "     width: 100px;\n"
                                      "    border-radius: 6px;\n"
                                      "    padding: 4px;\n"
                                      "}\n"
                                      "          \n"
                                      "QPushButton:hover {\n"
                                      "    background: #b71c1c;\n"
                                      " }")
        self.clear_filters.setObjectName("clear_filters")
        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setText('Сбросить фильтры')
        self.save_btn.setGeometry(QtCore.QRect(30, 480, 271, 31))
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
        self.student_name = QtWidgets.QLineEdit(self)
        self.student_name.setGeometry(QtCore.QRect(250, 86, 321, 22))
        self.student_name.setPlaceholderText('Имя подавшего заявку...')
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(True)
        self.student_name.setFont(font)
        self.student_name.setStyleSheet("padding: 0 2.5px;\n"
                                        "outline: none;\n"
                                        " border: 1px solid rgb(183, 183, 183);")
        self.student_name.setObjectName("student_name")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Список заявок на получение справки"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя подавшего заявку студента"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Направление"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Статус (распечатано/не распечатано)"))

        QtCore.QMetaObject.connectSlotsByName(self)

        self.init_logic()

    def init_logic(self):
        # Добавление записей в таблицу, бизнес-логика
        certificates = DataManager().certificate_list

        self.search_btn.clicked.connect(lambda: self.draw_table(self.get_filtered_data()))
        self.save_btn.clicked.connect(self.save_handler)
        self.clear_filters.clicked.connect(lambda: self.draw_table(DataManager().certificate_list))
        self.tableWidget.doubleClicked.connect(self.cell_click_handler)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.draw_table(certificates)

    def draw_table(self, certificates: list[Certificate]):
        self.tableWidget.setRowCount(len(certificates))

        for idx, certificate in enumerate(certificates):
            a = QtWidgets.QTableWidgetItem(certificate.name)
            b = QtWidgets.QTableWidgetItem(str(certificate.direction))
            icon = QtGui.QIcon('assets/img/success.png' if certificate.is_checked else 'assets/img/error.png')
            c = QtWidgets.QTableWidgetItem()
            c.setIcon(icon)

            a.setFlags(QtCore.Qt.ItemIsEnabled)
            b.setFlags(QtCore.Qt.ItemIsEnabled)
            c.setFlags(QtCore.Qt.ItemIsEnabled)

            self.tableWidget.setItem(idx, 0, a)
            self.tableWidget.setItem(idx, 1, b)
            self.tableWidget.setItem(idx, 2, c)

    def cell_click_handler(self, item: QtCore.QModelIndex):
        """ Обработчик нажатия на строку таблицы """
        from src.ui.detail import DetailScreen

        data_manager = DataManager()
        data_manager.certificate_detail = data_manager.certificate_list[item.row()]

        ScreenManager.set_screen(DetailScreen(ScreenManager.get_ui()), self)

    def save_handler(self):
        try:
            for data in self.get_filtered_data():
                for i in range(data.copies_count // 2):
                    doc = DocxTemplate('assets/certificate.docx')

                    doc.render({
                        'now': date.today(),
                        'enrolment_order': data.enrolment_order,
                        'name': data.name,
                        'birthday': data.birthday,
                        'course': data.course,
                        'base': data.base,
                        'direction': data.direction,
                        'from_date': data.from_date,
                        'to_date': data.to_date,
                        'id': data.spr_id
                    })

                    doc.save(f'{data.name}_{i+1}.docx')

                data.update_db()
        except PackageNotFoundError:
            message = QtWidgets.QMessageBox(self)
            message.setWindowTitle('Ошибка!')
            message.setText('Файл assets/certificate.docx не найден')
            font = QtGui.QFont()
            font.setFamily("Montserrat")
            font.setPointSize(10)
            message.setFont(font)
            message.exec_()
        else:
            message = QtWidgets.QMessageBox(self)
            message.setWindowTitle('Успех!')
            message.setText('Справки сохранились в директорию, где находиться приложение')
            font = QtGui.QFont()
            font.setFamily("Montserrat")
            font.setPointSize(10)
            message.setFont(font)
            message.exec_()

    def get_filtered_data(self) -> list[Certificate]:
        """ Возвращает отфильтрованные данные, по фильтрам в интерфейсе """
        name = self.student_name.text().strip()

        if name:
            return list(filter(lambda el: el.is_checked == self.is_checked.isChecked() and name.lower() in el.name.lower(), DataManager().certificate_list))
        else:
            return list(filter(lambda el: el.is_checked == self.is_checked.isChecked(), DataManager().certificate_list))