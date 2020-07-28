import random

from Common.handle_db import HandleDB
from Common.get_config import conf
from Common.handle_request import send_requests
import requests

phone_head = [150, 151, 152, 153, 155, 156, 157, 158, 159, 130, 131, 132, 133,
                134, 135, 136, 137, 138, 139, 147, 180, 182, 185, 186, 187, 188, 189]


def get_new_phone():
    con_db = HandleDB()
    while True:
        phone = __generate_phone()
        count = con_db.get_count('select mobile_phone from member where mobile_phone="{}"'.format(phone))
        if count == 0:
            con_db.close()
            return phone


def get_old_phone():
    phone = conf.get("default_user", "phone")
    pwd = conf.get("default_user", "pwd")
    # send_requests("post", "member/register", data={"mobile_phone": phone, "pwd": pwd})
    requests.post(url="http://api.lemonban.com/futureloan/member/register", json={"mobile_phone": phone, "pwd": pwd})
    return phone, pwd


def __generate_phone():
    phone = str(random.choice(phone_head))
    for _ in range(0, 8):
        i = str(random.randint(0, 9))
        phone += i
    return phone


if __name__ == '__main__':
    print(get_new_phone())