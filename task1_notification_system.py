class Notification:
    def __init__(self,recepient):
        self.recepient = recepient
    def send(self):
        print(self.recepient)
class EmailNotification(Notification):
    def send(self):
        print(f'Sending email to {self.recepient} ')
class SMSNotification(Notification):
    def send(self):
        print(f'Sending SMS to {self.recepient} ')
email = EmailNotification('user@example.com')
sms = SMSNotification('0812345678')
notification = [email,sms]
for noti in notification:
    noti.send()