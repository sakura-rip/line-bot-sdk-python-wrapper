from flask import Flask, request, abort
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot_wrapper import LineClient
from linebot_wrapper.ttype import OpType

client = LineClient(
    "AccessToken",
    "Secret"
)

app = Flask(__name__)


def receive_message(bot, op):
    bot.reply_text("hello world")


client.add_op_interrupt(OpType.RECEIVE_MESSAGE, receive_message)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        client.handle_operation(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
