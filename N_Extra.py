import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class CustomFormWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Selección de Categoría y Valor")
        self.setGeometry(100, 100, 500, 300)  # Tamaño de la ventana

        # Configuración del fondo negro y colores
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
                margin-bottom: 5px;
            }
            QComboBox, QSpinBox {
                background-color: #FFFFFF;
                color: #000000;
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

        # Etiqueta para seleccionar categoría
        self.category_label = QLabel("Seleccione una categoría:")
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(["...", "Terror", "Comedia", "Romance", "Suspenso"])

        # Etiqueta para seleccionar un número con el SpinBox
        self.number_label = QLabel("Seleccione un número:")
        self.number_spinbox = QSpinBox()
        self.number_spinbox.setRange(0, 100)  # Rango de valores permitidos

        # Botón para enviar los datos
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_selected_info)

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout para organizar la categoría
        category_layout = QVBoxLayout()
        category_layout.addWidget(self.category_label)
        category_layout.addWidget(self.category_combobox)

        # Layout para organizar el número
        number_layout = QVBoxLayout()
        number_layout.addWidget(self.number_label)
        number_layout.addWidget(self.number_spinbox)

        # Añadir layouts al layout principal
        main_layout.addLayout(category_layout)
        main_layout.addLayout(number_layout)
        main_layout.addWidget(self.submit_button)

        # Establecer el layout principal en la ventana
        self.setLayout(main_layout)

    def show_selected_info(self):
        # Obtener la categoría seleccionada y el valor del SpinBox
        selected_category = self.category_combobox.currentText()
        selected_number = self.number_spinbox.value()
        
        # Mostrar en consola los valores seleccionados
        print(f"Categoría seleccionada: {selected_category}")
        print(f"Valor seleccionado: {selected_number}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CustomFormWindow()
    window.show()

    sys.exit(app.exec_())
