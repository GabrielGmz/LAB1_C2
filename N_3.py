import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Ingrese Su Información")
        self.setGeometry(100, 100, 400, 250)  # Tamaño de la ventana

        # Configurar el fondo negro y colores
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
            }
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QLineEdit {
                background-color: #444444;
                color: #ffffff;
                font-size: 14px;
                padding: 8px;
                border: 2px solid #ffffff;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            QPushButton {
                background-color: #6702ED;
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #B402ED;
            }
        """)

        # Etiquetas y campos de entrada
        self.cedula_label = QLabel("Número de Cédula:")
        self.name_label = QLabel("Nombre Completo:")

        self.cedula_input = QLineEdit()
        self.cedula_input.setPlaceholderText("Ingrese su número de cédula")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ingrese su nombre completo")

        # Botón para enviar la información
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_info)

        # Layout para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)

        # Establecer el layout a la ventana
        self.setLayout(layout)

    def show_info(self):
        # Obtener el texto ingresado
        cedula = self.cedula_input.text()
        name = self.name_input.text()
        # Aquí podrías agregar el código para procesar la información
        print(f"Número de Cédula: {cedula}")
        print(f"Nombre Completo: {name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = InfoWindow()
    window.show()

    sys.exit(app.exec_())
