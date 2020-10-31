from traceback import print_exc
from typing import Callable, Dict

from linebot.models.events import Event


class Poll:
    def __init__(self):
        self.op_interrupts = {}

    def handle_operation(self, body, signature):
        ops = self.parser.parse(body, signature)
        for op in ops:
            if op.type not in self.op_interrupts:
                continue
            self.execute_func(op)

    def execute_func(self, op):
        assert op.type not in self.op_interrupts, f"{op.type} is already added to interrupts"
        try:
            self.op_interrupts[op.type](self.bot, op)
        except Exception:
            print_exc()

    def add_op_interrupt(self, op: Event, func: Callable):
        self.op_interrupts[op.type] = func

    def add_op_interrupts(self, dicts: Dict[Event, Callable]):
        for event, fnc in dicts.items():
            self.op_interrupts[event.type] = fnc
