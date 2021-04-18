from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QApplication
from PyQt5.QtCore import Qt


class DelUserDialog(QDialog):
    """
    Класс - диалог выбора контакта для удаления.
    """
    def __init__(self, server):
        super().__init__()

        self.db_session = server.database.create_session()
        self.server = server

        self.setFixedSize(350, 120)
        self.setWindowTitle('Удаление пользователя')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.selector_label = QLabel(
            'Выберите пользователя для удаления:', self)
        self.selector_label.setFixedSize(200, 20)
        self.selector_label.move(10, 0)

        self.selector = QComboBox(self)
        self.selector.setFixedSize(200, 20)
        self.selector.move(10, 30)

        self.btn_ok = QPushButton('Удалить', self)
        self.btn_ok.setFixedSize(100, 30)
        self.btn_ok.move(230, 20)
        self.btn_ok.clicked.connect(self.remove_user)

        self.btn_cancel = QPushButton('Отмена', self)
        self.btn_cancel.setFixedSize(100, 30)
        self.btn_cancel.move(230, 60)
        self.btn_cancel.clicked.connect(self.close)

        self.all_users_fill()

    def all_users_fill(self):
        """
        Метод заполняющий список пользователей.
        """
        self.selector.addItems([item[0] for item in self.db_session.users_list()])

    def remove_user(self):
        """
        Метод - обработчик удаления пользователя.
        """
        self.db_session.remove_user(self.selector.currentText())
        if self.selector.currentText() in self.server.messengers:
            self.server.remove_client(self.server.messengers[self.selector.currentText()].sock)
        # Рассылаем клиентам сообщение о необходимости обновить справочники
        self.server.service_update_lists()
        self.close()
