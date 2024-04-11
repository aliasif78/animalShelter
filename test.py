import pywhatkit as kit

# Replace the following with your own phone number and the message
phone_number = "+923331008936"  # Your phone number with country code
message = "This is a test message sent to myself using Python."

# Send the message to yourself
kit.sendwhatmsg_instantly(phone_number, message)
