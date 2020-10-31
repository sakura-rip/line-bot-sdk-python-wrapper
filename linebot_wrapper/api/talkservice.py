from typing import Union, List

from linebot.models import SendMessage, TextSendMessage

from .struct import VideoMessage, ImageMessage, TextMessage


class TalkService:
    def __init__(self):
        self.reply_token = None

    def reply_message(self, messages: Union[SendMessage, List[SendMessage]]):
        """Reply Message
        LINEからできたEventに対する返信を行います
        :param messages: Message object which you want to sent
        :return: None
        """
        self.bot.reply_message(
            self.reply_token, messages
        )

    def reply_text(self, *texts: Union[str, List[str], TextMessage, List[TextMessage]]):
        """
        Reply text message
        :param texts:
        :type
        :return:
        """
        self.reply_message(
            [TextSendMessage(text=text) if isinstance(text, str) else text.create_message()
             for text in texts]
        )

    def reply_image(self, *images: Union[ImageMessage, List[ImageMessage]]):
        self.reply_message(
            [image.create_message() for image in images]
        )

    def reply_video(self, *videos: Union[VideoMessage, List[VideoMessage]]):
        self.reply_message(
            [video.create_message() for video in videos]
        )
