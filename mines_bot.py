import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 ¡Hola! Soy un bot predictor de Minas de Stake. Usa /predice")

async def predice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    minas = 3
    tablero = [["⬜️" for _ in range(5)] for _ in range(5)]
    minas_pos = set()
    while len(minas_pos) < minas:
        fila = random.randint(0, 4)
        col = random.randint(0, 4)
        minas_pos.add((fila, col))

    for i in range(5):
        for j in range(5):
            if (i, j) in minas_pos:
                tablero[i][j] = "💣"
            else:
                tablero[i][j] = "✅"

    mensaje = "\n".join([" ".join(fila) for fila in tablero])
    await update.message.reply_text(f"🎮 Predicción con {minas} minas:\n{mensaje}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predice", predice))
app.run_polling()
