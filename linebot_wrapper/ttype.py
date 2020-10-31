class OpType:
    RECEIVE_MESSAGE = "message"
    FOLLOW = "follow"
    UNFOLLOW = "unfollow"
    JOIN = "join"
    LEAVE = "leave"
    POSTBACK = "postback"
    BEACON = "beacon"
    MEMBER_JOINED = "memberJoined"
    MEMBER_LEFT = "memberLeft"
    ACCOUNT_LINK = "accountLink"
    THINGS = "things"


class ToType:
    USER = "user"
    ROOM = "room"
    GROUP = "group"
