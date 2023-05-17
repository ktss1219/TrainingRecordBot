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
#awa