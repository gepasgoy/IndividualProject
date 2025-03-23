from disnake.ext import commands

class Test(commands.Cog): # Группировка команд и слушателей в класс

    def __init__(self, bot): # Конструктор класса, принимающий объект бота
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): # Событие, которое срабатывает, когда бот готов к работе
        print("Работает, полёт нормальный")

    @commands.Cog.listener()
    async def on_message(self, message): # Событие, которое срабатывает при получении сообщения
        if message.content == "nice": # Проверка содержимого сообщения
            await message.channel.send("for real") # Ответ в канал

    @commands.command()
    async def hello(self, ctx): # Команда, которая отвечает "Hiiii!"
        await ctx.send("Hiiii! :3") # Отправка сообщения в канал

def setup(bot): # Функция для добавления кога к боту
    bot.add_cog(Test(bot))
