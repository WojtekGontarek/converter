import sys

from PyQt6.QtGui import qPremultiply
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.convertButton.clicked.connect(self.convert)
        self.ui.rawText.textChanged.connect(self.convert)
        # self.rawText = ''
        # self.convertedText = ''
        self.show()

    def convert(self):
        rawText = self.ui.rawText.text()
        convertedText = rawText
        if self.ui.upperRadio.isChecked():
            convertedText = rawText.upper()
        elif self.ui.lowerRadio.isChecked():
            convertedText = rawText.lower()
        elif self.ui.invertRadio.isChecked():
            convertedText = rawText.swapcase()

        self.ui.convertedText.setText(convertedText)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())