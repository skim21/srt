from twilio.rest import Client

account_sid = 'ACbabab7517751d932184bb7b22d2505ea'
auth_token = 'e9e6890fd31b1884ca9b1dd2d0de9317'

client = Client(account_sid, auth_token)


def create_message(txt):
    korail_reserve_notification_message = client.messages.create(
        to="+8201050119566",
        from_="+19472253112",
        body=txt
    )
    print(korail_reserve_notification_message)

def send_message(txt=None):
    create_message(txt)