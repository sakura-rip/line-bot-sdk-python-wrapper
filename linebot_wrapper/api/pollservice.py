from traceback import print_exc
from typing import Callable, Dict

from linebot.models import (
    Event
)


class PollService:
    def __init__(self):
        self.op_interrupts = {}

    def handle_operation(self, body: str, signature: str):
        """Operation Handler
        LINEから飛んできたWebhookをParseし、Wrapper向けに書き直す
        :param body: string 飛んできたWebHookの内容
        :param signature: string シグネチャー
        :return: None
        """
        ops = self.parser.parse(body, signature)
        for op in ops:
            if op.type not in self.op_interrupts:
                continue
            self.set_reply_token(op)
            self.execute_func(op.type)

    def set_reply_token(self, op: Event):
        """
        set reply token for talk Service
        :param op: Event
        :return: None
        """
        self.reply_token = getattr(op, "reply_token")

    def execute_func(self, op_type: OpType):
        """func executer
        :param op_type: parsed Event from Webhook
        :return: None
        """
        try:
            self.op_interrupts[op_type](self, op_type)
        except Exception:
            print_exc()

    def add_op_interrupt(self, op_type: OpType, func: Callable):
        """ Add Event to handler
        :param op_type: Event which you want to handle
        :param func: Function which you want to call
        :return: None
        """
        assert op_type not in self.op_interrupts, f"{op_type} is already added to interrupts"
        self.op_interrupts[op_type] = func

    def add_op_interrupts(self, dicts: Dict[OpType, Callable]):
        """Add Events to handler
        :param dicts: Dict[Event, func]
        :return: None
        """
        for event, fnc in dicts.items():
            self.add_op_interrupt(event, fnc)
