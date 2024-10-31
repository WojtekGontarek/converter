import sys

from PyQt6.QtGui import qPremultiply
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.convertButton.clicked.connect(self.convert)
        self.rawText = ''
        self.convertedText = ''
        self.show()

    def convert(self):
        self.rawText = self.ui.rawText.text()
        if self.ui.upperRadio.isChecked():
            self.convertedText = self.rawText.upper()
        elif self.ui.lowerRadio.isChecked():
            self.convertedText = self.rawText.lower()
        elif self.ui.invertRadio.isChecked():
            self.convertedText = self.rawText.swapcase()

        self.ui.convertedText.setText(self.convertedText)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())