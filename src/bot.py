# Main script that runs the bot
import time
from rocket_client import RocketChatClient
from handlers import greet_login, greet_logout

client = RocketChatClient()


logged_in_users = set()


def poll_login_logout(interval=10):
    global logged_in_users

    while True:
        users = client.get_users()
        current_users = {u["_id"] for u in users if u.get("status") == "online"}

        # Detect logins
        for uid in current_users - logged_in_users:
            user = next(u for u in users if u["_id"] == uid)
            greet_login(user)

        # Detect logouts
        for uid in logged_in_users - current_users:
            user = next(u for u in users if u["_id"] == uid)
            greet_logout(user)

        logged_in_users = current_users
        time.sleep(interval)


if __name__ == "__main__":
    poll_login_logout()
