from PySide6 import QtWidgets
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
                button.clicked.connect(self.on_button_clicked)
                self.buttonsLayout.addWidget(button, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1

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
