

**UncertaintyApp** - это настольное приложение на PyQt5 для анализа неопределенности измерений в соответствии с международными метрологическими стандартами. [1](#0-0) 

### Основные возможности

- **Табличный анализ неопределенности**: Приложение предоставляет структурированную таблицу для ввода и анализа измеренных значений с расчетом различных типов неопределенности. [2](#0-1) 

- **Настройка доверительной вероятности**: Пользователи могут задавать доверительную вероятность через специальный диалог для корректного статистического анализа (по умолчанию 95%). [3](#0-2) [4](#0-3) 

- **Расчет типов неопределенности**: Поддержка расчета неопределенности типа A (статистическая), типа B (систематическая), суммарной и расширенной неопределенности. [5](#0-4) 

### Архитектура

Приложение построено на архитектуре Model-View-Controller с использованием PyQt5: [6](#0-5) 

- **Главное окно**: `UncertaintyApp` класс управляет основной логикой приложения и таблицей неопределенности
- **Диалоги конфигурации**: Отдельные диалоги для настройки параметров анализа
- **Генерируемый UI**: Интерфейс создается через Qt Designer с автоматической генерацией кода

### Технические требования

- Python 3.x
- PyQt5
- Поддержка SVG иконок через систему ресурсов Qt

### Использование

Запуск приложения осуществляется через `main.py`, которое создает главное окно в развернутом виде для удобной работы с таблицами данных. [7](#0-6) 

## Notes

Приложение специализируется на метрологическом анализе и следует стандартным практикам расчета неопределенности измерений. Интерфейс полностью на русском языке, что указывает на целевую аудиторию в русскоязычных метрологических лабораториях. Код содержит готовую структуру для расширения функциональности расчетов различных типов неопределенности.

Wiki pages you might want to explore:
- [Application Architecture (darkyz12345/uncertainty)](/wiki/darkyz12345/uncertainty#2)
- [Statistical Parameters and Confidence Intervals (darkyz12345/uncertainty)](/wiki/darkyz12345/uncertainty#5.2)

### Citations

**File:** main.py (L4-8)
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.Qt import Qt

from mainwndow import Ui_MainWindow
from confidence_dialog_class import ConfidenceDialog
```

**File:** main.py (L11-18)
```python
class UncertaintyApp(QMainWindow):
    dlg = None
    confidence_probability: float = 0.95

    def __init__(self):
        super(UncertaintyApp, self).__init__()
        self.name_table = "Название прибора, единица измереня прибора"
        self.setWindowTitle("UncertaintyApp")
```

**File:** main.py (L44-77)
```python
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
```

**File:** main.py (L101-108)
```python
    def confidence_btn(self):
        if self.dlg is not None and self.dlg.isHidden:
            self.dlg.close()
        self.dlg = ConfidenceDialog()
        self.dlg.ui.value_confidence_line.setText(str(self.confidence_probability))
        self.dlg.ui.save_btn.clicked.connect(self.value_confidence_dialog_btn)
        self.dlg.ui.cancel_btn.clicked.connect(self.cancel_dialog_btn)
        self.dlg.exec()
```

**File:** main.py (L117-121)
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UncertaintyApp()
    window.showMaximized()
    sys.exit(app.exec())
```
