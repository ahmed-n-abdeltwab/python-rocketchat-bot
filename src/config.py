# Configuration variables (URLs, credentials, etc.)
import os

ROCKETCHAT_URL = os.getenv("ROCKETCHAT_URL", "http://localhost:3000")
ROCKETCHAT_USER = os.getenv("ROCKETCHAT_USER", "rocketchat.internal.admin.test")
ROCKETCHAT_PASSWORD = os.getenv("ROCKETCHAT_PASSWORD", "rocketchat.internal.admin.test")
CHANNEL = os.getenv("CHANNEL", "general")
