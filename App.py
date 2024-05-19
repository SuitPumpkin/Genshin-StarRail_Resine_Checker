import sys
import asyncio
from datetime import datetime, timezone
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import genshin
from qasync import QEventLoop, asyncSlot

correo = ""
contraseña = ""

# Leer el archivo de credenciales
with open("Credenciales.txt", 'r') as file:
    for line in file:
        # Eliminar espacios en blanco alrededor de la línea
        line = line.strip()
        # Comprobar si la línea contiene el correo
        if line.startswith('u:'):
            correo = line[2:].strip()
        # Comprobar si la línea contiene la contraseña
        elif line.startswith('c:'):
            contraseña = line[2:].strip()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icon = QIcon("Icono.png")
        self.setWindowIcon(icon)
        # Establecer las dimensiones de la ventana y evitar que se pueda redimensionar
        self.setFixedSize(800, 300)
        self.setWindowTitle("Resine Checker")

        # Crear el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #262626;")

        # Crear el layout principal como QVBoxLayout
        main_layout = QVBoxLayout()

        # Crear la sección superior
        upper_layout = QHBoxLayout()

        # Crear la primera sección (Genshin Impact)
        section1 = QWidget()
        section1_layout = QVBoxLayout()
        section1.setLayout(section1_layout)

        # Icono Genshin Impact
        icon_genshin = QLabel()
        pixmap_genshin = QPixmap("icono-genshin.png").scaled(400, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Doble de tamaño
        icon_genshin.setPixmap(pixmap_genshin)
        icon_genshin.setAlignment(Qt.AlignCenter)
        icon_genshin.setStyleSheet("margin-top: 20px; margin-bottom: 20px;")
        section1_layout.addWidget(icon_genshin)

        # Información de Genshin Impact
        self.genshin_resin_label = QLabel()
        self.genshin_resin_label.setStyleSheet("color: white;")
        self.genshin_resin_label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        section1_layout.addWidget(self.genshin_resin_label)

        self.genshin_tea_label = QLabel()
        self.genshin_tea_label.setStyleSheet("color: white;")
        self.genshin_tea_label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        section1_layout.addWidget(self.genshin_tea_label)

        self.genshin_missions_label = QLabel()
        self.genshin_missions_label.setStyleSheet("color: white;")
        self.genshin_missions_label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        section1_layout.addWidget(self.genshin_missions_label)

        # Crear la segunda sección (Honkai Star Rail)
        section2 = QWidget()
        section2_layout = QVBoxLayout()
        section2.setLayout(section2_layout)

        # Icono Honkai Star Rail
        icon_star_rail = QLabel()
        pixmap_star_rail = QPixmap("icono-star-rail.png").scaled(400, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Doble de tamaño
        icon_star_rail.setPixmap(pixmap_star_rail)
        icon_star_rail.setAlignment(Qt.AlignCenter)
        section2_layout.addWidget(icon_star_rail)

        # Información de Honkai Star Rail
        self.star_rail_power_label = QLabel()
        self.star_rail_power_label.setStyleSheet("color: white;")
        self.star_rail_power_label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        section2_layout.addWidget(self.star_rail_power_label)

        self.star_rail_train_label = QLabel()
        self.star_rail_train_label.setStyleSheet("color: white;")
        self.star_rail_train_label.setAlignment(Qt.AlignCenter)  # Centrar horizontalmente
        section2_layout.addWidget(self.star_rail_train_label)

        # Añadir las secciones al layout superior
        upper_layout.addWidget(section1)
        upper_layout.addWidget(section2)

        # Añadir el layout superior al layout principal
        main_layout.addLayout(upper_layout)

        # Añadir el botón de Actualizar centrado horizontalmente debajo de las secciones
        update_button = QPushButton("Actualizar")
        update_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 14px;")
        update_button.clicked.connect(self.update_info)
        main_layout.addWidget(update_button, alignment=Qt.AlignHCenter)

        # Establecer el layout principal en el widget central
        central_widget.setLayout(main_layout)

        # Obtener la información de Genshin Impact y Honkai Star Rail
        asyncio.ensure_future(self.get_game_info())

    @asyncSlot()
    async def get_game_info(self):
        email = correo
        password = contraseña
        client = genshin.Client()

        try:
            await client.login_with_password(email, password)
            
            # Obtener información de Genshin Impact
            genshin_info = await client.get_notes()
            # Obtener información de Honkai Star Rail
            star_rail_info = await client.get_starrail_notes()

            now = datetime.now(timezone.utc)

            # Formatear la información
            self.genshin_resin_label.setText(f"Resina: {genshin_info.current_resin}/{genshin_info.max_resin} Se llena en: {genshin_info.resin_recovery_time - now}")
            self.genshin_tea_label.setText(f"Tetera: {genshin_info.current_realm_currency}/{genshin_info.max_realm_currency} Se llena en: {genshin_info.realm_currency_recovery_time - now}")
            self.genshin_missions_label.setText(f"Misiones completas: {genshin_info.completed_commissions}/{genshin_info.max_commissions}")
            self.star_rail_power_label.setText(f"Poder de Trazacaminos: {star_rail_info.current_stamina}/{star_rail_info.max_stamina} Se llena en: {star_rail_info.stamina_recovery_time - now}")
            self.star_rail_train_label.setText(f"Entrenamiento diario completado: {star_rail_info.current_train_score//100}/{star_rail_info.max_train_score//100}")
            
        except Exception as e:
            self.genshin_resin_label.setText(f"Error al obtener la información: {str(e)}")
            self.genshin_tea_label.setText("")
            self.genshin_missions_label.setText("")
            self.star_rail_power_label.setText(f"Error al obtener la información: {str(e)}")
            self.star_rail_train_label.setText("")

    def update_info(self):
        self.genshin_resin_label.setText("Obteniendo información...")
        self.genshin_tea_label.setText("")
        self.genshin_missions_label.setText("")
        self.star_rail_power_label.setText("Obteniendo información...")
        self.star_rail_train_label.setText("")
        asyncio.ensure_future(self.get_game_info())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()
