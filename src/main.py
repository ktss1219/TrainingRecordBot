from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ButtonsTemplate, PostbackTemplateAction, TemplateSendMessage, FollowEvent, PostbackEvent
from apscheduler.schedulers.background import BackgroundScheduler
import os, dotenv
import datetime
 
app = Flask(__name__)

dotenv.load_dotenv()
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
 
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
 
# Webhookからのリクエストの署名検証部分
@app.route("/callback", methods=['POST'])
def callback():
    # 署名検証のための値
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # 署名検証
    try:
        handler.handle(body, signature)
    except InvalidSignatureError: # 失敗したとき エラー
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# ===================================================================
@handler.add(PostbackEvent)
def handle_messafe_event(event):
  handle_message(event)

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data

    if data in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:

# ===================================================================

# python main.py　で動作
if __name__ == "__main__":
    app.run(port=5000)
