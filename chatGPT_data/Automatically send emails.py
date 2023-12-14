import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_email(sender, receiver, subject, message):
    # メールの内容を作成
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    # SMTPサーバーに接続
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)
    # メールを送信
    smtp_connection.sendmail(sender, receiver, msg.as_string())
    # SMTPサーバーとの接続を終了
    smtp_connection.quit()
# メールの送信元、送信先、件名、本文を指定してメールを送信
sender = "sender@example.com"
receiver = "receiver@example.com"
subject = "Test Email"
message = "This is a test email."
send_email(sender, receiver, subject, message)
