import requests
import time
from datetime import datetime

_COOKIE = "PUT REAL COOKIE HERE"

def changeStatus(cookie, text, emoji):
    print("Changed status")
    url = "https://discord.com:443/api/v8/users/@me/settings"
    cookies = {"__cfduid": cookie, "_gat_UA-53577205-2":"1"}
    headers = {"Connection": "close", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg0LjAuNDE0Ny44OSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODQuMC40MTQ3Ljg5Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjgxNTI2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "Authorization": "NDYyMjMxOTY3MTQwODA2NjU2.YG88Gg.TxhX6FISYVjXIJOJvfrbtQcTxIk", "Accept-Language": "en-US", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://discord.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://discord.com/channels/@me", "Accept-Encoding": "gzip, deflate"}
    if emoji is not None:
        json={"custom_status": {"text": text, "emoji_name": emoji}}
    else:
        json={"custom_status": {"text": text}}
    response = requests.patch(url, headers=headers, cookies=cookies, json=json)
    print(response)

def AMPM(hour):
    if hour < 12:
        return hour
    else:
        return hour - 12

if __name__ == "__main__":
    while True:
        timeNow = datetime.now()
        hour = timeNow.hour
        minute = timeNow.minute
        lastRecordedTime = minute
        while lastRecordedTime == minute:
            time.sleep(0.5)
            timeNow = datetime.now()
            hour = timeNow.hour
            minute = timeNow.minute
        lastRecordedTime = minute
        changeStatus(_COOKIE, "🕒 " + str(AMPM(hour)) + ":" + str(minute) + " 🕒", None)
