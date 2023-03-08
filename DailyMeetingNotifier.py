import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import smtplib
import time

# Function to display meeting details on the GUI
def mail_meetings():
    current_time = datetime.now().strftime("%H:%M")
    current_day = datetime.now().strftime("%A").lower()

    # Set up Google Sheets API credentials
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheets document for the current day
    sheet = client.open(f"{current_day}").sheet1
    rows = sheet.get_all_values()

    # Loop through the rows in the CSV file
    for row in rows:
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
