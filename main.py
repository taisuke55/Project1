from logic import *

def main():
    application = QApplication([])
    window = TelevisionLogic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()