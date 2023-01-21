import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13726853"))
    API_HASH = os.environ.get("API_HASH", "749e522c40616d1fee242fe8974527b9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5781064175:AAFcZq82PrsrNrGw0zx2M5_wGT8pIMGDgpA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBKlqRKPwKYiouUV2m1xvt2reRTyjSGFRHLJi7nR5szKlSWXl9_A4T67laLClX8SXn_jBccmV61r-5ZjrWadZ9yFx-N0VZn-XiZ2iY3MtYAxeru8mZECsfiN9c3mfKy6NYXXkrKV53A1yft0P8Y0zrf6jZ-D3V5jPToUtHR4SbMjsLfZNFOiuVinb1qwV30nT89RUvbkE-xm6dHXJQYY863Zce-9P0zxqfFF5VHjS8Kgavh8VFwJ4xWZ9GLf9VMrvZmgjeJijvALZ47SCcEfrnD4I--9TQqtRw72FHZX57WPp1vYyFqpZ3Ycng7TFkxN1zg13F9L9hmCcGNy7QWxfU-AAAAAS8lsr0A")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "True")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Dreamxgirl_robot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/mirachlenetwork") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/darkdevilfederation") # Your Channel
    Source_code = os.environ.get("Source_code"," abe laude  repo chahiye to group join kar 🤨🤨") #your Source_code
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/44bb9002b357dac5c2d6a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/6e5cd3bf33db8bd03a91c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5085967037")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
