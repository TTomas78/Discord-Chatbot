import threading
from datetime import datetime

class MessageDeliverService():
    
    def __init__(self,default_countdown_time, assistant, user_id, discord, logger_service):
        self.messages = []
        self.countdown_time = 0
        self.default_countdown_time = default_countdown_time
        self.assistant = assistant
        self.user_id = user_id
        self.discord_bot = discord
        self.logger_service = logger_service

    def add_message(self, message):
        self.messages.append(message)
        self.logger_service.log_message(self.user_id, message, datetime.now())
        self._reset_countdown()
        if len(self.messages) == 1:
            threading.Thread(target=self.countdown).start()
            

    def countdown(self):
        while self.countdown_time > 0:
            self.countdown_time -= 1
            threading.Event().wait(1)
        self._answer_messages()

    def _answer_messages(self):
        #go to the AI and send the message
        message = "\n".join(self.messages)
        self._clean_messages()
        response = self.assistant.send_message(message).replace(". ", "\n")
        #Reply the message to the user
        self.discord_bot.loop.create_task(self.send_message(self.user_id, response))

        

    def _reset_countdown(self):
        self.countdown_time = self.default_countdown_time

    def _clean_messages(self):
        self.messages = []

    async def send_message(self,user_id, message):
        user = await self.discord_bot.fetch_user(user_id)
        await user.send(message)
        logs = message.split("\n")
        for log in logs:
            self.logger_service.log_message('AI response', log, datetime.now())
