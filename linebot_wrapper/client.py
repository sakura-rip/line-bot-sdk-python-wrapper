from linebot import LineBotApi, WebhookParser

from .api.pollservice import PollService
from .api.messageservice import MessageService


class LineClient(MessageService, PollService):
    def __init__(self, access_token: str, secret: str):
        self.bot = LineBotApi(access_token)
        self.parser = WebhookParser(secret)
        self.init_all()

    def init_all(self):
        MessageService.__init__(self)
        PollService.__init__(self)
