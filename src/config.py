# Configuration variables (URLs, credentials, etc.)
import os

ROCKETCHAT_URL = os.getenv("ROCKETCHAT_URL", "http://localhost:3000")
ROCKETCHAT_USER = os.getenv("ROCKETCHAT_USER", "bot")
ROCKETCHAT_PASSWORD = os.getenv("ROCKETCHAT_PASSWORD", "botpassword")
GREET_CHANNEL = os.getenv("GREET_CHANNEL", "general")
