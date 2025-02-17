import pywhatkit as kit
import schedule
import time
from datetime import datetime

# List of contacts (Phone numbers in WhatsApp format +<CountryCode><Number>)
contacts = input("Enter contacts (comma separated with country code) e.g., +1234567890, +1987654321: ").split(',')

# Define a function to send the Good Morning message
def send_good_morning():
    now = datetime.now()
    # Custom message to send
    message = f"Good Morning! Have a wonderful day ahead! - Sent at {now.strftime('%H:%M:%S')}"
    
    for contact in contacts:
        contact = contact.strip()  # Remove leading/trailing spaces
        kit.sendwhatmsg(contact, message, now.hour, now.minute + 1)  # Send at next minute

    print("Good Morning message sent!")

# Schedule to run at 6 AM every day
schedule.every().day.at("08:00").do(send_good_morning)

# Keep the script running
while True:
    schedule.run_pending()  # Run the scheduled tasks
    time.sleep(60)  # Check every minute
