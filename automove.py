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
        self.isFoldersExist()
    def on_modified(self, event):
        
        for filename in os.listdir(targetFolder):
            newName = str(self.fileCounter) + "_newFile" + filename
            fileExists = os.path.isfile(destinationFolder+ '/'+ newName)
            while fileExists:
                
                self.fileCounter += 1
                newName = str(self.fileCounter) + "_newFile_" + filename
                fileExists = os.path.isfile(destinationFolder+ '/'+ newName)
                
                    
            
            src = targetFolder + '/'+ filename
            newDestination = destinationFolder + '/'+ newName
            os.rename(src, newDestination)
    # Checking directory exist OR nor
    def isFoldersExist(self):
        tfolder = os.path.isdir(targetFolder)#target directory
        dfolder = os.path.isdir(destinationFolder)# Destination directory
        if tfolder == False : os.mkdir(targetFolder)
        if dfolder == False : os.mkdir(destinationFolder)
    
targetFolder = 'firstFolder'
destinationFolder = 'secondFolder2'

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