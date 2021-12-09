# Github's integration with Telegram bot

myGit is the your GiHub assistant. In your conversations with your team, you can simply insert the information about the projects you are working at. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install python-telegram-bot
pip install PyGithub
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To cotribute you should create your **own** Telegram bot for development (e.g. development_myGit_bot). To create a new bot you need to open the Telegram app and find BotFather. Type **/newbot** and there will appear the instructions. After you received your telegram's bot API token you need to copy it **'/token/token.txt'**.

Now you are good to go.

```python
python main.py
```

## Docs

Get connected to the GitHub's API
```python
import get_connection as github
git = github.get_connection(telegram_user_id)
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
