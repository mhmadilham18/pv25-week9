from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog, QFontDialog, QFileDialog, QColorDialog,
                             QMessageBox, QMainWindow)
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon, QPalette, QColor
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(800, 600)

        # Create central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create main layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)

        # Create header label
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.headerLabel)

        # Create tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.mainLayout.addWidget(self.tabWidget)

        # Set up status bar with clock
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Create clock label
        self.clockLabel = QtWidgets.QLabel()
        self.statusbar.addPermanentWidget(self.clockLabel)

        # Set up clock timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateClock)
        self.timer.start(1000)  # Update every second

        # Initialize tabs
        self.setup_tab_input_nama()
        self.setup_tab_pilih_font()
        self.setup_tab_buka_file()
        self.setup_tab_ubah_warna()
        self.setup_tab_notepad()

        # Set up menu bar
        self.setup_menu_bar(MainWindow)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Apply stylesheet
        self.apply_stylesheet(MainWindow)

        # Connect signals
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def setup_tab_input_nama(self):
        # Tab 1: Input Nama
        self.tab_nama = QtWidgets.QWidget()
        self.tab_nama.setObjectName("tab_nama")

        # Create layout for tab
        self.tab_nama_layout = QtWidgets.QVBoxLayout(self.tab_nama)

        # Add widgets
        self.pushButton_nama = QtWidgets.QPushButton(self.tab_nama)
        self.pushButton_nama.setObjectName("pushButton_nama")
        self.pushButton_nama.setMinimumHeight(40)
        self.pushButton_nama.clicked.connect(self.input_nama)
        self.tab_nama_layout.addWidget(self.pushButton_nama)

        self.label_nama = QtWidgets.QLabel(self.tab_nama)
        self.label_nama.setObjectName("label_nama")
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setMinimumHeight(40)
        self.tab_nama_layout.addWidget(self.label_nama)

        # Add welcome image
        self.welcome_label = QtWidgets.QLabel(self.tab_nama)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setText("👋 Selamat Datang 👋")
        self.welcome_label.setStyleSheet("font-size: 24px; margin-top: 20px;")
        self.tab_nama_layout.addWidget(self.welcome_label)

        # Add to tab widget
        self.tabWidget.addTab(self.tab_nama, "")

    def setup_tab_pilih_font(self):
        # Tab 2: Pilih Font
        self.tab_font = QtWidgets.QWidget()
        self.tab_font.setObjectName("tab_font")

        # Create layout for tab
        self.tab_font_layout = QtWidgets.QVBoxLayout(self.tab_font)

        # Add widgets
        self.pushButton_font = QtWidgets.QPushButton(self.tab_font)
        self.pushButton_font.setObjectName("pushButton_font")
        self.pushButton_font.setMinimumHeight(40)
        self.pushButton_font.clicked.connect(self.pilih_font)
        self.tab_font_layout.addWidget(self.pushButton_font)

        self.label_font = QtWidgets.QLabel(self.tab_font)
        self.label_font.setObjectName("label_font")
        self.label_font.setAlignment(QtCore.Qt.AlignCenter)
        self.label_font.setMinimumHeight(40)
        self.label_font.setText("Nama: ")
        self.tab_font_layout.addWidget(self.label_font)

        # Add font preview
        self.font_preview = QtWidgets.QTextEdit(self.tab_font)
        self.font_preview.setObjectName("font_preview")
        self.font_preview.setPlainText("Ini adalah contoh teks untuk melihat tampilan font yang dipilih.")
        self.font_preview.setReadOnly(True)
        self.tab_font_layout.addWidget(self.font_preview)

        # Add to tab widget
        self.tabWidget.addTab(self.tab_font, "")

    def setup_tab_buka_file(self):
        # Tab 3: Buka File
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")

        # Create layout for tab
        self.tab_file_layout = QtWidgets.QVBoxLayout(self.tab_file)

        # Add control layout
        self.file_control_layout = QtWidgets.QHBoxLayout()

        # Add widgets
        self.pushButton_file = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_file.setObjectName("pushButton_file")
        self.pushButton_file.setMinimumHeight(40)
        self.pushButton_file.clicked.connect(self.buka_file)
        self.file_control_layout.addWidget(self.pushButton_file)

        self.file_path_label = QtWidgets.QLabel(self.tab_file)
        self.file_path_label.setObjectName("file_path_label")
        self.file_path_label.setText("Belum ada file dipilih")
        self.file_control_layout.addWidget(self.file_path_label)

        # Add layout to main tab layout
        self.tab_file_layout.addLayout(self.file_control_layout)

        # Add text browser
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_file)
        self.textBrowser.setObjectName("textBrowser")
        self.tab_file_layout.addWidget(self.textBrowser)

        # Add to tab widget
        self.tabWidget.addTab(self.tab_file, "")

    def setup_tab_ubah_warna(self):
        # Tab 4: Ubah Warna (New Feature)
        self.tab_warna = QtWidgets.QWidget()
        self.tab_warna.setObjectName("tab_warna")

        # Create layout for tab
        self.tab_warna_layout = QtWidgets.QVBoxLayout(self.tab_warna)

        # Add widgets
        self.pushButton_warna = QtWidgets.QPushButton(self.tab_warna)
        self.pushButton_warna.setObjectName("pushButton_warna")
        self.pushButton_warna.setText("Pilih Warna")
        self.pushButton_warna.setMinimumHeight(40)
        self.pushButton_warna.clicked.connect(self.pilih_warna)
        self.tab_warna_layout.addWidget(self.pushButton_warna)

        self.color_preview = QtWidgets.QFrame(self.tab_warna)
        self.color_preview.setObjectName("color_preview")
        self.color_preview.setMinimumHeight(200)
        self.color_preview.setFrameShape(QtWidgets.QFrame.Box)
        self.color_preview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_preview.setStyleSheet("background-color: white;")
        self.tab_warna_layout.addWidget(self.color_preview)

        self.color_value_label = QtWidgets.QLabel(self.tab_warna)
        self.color_value_label.setObjectName("color_value_label")
        self.color_value_label.setText("RGB: 255, 255, 255")
        self.color_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_warna_layout.addWidget(self.color_value_label)

        # Add to tab widget
        self.tabWidget.addTab(self.tab_warna, "Ubah Warna")

    def setup_tab_notepad(self):
        # Tab 5: Simple Notepad (New Feature)
        self.tab_notepad = QtWidgets.QWidget()
        self.tab_notepad.setObjectName("tab_notepad")

        # Create layout for tab
        self.tab_notepad_layout = QtWidgets.QVBoxLayout(self.tab_notepad)

        # Add control buttons
        self.notepad_controls = QtWidgets.QHBoxLayout()

        self.notepad_save_button = QtWidgets.QPushButton(self.tab_notepad)
        self.notepad_save_button.setObjectName("notepad_save_button")
        self.notepad_save_button.setText("Simpan")
        self.notepad_save_button.clicked.connect(self.save_notepad)
        self.notepad_controls.addWidget(self.notepad_save_button)

        self.notepad_clear_button = QtWidgets.QPushButton(self.tab_notepad)
        self.notepad_clear_button.setObjectName("notepad_clear_button")
        self.notepad_clear_button.setText("Bersihkan")
        self.notepad_clear_button.clicked.connect(self.clear_notepad)
        self.notepad_controls.addWidget(self.notepad_clear_button)

        self.tab_notepad_layout.addLayout(self.notepad_controls)

        # Add text editor
        self.notepad_editor = QtWidgets.QTextEdit(self.tab_notepad)
        self.notepad_editor.setObjectName("notepad_editor")
        self.notepad_editor.setPlaceholderText("Tulis catatan Anda di sini...")
        self.tab_notepad_layout.addWidget(self.notepad_editor)

        # Add word count
        self.word_count_label = QtWidgets.QLabel(self.tab_notepad)
        self.word_count_label.setObjectName("word_count_label")
        self.word_count_label.setText("Jumlah kata: 0")
        self.word_count_label.setAlignment(QtCore.Qt.AlignRight)
        self.tab_notepad_layout.addWidget(self.word_count_label)

        # Connect text changed signal
        self.notepad_editor.textChanged.connect(self.update_word_count)

        # Add to tab widget
        self.tabWidget.addTab(self.tab_notepad, "Notepad")

    def setup_menu_bar(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        # File menu
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setTitle("File")

        # Fitur menu
        self.menuFitur = QtWidgets.QMenu(self.menubar)
        self.menuFitur.setObjectName("menuFitur")
        self.menuFitur.setTitle("Fitur")

        # Tema menu (New)
        self.menuTema = QtWidgets.QMenu(self.menubar)
        self.menuTema.setObjectName("menuTema")
        self.menuTema.setTitle("Tema")

        # Bantuan menu (New)
        self.menuBantuan = QtWidgets.QMenu(self.menubar)
        self.menuBantuan.setObjectName("menuBantuan")
        self.menuBantuan.setTitle("Bantuan")

        MainWindow.setMenuBar(self.menubar)

        # File actions
        self.actionKeluar = QtWidgets.QAction(MainWindow)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionKeluar.setText("Keluar")
        self.actionKeluar.triggered.connect(QtWidgets.qApp.quit)
        self.menuFile.addAction(self.actionKeluar)

        # Fitur actions
        self.actionInput_Nama = QtWidgets.QAction(MainWindow)
        self.actionInput_Nama.setObjectName("actionInput_Nama")
        self.actionInput_Nama.setText("Input Nama")
        self.actionInput_Nama.triggered.connect(lambda: self.tabWidget.setCurrentIndex(0))

        self.actionPilih_Font = QtWidgets.QAction(MainWindow)
        self.actionPilih_Font.setObjectName("actionPilih_Font")
        self.actionPilih_Font.setText("Pilih Font")
        self.actionPilih_Font.triggered.connect(lambda: self.tabWidget.setCurrentIndex(1))

        self.actionBuka_File = QtWidgets.QAction(MainWindow)
        self.actionBuka_File.setObjectName("actionBuka_File")
        self.actionBuka_File.setText("Buka File")
        self.actionBuka_File.triggered.connect(lambda: self.tabWidget.setCurrentIndex(2))

        self.actionUbah_Warna = QtWidgets.QAction(MainWindow)
        self.actionUbah_Warna.setObjectName("actionUbah_Warna")
        self.actionUbah_Warna.setText("Ubah Warna")
        self.actionUbah_Warna.triggered.connect(lambda: self.tabWidget.setCurrentIndex(3))

        self.actionNotepad = QtWidgets.QAction(MainWindow)
        self.actionNotepad.setObjectName("actionNotepad")
        self.actionNotepad.setText("Notepad")
        self.actionNotepad.triggered.connect(lambda: self.tabWidget.setCurrentIndex(4))

        self.menuFitur.addAction(self.actionInput_Nama)
        self.menuFitur.addAction(self.actionPilih_Font)
        self.menuFitur.addAction(self.actionBuka_File)
        self.menuFitur.addAction(self.actionUbah_Warna)
        self.menuFitur.addAction(self.actionNotepad)

        # Tema actions
        self.actionTemaTerang = QtWidgets.QAction(MainWindow)
        self.actionTemaTerang.setObjectName("actionTemaTerang")
        self.actionTemaTerang.setText("Tema Terang")
        self.actionTemaTerang.triggered.connect(lambda: self.set_theme("light"))

        self.actionTemaGelap = QtWidgets.QAction(MainWindow)
        self.actionTemaGelap.setObjectName("actionTemaGelap")
        self.actionTemaGelap.setText("Tema Gelap")
        self.actionTemaGelap.triggered.connect(lambda: self.set_theme("dark"))

        self.actionTemaClassic = QtWidgets.QAction(MainWindow)
        self.actionTemaClassic.setObjectName("actionTemaClassic")
        self.actionTemaClassic.setText("Tema Klasik")
        self.actionTemaClassic.triggered.connect(lambda: self.set_theme("classic"))

        self.menuTema.addAction(self.actionTemaTerang)
        self.menuTema.addAction(self.actionTemaGelap)
        self.menuTema.addAction(self.actionTemaClassic)

        # Bantuan actions
        self.actionTentang = QtWidgets.QAction(MainWindow)
        self.actionTentang.setObjectName("actionTentang")
        self.actionTentang.setText("Tentang")
        self.actionTentang.triggered.connect(self.show_about)

        self.menuBantuan.addAction(self.actionTentang)

        # Add menus to menubar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFitur.menuAction())
        self.menubar.addAction(self.menuTema.menuAction())
        self.menubar.addAction(self.menuBantuan.menuAction())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M Ilham Abdul Shaleh (F1D022061) - Aplikasi PyQt5"))

        # Header
        self.headerLabel.setText(_translate("MainWindow", "Tugas Week 9"))

        # Tab 1: Input Nama
        self.pushButton_nama.setText(_translate("MainWindow", "Input Nama"))
        self.label_nama.setText(_translate("MainWindow", "Nama : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nama), _translate("MainWindow", "Input Nama"))

        # Tab 2: Pilih Font
        self.pushButton_font.setText(_translate("MainWindow", "Pilih Font"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_font), _translate("MainWindow", "Pilih Font"))

        # Tab 3: Buka File
        self.pushButton_file.setText(_translate("MainWindow", "Buka File .Txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "Buka File"))

        # Update clock
        self.updateClock()

    def apply_stylesheet(self, MainWindow):
        # Default to light theme
        self.set_theme("light")

    def set_theme(self, theme):
        if theme == "light":
            style = """
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTabWidget::pane {
                border: 1px solid #c0c0c0;
                background-color: #fafafa;
                border-radius: 5px;
            }
            QTabBar::tab {
                background-color: #e0e0e0;
                border: 1px solid #c0c0c0;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                min-width: 100px;
                padding: 8px;
            }
            QTabBar::tab:selected {
                background-color: #ffffff;
                border-bottom: none;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                color: #333333;
            }
            QTextEdit, QTextBrowser {
                border: 1px solid #c0c0c0;
                border-radius: 4px;
                padding: 5px;
                background-color: white;
            }
            QHeaderLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            """
        elif theme == "dark":
            style = """
            QMainWindow {
                background-color: #2c3e50;
            }
            QTabWidget::pane {
                border: 1px solid #34495e;
                background-color: #34495e;
                border-radius: 5px;
            }
            QTabBar::tab {
                background-color: #2c3e50;
                border: 1px solid #34495e;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                min-width: 100px;
                padding: 8px;
                color: #ecf0f1;
            }
            QTabBar::tab:selected {
                background-color: #34495e;
                border-bottom: none;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QLabel {
                color: #ecf0f1;
            }
            QTextEdit, QTextBrowser {
                border: 1px solid #7f8c8d;
                border-radius: 4px;
                padding: 5px;
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QHeaderLabel {
                font-size: 16pt;
                font-weight: bold;
                color: #ecf0f1;
                margin-bottom: 10px;
            }
            QStatusBar {
                background-color: #34495e;
                color: #ecf0f1;
            }
            QMenuBar {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QMenuBar::item {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QMenuBar::item:selected {
                background-color: #34495e;
            }
            QMenu {
                background-color: #2c3e50;
                color: #ecf0f1;
            }
            QMenu::item:selected {
                background-color: #34495e;
            }
            """
        else:  # classic
            style = """
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTabWidget::pane {
                border: 2px solid #c4c4c4;
                background-color: #f5f5f5;
            }
            QTabBar::tab {
                background-color: #e1e1e1;
                border: 1px solid #c4c4c4;
                padding: 5px;
                min-width: 80px;
            }
            QTabBar::tab:selected {
                background-color: #f5f5f5;
                border-bottom: none;
            }
            QPushButton {
                background-color: #e1e1e1;
                border: 1px solid #c4c4c4;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #d4d4d4;
            }
            QHeaderLabel {
                font-size: 14pt;
                font-weight: bold;
                color: #333333;
            }
            """

        # Apply style
        QtWidgets.QApplication.instance().setStyleSheet(style)

    def input_nama(self):
        text, ok = QInputDialog.getText(None, "Input Nama", "Masukkan Nama Anda:")
        if ok and text:
            self.label_nama.setText(f"Nama : {text}")
            # Also update the font tab label
            self.label_font.setText(f"Nama : {text}")
            # Show a welcome message
            QMessageBox.information(None, "Selamat Datang", f"Halo, {text}! Selamat datang di aplikasi PyQt5.")

    def pilih_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_font.setFont(font)
            self.font_preview.setFont(font)

            # Display font info
            font_info = f"Font: {font.family()}, Size: {font.pointSize()}, Weight: {font.weight()}"
            if font.bold():
                font_info += ", Bold"
            if font.italic():
                font_info += ", Italic"

            self.font_preview.setPlaceholderText(font_info)

    def buka_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Buka File .txt", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.textBrowser.setText(content)
                    self.file_path_label.setText(os.path.basename(file_path))

                    # Show file stats
                    lines = content.count('\n') + 1
                    words = len(content.split())
                    chars = len(content)

                    stats = f"Statistik File: {lines} baris, {words} kata, {chars} karakter"
                    self.statusbar.showMessage(stats, 5000)  # Show for 5 seconds
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Gagal membuka file: {str(e)}")

    def pilih_warna(self):
        color = QColorDialog.getColor()
        if color.isValid():
            # Set color to preview frame
            self.color_preview.setStyleSheet(f"background-color: {color.name()};")

            # Update color value label
            self.color_value_label.setText(f"RGB: {color.red()}, {color.green()}, {color.blue()} | Hex: {color.name()}")

    def save_notepad(self):
        text = self.notepad_editor.toPlainText()
        if not text:
            QMessageBox.warning(None, "Perhatian", "Tidak ada teks untuk disimpan.")
            return

        file_path, _ = QFileDialog.getSaveFileName(None, "Simpan File", "", "Text Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
                QMessageBox.information(None, "Berhasil", f"File berhasil disimpan ke {file_path}")
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Gagal menyimpan file: {str(e)}")

    def clear_notepad(self):
        if self.notepad_editor.toPlainText():
            reply = QMessageBox.question(None, "Konfirmasi",
                                         "Anda yakin ingin menghapus semua teks?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.notepad_editor.clear()
        else:
            QMessageBox.information(None, "Info", "Notepad sudah kosong.")

    def update_word_count(self):
        text = self.notepad_editor.toPlainText()
        if text:
            words = len(text.split())
            chars = len(text)
            self.word_count_label.setText(f"Jumlah kata: {words} | Karakter: {chars}")
        else:
            self.word_count_label.setText("Jumlah kata: 0 | Karakter: 0")

    def updateClock(self):
        current_time = QDateTime.currentDateTime()
        display_text = current_time.toString('dd-MM-yyyy hh:mm:ss')
        self.clockLabel.setText(display_text)

    def show_about(self):
        about_text = """
        <h2>Tugas Week 9</h2>
        <p>Dibuat oleh: M Ilham Abdul Shaleh (F1D022061)</p>
        <p>Fitur aplikasi:</p>
        <ul>
            <li>Input nama dengan dialog</li>
            <li>Pengubahan font dan preview</li>
            <li>Pembuka file teks dengan statistik</li>
            <li>Pemilihan warna dengan preview</li>
            <li>Notepad sederhana dengan penghitung kata</li>
            <li>Tema yang dapat diganti</li>
            <li>Tampilan jam real-time</li>
        </ul>
        """
        QMessageBox.about(None, "Tentang Aplikasi", about_text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        """Handle window close event"""
        reply = QMessageBox.question(self, 'Konfirmasi Keluar',
                                     'Anda yakin ingin keluar dari aplikasi?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Set application info
    app.setApplicationName("Week 9")
    app.setOrganizationName("M Ilham Abdul Shaleh")

    # Create and show the main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())