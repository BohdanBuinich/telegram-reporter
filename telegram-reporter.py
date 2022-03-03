import subprocess
import sys

import pkg_resources

required = {"telethon", "colorama", "getpass4"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])

import asyncio
import random
import requests
import signal
from os import system

from colorama import Fore
from getpass4 import getpass
from telethon import TelegramClient, functions, types
from telethon.sync import TelegramClient

system("cls || clear")

red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
lightgreen = Fore.LIGHTGREEN_EX

print(
    f"""
████████╗███████╗██╗░░░░░███████╗░██████╗░██████╗░░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗████╗░████║
░░░██║░░░█████╗░░██║░░░░░█████╗░░██║░░██╗░██████╔╝███████║██╔████╔██║
░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗███████╗███████╗╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

██████╗░███████╗██████╗░░█████╗░██████╗░████████╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░█████╗░░██████╔╝
██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    """
)

MESSAGES = [
    "The channel undermines the integrity of the Ukrainian state. Spreading fake news, misleading and misleading people. Block it as soon as possible!",
    "There are many posts with threats against the Ukrainian military. Lots of photos of the dead, blood and weapons. Block it!",
    "Propaganda of the war in Ukraine. Propaganda of murders of Ukrainians and Ukrainian soldiers. Block it!",
    "Dissemination of military personal data. Block the channel!",
    "Publication of military deaths, brutal killings, violence and hostilities. Please block the channel!",
    "Пропаганда. Розповсюдження некоректної інформації (пропаганда), що призводить до розпалення міжнаціонального конфлікту. Заблокуйте його якомога швидше!",
    "Міжнаціональний конфлікт. Розповсюдження некоректної інформації, яка вводить в оману користувачів та посилює міжнаціональний конфлікт. Заблокуйте його",
    "Розпалення військового конфлікту. Контент групи/каналу використовується у цілях вчинення дій, що розпалюють військовий конфлікт та призводять до збільшення кількості людських жертв. Будь ласка, заблокуйте його якомога швидше!",
]

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

LINK = "https://raw.githubusercontent.com/BohdanBuinich/telegram-reporter/master/channels.txt"
CHANNELS = [line.rstrip() for line in requests.get(LINK).text.splitlines()]
random.shuffle(CHANNELS)


async def main():
    await client.start()

    for channel in CHANNELS[:130]:
        try:
            result = await client(
                functions.account.ReportPeerRequest(
                    peer=channel,
                    reason=types.InputReportReasonViolence(),
                    message=random.choice(MESSAGES),
                )
            )
            print(f"Reported {channel} - with status {result}")
        except Exception:
            print(f"Failed to report {channel}")
        await asyncio.sleep(random.randint(10, 15))


def exit_gracefully(signal, frame):
    print(red + "\nApplication shutdown. Русский корабль иди на хуй!")
    sys.exit(1)


with client:
    signal.signal(signal.SIGINT, exit_gracefully)
    client.loop.run_until_complete(main())
    print(red + "Work completed. Русский корабль иди на хуй!")
