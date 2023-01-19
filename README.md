# CoreKeeper Bot
This is a simple Discord Webhook that will send notifications to the specified Discord channel when a player joins or leaves a dedicated CoreKeeper server. It works by constantly monitoring the CoreKeeper log file and detects if a player has joined or left the game. Keep in mind that the server/computer that this program is running on would need to constantly be on for it to work.

# Required Packages
To install python packages using a requirements.txt file, you will need to have Python and pip (the package installer for Python) installed on your computer. If you don't have these tools, you can download them from the official Python website (https://www.python.org/downloads/).

1. Open a terminal or command prompt and navigate to the directory where the requirements.txt file is located.
2. Run the following command to install the packages listed in the file:
```
pip install -r requirements.txt
```
This will install all the packages listed in the requirements.txt file to your Python environment. If you want to install the packages in a virtual environment, you can create one using virtualenv and activate it before running the above command.

# Installation
1. Clone the repository into the same directory that the CoreKeeperLog.txt file is located
2. Run the program using Python:
```
py corekeeper.py
```