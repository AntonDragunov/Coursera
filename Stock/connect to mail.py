import base64
import imaplib
import os
import smtplib

import psycopg2

mail = imaplib.IMAP4_SSL('imap.yandex.ru')
mail.login('a.dragunov@vistauto.ru', '12345678qaZ')

mail.list()
mail.select("KMR")
detach_dir = ''
import datetime

#date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
#result, data = mail.search('None', '(SINCE "24-Mar-2022" BEFORE "28-Mar-2022")'.format(date=date))

date = datetime.date.today().strftime("%d-%b-%Y")  # + datetime.timedelta(1))
result, data = mail.search('None', '(SINCE {date})'.format(date=date))

ids = data[0]

id_list = ids.split()

i = 0
for element in id_list:
    print(id_list[i])
    latest_email_id = id_list[i]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    import email

    email_message = email.message_from_string(raw_email_string)
    raw_email_string = raw_email.decode('utf-8')
    print(email_message['Date'])
    from email.header import decode_header

    a = []
    for part in decode_header(email_message['Subject']):
        a.append(str(*part))
        # print(a)
    # print(a[0])
    if 'KMR Price-list' in a[0]:
        # print(a[0])
        for part in email_message.walk():
            # multipart are just containers, so we skip them
            if part.get_content_maintype() == 'multipart':
                continue

            # is this part an attachment ?
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            counter = 1

            # def get_part_filename(msg: email_message):
            #     filename = msg.get_filename()
            #     if decode_header(filename)[0][1] is not None:
            #         filename = decode_header(filename)[0][0].decode(decode_header(filename)[0][1])
            #     return filename
            # if there is no filename, we create one with a counter to avoid duplicates
            if not filename:
                filename = 'part-%03d%s' % (counter, 'bin')
                counter += 1

        if filename[:11] == '=?KOI8-R?B?':
            filename = base64.b64decode(filename[11:]).decode('KOI8-R')
        if filename[:10] == '=?utf-8?B?':
            filename = base64.b64decode(filename[10:])

        filename_real = str(filename)[2:-1]
        att_path = os.path.join(detach_dir, filename_real)
        with open(os.path.join(detach_dir, filename_real), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
        print('Прайс сохранен за' + email_message['Date'])
        break
    else:
        print("это не прайс!")
    i += 1



    # print(email_message['To'])
    # print(email.utils.parseaddr(email_message['From']))
    # print(email_message['Date'])
    # print(email_message['Subject'])
    # print(email_message['Message-Id'])

    # print(email_message)

# print(filename)
# b = []
# for part in decode_header(email_message['attachments']):
#     b.append(str(*part))
# print(b)
# #Check if its already there
# if not os.path.isfile(att_path):
#     # finally write the stuff
#     fp = open(att_path, 'wb')
#     fp.write(part.get_payload(decode=True))
#     fp.close()
