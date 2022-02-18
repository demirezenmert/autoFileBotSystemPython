
# Python File Manager

Python FileManager is the file handling move to source to target folder automatically. You just put in data into it and it will automatically store in on 
target folder.
It's automation example, you'll just run the script in the background it will automatically handle the all the events occurs in the folder. And move from automatically
source to target folder.

Note: This script is designed to work on UNIX/Linux(May work on Windows)
Anyone is welcome to fork this and modify as they please.

I hope someone finds this useful. I use it to move files older than 15 days from Downloads to a trash folder on my machine to save space.

### Built With
* [Python3](https://www.python.org/download/releases/3.0/)
* [Watchdog](https://pypi.org/project/watchdog/)




### Prerequisites
The script is installing automatically all the libraries what needs.

But just in case you can manually install libraries;
```sh
pip install watchdog
```
```sh
pip install EventHandler
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/demirezenmert/autoFileBotSystemPython.git
```
2. Change your directory into script folder
```sh
cd autoFileBotSystemPython
```
3. Run the script (python/ python3)
```sh
python automove.py
```
