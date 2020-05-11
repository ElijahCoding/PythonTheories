import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = ""
password = ""


def send_mail(text='Email body', subject='hello', from_email=f"my email + {username}", to_emails=None):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText("<h1>This is working</h1>", 'html')
    msg.attach(html_part)

    msg_str = msg.as_string()
    # login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    server.sendmail(from_email, to_emails, msg_str)

    server.quit()