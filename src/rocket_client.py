# Wrapper for RocketChat API interactions
from rocketchat_API.rocketchat import RocketChat
import config


class RocketChatClient:
    def __init__(self): ...

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

    def post_message(self, message, room):
        return self.client.chat_post_message(message, room_id=room)

    def get_users(self):
        return self.client.users_list().json().get("users", [])

    def get_room_id(self, room_name):
        rooms = self.client.channels_list().json().get("channels", [])
        for room in rooms:
            if room["name"] == room_name.lstrip("#"):
                return room["_id"]
        return None
