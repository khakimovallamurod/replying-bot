from dotenv import load_dotenv
import os

load_dotenv()
def get_token():
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise ValueError("TOKEN not found.")
    return TOKEN

def get_chatid():
    CHAT_ID = os.getenv("CHAT_ID")
    if CHAT_ID is None:
        raise ValueError("CHAT_ID not found.")
    return CHAT_ID

