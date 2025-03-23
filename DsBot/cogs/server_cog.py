from disnake.ext import commands
import socket #Серверные функции
import threading #Мультипоточность

class serv(commands.Cog): # Определение класса Cog для группировки команд и слушателей

    def __init__(self, bot): # Конструктор класса, принимающий объект бота
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): # Событие, которое срабатывает, когда бот готов к работе
        print("Серверный ког иницилизирован") # Вывод сообщения в консоль

def start_server(): # Функция для запуска сервера

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создание сокета

    # Указываем IP-адрес и порт для прослушивания (в данном случае 8080)
    host = '0.0.0.0'
    port = 8080

    # Связываем сокет с адресом и портом
    server_socket.bind((host, port))

    # Запускаем прослушивание входящих соединений
    server_socket.listen(5)
    print(f"Сервер запущен и прослушивает порт {port}...")

    while True: # Бесконечный цикл

        # Ожидаем подключения от клиента
        client_socket, address = server_socket.accept() # Принятие входящего соединения
        print(f"Подключение от {address}") # Вывод информации о подключении

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        print(f"Данные от клиента: {data}")

        # Отправляем ответ клиенту
        response = "HTTP/1.1 200 OK\n\nПривет, клиент!"
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом
        client_socket.close()

# Функция для запуска сервера в отдельном потоке
def run_server_in_thread():
    server_thread = threading.Thread(target=start_server) # Создание потока для сервера
    server_thread.daemon = True  # Устанавливаем поток как "демон", чтобы он завершался при закрытии основного потока
    server_thread.start() # Запуск потока
    print("Сервер работает в фоновом потоке.") # Вывод

# Основная программа продолжает работать
print("Основной поток продолжает выполняться...") # Вывод сообщения о продолжении работы основного потока

def setup(bot): # Функция для добавления ког в бот
    bot.add_cog(serv(bot)) # Передаём ког боту
    run_server_in_thread() # Запуск сервера в отдельном потоке
