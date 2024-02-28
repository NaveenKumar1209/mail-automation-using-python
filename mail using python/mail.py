import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Use TLS
        server.login(sender_email, sender_password)  # Login to the email account
        server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

# Replace these variables with your own values
sender_email = 'kavinkumar2628@gmail.com'
sender_password = 'zjwa aihu lzzi hbfz'
recipient_email = 'naveenkumars.20msc@kongu.edu'
subject = 'Hi'
body = 'Naveen , Are you fine now?'

# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, body)