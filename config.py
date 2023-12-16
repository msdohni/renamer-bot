import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26579601")
API_HASH = os.environ.get("API_HASH", "5b811e9e89adfe6c636d3328b247779d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5402380823:AAGMW-Fqp_U8jrQJlaeZOn4l6aCUDYrnbhw") 
#TOKEN_ONE = os.environ.get("TOKEN_ONE", "5402380823:AAGMW-Fqp_U8jrQJlaeZOn4l6aCUDYrnbhw")

CHANNEL = os.environ.get("CHANNEL", "ATL_Univers") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","ATL_Univers") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","HMF_Owner_1")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","stautofilesbot")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://stautofilesbot:stautofilesbot@cluster0.gok4b.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6838589973').split()]
PORT = os.environ.get('PORT', '80')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001790795488"))
