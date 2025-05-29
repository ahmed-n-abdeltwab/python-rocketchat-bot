# Wrapper for RocketChat API interactions
from pprint import pprint
from typing import Any, Optional
from rocketchat_API.rocketchat import RocketChat
import config


class RocketChatClient:
    def __init__(self):
        self.user = config.ROCKETCHAT_USER
        self.password = config.ROCKETCHAT_PASSWORD
        self.server_url = config.ROCKETCHAT_URL
        self.channel = config.CHANNEL
        self.client = None

    def connect(self):
        """
        Initialize RocketChat client and login.
        """
        try:
            self.client = RocketChat(
                user=self.user,
                password=self.password,
                server_url=self,
            )
            print("Bot connected successfully")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise

        def send_message(
            self,
            text: Any,
            room_id: Optional[Any] = None,
            channel: Optional[Any] = None,
            **kwargs: Any,
        ):
            """
            Send a message to a given room
            """
            try:
                self.client.chat_post_message(
                    text=text, room_id=room_id, channel=channel, **kwargs
                )
                if room_id is None:
                    print(f"Sent a message to channel({channel}): {text}")
                else:
                    print(f"Sent a message to room({room_id}): {text}")
            except Exception as e:
                print(f"Failed to send a message: {str(e)}")
                raise

    def get_users(self, **kwargs: Any):
        """
        All of the users and their information, limited to permissions.
        """
        try:
            return self.client.users_list(kwargs)
        except Exception as e:
            print(f"Failed to get the users: {str(e)}")
            raise

    def get_room_id(
        self, room_id: Optional[Any] = None, room_name: Optional[Any] = None
    ):
        """
        Retrieves the information about the room.
        """
        try:
            return self.client.rooms_info(
                room_id,
                room_name,
            )
        except Exception as e:
            print(f"Failed to get the room id: {str(e)}")
            raise
