import sys
import threading
import time
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.lab = QLabel("Compteur")
        self.text = QLineEdit("")
        self.text.setPlaceholderText("0")
        self.text.setReadOnly(True)
        self.start = QPushButton("Start")
        self.quit = QPushButton("Quitter")
        self.stop = QPushButton("Stop")
        self.reset = QPushButton("Reset")
        self.connect = QPushButton("Connect")



        grid.addWidget(self.lab, 0, 0, 1, 2)
        grid.addWidget(self.text, 1, 0, 1, 2)
        grid.addWidget(self.start, 2, 0, 1, 2)
        grid.addWidget(self.quit, 4, 1, 1, 1)
        grid.addWidget(self.stop, 3, 1, 1, 1)
        grid.addWidget(self.reset, 3, 0, 1, 1)
        grid.addWidget(self.connect, 4, 0, 1, 1)



        self.start.clicked.connect(self.__actionStart)
        self.quit.clicked.connect(self.__actionQuitter)
        self.reset.clicked.connect(self.__actionReset)
        self.stop.clicked.connect(self.__actionStop)
        self.connect.clicked.connect(self.__actionConnect)
        self.setWindowTitle("Chronomètre")


    def _start(self):
        try:
            while self.stop != True:
                time.sleep(1)
                self.text+ 1
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Entrez un chiffre ou un nombre")


    def __actionStart():
        t1 = threading.Thread(target=_start)
        t1.start()
        t1.join()

    def __actionStop(self):
        pass
        """""
        while True:
            arret_thread = True
        """
    
    def __actionReset(self):
        if self.text !="0":
            self.text.setText("0")


    def __actionQuitter(self):
        QApplication.exit(0)
    def __actionConnect(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

