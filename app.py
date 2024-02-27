# костяк программы.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox, QListView, QPushButton, QVBoxLayout, QWidget, QLineEdit, QListWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel
from ui_main import Ui_PDFParserDB
from db_and_parsing import data_for_podkluchenie_k_bd

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_PDFParserDB()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.vybor_files_pdf)
        self.ui.button_go.clicked.connect(self.podkluschenie_k_db_i_parsing)


    def vybor_files_pdf(self):
        # Открываем диалоговое окно выбора файла
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "PDF Files (*.pdf)")
        
        if file_path:  # Если пользователь выбрал файл
            # Добавляем путь к файлу в QLineEdit или выполняем другие нужные действия
            self.ui.way_to_file.setText(file_path)
    
    def podkluschenie_k_db_i_parsing(self):
        text_to_add = "Process...."
        item = QStandardItem(text_to_add)

        # Проверка, существует ли модель у QListView
        if self.ui.log.model() is None:
        # Если модели нет, создаем новую модель
            model = QStandardItemModel()
            self.ui.log.setModel(model)
        else:
        # Если модель уже существует, получаем ее
            model = self.ui.log.model()

    # Добавляем элемент в модель
        model.appendRow(item)
        host = self.ui.lineEdit.text()
        nameDB = self.ui.lineEdit_2.text()
        login = self.ui.lineEdit_3.text()
        password = self.ui.enter_password.text()
        #print(host, nameDB, login, password)
        data_for_podkluchenie_k_bd(host, nameDB, login, password)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())