"""
Unit tests for the File Monitor module.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.monitor import FileMonitor, FileChangeHandler
from src.hash_generator import HashGenerator
from src.alert_system import AlertSystem

class TestFileMonitor(unittest.TestCase):
    """
    Unit tests for the FileMonitor class.
    """
    @patch('src.monitor.Observer')
    @patch('src.monitor.HashGenerator')
    @patch('src.monitor.AlertSystem')
    def setUp(self, MockAlertSystem, MockHashGenerator, MockObserver):
        self.mock_observer = MockObserver()
        self.mock_hash_generator = MockHashGenerator()
        self.mock_alert_system = MockAlertSystem()
        self.file_monitor = FileMonitor('/path/to/watch')

    def test_start_monitoring(self):
        """
        Test that the monitoring process starts correctly.
        """
        self.file_monitor.start_monitoring()
        self.mock_observer.schedule.assert_called_once()
        self.mock_observer.start.assert_called_once()

    @patch('src.monitor.time.sleep', return_value=None)
    def test_monitoring_loop(self, mock_sleep):
        """
        Test the monitoring loop.
        """
        with patch.object(self.file_monitor.observer, 'stop') as mock_stop:
            with patch.object(self.file_monitor.observer, 'join') as mock_join:
                with self.assertRaises(KeyboardInterrupt):
                    self.file_monitor.start_monitoring()
                mock_stop.assert_called_once()
                mock_join.assert_called_once()

class TestFileChangeHandler(unittest.TestCase):
    """
    Unit tests for the FileChangeHandler class.
    """
    @patch('src.monitor.HashGenerator')
    @patch('src.monitor.AlertSystem')
    def setUp(self, MockHashGenerator, MockAlertSystem):
        self.mock_hash_generator = MockHashGenerator()
        self.mock_alert_system = MockAlertSystem()
        self.file_change_handler = FileChangeHandler(self.mock_hash_generator, self.mock_alert_system)

    @patch('src.monitor.logging.getLogger')
    def test_on_modified(self, mock_get_logger):
        """
        Test the on_modified event handler.
        """
        mock_event = MagicMock()
        mock_event.is_directory = False
        mock_event.src_path = '/path/to/file'
        self.mock_hash_generator.generate_hash.return_value = 'new_hash'
        self.file_change_handler.on_modified(mock_event)
        self.mock_hash_generator.generate_hash.assert_called_once_with('/path/to/file')
        self.mock_alert_system.send_alert.assert_called_once()

if __name__ == '__main__':
    unittest.main()