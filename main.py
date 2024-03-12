import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                             QFileDialog, QMenuBar, QVBoxLayout, QWidget,
                             QSplitter, QTreeView, QFileSystemModel, QPushButton)
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtCore import Qt
import darkdetect

from Views.Utils.themes import dark_stylesheet, light_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Detect OS theme and set application style accordingly
        if darkdetect.isDark():
            # Apply dark theme stylesheet
            self.setStyleSheet(dark_stylesheet)
        else:
            # Apply light theme stylesheet
            self.setStyleSheet(light_stylesheet)


        self.setWindowTitle('QMeter')
        self.setGeometry(100, 100, 1200, 800)

        # Create Menu Bar
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')
        self.editMenu = self.menuBar.addMenu('Edit')
        self.viewMenu = self.menuBar.addMenu('View')
        self.toolsMenu = self.menuBar.addMenu('Tools')
        self.helpMenu = self.menuBar.addMenu('Help')

        # Create Actions for File Menu
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.fileMenu.addAction(exitAction)

        # Create Toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # Create Central Widget and Layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Create Splitter for Left and Right Panels
        splitter = QSplitter(Qt.Horizontal)

        # Create Left Panel (e.g., for Test Plan)

        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(['Test Plan'])

        splitter.addWidget(self.treeView)



        # Create Right Panel (e.g., for Details)
        self.textEdit = QTextEdit()
        splitter.addWidget(self.textEdit)

        # Adjust Splitter Sizes
        splitter.setSizes([300, 900])

        layout.addWidget(splitter)

        # Status Bar
        self.statusBar().showMessage('Ready')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
