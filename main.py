from logic import *
from PyQt6.QtWidgets import *


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
