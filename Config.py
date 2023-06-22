import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23860620"))
    API_HASH = os.environ.get("API_HASH", "347c94d92d0bbcfbc223651b73d71345")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6099476874:AAGt2sKPtqrgBRD91Qr-yoIPs2j4cAXkgH8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu2D0RJaDUKK_mFRQHxd3tYLaVqIwYu6XObGWFGrsm-v0WuSLCuirINHwr3GzLgyVYYtTb5C8dROBonzNs1jZXwFsZucvXsqhpI6ebx3-5sYO2ZhFizWy37RebxtpMxRlsDKIAFB7qMxeUkI9mokueYIU-JvEZ6GNqU06Wq1QaGtDUKoioKXowgmAdDTpAd5yhPgTppLKUvvPFjeJRPjYFac8nU87wtVcvEhNQx3wAsYqD-RF9fjYnqAPyIKFVCT45cJncypV-7PIghv36xTz-afboj0jYMq_lBD0VfQunP7ELJXGXyXi-3nVAJA16B055V9R-_8CItPbW0rJGX9pyxw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TelethonAzMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TelethonmusicAzSup") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TelethonmusicAzChanel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5508658149")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
