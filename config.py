# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25352517"))
API_HASH = getenv("API_HASH", "2b7e6cf7752c3af91f958d67793a3e0b")
BOT_TOKEN = getenv("BOT_TOKEN", "7453258851:AAHBn_uEs9gmCtjKN-MOKJOaeQnXdL85axk")
OWNER_ID = int(getenv("OWNER_ID", "6095243761"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002204734880"))
FORCESUB = getenv("FORCESUB", "might")
