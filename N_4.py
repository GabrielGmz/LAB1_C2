import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class PetsWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 500, 400)  # Tamaño de la ventana

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

        # Crear etiquetas y campos para las mascotas
        self.pet_labels = [QLabel(f"Mascota {i+1}") for i in range(3)]
        self.name_inputs = [QLineEdit() for _ in range(3)]
        self.age_inputs = [QLineEdit() for _ in range(3)]
        self.type_inputs = [QLineEdit() for _ in range(3)]

        # Añadir placeholders para los campos de entrada
        for i in range(3):
            self.name_inputs[i].setPlaceholderText("Nombre")
            self.age_inputs[i].setPlaceholderText("Edad")
            self.type_inputs[i].setPlaceholderText("Tipo (e.g., Perro)")

        # Botón para enviar la información
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_pets_info)

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout para cada mascota (alineado horizontalmente)
        for i in range(3):
            pet_layout = QVBoxLayout()
            
            # Crear un layout horizontal para organizar los datos de cada mascota
            name_layout = QHBoxLayout()
            age_layout = QHBoxLayout()
            type_layout = QHBoxLayout()
            
            name_layout.addWidget(QLabel("Nombre:"))
            name_layout.addWidget(self.name_inputs[i])

            age_layout.addWidget(QLabel("Edad:"))
            age_layout.addWidget(self.age_inputs[i])

            type_layout.addWidget(QLabel("Tipo:"))
            type_layout.addWidget(self.type_inputs[i])

            # Añadir la etiqueta de mascota y los campos al layout vertical
            pet_layout.addWidget(self.pet_labels[i])
            pet_layout.addLayout(name_layout)
            pet_layout.addLayout(age_layout)
            pet_layout.addLayout(type_layout)

            # Añadir el layout de cada mascota al layout principal
            main_layout.addLayout(pet_layout)

        # Añadir el botón al layout principal
        main_layout.addWidget(self.submit_button)

        # Establecer el layout principal a la ventana
        self.setLayout(main_layout)

    def show_pets_info(self):
        # Obtener la información ingresada y mostrarla en consola
        for i in range(3):
            name = self.name_inputs[i].text()
            age = self.age_inputs[i].text()
            pet_type = self.type_inputs[i].text()
            print(f"Mascota {i+1}: Nombre: {name}, Edad: {age}, Tipo: {pet_type}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PetsWindow()
    window.show()

    sys.exit(app.exec_())

