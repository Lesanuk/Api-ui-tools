import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500) # x, y, width, height

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial Black", 40))
        label.setGeometry(0, 10, 300, 100) # x, y, width, height
        label.setStyleSheet("color: #9262bf;"
                            "background-color: #bea5d6;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # and if instead of typing "color" or something else we type non-existing property, it will be ignored and the program will say that the property is not valid, but it will not crash the program

        #label.setAlignment(Qt.AlignTop) # vertically top
        label.setAlignment(Qt.AlignBottom) # vertically bottom
        #label.setAlignment(Qt.AlignVCenter) # vertically center

        #label.setAlignment(Qt.AlignRight) # horizontally right
        #label.setAlignment(Qt.AlignHCenter) # horizontally center
        #label.setAlignment(Qt.AlignLeft) # horizontally left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter | Qt.AlignCenter) # CENTER & CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
