import requests
import json


class TelegramBot:
    def __init__(self):
        prefix = 'https://api.telegram.org/bot'
        token = '1042920896:AAGgV1HRkOCKGQUiSkDIe4fICAk82nKhfPY'
        self.urlGetMe = f'{prefix}{token}/getMe'
        self.urlGetUpdates = f'{prefix}{token}/getUpdates'
        self.urlSendMessage = f'{prefix}{token}/sendMessage'

    def get_messages_as_json(self, offset=0):
        response = requests.get(self.urlGetUpdates, params={'offset': offset})
        messages_as_json = json.loads(response.text)
        return messages_as_json['result']

    def post_message_to_user(self, chat_id, text):
        response = requests.post(self.urlSendMessage, params={'chat_id': chat_id, 'text': text})
        response_as_json = json.loads(response.text)
        return response_as_json