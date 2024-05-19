import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Creamos una subclase de la clase QWidget para nuestra ventana principal
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Creamos un layout vertical para organizar los widgets
        layout = QVBoxLayout()

        # Creamos un botón
        boton = QPushButton('Haz clic aquí', self)

        # Conectamos la señal "clicked" del botón a un método
        boton.clicked.connect(self.on_button_clicked)

        # Añadimos el botón al layout
        layout.addWidget(boton)

        # Establecemos el layout para nuestra ventana
        self.setLayout(layout)

    # Método que se ejecutará cuando se haga clic en el botón
    def on_button_clicked(self):
        print('¡Has hecho clic en el botón!')

if __name__ == '__main__':
    # Creamos una instancia de QApplication, que maneja la aplicación
    app = QApplication(sys.argv)

    # Creamos una instancia de nuestra ventana personalizada
    ventana = MiVentana()

    # Mostramos la ventana
    ventana.show()

    # Ejecutamos el bucle de eventos de la aplicación
    sys.exit(app.exec_())
