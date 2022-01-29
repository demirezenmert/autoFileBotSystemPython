from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os,json

class MyHandler(FileSystemEventHandler):
    def __init__(self,fileCounter = 1):
        self.fileCounter = fileCounter
    def on_modified(self, event):
        
        for filename in os.listdir(folder_to_track):
            newName = str(self.fileCounter) + "_newFile" + filename
            fileExists = os.path.isfile(folderDestination+ '/'+ newName)
            while fileExists:
                self.fileCounter += 1
                newName = str(self.fileCounter) + "_newFile_" + filename
            self.fileCounter += 1
            src = folder_to_track + '/'+ filename
            newDestination = folderDestination + '/'+ newName
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