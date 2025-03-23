import os # Взаимодействие с операционной системой
from dotenv import load_dotenv, find_dotenv # Работа с переменными окружения из файла .env
import disnake # Импорт библиотеки для взаимодействия с Discord API
from disnake.ext import commands # Импорт шаблонов для команд

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[898250287221997598]) # Инициализация бота

load_dotenv(find_dotenv()) # Поиск и загрузка переменных из env
token = os.getenv("TOKEN") # Выгрузка токена

# Команда для загрузки кога бота
@bot.command()
@commands.is_owner()
async def load(ctx, extension): # Загрузка указанного расширения
    bot.load_extension(f"cogs.{extension}")

# Команда для выгрузки кога бота
@bot.command()
@commands.is_owner()
async def unload(ctx, extension): # Выгрузка указанного расширения
    bot.unload_extension(f"cogs.{extension}")

# Команда для перезагрузки кога бота
@bot.command()
@commands.is_owner()
async def reload(ctx, extension): # Перезагрузка указанного расширения
    bot.reload_extension(f"cogs.{extension}")

# Загрузка всех когов из папки ./cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"): # Проверка, что файл имеет расширение .py
        bot.load_extension(f"cogs.{filename[:-3]}") # Загрузка расширения без .py

bot.run(token) # Запуск бота
