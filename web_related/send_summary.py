import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
# load_dotenv()


def send_email(content, email):


    sg = sendgrid.SendGridAPIClient("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")

    message = Mail(
        from_email='homeworkcheckerpython@proton.me',
        to_emails='aatenorio.estruch@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=f'{content}')


    # Send an HTTP POST request to /mail/send
    response = sg.send(message)
    print(response.status_code)
    print(response.headers)
    print("finished")
