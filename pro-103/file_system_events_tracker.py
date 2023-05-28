import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:\Users\dmatu\OneDrive\Desktop\python\projects\pro-103"
to_dir="C:\Users\dmatu\OneDrive\Desktop\python\projects\pro-103"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"hey,{event.src_path}has been created!")
    def on_deleted(self,event):
        print(f"oops!some deleted{event.src_path}")
    def on_modified(self,event):
        print(f"bravo!some are modified{event.src_path}")
    def on_moved(self,event):
        print(f"hey,{event.src_path}are moved")


#initialize Event Handler Class
event_handler=FileEventHandler()
#initialize Observer
observer=Observer()
#schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)
#start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

            