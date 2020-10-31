from linebot import LineBotApi, WebhookParser

from .api.talk import Talk, Poll


class LineClient(Talk, Poll):
    def __init__(self, access_token: str, secret: str):
        self.bot = LineBotApi(access_token)
        self.parser = WebhookParser(secret)
