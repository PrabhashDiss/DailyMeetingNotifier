import csv
from datetime import datetime

# Function to display meeting details on the GUI
def display_meetings():
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
                pass
