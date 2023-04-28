import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QCheckBox, QScrollArea, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame
from PySide6.QtCore import Qt, QDate, QTime
import sqlite3

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escola Deus me Chama")
        self.initUI()


        
    def initUI(self):
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle("Escola Deus me Chama")
        self.message_label = QLabel("Bem vindo(a) ao sistema de gerenciamento de notas da Escola Deus me Chama!\nPara continuar, faça login.")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.main_layout.addWidget(self.message_label)
        self.login_button = QPushButton("Fazer Login")
        self.login_button.clicked.connect(self.login_dialog)
        self.main_layout.addWidget(self.login_button)


    def login_dialog(self): # Janela de login
        login_dialog = QDialog()
        login_dialog.setWindowTitle('Fazer Login') # Título da janela
        login_dialog.setWindowFlag(Qt.WindowCloseButtonHint, True)
        login_layout = QVBoxLayout()
        
        self.username_label = QLabel("Usuário:") # Label do usuário
        login_layout.addWidget(self.username_label)
        self.username = QComboBox() # Campo de texto para o usuário
        self.username.setEditable(True)
        login_layout.addWidget(self.username)
        # Create a connection to the database and populate a variable with the usernames
        connection = sqlite3.connect("esc_deus_ch.db")
        cursor = connection.cursor()
        cursor.execute("SELECT USERNAME FROM USERS")
        result = cursor.fetchall()
        connection.close()
        for username in result:
            self.username.addItem(username[0])
        
        self.password_label = QLabel("Senha:") # Label da senha
        login_layout.addWidget(self.password_label)
        self.password = QLineEdit() # Campo de texto para a senha
        self.password.setEchoMode(QLineEdit.Password)
        login_layout.addWidget(self.password)
        # Create a connection to the database and populate it with the passwords that match user input
        connection = sqlite3.connect("esc_deus_ch.db")
        cursor = connection.cursor()
        cursor.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = ?", (self.username.currentText(),))
        result = cursor.fetchall()
        connection.close()
        for password in result:
            self.password.setText(password[0])

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) # Botões de OK e Cancelar
        button_box.accepted.connect(login_dialog.accept)
        button_box.rejected.connect(login_dialog.reject)
        login_layout.addWidget(button_box)
        
        self.change_password_button = QPushButton("Alterar Senha") # Botão para alterar a senha
        self.change_password_button.clicked.connect(self.change_password_dialog)
        login_layout.addWidget(self.change_password_button) # Adiciona o botão alterar senha ao layout
        
        self.create_user_button = QPushButton("Criar Usuário") # Botão para criar um novo usuário
        self.create_user_button.clicked.connect(self.create_user_dialog)
        login_layout.addWidget(self.create_user_button) # Adiciona o botão criar usuário ao layout
        
        login_dialog.setLayout(login_layout)
        
        connection = sqlite3.connect("esc_deus_ch.db")
        cursor = connection.cursor()
        cursor.execute("SELECT USERNAME FROM USERS WHERE USERNAME = ?", (self.username.currentText(),))
        result_username = cursor.fetchall()
        connection = sqlite3.connect("esc_deus_ch.db")
        cursor = connection.cursor()
        cursor.execute("SELECT PASSWORD FROM USERS WHERE PASSWORD = ?", (self.password.text(),))
        result_password = cursor.fetchall()
        connection.close()
        
        result_login = login_dialog.exec()
        
        # Se o usuário clicar em OK e os resultados  forem iguais, o login é feito com sucesso e retorna para a janela principal
        if result_login == QDialog.Accepted and result_username == result_password:
            self.message_label.setText("Login efetuado com sucesso!")
            return self.initUI()
        
        # Se o usuário clicar em OK e os resultados forem diferentes, o login não é feito
        elif result_login == QDialog.Accepted and result_username != result_password:
            self.message_label.setText("Usuário ou senha incorretos!")
            return self.initUI()
        
        
        
        
        
        
        
        
    def create_user_dialog(self): # Criar um novo usuário
        pass
    
    def change_password_dialog(self): # Alterar a senha
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
    
    

        
        
