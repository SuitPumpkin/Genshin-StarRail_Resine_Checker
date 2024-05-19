import sys
import asyncio
from datetime import datetime, timezone
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
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

        # Establecer las dimensiones de la ventana y evitar que se pueda redimensionar
        self.setFixedSize(800, 500)
        self.setWindowTitle("Resine Checker")

        # Crear el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #262626;")

        # Crear el layout horizontal
        main_layout = QHBoxLayout()

        # Crear la primera sección
        section1 = QWidget()
        section1.setFixedSize(400, 500)
        section1_layout = QVBoxLayout()
        section1_label = QLabel("Genshin Impact")
        section1_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        section1_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        section1_layout.addWidget(section1_label)

        # Información de Genshin Impact
        self.genshin_impact_info_label = QLabel("Obteniendo información...")
        self.genshin_impact_info_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.genshin_impact_info_label.setStyleSheet("color: white;")
        section1_layout.addWidget(self.genshin_impact_info_label)

        section1_layout.addStretch(1)  # Para empujar el label hacia la parte superior
        section1.setLayout(section1_layout)
        section1.setStyleSheet("background-color: #262626; color: white;")

        # Crear la división
        divider = QFrame()
        divider.setFrameShape(QFrame.VLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("background-color: #767676; width: 2px;")

        # Crear la segunda sección
        section2 = QWidget()
        section2.setFixedSize(400, 500)
        section2_layout = QVBoxLayout()
        section2_label = QLabel("Honkai Star Rail")
        section2_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        section2_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        section2_layout.addWidget(section2_label)

        # Información de Honkai Star Rail
        self.star_rail_info_label = QLabel("Obteniendo información...")
        self.star_rail_info_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.star_rail_info_label.setStyleSheet("color: white;")
        section2_layout.addWidget(self.star_rail_info_label)

        section2_layout.addStretch(1)  # Para empujar el label hacia la parte superior
        section2.setLayout(section2_layout)
        section2.setStyleSheet("background-color: #262626; color: white;")

        # Añadir las secciones y el divisor al layout principal
        main_layout.addWidget(section1)
        main_layout.addWidget(divider)
        main_layout.addWidget(section2)

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
            genshin_text = (
                f"Resina Actual: {genshin_info.current_resin}/{genshin_info.max_resin}\n"
                f"Resina llena en: {genshin_info.resin_recovery_time - now}\n"
                f"Misiones Diarias Completadas: {genshin_info.completed_commissions}/{genshin_info.max_commissions}\n"
                f"Dinero de la Relajatetera: {genshin_info.current_realm_currency}/{genshin_info.max_realm_currency}\n"
                f"Relajatetera llena en: {genshin_info.realm_currency_recovery_time - now}\n"
            )

            star_rail_text = (
                f"Poder de trazacaminos actual: {star_rail_info.current_stamina}/{star_rail_info.max_stamina}\n"
                f"Tiempo para llenarse: {star_rail_info.stamina_recover_time}\n"
                f"Entrenamiento diario completado: {star_rail_info.current_train_score//100}/{star_rail_info.max_train_score//100}"
            )

            # Actualizar las etiquetas con la información
            self.genshin_impact_info_label.setText(genshin_text)
            self.star_rail_info_label.setText(star_rail_text)
        except Exception as e:
            self.genshin_impact_info_label.setText(f"Error al obtener la información: {str(e)}")
            self.star_rail_info_label.setText(f"Error al obtener la información: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()
