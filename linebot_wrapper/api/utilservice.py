from linebot.models import Event

from linebot_wrapper.ttype import ToType


class UtilService:
    def get_contact(self, op: Event):
        """
        Get Profile For all chat type
        :param op:
        :return:
        """
        if op.source.type == ToType.GROUP:
            return self.api.get_group_member_profile(op.source.group_id, op.source.user_id)
        elif op.source.type == ToType.ROOM:
            return self.api.get_room_member_profile(op.source.room_id, op.source.user_id)
        else:
            return self.get_profile(op.source.user_id)

    def get_to_id(self, op: Event):
        """
        Get to Id from Op
        :param op:
        :return:
        """
        if op.source.type == ToType.GROUP:
            return op.source.group_id
        elif op.source.type == ToType.ROOM:
            return op.source.room_id
        else:
            return op.source.user_id

    def download_message(self, message_id: str, f_name: str=None):
        """
        Download image, video and so on from id
        :param message_id:
        :param f_name:
        :return:
        """
        content = self.api.get_message_content(message_id)
        if not f_name:
            f_name = f"{message_id}.{content.content_type.split('/')[1]}"
        with open(f_name, "wb") as f:
            f.write(content.content)

    def get_mentioned_user_id(self, event: Event):
        if not event.message.mention:
            return []
        return [
            men.user_id for men in event.message.mention.mentionees
        ]
