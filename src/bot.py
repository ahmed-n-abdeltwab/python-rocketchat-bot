# Main script that runs the bot
from dotenv import load_dotenv

load_dotenv()

import time
import logging
import traceback
from handlers import greet_login, greet_logout, get_users, connect, logout


logged_in_users = set()


def poll_login_logout(interval=10):
    global logged_in_users

    while True:
        users = get_users()
        user_dict = {u["_id"]: u for u in users}
        current_users = {
            uid for uid, u in user_dict.items() if u.get("status") == "online"
        }

        # Detect logins
        for uid in current_users - logged_in_users:
            greet_login(user_dict[uid])

        # Detect logouts
        for uid in logged_in_users - current_users:
            greet_logout(user_dict[uid])

        logged_in_users = current_users
        time.sleep(interval)


def start():
    """Start the bot and keep it running."""
    try:
        connect()
        print("Bot is running. Press Ctrl+C to stop.")
        poll_login_logout()
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except RuntimeError as e:
        logging.exception("Runtime error occurred", exc_info=e)
    except Exception as e:
        logging.exception("Bot crashed", exc_info=e)
    finally:
        logout()


if __name__ == "__main__":
    start()
