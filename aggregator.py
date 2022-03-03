import subprocess
import sys

import pkg_resources

required = {"telethon", "colorama", "getpass4"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

import re
import signal
from os import system

from colorama import Fore
from getpass4 import getpass
from telethon import TelegramClient
from telethon.sync import TelegramClient

system("cls || clear")

red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
lightgreen = Fore.LIGHTGREEN_EX

print(
    red
    + "Get Telegram developer credentials from https://my.telegram.org/auth\n"
    + white
)

name = "Telegram reporter"
api_id = getpass(
    red
    + "┌─["
    + lightgreen
    + name
    + blue
    + "~"
    + white
    + "@API-ID"
    + red
    + """]
└──╼ """
    + white
)
api_hash = getpass(
    red
    + "┌─["
    + lightgreen
    + name
    + blue
    + "~"
    + white
    + "@API-HASH"
    + red
    + """]
└──╼ """
    + white
)

client = TelegramClient(name, api_id, api_hash)

LINKS = []


def save_unique(list1):

    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    textfile = open("new_channels.txt", "w")
    for element in unique_list:
        textfile.write(element + "\n")
    textfile.close()


async def main(channel):
    await client.start()
    async for message in client.iter_messages(channel):
        LINKS.extend(re.findall("https?://t.me/[^\s]+", str(message.message)))
        # print(utils.get_display_name(message.sender), message.message)
    LINKS.sort()
    save_unique(LINKS)


def exit_gracefully(signal, frame):
    print("\nApplication shutdown")
    sys.exit(1)


with client:
    signal.signal(signal.SIGINT, exit_gracefully)
    client.loop.run_until_complete(main(sys.argv[1]))
