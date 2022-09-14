from core.app import *

# START MAIN WINDOW
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    try:
        sys.exit(app.exec_())
    finally:
        window.closeToir()