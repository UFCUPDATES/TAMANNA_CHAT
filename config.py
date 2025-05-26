from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8195333063"))
SUPPORT_GRP = "UFC_UPDATES"
UPDATE_CHNL = "ll_P_U_L_lI"
OWNER_USERNAME = "l_HEART_BEAT_l"
