import os

ADMIN_BOT_TOKEN = os.getenv("ADMIN_BOT_TOKEN", "8929358983:AAG8_6ZDZcjgnDWPPTd3UX-tawjJ8IZN8ao")
STORE_BOT_TOKEN = os.getenv("STORE_BOT_TOKEN", "8987080415:AAGeICGQQlUCyctIsdQUxGLlwS93lLVrT4Q")

# Owner(s) - can add/remove other sellers. Comma separated telegram user ids.
OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS", "8656857571").split(",") if x.strip().isdigit()]

STORE_NAME = "Uchiro Store 🇰🇭"
CURRENCY = "$"
CATEGORIES = ["Account", "Fruit", "Gamepass"]
DB_PATH = os.getenv("DB_PATH", "store.db")

ADMIN_CONTACT_USERNAME = "noreakyout"  # @noreakyout
