import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class SecretWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Clave Secreta")
        self.setGeometry(100, 100, 400, 200)  # Tamaño de la ventana

        # Configurar el fondo negro y colores
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
            }
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #444444;
                color: #ffffff;
                font-size: 14px;
                padding: 8px;
                border: 2px solid #ffffff;
                border-radius: 5px;
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

        # Etiqueta instructiva
        self.label = QLabel("Escriba la clave secreta:")
        self.label.setAlignment(Qt.AlignCenter)

        # Campo de entrada para la clave secreta
        self.secret_input = QLineEdit()
        self.secret_input.setEchoMode(QLineEdit.Password)  # Ocultar caracteres
        self.secret_input.setPlaceholderText("Clave secreta")

        # Botón para enviar la clave
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_secret)

        # Layout para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.secret_input)
        layout.addWidget(self.submit_button)

        # Establecer el layout a la ventana
        self.setLayout(layout)

    def show_secret(self):
        # Obtener el texto ingresado (la clave)
        secret = self.secret_input.text()
        print(f"La clave ingresada es: {secret}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SecretWindow()
    window.show()

    sys.exit(app.exec_())
