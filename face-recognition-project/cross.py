import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Invalid")

        # Set up the label to display the GIF image
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Load the GIF image
        self.movie = QMovie("images/cross.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # Add horizontal and vertical spacers to center the label
        hbox = QHBoxLayout(self)
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addStretch(1)

        vbox = QVBoxLayout(self)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # Set the layout of the window
        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
