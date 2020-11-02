from linebot import LineBotApi

from .api.pollservice import PollService
from .api.messageservice import MessageService
from .api.utilservice import UtilService


class LineClient(MessageService, PollService, LineBotApi, UtilService):
    def __init__(self, access_token: str, secret: str):
        self.api = LineBotApi(access_token)
        self.__init_all(access_token, secret)

    def __init_all(self, access_token: str, secret: str):
        LineBotApi.__init__(self, access_token)
        MessageService.__init__(self)
        PollService.__init__(self, secret)
