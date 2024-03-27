import smtplib
from email.mime.text import MIMEText
import sys

def send_email(message, from_email, to_emails, smtp_server, smtp_port, smtp_login, smtp_password):
    msg = MIMEText(message, 'plain')
    msg['From'] = from_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # This is to secure the connection
        server.login(smtp_login, smtp_password)
        for email in to_emails:
            server.sendmail(from_email, email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main(email_txt, message_file, from_email, smtp_details):
    # 1. Read email addresses
    with open(email_txt, 'r') as f:
        emails = [line.strip() for line in f if line.strip()]

    # 2. Read the message content
    with open(message_file, 'r') as file:
        message = file.read()

    # 3. Send the email
    send_email(message, from_email, emails, *smtp_details)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please input: python3 emailSender.py receivers.txt message.txt")
        sys.exit(1)

    email_txt = sys.argv[1]  # email receivers
    message_file = sys.argv[2]  # message
    from_email = "rynnefan@gmail.com"   # Sender's email address (Here is mine)
    smtp_details = ('smtp.gmail.com', 587, 'rynnefan@gmail.com', 'some-16-character-string')  
    # smtp server   //  port    //  sender's email  //  app password
    '''
    The script is customed for gmail, so the smtp server is gmail's smtp server
    And the port 587 is also for gmail!
    And the password is not the password to login gmail: You need to generate an **app password**
    How to generarate: 1. Go to your google account, select "Security" and then "App passwords"
                       2. Select "Mail" and Click "Generate" and you will get a app password. Put it 
                          as the last element of the tuple. It should be a 16-character string.  
    '''

    main(email_txt, message_file, from_email, smtp_details)
