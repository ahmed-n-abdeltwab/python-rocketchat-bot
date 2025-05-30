# Handles login/logout and message logic
from rocket_client import RocketChatClient
import config

client = RocketChatClient()


def connect():
    """
    Connect to the RocketChat server.
    """
    client.connect()


def logout():
    """
    Logout from the RocketChat server.
    """
    if not client.is_connected():
        raise RuntimeError("RocketChat client is not connected. Call connect() first.")

    try:
        client.logout()
        print("Logged out successfully")
    except Exception as e:
        print(f"Failed to logout: {str(e)}")
        raise


def get_users(**kwargs) -> list:
    """
    Retrieve all users and their information, limited to permissions.
    """
    if not client.is_connected():
        raise RuntimeError("RocketChat client is not connected. Call connect() first.")

    try:
        return client.get_users(**kwargs)
    except Exception as e:
        print(f"Failed to get the users: {str(e)}")
        raise


def greet_login(user: dict):
    """
    Send a welcome message to the greet channel when a user logs in.
    """
    message = f"Welcome, @{user['username']}! Glad you're here! 🚀"
    room_id = client.get_room_id(room_name=config.CHANNEL)
    client.send_message(text=message, room_id=room_id)


def greet_logout(user: dict):
    """
    Send a goodbye message to the greet channel when a user logs out.
    """
    message = f"See you later, @{user['username']}! 👋"
    room_id = client.get_room_id(room_name=config.CHANNEL)
    client.send_message(text=message, room_id=room_id)
