#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url="https://res.klook.com/image/upload/v1628149846/hln31fpguudxtpqrfahl.jpg",
            title="空氣品質查詢",
            text="請選擇查詢類別",
            actions=[
                MessageTemplateAction(
                    label="1：縣市查詢",
                    text="1"
                ),
                MessageTemplateAction(
                    label="2：測站查詢",
                    text="2"
                )
            ]
        )
    )
    return message


#關於LINEBOT聊天內容範例