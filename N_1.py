import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Mi Información Personal")
        self.setGeometry(100, 100, 400, 200)  # Establecer tamaño de la ventana

        # Crear etiquetas para el nombre y la edad
        self.name_label = QLabel("Gabriel Alonso Gómez García")
        self.age_label = QLabel("22 Años")

        # Alinear el texto en el centro
        self.name_label.setAlignment(Qt.AlignCenter)
        self.age_label.setAlignment(Qt.AlignCenter)

        # Añadir estilo para mejorar la apariencia
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
            }
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #ffffff;
                padding: 2px;
            }
            QLabel:hover{
                color: #fff222;
            }
        """)

        # Layout para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.age_label)

        # Establecer el layout a la ventana
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
