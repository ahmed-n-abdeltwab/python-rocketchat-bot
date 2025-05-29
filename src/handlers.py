# Handles login/logout and message logic
from rocket_client import RocketChatClient
import config

client = RocketChatClient()


def greet_login(user):
    """
    Send a welcome message to the greet channel when a user logs in.
    """
    message = f"Welcome, @{user}! Glad you're here! 🚀"
    room_id = client.get_room_id(room_name=config.GREET_CHANNEL)
    client.send_message(message=message, room=room_id)


def greet_logout(user):
    """
    Send a goodbye message to the greet channel when a user logs out.
    """
    message = f"See you later, @{user}! 👋"
    room_id = client.get_room_id(config.GREET_CHANNEL)
    client.send_message(message, room_id)
