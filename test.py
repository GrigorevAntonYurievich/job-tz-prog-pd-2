from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QPushButton, QLineEdit, QStandardItem, QStandardItemModel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример QListViev")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.log_view = QListView()
        self.layout.addWidget(self.log_view)

        self.log_model = QStandardItemModel(self.log_view)
        self.log_view.setModel(self.log_model)

        self.button = QPushButton("Выполнить функцию")
        self.button.clicked.connect(self.parsing_and_zapis_v_bd)
        self.layout.addWidget(self.button)

    def parsing_and_zapis_v_bd(self):
        # Здесь производится какая-то обработка или вычисления
        # После этого вы хотите вывести результат в окно log
        text_to_add = "Ваш результат обработки или вычисления"
        
        # Создаем элемент для списка
        item = QStandardItem(text_to_add)
        
        # Добавляем элемент в модель
        self.log_model.appendRow(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())