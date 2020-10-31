from linebot import LineBotApi, WebhookParser

from .api.pollservice import PollService
from .api.messageservice import MessageService


class LineClient(MessageService, PollService, LineBotApi):
    def __init__(self, access_token: str, secret: str):
        self.api = LineBotApi(access_token)
        self.parser = WebhookParser(secret)
        self.init_all(access_token)

    def init_all(self, access_token):
        LineBotApi.__init__(self, access_token)
        MessageService.__init__(self)
        PollService.__init__(self)
