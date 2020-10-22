import time

from telegrambot import TelegramBot
from robot import LuckyRobot
from robot import SmileRobot

last_message_id = 0
while True:
    # 1. Обращаться к телеграмм за последними сообщениями
    bot = TelegramBot()
    messages = bot.get_messages_as_json(last_message_id + 1)
    for message in messages:
        robot_lucky = LuckyRobot()
        robot_smile = SmileRobot()
        robot_list = [robot_lucky.get_name(), robot_smile.get_name()]
        # TODO
        last_message_id = max(last_message_id, message['update_id'])
        chat_id = message['message']['chat']['id']
        text = message['message']['text']
        user_name = message['message']['chat']['username']
        # 2. Обратотка ответа от телеграмм
        answer = f'{user_name}, робот не найден ...'
        if text == robot_lucky.get_name():
            answer = f'{user_name}, мы нашли робота: {robot_lucky.get_command()}'
        if text == robot_smile.get_name():
            answer = f'{user_name}, мы нашли робота: {robot_smile.get_command()}'
        result = bot.post_message_to_user(chat_id, answer)
        print(result)
    # 3. Отправить ответ в телеграмм
    time.sleep(1)
