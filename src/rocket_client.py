# Wrapper for RocketChat API interactions
from pprint import pprint
from typing import Any, Optional
from rocketchat_API.rocketchat import RocketChat
import config


class RocketChatClient:
    """
    A client for interacting with RocketChat API.
    This class provides methods to connect to the RocketChat server,
    send messages, retrieve users, and get room information.
    """

    def __init__(self):
        """
        Initialize the RocketChat client with configuration parameters.
        """
        self.user = config.ROCKETCHAT_USER
        self.password = config.ROCKETCHAT_PASSWORD
        self.server_url = config.ROCKETCHAT_URL
        self.channel = config.CHANNEL
        self.client = None

    def connect(self) -> None:
        """
        Initialize RocketChat client and login.
        """
        try:
            self.client = RocketChat(
                user=self.user,
                password=self.password,
                server_url=self.server_url,
            )
            print("Bot connected successfully")
        except Exception as e:
            print(f"Failed to connect: {str(e)}")
            raise

    def send_message(
        self,
        text: str,
        room_id: Optional[str] = None,
        channel: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
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

    def get_users(self, **kwargs: Any) -> list:
        """
        All of the users and their information, limited to permissions.
        """
        if not self.is_connected():
            raise RuntimeError(
                "RocketChat client is not connected. Call connect() first."
            )

        try:
            return self.client.users_list(**kwargs).json().get("users", [])
        except Exception as e:
            print(f"Failed to get the users: {str(e)}")
            raise

    def get_room_id(
        self, room_id: Optional[str] = None, room_name: Optional[str] = None
    ):
        """
        Retrieves the information about the room.
        """
        if not self.is_connected():
            raise RuntimeError(
                "RocketChat client is not connected. Call connect() first."
            )

        if room_id is None and room_name is None:
            raise ValueError("Either room_id or room_name must be provided.")

        try:
            return self.client.rooms_info(room_name=room_name)
        except Exception as e:
            print(f"Failed to get the room id: {str(e)}")
            raise

    def logout(self):
        """
        Logout the client.
        """
        if not self.is_connected():
            print("RocketChat client is not connected. No need to logout.")
            return

        try:
            self.client.logout()
            print("Logged out successfully")
        except Exception as e:
            print(f"Failed to logout: {str(e)}")
            raise

    def is_connected(self) -> bool:
        """
        Check if the client is connected.
        """
        return self.client is not None and self.client.me().json().get("success", False)

    def __del__(self):
        """
        Ensure the client is logged out when the instance is deleted.
        """
        if self.client is not None:
            self.logout()
            print("Destructor: RocketChat client instance deleted and logged out.")
        else:
            print(
                "Destructor: RocketChat client instance deleted without logout (not connected)."
            )
        self.client = None
        print("Destructor: RocketChat client instance deleted.")
