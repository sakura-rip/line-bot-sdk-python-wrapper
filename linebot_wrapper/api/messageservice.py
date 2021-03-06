from typing import Union, List

from linebot.models import (
    SendMessage,
    TextSendMessage
)

from .message_struct import (
    VideoMessage,
    ImageMessage,
    TextMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    message_types
)


class MessageService:
    def __init__(self):
        self.reply_token = None

    def reply_message_base(self, messages: Union[SendMessage, List[SendMessage]]):
        """Reply Message
        Respond to events from users, groups, and rooms.
        :param messages: Message object which you want to send
        :return: None
        """
        self.api.reply_message(
            self.reply_token, messages
        )

    def reply_message(self, *messages: message_types):
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
        """
        Reply audio message
        :param audios: AudioMessage object which you want to send
        :return:
        """
        self.reply_message_base(
            [audio.create_message() for audio in audios]
        )

    def reply_location(self, *locations: Union[LocationMessage, List[LocationMessage]]):
        """
        Reply location message
        :param locations: LocationMessage object which you want to send
        :return:
        """
        self.reply_message_base(
            [location.create_message() for location in locations]
        )

    def reply_sticker(self, *stickers: Union[StickerMessage, List[StickerMessage]]):
        """
        Reply sticker message
        :param stickers: StickerMessage object which you want to send
        :return:
        """
        self.reply_message_base(
            [sticker.create_message() for sticker in stickers]
        )

    def push_message(self, to: str, *messages: message_types):
        """
        Send messages to users, groups, and rooms at any time.
        :param to:
        :param messages:
        :return:
        """
        self.api.push_message(to,
            [message.create_message() for message in messages]
        )

    def multicast(self, uids: Union[str, List[str]], *messages: message_types):
        """
        Send push messages to multiple users at any time. Messages cannot be sent to groups or rooms.
        :param uids:
        :param messages:
        :return:
        """
        self.api.multicast(uids,
            [message.create_message() for message in messages]
        )

    def broadcast(self, *messages: message_types):
        """
        Send push messages to multiple users at any time.
        :param messages:
        :return:
        """
        self.api.broadcast(
            [message.create_message() for message in messages]
        )
