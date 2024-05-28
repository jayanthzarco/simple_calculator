from PySide6 import QtWidgets, QtGui
import math


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")

        # Layouts
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QtWidgets.QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        self.buttonsLayout = QtWidgets.QGridLayout()
        self.layout.addLayout(self.buttonsLayout)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '√',
            '0', '.', '=', '+', 'x²'
        ]

        row, col = 0, 0
        for text in buttons:
            if text:
                button = QtWidgets.QPushButton(text)
                button.setObjectName(text)  # Set object name for styling
                button.clicked.connect(self.on_button_clicked)
                self.buttonsLayout.addWidget(button, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1

        self.apply_stylesheet()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
            QLineEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: none;
                padding: 20px;
                font-size: 30px;
            }
            QPushButton {
                background-color: #4B4B4B;
                color: #FFFFFF;
                border: none;
                padding: 15px;
                font-size: 18px;
            }
            QPushButton:pressed {
                background-color: #616161;
            }
            QPushButton#C {
                color: #FF5555;
            }
        """)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        elif text == 'C':
            self.display.clear()
        elif text == '←':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == '√':
            try:
                result = str(math.sqrt(float(self.display.text())))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        elif text == 'x²':
            try:
                result = str(float(self.display.text()) ** 2)
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Calculator()
    window.show()
    app.exec_()
