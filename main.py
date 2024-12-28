"""
Main script to start the File Integrity Monitor.
"""

import argparse
from src.monitor import FileMonitor
import logging

def setup_logging():
    """
    Sets up logging for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='logs/changes.log'
    )

def main():
    """
    Main function to parse arguments and start monitoring.
    """
    parser = argparse.ArgumentParser(
        description='File Integrity Monitor'
    )
    parser.add_argument(
        'path',
        help='Path to monitor'
    )
    args = parser.parse_args()

    setup_logging()
    monitor = FileMonitor(args.path)
    monitor.start_monitoring()

if __name__ == '__main__':
    main()