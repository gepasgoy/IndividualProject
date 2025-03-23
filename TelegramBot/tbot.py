import asyncio #Библиотека для асинхронного программирования
import os #Библиотека для взаимодействия с системой
from aiogram import Bot, Dispatcher #модули тбота
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import find_dotenv,load_dotenv #Работа с env
import socket #Серверные функции
import threading #Мультипоточность

load_dotenv(find_dotenv()) # Поиск и загрузка переменных из файла env
token = os.getenv("TOKEN") # Выгрузка токена

bot = Bot(f"{token}") # Загрузка токена
dp = Dispatcher() #получение апдейтов от Telegram

def start_server_in_thread(): # Функция для поддержания соединения с сервером в отдельном потоке
  server_thread = threading.Thread(target=start_server) # Создание потока для сервера.
  server_thread.daemon = True # Устанавливаем поток как "демон"
  server_thread.start() # Запуск потока
  print("Сервер работает в фоновом потоке.") # Вывод


# Базовые команды
@dp.message(Command("start")) #Вывод приветствия при старте
async def hello(message: Message):
     await message.answer(f"Здравья желаю, {message.from_user.first_name}")

@dp.message(Command("ping")) #Ответ пользователю
async def ping(message: Message):
    await message.answer(f"Pong!")


async def main(): #Функция запуска бота
    await bot.delete_webhook(drop_pending_updates=True) # Удаление вебхука.
    await dp.start_polling(bot) #Запуск поллинга

def start_server():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создание сокета

  # Указываем IP-адрес и порт для прослушивания (в данном случае 8080)
  host = '0.0.0.0'
  port = 8080

  # Связывает сокет с адресом и портом
  server_socket.bind((host, port))

  # Запускаем прослушивание
  server_socket.listen(5)
  print(f"Сервер запущен и прослушивает порт {port}...")

  while True: #Бесконечный цикл
    # Ожидаем подключения
    client_socket, address = server_socket.accept()
    print(f"Подключение от {address}")

    # Получаем данные от клиента
    data = client_socket.recv(1024).decode()
    print(f"Данные от клиента: {data}")

    # Отправляем ответ клиенту
    response = "HTTP/1.1 200 OK\n\nПривет, клиент!"
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()


if __name__ == "__main__": #Точка входа
    start_server_in_thread() #Запуск сервера в отдельном потоке
    asyncio.run(main()) #Запуск бота