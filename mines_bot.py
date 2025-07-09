import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Función para responder al comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 ¡Hola! Soy un bot que predice jugadas para el juego de Minas de Stake. Escribe /predice para ver una sugerencia.")

# Función para simular una predicción
async def predice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    minas = 3  # puedes permitir al usuario cambiarlo
    tablero = [["⬜️" for _ in range(5)] for _ in range(5)]

    # Genera posiciones aleatorias para las minas
    minas_pos = set()
    while len(minas_pos) < minas:
        fila = random.randint(0, 4)
        col = random.randint(0, 4)
        minas_pos.add((fila, col))

    # Coloca minas y seguros
    for i in range(5):
        for j in range(5):
            if (i, j) in minas_pos:
                tablero[i][j] = "💣"
            else:
                tablero[i][j] = "✅"

    mensaje = "\n".join([" ".join(fila) for fila in tablero])
    await update.message.reply_text(f"🎮 Tablero simulado con {minas} minas:\n{mensaje}")

# Ejecutar el bot
app = ApplicationBuilder().token(8092792974:AAFz5qrUwXBdze25x-8Wnv-BJpLx_WFiAJg).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predice", predice))

print("✅ Bot ejecutándose...")
app.run_polling()