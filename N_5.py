import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class PersonInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Datos Característicos de una Persona")
        self.setGeometry(100, 100, 600, 500)  # Tamaño de la ventana

        # Configurar el fondo negro y colores
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
                margin-bottom: 5px;
            }
            QLineEdit {
                background-color: #444444;
                color: #ffffff;
                font-size: 12px;
                padding: 8px;
                border: 2px solid #ffffff;
                border-radius: 5px;
                margin-bottom: 10px;
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

        # Crear etiquetas y campos para los 10 datos característicos
        self.labels = [
            QLabel("Nombre Completo:"), QLabel("Edad:"), QLabel("Género:"),
            QLabel("Altura (cm):"), QLabel("Peso (kg):"), QLabel("Color de Cabello:"),
            QLabel("Color de Ojos:"), QLabel("Nacionalidad:"), QLabel("Profesión:"),
            QLabel("Hobby favorito:")
        ]
        self.inputs = [QLineEdit() for _ in range(10)]

        # Añadir placeholders para cada campo de entrada
        placeholders = [
            "Ejemplo: Gabriel Alonso Gómez García", "Ejemplo: 22", "Ejemplo: Masculino",
            "Ejemplo: 180", "Ejemplo: 75", "Ejemplo: Castaño",
            "Ejemplo: Marrones", "Ejemplo: Mexicano", "Ejemplo: Ingeniero",
            "Ejemplo: Programar"
        ]
        for i, input_field in enumerate(self.inputs):
            input_field.setPlaceholderText(placeholders[i])

        # Botón para enviar la información
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_person_info)

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout horizontal para organizar los datos en pares
        for i in range(0, 10, 2):
            data_layout = QHBoxLayout()
            
            # Primera columna
            col1_layout = QVBoxLayout()
            col1_layout.addWidget(self.labels[i])
            col1_layout.addWidget(self.inputs[i])

            # Segunda columna (si hay)
            col2_layout = QVBoxLayout()
            col2_layout.addWidget(self.labels[i + 1])
            col2_layout.addWidget(self.inputs[i + 1])

            # Añadir las dos columnas al layout horizontal
            data_layout.addLayout(col1_layout)
            data_layout.addLayout(col2_layout)

            # Añadir el layout al layout principal
            main_layout.addLayout(data_layout)

        # Añadir el botón al layout principal
        main_layout.addWidget(self.submit_button)

        # Establecer el layout principal a la ventana
        self.setLayout(main_layout)

    def show_person_info(self):
        # Obtener y mostrar en consola los datos ingresados
        for i in range(10):
            print(f"{self.labels[i].text()} {self.inputs[i].text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PersonInfoWindow()
    window.show()

    sys.exit(app.exec_())
