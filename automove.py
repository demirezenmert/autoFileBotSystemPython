try:
    from watchdog.observers import Observer
    import time
    from watchdog.events import FileSystemEventHandler
    import os,json
        
except ModuleNotFoundError:
    from subprocess import call
    modules = ['watchdog']
    call('pip install '+ ''.join(modules),shell=True)


class MyHandler(FileSystemEventHandler):
    def __init__(self,fileCounter = 1):
        self.fileCounter = fileCounter
    def on_modified(self, event):
        
        for filename in os.listdir(targetFolder):
            newName = str(self.fileCounter) + "_newFile" + filename
            fileExists = os.path.isfile(folderDestination+ '/'+ newName)
            while fileExists:
                
                self.fileCounter += 1
                newName = str(self.fileCounter) + "_newFile_" + filename
                fileExists = os.path.isfile(folderDestination+ '/'+ newName)
                
                    
            
            src = targetFolder + '/'+ filename
            newDestination = folderDestination + '/'+ newName
            os.rename(src, newDestination)
    
targetFolder = 'firstFolder'
folderDestination = 'secondFolder'
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, targetFolder, recursive= True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()