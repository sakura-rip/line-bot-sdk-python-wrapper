from dataclasses import dataclass

from linebot.models import ImageSendMessage, QuickReply, VideoSendMessage, TextSendMessage, AudioSendMessage, \
    LocationSendMessage, StickerSendMessage


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
            original_content_url=self.content_url,
            preview_image_url=self.preview_url,
            quick_reply=self.quick_reply
        )


@dataclass
class AudioMessage:
    content_url: str
    duration: int
    quick_reply: QuickReply

    def create_message(self):
        return AudioSendMessage(
            original_content_url=self.content_url,
            duration=self.duration,
            quick_reply=self.quick_reply
        )


@dataclass
class LocationMessage:
    title: str
    address: str
    latitude: float
    longitude: float
    quick_reply: QuickReply

    def create_message(self):
        return LocationSendMessage(
            title=self.title,
            address=self.address,
            latitude=self.latitude,
            longitude=self.longitude,
            quick_reply=self.quick_reply
        )


@dataclass
class StickerMessage:
    package_id: str
    sticker_id: str
    quick_reply: QuickReply

    def create_message(self):
        return StickerSendMessage(
            package_id=self.package_id,
            sticker_id=self.sticker_id,
            quick_reply=self.quick_reply
        )
