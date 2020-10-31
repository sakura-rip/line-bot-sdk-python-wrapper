from dataclasses import dataclass

from linebot.models import ImageSendMessage, QuickReply, VideoSendMessage, TextSendMessage


@dataclass
class TextMessage:
    text: str
    quick_reply: QuickReply

    def create_message(self):
        return TextSendMessage(
            text=self.text,
            quick_reply=self.quick_reply
        )


@dataclass
class VideoMessage:
    content_url: str
    preview_url: str
    quick_reply: QuickReply

    def create_message(self):
        return VideoSendMessage(
            original_content_url=self.content_url,
            preview_image_url=self.preview_url,
            quick_reply=self.quick_reply
        )


@dataclass
class ImageMessage:
    content_url: str
    preview_url: str
    quick_reply: QuickReply

    def create_message(self):
        return ImageSendMessage(
            riginal_content_url=self.content_url,
            preview_image_url=self.preview_url,
            quick_reply=self.quick_reply
        )
