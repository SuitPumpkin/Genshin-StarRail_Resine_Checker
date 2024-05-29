from PyQt5 import QtCore, QtGui, QtWidgets
import Recursos_rc
import asyncio
import genshin
from qasync import QEventLoop, asyncSlot
from datetime import datetime, timezone, timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
import sys

# Leer el archivo de credenciales
with open("HoyoCredentials.txt", 'r') as file:
    for line in file:
        # Eliminar espacios en blanco alrededor de la línea
        line = line.strip()
        # Comprobar si la línea contiene el correo
        if line.startswith('m:'):
            correo = line[2:].strip()
        # Comprobar si la línea contiene la contraseña
        elif line.startswith('p:'):
            contraseña = line[2:].strip()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:#262626;")
        self.centralwidget.setObjectName("centralwidget")
        self.Genshin = QtWidgets.QWidget(self.centralwidget)
        self.Genshin.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.Genshin.setObjectName("Genshin")
        self.Foto = QtWidgets.QLabel(self.Genshin)
        self.Foto.setGeometry(QtCore.QRect(30, 10, 341, 151))
        self.Foto.setObjectName("Foto")
        self.InfoResina = QtWidgets.QWidget(self.Genshin)
        self.InfoResina.setGeometry(QtCore.QRect(80, 180, 221, 61))
        self.InfoResina.setObjectName("InfoResina")
        self.Icono1 = QtWidgets.QLabel(self.InfoResina)
        self.Icono1.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.Icono1.setObjectName("Icono1")
        self.TiempoResina = QtWidgets.QLabel(self.InfoResina)
        self.TiempoResina.setGeometry(QtCore.QRect(65, 35, 171, 21))
        self.TiempoResina.setObjectName("TiempoResina")
        self.Resina = QtWidgets.QLabel(self.InfoResina)
        self.Resina.setGeometry(QtCore.QRect(65, 5, 71, 31))
        self.Resina.setObjectName("Resina")
        self.InfoTetera = QtWidgets.QWidget(self.Genshin)
        self.InfoTetera.setGeometry(QtCore.QRect(80, 240, 221, 61))
        self.InfoTetera.setObjectName("InfoTetera")
        self.Icono2 = QtWidgets.QLabel(self.InfoTetera)
        self.Icono2.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.Icono2.setObjectName("Icono2")
        self.TiempoTetera = QtWidgets.QLabel(self.InfoTetera)
        self.TiempoTetera.setGeometry(QtCore.QRect(65, 35, 171, 21))
        self.TiempoTetera.setObjectName("TiempoTetera")
        self.Tetera = QtWidgets.QLabel(self.InfoTetera)
        self.Tetera.setGeometry(QtCore.QRect(65, 5, 100, 31))
        self.Tetera.setObjectName("Tetera")
        self.InfoDiarias = QtWidgets.QWidget(self.Genshin)
        self.InfoDiarias.setGeometry(QtCore.QRect(80, 300, 221, 61))
        self.InfoDiarias.setObjectName("InfoDiarias")
        self.Icono3 = QtWidgets.QLabel(self.InfoDiarias)
        self.Icono3.setGeometry(QtCore.QRect(15, 0, 41, 61))
        self.Icono3.setObjectName("Icono3")
        self.TiempoDiariasGenshin = QtWidgets.QLabel(self.InfoDiarias)
        self.TiempoDiariasGenshin.setGeometry(QtCore.QRect(65, 35, 171, 21))
        self.TiempoDiariasGenshin.setObjectName("TiempoDiariasGenshin")
        self.DiariasGenshin = QtWidgets.QLabel(self.InfoDiarias)
        self.DiariasGenshin.setGeometry(QtCore.QRect(65, 5, 71, 31))
        self.DiariasGenshin.setObjectName("DiariasGenshin")
        self.LogginDiario = QtWidgets.QWidget(self.Genshin)
        self.LogginDiario.setGeometry(QtCore.QRect(140, 370, 120, 71))
        self.LogginDiario.setObjectName("LogginDiario")
        self.Texto = QtWidgets.QLabel(self.LogginDiario)
        self.Texto.setGeometry(QtCore.QRect(5, 0, 111, 31))
        self.Texto.setObjectName("Texto")
        self.ReclamarLogginGenshin = QtWidgets.QPushButton(self.LogginDiario)
        self.ReclamarLogginGenshin.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.ReclamarLogginGenshin.setStyleSheet("background: white;")
        self.ReclamarLogginGenshin.setObjectName("ReclamarLogginGenshin")
        self.StarRail = QtWidgets.QWidget(self.centralwidget)
        self.StarRail.setGeometry(QtCore.QRect(400, 0, 400, 500))
        self.StarRail.setStyleSheet("background: #262626;")
        self.StarRail.setObjectName("StarRail")
        self.Foto_2 = QtWidgets.QLabel(self.StarRail)
        self.Foto_2.setGeometry(QtCore.QRect(20, 0, 351, 181))
        self.Foto_2.setObjectName("Foto_2")
        self.InfoResina_2 = QtWidgets.QWidget(self.StarRail)
        self.InfoResina_2.setGeometry(QtCore.QRect(100, 200, 221, 61))
        self.InfoResina_2.setObjectName("InfoResina_2")
        self.Icono1_2 = QtWidgets.QLabel(self.InfoResina_2)
        self.Icono1_2.setGeometry(QtCore.QRect(5, 0, 61, 61))
        self.Icono1_2.setObjectName("Icono1_2")
        self.TiempoResina_2 = QtWidgets.QLabel(self.InfoResina_2)
        self.TiempoResina_2.setGeometry(QtCore.QRect(65, 35, 171, 21))
        self.TiempoResina_2.setObjectName("TiempoResina_2")
        self.Resina_2 = QtWidgets.QLabel(self.InfoResina_2)
        self.Resina_2.setGeometry(QtCore.QRect(65, 5, 71, 31))
        self.Resina_2.setObjectName("Resina_2")
        self.LogginDiario_2 = QtWidgets.QWidget(self.StarRail)
        self.LogginDiario_2.setGeometry(QtCore.QRect(160, 330, 120, 71))
        self.LogginDiario_2.setObjectName("LogginDiario_2")
        self.Texto_2 = QtWidgets.QLabel(self.LogginDiario_2)
        self.Texto_2.setGeometry(QtCore.QRect(5, 0, 111, 31))
        self.Texto_2.setObjectName("Texto_2")
        self.ReclamarLogginStarRail = QtWidgets.QPushButton(self.LogginDiario_2)
        self.ReclamarLogginStarRail.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.ReclamarLogginStarRail.setStyleSheet("background: white;")
        self.ReclamarLogginStarRail.setObjectName("ReclamarLogginStarRail")
        self.InfoDiarias_2 = QtWidgets.QWidget(self.StarRail)
        self.InfoDiarias_2.setGeometry(QtCore.QRect(100, 260, 221, 61))
        self.InfoDiarias_2.setObjectName("InfoDiarias_2")
        self.Icono4 = QtWidgets.QLabel(self.InfoDiarias_2)
        self.Icono4.setGeometry(QtCore.QRect(15, 0, 41, 61))
        self.Icono4.setObjectName("Icono4")
        self.TiempoDiariasStarRail = QtWidgets.QLabel(self.InfoDiarias_2)
        self.TiempoDiariasStarRail.setGeometry(QtCore.QRect(65, 35, 171, 21))
        self.TiempoDiariasStarRail.setObjectName("TiempoDiariasStarRail")
        self.DiariasStarRail = QtWidgets.QLabel(self.InfoDiarias_2)
        self.DiariasStarRail.setGeometry(QtCore.QRect(65, 5, 71, 31))
        self.DiariasStarRail.setObjectName("DiariasStarRail")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(398, 0, 4, 500))
        self.line.setStyleSheet("background: gray;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ActualizarInfo = QtWidgets.QPushButton(self.centralwidget)
        self.ActualizarInfo.setGeometry(QtCore.QRect(360, 460, 75, 23))
        self.ActualizarInfo.setStyleSheet("background: white;")
        self.ActualizarInfo.setObjectName("ActualizarInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        # Obtener la información de Genshin Impact y Honkai Star Rail
        asyncio.ensure_future(self.get_game_info()) 
        #Configurar el temporizador
        self.timer = QTimer()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reclamar_login_genshin(self):
        self.ReclamarLogginGenshin.clicked.disconnect(self.reclamar_login_genshin) #desactivo el botón para evitar spam
        asyncio.ensure_future(self.logingenshin())
    async def logingenshin(self):
        client = genshin.Client()
        await client.login_with_password(correo, contraseña)
        client.default_game = genshin.Game.GENSHIN
        alerta = QMessageBox()
        # claim daily reward
        try:
            reward = await client.claim_daily_reward()
        except genshin.AlreadyClaimed:
            alerta.setWindowTitle("Claimed")
            alerta.setText("Allready Claimed")
            alerta.setIcon(QMessageBox.Information)
            alerta.setStandardButtons(QMessageBox.Ok)
            alerta.exec_()
        else:
            alerta.setWindowTitle("Claimed")
            alerta.setText(f"Claimed {reward.amount}x {reward.name}")
            alerta.setIcon(QMessageBox.Information)
            alerta.setStandardButtons(QMessageBox.Ok)
            alerta.exec_()
    def reclamar_login_starrail(self):
        self.ReclamarLogginStarRail.clicked.disconnect(self.reclamar_login_starrail) #desactivo el botón para evitar spam
        asyncio.ensure_future(self.logingenshin())
    async def loginstarrail(self):
        client = genshin.Client()
        await client.login_with_password(correo, contraseña)
        client.default_game = genshin.Game.STARRAIL
        alerta = QMessageBox()
        # claim daily reward
        try:
            reward = await client.claim_daily_reward()
        except genshin.AlreadyClaimed:
            alerta.setWindowTitle("Claimed")
            alerta.setText("Allready Claimed")
            alerta.setIcon(QMessageBox.Information)
            alerta.setStandardButtons(QMessageBox.Ok)
            alerta.exec_()
        else:
            alerta.setWindowTitle("Claimed")
            alerta.setText(f"Claimed {reward.amount}x {reward.name}")
            alerta.setIcon(QMessageBox.Information)
            alerta.setStandardButtons(QMessageBox.Ok)
            alerta.exec_()
    def actualizar_info(self):
        self.ActualizarInfo.clicked.disconnect(self.actualizar_info) #desactivo el botón para evitar spam
        self.timer.stop()
        # Formatear la información
        self.set_resina_info("0/160","fills in: 0:0:0")
        self.set_tetera_info(f"0/2400","fills in: 0:0:0")
        self.set_diarias_genshin_info(f"0/4","Resets in 0:0:0")
        self.set_resina_2_info(f"0/240","fills in: 0:0:0")
        self.set_diarias_star_rail_info(f"0/5","Resets in 0:0:0")

        asyncio.ensure_future(self.get_game_info())

    def set_resina_info(self, resina_value, tiempo_resina_value):
        self.Resina.setText(f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">{resina_value}</span></p></body></html>")
        self.TiempoResina.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">{tiempo_resina_value}</span></p></body></html>")

    def set_tetera_info(self, tetera_value, tiempo_tetera_value):
        self.Tetera.setText(f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">{tetera_value}</span></p></body></html>")
        self.TiempoTetera.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">{tiempo_tetera_value}</span></p></body></html>")

    def set_diarias_genshin_info(self, diarias_value, tiempo_diarias_value):
        self.DiariasGenshin.setText(f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">{diarias_value}</span></p></body></html>")
        self.TiempoDiariasGenshin.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">{tiempo_diarias_value}</span></p></body></html>")

    def set_resina_2_info(self, resina_2_value, tiempo_resina_2_value):
        self.Resina_2.setText(f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">{resina_2_value}</span></p></body></html>")
        self.TiempoResina_2.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">{tiempo_resina_2_value}</span></p></body></html>")

    def set_diarias_star_rail_info(self, diarias_star_rail_value, tiempo_diarias_star_rail_value):
        self.DiariasStarRail.setText(f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">{diarias_star_rail_value}</span></p></body></html>")
        self.TiempoDiariasStarRail.setText(f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">{tiempo_diarias_star_rail_value}</span></p></body></html>")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resin Checker"))
        self.Foto.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/icono-genshin.png\"/></p></body></html>"))
        self.Icono1.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/image 2.png\"/></p></body></html>"))
        self.TiempoResina.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Fills in 0 days 0:0:0</span></p></body></html>"))
        self.Resina.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">0/160</span></p></body></html>"))
        self.Icono2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/image 3.png\"/></p></body></html>"))
        self.TiempoTetera.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Fills in 0 days 0:0:0</span></p></body></html>"))
        self.Tetera.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">0/2400</span></p></body></html>"))
        self.Icono3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/image 5.png\"/></p></body></html>"))
        self.TiempoDiariasGenshin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Resets in 0 days 0:0:0</span></p></body></html>"))
        self.DiariasGenshin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">0/4</span></p></body></html>"))
        self.Texto.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Loggin Diario</span></p></body></html>"))
        self.ReclamarLogginGenshin.setText(_translate("MainWindow", "Reclamar"))
        self.Foto_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/icono-star-rail.png\"/></p></body></html>"))
        self.Icono1_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/image 4.png\"/></p></body></html>"))
        self.TiempoResina_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Fills in 00 days 0:0:0</span></p></body></html>"))
        self.Resina_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">0/160</span></p></body></html>"))
        self.Texto_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Loggin Diario</span></p></body></html>"))
        self.ReclamarLogginStarRail.setText(_translate("MainWindow", "Reclamar"))
        self.Icono4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Imagenes/image 5.png\"/></p></body></html>"))
        self.TiempoDiariasStarRail.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Resets in 0 days 0:0:0</span></p></body></html>"))
        self.DiariasStarRail.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">0/4</span></p></body></html>"))
        self.ActualizarInfo.setText(_translate("MainWindow", "Actualizar"))

    def tick(self):
            #actualiza la info de los tiempos de llenado
            global TiempoPoder, TiempoResina, TiempoTetera, ResinaActual, TeteraActual, PoderActual, ResinaMaxima, TeteraMaxima, PoderMaximo, contador, Reset, DiariasGenshin, DiariasStarRail, resinita, teterita, podercito
            contador += 1
            TiempoResina -= timedelta(seconds=1)
            TiempoTetera -= timedelta(seconds=1)
            TiempoPoder -= timedelta(seconds=1)

            resinita += 1
            teterita += 1
            podercito += 1

            if resinita == 480 :
                resinita = 0
                ResinaActual += 1 #pq se suma 1 cada 8 minutos
            
            if teterita == 3600 :
                teterita = 0
                TeteraActual += 30 #pq se suman 30 cada hora
                
            if podercito == 360 :
                podercito = 0
                PoderActual += 30 #pq se suma 1 cada 6 minutos

            Reset = Reset - timedelta(seconds=1)
            #actualizar info en interfáz
            self.set_resina_info(f"{ResinaActual}/{ResinaMaxima}",f"fills in: {TiempoResina}")
            self.set_tetera_info(f"{TeteraActual}/{TeteraMaxima}",f"fills in: {TiempoTetera}")
            self.set_diarias_genshin_info(f"{DiariasGenshin}",f"Resets in {Reset}")
            self.set_resina_2_info(f"{PoderActual}/{PoderMaximo}",f"fills in: {TiempoPoder}")
            self.set_diarias_star_rail_info(f"{DiariasStarRail}",f"Resets in {Reset}")

            QApplication.processEvents()

    @asyncSlot()
    async def get_game_info(self):
        global TiempoPoder, TiempoResina, TiempoTetera, ResinaActual, TeteraActual, PoderActual, ResinaMaxima, TeteraMaxima, PoderMaximo, contador, Reset, DiariasGenshin, DiariasStarRail, resinita, teterita, podercito
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

            #actualizar variables antiguas
            contador = 0
            resinita = 0
            teterita = 0
            podercito = 0
            
            TiempoResina = genshin_info.resin_recovery_time - now
            TiempoTetera = genshin_info.realm_currency_recovery_time - now
            TiempoPoder = star_rail_info.stamina_recovery_time - now
            Reset = (now.replace(hour=3, minute=0, second=0) + timedelta(days=1 if now.hour >= 3 else 0)) - now

            ResinaActual = genshin_info.current_resin
            TeteraActual = genshin_info.current_realm_currency
            PoderActual = star_rail_info.current_stamina
            DiariasGenshin = f"{genshin_info.completed_commissions}/{genshin_info.max_commissions}"
            DiariasStarRail = f"{star_rail_info.current_train_score//100}/{star_rail_info.max_train_score//100}"

            ResinaMaxima = genshin_info.max_resin
            TeteraMaxima = genshin_info.max_realm_currency
            PoderMaximo = star_rail_info.max_stamina

            # Formatear la información
            self.set_resina_info(f"{ResinaActual}/{ResinaMaxima}",f"fills in: {TiempoResina}")
            self.set_tetera_info(f"{TeteraActual}/{TeteraMaxima}",f"fills in: {TiempoTetera}")
            self.set_diarias_genshin_info(f"{DiariasGenshin}",f"Resets in {Reset}")
            self.set_resina_2_info(f"{PoderActual}/{PoderMaximo}",f"fills in: {TiempoPoder}")
            self.set_diarias_star_rail_info(f"{DiariasStarRail}",f"Resets in {Reset}")
            
            QApplication.processEvents()

            #inicia el timer
            self.timer.start(1000)  # Configurar el temporizador para que haga tick cada segundo
            self.timer.timeout.connect(self.tick) 

            #evito que se puedan tocar los botones hasta recuperar la info una vez
            self.ActualizarInfo.clicked.connect(self.actualizar_info)
            self.ReclamarLogginGenshin.clicked.connect(self.reclamar_login_genshin)
            self.ReclamarLogginStarRail.clicked.connect(self.reclamar_login_starrail)
            
        except Exception as e:
            alerta = QMessageBox()
            alerta.setWindowTitle("Error")
            alerta.setText(f"Error: {e}")
            alerta.setIcon(QMessageBox.Information)
            alerta.setStandardButtons(QMessageBox.Ok)
            alerta.exec_()
        QApplication.processEvents()

#cosas para iniciar la app
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    # Ejecutar el bucle de eventos de QEventLoop
    with loop:
        sys.exit(loop.run_forever())