# Wrapper for RocketChat API interactions
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import config


class RocketChatClient:
    def __init__(self):
        self.client = None

    def connect(self):
        """Initialize RocketChat client and login."""
        try:
            self.client = RocketChatAPI(
                user=config.ROCKETCHAT_USER,
                password=config.ROCKETCHAT_PASSWORD,
                server_url=config.ROCKETCHAT_URL,
            )
            print("Bot connected successfully")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise

    def send_message(self, message, room, **kwargs):
        """
        Send a message to a given room
        """
        try:
            self.client.send_message(
                kwargs,
                message=message,
                room_id=room,
            )
            print(f"Sent a message to room({room}): {message}")
        except Exception as e:
            print(f"Failed to send a message: {str(e)}")
            raise

    def get_users(self, **kwargs):
        """
        Gets all of the users in the system and their information
        :param kwargs:
        :return:
        """
        try:
            return self.client.get_users(kwargs)
        except Exception as e:
            print(f"Failed to get the users: {str(e)}")
            raise

    def get_room_id(self, room_name, **kwargs):
        """
        Get room ID
        :param room_name:
        :param kwargs:
        :return:
        """
        try:
            return self.client.get_room_id(
                kwargs,
                room_name=room_name,
            )
        except Exception as e:
            print(f"Failed to get the room id: {str(e)}")
            raise
