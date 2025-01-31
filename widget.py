# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.setWindowTitle("Toolbar Alignment")
#        self.setGeometry(100, 100, 800, 600)

        # Apply dark background and widget styles
        self.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E; /* Dark grey */
            color: white; /* White text */
        }
        QLabel {
            color: white; /* Label text color */
        }
        QLineEdit {
            background-color: #3E3E3E; /* Slightly lighter grey */
            color: white;
            border: 1px solid #5E5E5E;
            padding: 5px;
        }
        QPushButton {
            background-color: #5A5A5A; /* Button background */
            color: white;
            border: 1px solid #3E3E3E;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #777777; /* Lighter grey when hovering */
        }
        QComboBox {
            background-color: #3E3E3E;
            color: white;
            border: 1px solid #5E5E5E;
            padding: 5px;
        }
        QTextEdit {
            background-color: #3E3E3E;
            color: white;
            border: 1px solid #5E5E5E;
        }
        QSlider::groove:horizontal {
            background: #5A5A5A; /* Slider groove background */
            height: 10px;
        }
        QSlider::handle:horizontal {
            background: #777777; /* Slider handle */
            width: 15px;
            margin: -5px 0; /* Align handle with groove */
        }
    """)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
