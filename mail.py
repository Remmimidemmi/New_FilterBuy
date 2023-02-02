import imaplib
import email
import re
from email.header import decode_header
import webbrowser
import os
import copy


class ReadLettersFromGmail:
    def __init__(self):
        self.username = "zast0tsaz@gmail.com"
        self.password = "xzyzfmfuktumsfbd"
        self.server = "imap.gmail.com"
        self.mess = self.read_mess_from_email()

    def read_mess_from_email(self):
        imap = imaplib.IMAP4_SSL(self.server)
        imap.login(self.username, self.password)
        imap.select("INBOX")
        result, data = imap.search(None, "ALL")
        ids = data[0]  # Получаем сроку номеров писем
        id_list = ids.split()  # Разделяем ID писем
        latest_email_id = id_list[-1]  # Берем последний ID
        res, msg = imap.fetch(latest_email_id, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])
        letter_from = msg["Return-path"]  # e-mail отправителя
        letter_sub = decode_header(msg["Subject"])[0][0]
        print(letter_from, letter_sub)
        for part in msg.walk():
            # extract content type of email
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            # get the email body
            body = part.get_payload(decode=True)
            if content_type == "text/plain" and "attachment" not in content_disposition:
                # print text/plain emails and skip attachments
                bod = copy.copy(body).split()
                print(f'Bod - {bod}')
                bod_link = bod[-9]
                return bod_link

    def return_link_for_reset_password(self):
        letters = self.mess
        str_letters = str(letters)
        b_link = re.split(r'\'', str_letters)
        old_link = b_link[1]
        new_link = old_link.replace('filterbuy.com', "react.test.filterbuytest.com")
        print(f'\n{new_link}')
        return new_link
        # print(f'\n{letters}')
        # print(f'\n{b_link}')
        # print(f'\n{old_link}')



