# User-bot, which automates the reporting of Telegrams of Russian propagandist channels

## Be careful, Telegram can temporary block your account (This will prevent you from publishing new reports and joining new channels for about 20 hours)

## The bot works with a delay of 10-15 seconds per message to avoid a temporary ban.

## Install 
1. [Install python3](https://www.python.org/) and [git](https://git-scm.com/downloads).
2. Launch the terminal
<br>On Windows: click ctrl + r, and write **cmd**
<br>On Linux or MacOS: run terminal
3. Paste to terminal
```
git clone https://github.com/BohdanBuinich/telegram-reporter.git
cd telegram-reporter
python3 telegram-reporter.py
```
or on Windows
```
py telegram-reporter.py
```

4. Open the link [https://my.telegram.org](https://my.telegram.org/),and log in using your mobile phone number
Click **API development tools** enter **App title** and **Short name** **(App title and Short name can be whatever)**
<br>Then you get api_id and api_hash, which you can use in the program
5. The program will then ask you to enter api_id and api_hash, after which you will need to enter your phone number (in format +380XXXXXXXX) to which the telegram is used, and the code you will receive

**Example Working Application**
![Alt text](Screenshot.png?raw=true)