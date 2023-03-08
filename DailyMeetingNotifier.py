import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import smtplib
import time

# Function to display meeting details on the GUI
def mail_meetings():
    current_time = datetime.now().strftime("%H:%M")
    current_day = datetime.now().strftime("%A").lower()

    # Open the CSV file for the current day
    with open(f"{current_day}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

    # Loop through the rows in the CSV file
    for row in csv_reader:
        meeting_time = row[0]
        meeting_details = row[1]
        meeting_link = row[2]

        # If the meeting time matches the current time, display the details and link on the GUI
        if meeting_time == current_time:
            # Set up email server details
            smtp_server = 'smtp.gmail.com'
            port = 587
            sender_email = 'prabhashdissanayake2k@gmail.com'
            sender_password = 'qvcnbdxyiazedsjt'
            recipient_email = 'prabhashdissanayake2k@gmail.com'

            # Send email notification
            message = f'Subject: {meeting_details}\n\n{meeting_link}'
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, message)
                print('Email sent successfully')

# Schedule the function to run every 1 minutes
while True:
    mail_meetings()
    time.sleep(60)  # Wait for 1 minutes
