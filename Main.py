from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            filenameAux = filename.lower()
            if "." in filename and not filenameAux.endswith(".tmp"):
                try:
                    folder_destination = "/Users/rexli/Downloads/"
                    if filenameAux.endswith(".pdf"):
                        folder_destination += "PDFs"
                    elif filenameAux.endswith(".jpeg") or filenameAux.endswith(".jpg") or filenameAux.endswith(".png"):
                        folder_destination += "Images"
                    elif filenameAux.endswith(".exe"):
                        folder_destination += "Program Downloads exe"
                    elif filenameAux.endswith(".mv4") or filenameAux.endswith(".mp4"):
                        folder_destination += "Videos"
                    elif filenameAux.endswith(".docx"):
                        folder_destination += "Documents"
                    else:
                        folder_destination += "Unknown File Type"
                    new_destination = folder_destination + "/" + filename
                    src = folder_to_track + "/" + filename
                    time.sleep(5)
                    os.rename(src, new_destination)
                except PermissionError or FileNotFoundError or InterruptedError or FileExistsError:
                    pass


folder_to_track = "C:/Users/rexli/Downloads"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
