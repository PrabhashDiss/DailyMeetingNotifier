import csv
from datetime import datetime
from tkinter import *
import webbrowser

# Create a Tkinter window
window = Tk()
window.title("Daily Meeting Reminder")
window.withdraw()  # Hide the window initially

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
               # Create a Text widget to display the meeting details and link
                details_text = Text(window, wrap=WORD)
                details_text.insert(END, meeting_details + "\n")
                details_text.insert(END, meeting_link, "link")
                details_text.pack()

                # Create a clickable hyperlink for the link
                details_text.tag_config("link", foreground="blue", underline=True)
                details_text.tag_bind("link", "<Button-1>", lambda event: webbrowser.open_new(meeting_link))

                window.deiconify()

# Call the display_meetings function every minute
window.after(60000, display_meetings)
window.mainloop()
