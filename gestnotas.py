import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QCheckBox, QScrollArea, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QDateEdit, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QPlainTextEdit, QScrollArea, QFrame
from PySide6.QtCore import Qt, QDate, QTime
import sqlite3

class Gestnotas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escola Deus me Chama")
        self.initUI()
    
    def calculation(self):
        self.value = self.final_grade_input.currentText()
        self.result_grade = (self.first_bimester_input.value() + self.second_bimester_input.value() + self.third_bimester_input.value() + self.fourth_bimester_input.value()) / 4
        self.final_grade_label.setText(f"Média Final: {self.result_grade}")
        if self.result_grade <= 5:
            QMessageBox.about(self, "Resultado", f"Reprovado! Sua média final foi {self.result_grade}")
        else:
            QMessageBox.about(self, "Resultado", f"Aprovado! Sua média final foi {self.result_grade}")
        print (self.result_grade)
    
    def grade_registration(self):
    # Get the values from the inputs and final grade calculation and insert them into the database
        self.year = self.year_input.currentText()
        self.student_id = self.student_id_input.currentText()
        self.student_name = self.student_name_input.currentText()
        self.subject = self.subject_input.currentText()
        self.first_bimester = self.first_bimester_input.value()
        self.second_bimester = self.second_bimester_input.value()
        self.third_bimester = self.third_bimester_input.value()
        self.fourth_bimester = self.fourth_bimester_input.value()
        self.final_grade = self.result_grade
        
        conn = sqlite3.connect('esc_deus_ch.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO NOTAS (ANOREF, DISCIPLINA, ID_ALUNO, NOME, NOTA_1, NOTA_2, NOTA_3, NOTA_4, MEDIA_FINAL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.year, self.subject, self.student_id, self.student_name, self.first_bimester, self.second_bimester, self.third_bimester, self.fourth_bimester, self.final_grade))
        conn.commit()
        conn.close()
        if cursor.rowcount > 0:
            QMessageBox.about(self, "Resultado", "Notas registradas com sucesso!")
        else:
            QMessageBox.about(self, "Resultado", "Erro ao registrar notas! Tente novamente")
    


    
    def initUI(self):
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle("Escola Deus me Chama")
        
        self.message_label = QLabel("Insira os dados para cálculo da média anual:")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.main_layout.addWidget(self.message_label)
        
        self.year_label = QLabel("Ano:")
        self.year_label.setAlignment(Qt.AlignCenter)
        self.year_label.setWordWrap(True)
        self.main_layout.addWidget(self.year_label)
        self.year_input = QComboBox()
        self.year_input.addItems(["2021", "2022", "2023", "2024", "2025"])
        self.main_layout.addWidget(self.year_input)
        
        self.student_id_label = QLabel("Matrícula:")
        self.student_id_label.setAlignment(Qt.AlignCenter)
        self.student_id_label.setWordWrap(True)
        self.main_layout.addWidget(self.student_id_label)
        self.student_id_input = QComboBox()
        self.student_id_input.setEditable(True)
        conn = sqlite3.connect('esc_deus_ch.db')
        cursor = conn.cursor()
        cursor.execute("SELECT MATRICULA FROM ALUNOS")
        results = cursor.fetchall()
        for row in results:
            self.student_id_input.addItem(str(row[0]))
        self.main_layout.addWidget(self.student_id_input)

        self.student_name_label = QLabel("Nome:")
        self.student_name_label.setAlignment(Qt.AlignCenter)
        self.student_name_label.setWordWrap(True)
        self.main_layout.addWidget(self.student_name_label)
        self.student_name_input = QComboBox()
        self.student_name_input.setEditable(True)
        # Update the student name input according to the student id input trough the database
        conn = sqlite3.connect('esc_deus_ch.db')
        cursor = conn.cursor()
        cursor.execute("SELECT NOME FROM ALUNOS WHERE MATRICULA = ?", (self.student_id_input.currentText(),))
        results = cursor.fetchall()
        for row in results:
            self.student_name_input.addItem(str(row[0]))
        self.main_layout.addWidget(self.student_name_input)
        
        
        self.subject_label = QLabel("Disciplina:")
        self.subject_label.setAlignment(Qt.AlignCenter)
        self.subject_label.setWordWrap(True)
        self.main_layout.addWidget(self.subject_label)
        self.subject_input = QComboBox()
        self.subject_input.addItems(["Português", "Matemática", "História", "Geografia", "Ciências", "Inglês", "Educação Física", "Artes"])
        self.main_layout.addWidget(self.subject_input)

        self.first_bimester_label = QLabel("1º Bimestre:")
        self.first_bimester_label.setAlignment(Qt.AlignCenter)
        self.first_bimester_label.setWordWrap(True)
        self.main_layout.addWidget(self.first_bimester_label)
        self.first_bimester_input = QDoubleSpinBox()
        self.first_bimester_input.setRange(0, 10)
        self.first_bimester_input.setDecimals(2)
        self.first_bimester_input.setSingleStep(0.1)
        self.main_layout.addWidget(self.first_bimester_input)
        
        self.second_bimester_label = QLabel("2º Bimestre:")
        self.second_bimester_label.setAlignment(Qt.AlignCenter)
        self.second_bimester_label.setWordWrap(True)
        self.main_layout.addWidget(self.second_bimester_label)
        self.second_bimester_input = QDoubleSpinBox()
        self.second_bimester_input.setRange(0, 10)
        self.second_bimester_input.setDecimals(2)
        self.second_bimester_input.setSingleStep(0.1)
        self.main_layout.addWidget(self.second_bimester_input)
        
        self.third_bimester_label = QLabel("3º Bimestre:")
        self.third_bimester_label.setAlignment(Qt.AlignCenter)
        self.third_bimester_label.setWordWrap(True)
        self.main_layout.addWidget(self.third_bimester_label)
        self.third_bimester_input = QDoubleSpinBox()
        self.third_bimester_input.setRange(0, 10)
        self.third_bimester_input.setDecimals(2)
        self.third_bimester_input.setSingleStep(0.1)
        self.main_layout.addWidget(self.third_bimester_input)
        
        self.fourth_bimester_label = QLabel("4º Bimestre:")
        self.fourth_bimester_label.setAlignment(Qt.AlignCenter)
        self.fourth_bimester_label.setWordWrap(True)
        self.main_layout.addWidget(self.fourth_bimester_label)
        self.fourth_bimester_input = QDoubleSpinBox()
        self.fourth_bimester_input.setRange(0, 10)
        self.fourth_bimester_input.setDecimals(2)
        self.fourth_bimester_input.setSingleStep(0.1)
        self.main_layout.addWidget(self.fourth_bimester_input)
        
        self.final_grade_label = QLabel("Média Final:")
        self.final_grade_label.setAlignment(Qt.AlignCenter)
        self.final_grade_label.setWordWrap(True)
        self.main_layout.addWidget(self.final_grade_label)
        self.final_grade_input = QComboBox()
        self.main_layout.addWidget(self.final_grade_input)
        
        self.calculate_button = QPushButton("Calcular Média")
        self.calculate_button.clicked.connect(self.calculation)
        self.main_layout.addWidget(self.calculate_button)
        
        self.register_button = QPushButton("Registrar Notas")
        self.register_button.clicked.connect(self.grade_registration)
        self.main_layout.addWidget(self.register_button)

        
if __name__ == "__main__":
    app = QApplication([])
    window = Gestnotas()
    window.show()
    app.exec()

        
        
              
                                 
                        
        