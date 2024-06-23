import imghdr
import smtplib
from email.message import EmailMessage

# your generated gmail key
PASSWORD = ""
# your email
SENDER = ""
# receiver email
RECEIVER = ""


def send_email(path):
    print("Send email started")
    email_message = EmailMessage()
    email_message["Subject"] = "New object appeared in the frame"
    email_message.set_content("Check the attached file.")

    with open(path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    print("Send email ender")


if __name__ == "__main__":
    send_email("images/22.png")