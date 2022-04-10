import environ

from utils.email_template import create_email_template

env = environ.Env()
environ.Env.read_env('.env')


def send_email(quote):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    html, plain_text = create_email_template(quote)

    auth_user_email = env('EMAIL_HOST_USER')
    auth_user_pass = env('EMAIL_HOST_PASSWORD')
    email_to = env('EMAIL_TO').split(',')

    msg = MIMEMultipart('alternative')
    msg['From'] = auth_user_email
    msg['To'] = ", ".join(email_to)
    msg['Subject'] = "Quote of the day 🚀"

    msg.attach(MIMEText(html, 'html'))
    msg.attach(MIMEText(plain_text, 'text'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(auth_user_email, auth_user_pass)
    server.sendmail(auth_user_email, email_to, msg.as_string())
    server.quit()
