from linebot import LineBotApi, WebhookParser

from .api.pollservice import PollService
from .api.talkservice import TalkService


class LineClient(TalkService, PollService):
    def __init__(self, access_token: str, secret: str):
        self.bot = LineBotApi(access_token)
        self.parser = WebhookParser(secret)
        self.init_all()

    def init_all(self):
        TalkService.__init__(self)
        PollService.__init__(self)
