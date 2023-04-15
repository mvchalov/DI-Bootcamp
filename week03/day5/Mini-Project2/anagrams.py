import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton
from anagram_checker import AnagramChecker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Find an anagram")
        self.label = QLabel()
        self.input = QLineEdit()
        layout = QVBoxLayout()
        self.label.setText("Enter a word:")
        self.button = QPushButton("Submit!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.label2 = QLabel()

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.label2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        if self.input.text() != "":
            helper = AnagramChecker()
            if helper.is_valid_word(self.input.text().upper()):
                message = "'"+self.input.text()+"' is a valid English word.\n\n"
                results = helper.get_anagrams(self.input.text().upper())
                if len(results) > 0:
                    message += "This word has the following anagrams:\n"
                    message += "\n".join(results)
                else:
                    message += "This word doesn't have any anagrams."

                self.label2.setText(message)
            else:
                self.label2.setText("Please, enter a valid word!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
