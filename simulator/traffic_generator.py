import requests
import random
import time

API_URL = "http://127.0.0.1:8000/predict"

spam_messages = [
    "Congratulations you won a free lottery",
    "Claim your free prize now",
    "Limited time offer click here",
    "Win cash reward today",
    "Urgent call this number to claim prize"
]

ham_messages = [
    "Hey are we meeting tomorrow",
    "Call me when you reach home",
    "Let's have lunch today",
    "Project meeting at 3pm",
    "Can you send the report"
]

while True:

    if random.random() < 0.4:
        message = random.choice(spam_messages)
    else:
        message = random.choice(ham_messages)

    try:
        response = requests.post(API_URL, params={"text": message})

        print("Sent:", message)
        print("Response:", response.json())
        print("-" * 50)

    except Exception as e:
        print("Error:", e)

    time.sleep(2)