import requests
import smtplib
from email.message import EmailMessage

# API Key
api_key = "insert-api-key-here"

# Home Address Input
home = input("Enter home address:\n")

# Work Address Input
work = input("Enter work address:\n")

# Base URL
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# Get Response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + "AIzaSyAOv_VFZKT_vuAKvQvQPRYJn8g4MwZzDds")

# Return Time as Text and as Seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

# Print Total Travel Time
print("\nThe total time from home to work is", time)

# Check if Time > 1 Hour
if (seconds > 3600):

    # email constraints
    sender = input("Enter sender email:\n")
    recipient = input("Enter receiving email:\n")
    subject = "Sick Day"
    message = """
    Hi Boss, 
    
    Sorry for the inconvenience, but I can't make it to work today.
    
    Thanks, 
    Sam Park"""

    # Email 
    em = f"Subject: {subject}\n\n{message}"

    # Create and Start SMTP Server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Authentication
    server.login(sender, "insert-password-here")

    # Sending email
    server.sendmail(sender, recipient, em)

    # Success Message 
    print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long.")
else:
    print("\nEmail was not sent. The commute is short, lets get going to work!")
