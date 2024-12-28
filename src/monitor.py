"""
File Monitor module that uses watchdog to monitor file changes.
"""

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
from src.hash_generator import HashGenerator
from src.alert_system import AlertSystem

class FileChangeHandler(FileSystemEventHandler):
    """
    Handles file change events.
    """
    def __init__(self, hash_generator, alert_system):
        self.hash_generator = hash_generator
        self.alert_system = alert_system
        self.logger = logging.getLogger('FileMonitor')

    def on_modified(self, event):
        """
        Called when a file is modified.
        """
        if not event.is_directory:
            file_path = event.src_path
            new_hash = self.hash_generator.generate_hash(file_path)
            self.logger.info(f"File modified: {file_path}")
            self.alert_system.send_alert(
                f"File {file_path} has been modified\nNew hash: {new_hash}"
            )

class FileMonitor:
    """
    Monitors a directory for file changes.
    """
    def __init__(self, path_to_watch):
        self.path = path_to_watch
        self.observer = Observer()
        self.hash_generator = HashGenerator()
        self.alert_system = AlertSystem()
        self.event_handler = FileChangeHandler(
            self.hash_generator, 
            self.alert_system
        )

    def start_monitoring(self):
        """
        Starts the file monitoring process.
        """
        self.observer.schedule(
            self.event_handler, 
            self.path, 
            recursive=False
        )
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()