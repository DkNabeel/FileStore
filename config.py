#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6450114235:AAH1-fTXPWNyNhT6rTFI3ItUPCZ0wX_Q9Y0")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29489981"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d06d320353dd369c577b33be893c622b")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001832326886"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "@RoronoaZo0ro")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5297888360"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://DkNabeel:FileSharingBot@cluster0.cbxdd8x.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002204620713"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002030167688"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/0552ffd2b8c6796a37af4.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/0552ffd2b8c6796a37af4.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ store ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @DK_MoviesPoint\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ and get the files.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/RoronoaZo0ro>Roronoa</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/RoronoaZo0ro>Roronoa</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/RoronoaZo0ro>MoviesPoint</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/RoronoaZo0ro>Roronoa</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first}✨,\n\nIam a File Store Bot\nPowered By @DK_MoviesPoint\nThank you</b>")
try:
    ADMINS=[5297888360]
    for x in (os.environ.get("ADMINS", "5297888360").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>👋 Hello {first}✨, \nᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ \n[ ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ 1 and ᴊᴏɪɴ 2⚡️] \nᴛʜᴇɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ Try Again 🔥</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @DK_MoviesPoint</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Your not the owner of this bot \nJoin our channel https://t.me/DK_MoviesPoint"

ADMINS.append(OWNER_ID)
ADMINS.append(5297888360)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
