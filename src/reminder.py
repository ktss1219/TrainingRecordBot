def handle_message(event):
    template_message = TemplateSendMessage(
        alt_text='トレーニング曜日の選択',
        template=ButtonsTemplate(
            text='トレーニングは何曜日にしますか？',
            actions=[
                PostbackTemplateAction(label='日曜日', data='Sunday'),
                PostbackTemplateAction(label='月曜日', data='Monday'),
                PostbackTemplateAction(label='火曜日', data='Tuesday'),
                PostbackTemplateAction(label='水曜日', data='Wednesday'),
                PostbackTemplateAction(label='木曜日', data='Thursday'),
                PostbackTemplateAction(label='金曜日', data='Friday'),
                PostbackTemplateAction(label='土曜日', data='Saturday')
                ]
            )
        )
    line_bot_api.reply_message(event.reply_token, template_message)


def remind_training():
    # リマインドメッセージを作成
    message = TextSendMessage(text='今日のトレーニングを忘れないでください！')

    # 送信先ユーザーID
    user_id = 'USER_ID'

    # メッセージを送信
    line_bot_api.push_message(user_id, messages=message)

# 登録された曜日に応じてリマインドを設定
def setup_reminders():
    # 登録された曜日のリスト
    training_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # 現在の曜日を取得
    current_day = datetime.datetime.now().strftime('%A')

    # 現在の曜日が登録された曜日リストにある場合、リマインドを設定
    if current_day in training_days:
        # 朝にリマインドを送るための時間を設定（例：8時）
        remind_time = datetime.time(hour=8)

        # リマインドを設定
        scheduler.add_job(remind_training, 'cron', day_of_week=current_day, hour=remind_time.hour, minute=remind_time.minute)

# BackgroundSchedulerを作成
scheduler = BackgroundScheduler()

# リマインドの設定を実行
setup_reminders()

# スケジューラを開始
scheduler.start()