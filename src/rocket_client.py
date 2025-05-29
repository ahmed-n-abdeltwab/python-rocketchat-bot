# Wrapper for RocketChat API interactions
from rocketchat_API.rocketchat import RocketChat
import config


class RocketChatClient:
    def __init__(self):
        self.client = None

    def connect(self):
        """Initialize RocketChat client and login."""
        try:
            self.client = RocketChat(
                user=config.ROCKETCHAT_USER,
                password=config.ROCKETCHAT_PASSWORD,
                server_url=config.ROCKETCHAT_URL,
            )
            print("Bot connected successfully")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise

    def send_message(self, message, room):
        """Send a message to the configured room."""
        try:
            self.client.send_message(message, room_id=room)
            print(f"Sent a message to room({room}): {message}")
        except Exception as e:
            print(f"Failed to send a message: {str(e)}")
            raise

    def get_users(self):
        try:
            return self.client.get_users()
        except Exception as e:
            print(f"Failed to get the users: {str(e)}")
            raise

    def get_room_id(self, room_name):
        return self.client.get_room_id(room_name)
