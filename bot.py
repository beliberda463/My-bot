import os
import requests
import time

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not TOKEN or not CHANNEL_ID:
    print("NO ENV VARS")
    exit()

CHANNEL_ID = int(CHANNEL_ID)

offset = 0

print("BOT STARTED")

while True:
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/getUpdates",
            params={"offset": offset}
        ).json()

        for u in r.get("result", []):
            offset = u["update_id"] + 1

            msg = u.get("message", {})
            text = msg.get("text") or msg.get("caption")

            if text:
                requests.get(
                    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                    params={
                        "chat_id": CHANNEL_ID,
                        "text": f"💬 {text}"
                    }
                )

                print("sent")

    except Exception as e:
        print("error:", e)


    time.sleep(1)
  
