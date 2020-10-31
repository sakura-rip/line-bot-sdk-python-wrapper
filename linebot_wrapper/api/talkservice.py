from typing import Union, List

from linebot.models import SendMessage, TextSendMessage

from .message_struct import VideoMessage, ImageMessage, TextMessage, AudioMessage, LocationMessage, StickerMessage


class TalkService:
    def __init__(self):
        self.reply_token = None

    def reply_message_base(self, messages: Union[SendMessage, List[SendMessage]]):
        """Reply Message
        LINEからできたEventに対する返信を行います
        :param messages: Message object which you want to sent
        :return: None
        """
        self.bot.reply_message(
            self.reply_token, messages
        )

    def reply_message(self, *messages: Union[VideoMessage, ImageMessage, TextMessage, AudioMessage, LocationMessage, StickerMessage]):
        self.reply_message_base(
            [message.create_message() for message in messages]
        )

    def reply_text(self, *texts: Union[str, List[str], TextMessage, List[TextMessage]]):
        """
        Reply text message
        :param texts: Text object which you want to send
        :return: None
        """
        self.reply_message_base(
            [TextSendMessage(text=text) if isinstance(text, str) else text.create_message()
             for text in texts]
        )

    def reply_image(self, *images: Union[ImageMessage, List[ImageMessage]]):
        """
        Reply image message
        :param images: ImageMessage object which you want to send
        :return: None
        """
        self.reply_message_base(
            [image.create_message() for image in images]
        )

    def reply_video(self, *videos: Union[VideoMessage, List[VideoMessage]]):
        """
        Reply video message
        :param videos:  VideoMessage object which you want to send
        :return: None
        """
        self.reply_message_base(
            [video.create_message() for video in videos]
        )

    def reply_audio(self, *audios: Union[AudioMessage, List[AudioMessage]]):
        self.reply_message_base(
            [audio.create_message() for audio in audios]
        )

    def reply_location(self, *locations: Union[LocationMessage, List[LocationMessage]]):
        self.reply_message_base(
            [location.create_message() for location in locations]
        )

    def reply_sticker(self, *stickers: Union[StickerMessage, List[StickerMessage]]):
        self.reply_message_base(
            [sticker.create_message() for sticker in stickers]
        )
