from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


def send_mail(body):
    message = MIMEMultipart()
    message['Subject'] = 'ZZZZZZZZZ!'
    message['From'] = 'a.dragunov@vistauto.ru'
    message['To'] = 'a.dragunov@vistauto.ru'

    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()
    print(msg_body)
    server = SMTP('smtp.yandex.ru', 25)
    server.starttls()
    server.login(message['From'], '12345678qaZ')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()


def get_gdp_data():
    """
    GDP data
    :return:
    """
    gdp_dict = {'Country': ['United States', 'China', 'Japan', 'Germany', 'India'],
                'GDP': ['$21.44 trillion', '$14.14 trillion', '$5.15 trillion', '$3.86 trillion', '$2.94 trillion']}
    data = pd.DataFrame(gdp_dict)
    print(data)
    return data


from pretty_html_table import build_table


def send_country_list():
    gdp_data = get_gdp_data()
    print(gdp_data)
    output = build_table(gdp_data, 'blue_light')
    send_mail(output)
    return "Mail sent successfully."


send_country_list()
