# Handles login/logout and message logic
from rocket_client import RocketChatClient
import config

client = RocketChatClient()


def greet_login(user):
    message = f"👋 Welcome back, {user['username']}!"
    room_id = client.get_room_id(config.GREET_CHANNEL)
    client.post_message(message, room_id)


def greet_logout(user):
    message = f"👋 Goodbye, {user['username']}! See you later."
    room_id = client.get_room_id(config.GREET_CHANNEL)
    client.post_message(message, room_id)
