# Line-SDK-Python-Wrapper

Line's official sdk is not user-friendly.

This wrapper will make LineSDK more user-friendly.

LINE公式の提供してるSDKは正直言って使いにくいです。\
そこでこのラッパーの出番です。\
このラッパーは公式SDKをより使いやすくします。

[original](https://github.com/line/line-bot-sdk-python)

## usage

See Example.py to know how to use it

### Reply Message

text
```python
bot.reply_text("Hello World")
```
image
```python
bot.reply_image(ImageMessage("https://example.com/test.jpg"))
```
video
```python
video = VideoMessage("https://example.com/test.mp4", "https://example/test.jpg")
bot.reply_video(video)
```
And so on.

You can use [original's](https://github.com/line/line-bot-sdk-python) function(e.g, `unlink_rich_menu_from_user`)

Example:\
unlink_rich_menu_from_user is not implemented here,
but it is implemented on original Line-SDK
so you can use unlink_rich_menu_from_user like this

```python
bot.unlink_rich_menu_from_user(user_id)
```
