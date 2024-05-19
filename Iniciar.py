import asyncio
from datetime import datetime, timezone
import genshin

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

async def InfoGenshin():
    client = genshin.Client()
    cookies = await client.login_with_password(correo, contraseña)
    client = genshin.Client(cookies=cookies)
    # Obtener notas diarias
    notes = await client.get_notes()

    # Información de la resina
    current_resin = notes.current_resin
    resin_recovery_time = notes.resin_recovery_time

    # Calcular el tiempo restante para la resina
    now = datetime.now(timezone.utc)
    resin_time_left = resin_recovery_time - now

    # Información de las misiones diarias
    completed_commissions = notes.completed_commissions
    max_commissions = notes.max_commissions

    # Información de la relajatetera
    current_realm_currency = notes.current_realm_currency
    max_realm_currency = notes.max_realm_currency
    realm_currency_recovery_time = notes.realm_currency_recovery_time

    # Calcular el tiempo restante para la relajatetera
    realm_time_left = realm_currency_recovery_time - now

    print(f"Resina actual: {current_resin}")
    print(f"Tiempo restante para que se llene la resina: {resin_time_left}")
    print(f"Misiones Diarias completadas: {completed_commissions}/{max_commissions}")
    print(f"Dinero de la Relajatetera: {current_realm_currency}/{max_realm_currency}")
    print(f"Tiempo restante para que se llene la relajatetera: {realm_time_left}")
    # Información sobre expediciones
    print("Expediciones:")
    for expedition in notes.expeditions:
        status = "En curso" if expedition.remaining_time.total_seconds() > 0 else "Finalizada"
        print(f" - {expedition.character_icon}: {status}, Tiempo restante: {expedition.remaining_time}")

async def InfoStarRail():
    client = genshin.Client()
    cookies = await client.login_with_password(correo, contraseña)
    client = genshin.Client(cookies=cookies)

    # Obtener notas de Star Rail
    notes = await client.get_starrail_notes()

    # Información sobre la resina (TB power)
    print(f"Poder de Trazacaminos actual: {notes.current_stamina}/{notes.max_stamina}")
    print(f"Tiempo para recuperación completa: {notes.stamina_recover_time}")

    # Información sobre misiones diarias
    print(f"Diarias completadas: {notes.current_train_score/100}/{notes.max_train_score/100}")

    # Información sobre expediciones
    print("Expediciones:")
    for expedition in notes.expeditions:
        status = "En curso" if expedition.remaining_time.total_seconds() > 0 else "Finalizada"
        print(f" - {expedition.name}: {status}, Tiempo restante: {expedition.remaining_time}")

async def main():
    await InfoGenshin()

# Ejecutar la función asíncrona
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
