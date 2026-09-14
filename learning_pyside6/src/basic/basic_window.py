from PySide6.QtWidgets import QApplication, QWidget

# I don't know what is this used in yet
import sys

app = QApplication(sys.argv)


window = QWidget()
window.show()


app.exec()
