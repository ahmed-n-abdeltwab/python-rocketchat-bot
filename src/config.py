# Configuration variables (URLs, credentials, etc.)
import os

ROCKETCHAT_URL = os.getenv("ROCKETCHAT_URL")
ROCKETCHAT_USER = os.getenv("ROCKETCHAT_USER")
ROCKETCHAT_PASSWORD = os.getenv("ROCKETCHAT_PASSWORD")
GREET_CHANNEL = os.getenv("GREET_CHANNEL", "#general")
