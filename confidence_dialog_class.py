from confidence_dialog import Ui_Dialog

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class ConfidenceDialog(QDialog):
    def __init__(self):
        super(ConfidenceDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        validator = QRegExpValidator(QRegExp(r'([0-9].)+'))
        self.ui.value_confidence_line.setValidator(validator)