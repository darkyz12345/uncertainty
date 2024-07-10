import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.Qt import Qt

from mainwndow import Ui_MainWindow
from confidence_dialog_class import ConfidenceDialog


class UncertaintyApp(QMainWindow):
    dlg = None
    confidence_probability: float = 0.95

    def __init__(self):
        super(UncertaintyApp, self).__init__()
        self.name_table = "Название прибора, единица измереня прибора"
        self.setWindowTitle("UncertaintyApp")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fill_title_table()
        self.const_rows = self.ui.uncertainty_table.rowCount()
        self.cols = self.ui.uncertainty_table.columnCount()
        self.rows = 0
        self.ui.clear_btn.clicked.connect(self.clear_table_btn)
        self.ui.confidence_probability_btn.clicked.connect(self.confidence_btn)
        self.ui.add_value.clicked.connect(self.add_value_btn)

    def fill_title_table(self):
        self.ui.uncertainty_table.horizontalHeader().setVisible(False)
        self.ui.uncertainty_table.verticalHeader().setVisible(False)
        self.ui.uncertainty_table.setRowCount(2)
        self.ui.uncertainty_table.setColumnCount(8)
        # name of table
        self.ui.uncertainty_table.setSpan(0, 0, 1, 8)
        item = QTableWidgetItem(self.name_table)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(0, 0, item)
        # №
        item = QTableWidgetItem('№')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 0, item)

        # measured value X
        item = QTableWidgetItem('Измеренное значение X')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 1, item)
        # Average value X
        item = QTableWidgetItem('Среднее значение <X>')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 2, item)
        self.ui.uncertainty_table.setSpan(2, 2, 3, 1)
        # Uncertainty type A
        item = QTableWidgetItem(f'Неопределённость типа A, U(A)')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 3, item)
        self.ui.uncertainty_table.setSpan(2, 3, 3, 1)
        # Uncertainty type B
        item = QTableWidgetItem(f'Неопределённость типа B, U(B)')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 4, item)
        self.ui.uncertainty_table.setSpan(2, 4, 3, 1)
        # Total Uncertainty
        item = QTableWidgetItem(f'Суммарная неопределённость U(C)')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 5, item)
        self.ui.uncertainty_table.setSpan(2, 5, 3, 1)
        # Coverage rate k
        item = QTableWidgetItem(f'Коэффициент охвата k')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 6, item)
        self.ui.uncertainty_table.setSpan(2, 6, 3, 1)
        # Extended uncertainty
        item = QTableWidgetItem(f'Расширенная неопределённость U')
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.uncertainty_table.setItem(1, 7, item)
        self.ui.uncertainty_table.setSpan(2, 7, 3, 1)
        self.ui.uncertainty_table.resizeColumnsToContents()

    def clear_table(self):
        self.ui.uncertainty_table.clearContents()
        self.ui.uncertainty_table.setRowCount(0)
        self.ui.uncertainty_table.setColumnCount(0)

    def clear_table_btn(self):
        self.clear_table()
        self.fill_title_table()

    def value_confidence_dialog_btn(self):
        if self.dlg:
            if self.dlg.ui.value_confidence_line.text():
                self.confidence_probability = float(self.dlg.ui.value_confidence_line.text())
            self.dlg.close()
            self.dlg = None

    def cancel_dialog_btn(self):
        if self.dlg:
            self.dlg.close()
            self.dlg = None

    def confidence_btn(self):
        if self.dlg is not None and self.dlg.isHidden:
            self.dlg.close()
        self.dlg = ConfidenceDialog()
        self.dlg.ui.value_confidence_line.setText(str(self.confidence_probability))
        self.dlg.ui.save_btn.clicked.connect(self.value_confidence_dialog_btn)
        self.dlg.ui.cancel_btn.clicked.connect(self.cancel_dialog_btn)
        self.dlg.exec()

    def add_value_btn(self):
        print(self.rows, self.const_rows)
        self.ui.uncertainty_table.insertRow(self.rows + self.const_rows)
        self.rows += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UncertaintyApp()
    window.showMaximized()
    sys.exit(app.exec())
