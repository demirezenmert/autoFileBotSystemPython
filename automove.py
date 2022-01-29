from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os,json

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/'+ filename
            newDestination = folderDestination + '/'+ filename
            os.rename(src, newDestination)

folder_to_track = 'firstFolder'
folderDestination = 'secondFolder'
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, folder_to_track, recursive= True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()