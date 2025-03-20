import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "66951")) #⚠️optional
API_HASH = getenv("API_HASH", "") #⚠️optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split())) #⚠️ Separate by space
OWNER_ID = int(getenv("OWNER_ID", "7932740574")) 
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kurt67143:DLArCT171SF9wRKJ@alexsoza.xpoqv.mongodb.net/?retryWrites=true&w=majority&appName=Alexsoza")
BOT_TOKEN = getenv("BOT_TOKEN", "7606090885:AAGZccN6XRe1I7uewcNrTltt10uPBhXwBHg")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/4513f188be254572697e3.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1002509634565")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ichbinmusto/Gg") 
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1sBu1lxSCKlmjNuIXNxwQAPjG4DbZnpfsjRtDVnXdrZSlpuqVUVL1F0k1wZR1efLFvb9lOamh4uOgnjkRER1ACUjLQMU74OdxTeJBWHZDBlxWk6KPwtHfLcOM2i2NA1TRuEUa3nX91cgjEbKjMh4f5ARvlQHThpGWwfz_tSzUFVFfRJzlGtq1WhbFwmqQGDVhgpZP-4FTOqtgDJ1q_iOEhTfwN_rnVqS2ISJFXPV2yUhrxkS59mxr3DRsqVwdFIWdc-pMYtROIVytYAXCEl6B_--GrTnSS3Ky4ypfrpTzsnfRKvbzPqICoqhniI86-pEXIhqelEhxiSEAAcvACjH8XWsgQ=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
