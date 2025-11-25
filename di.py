import telebot
bot = telebot.TeleBot("8300420706:AAEjHPlmVAFxWI1WYKTF1_cBUaYlSoZCmW0")
snake = {
"snake":"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake Game</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="game-container">
        <div class="scores">
            <h1>Score: <span id="score">0</span></h1>
            <h1>High Score: <span id="high-score">0</span></h1>
        </div>
        <canvas id="game-board" width="400" height="400"></canvas>
        <h1 id="instruction-text">Press spacebar to start the game</h1>
    </div>
    <script src="script.js" defer></script>
</body>
</html>
"""}

bot.message_handler(["start"])
def start(xabar):
    print(xabar)

    bot.reply_to(xabar, "Assalomu alekum")
@bot.message_handler(["game"])

def game(xabar):
    bot.reply_to(xabar,snake["snake"])

bot.infinity_polling()