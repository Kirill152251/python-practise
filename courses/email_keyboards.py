import smtplib
import key_board_web_scraping

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login('email@.com', 'password')
from_address = ''
to_address = ''
subject = 'Цены на клавиатуры'
message = key_board_web_scraping.get_keyboards_info()
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()
