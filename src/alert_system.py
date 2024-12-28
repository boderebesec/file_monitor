"""
Alert System module for sending email alerts.
"""

import smtplib
from email.message import EmailMessage
import logging
import yaml

class AlertSystem:
    """
    Sends email alerts for file changes.
    """
    def __init__(self, config_path='config/monitor_config.yaml'):
        self.config = self._load_config(config_path)
        self.logger = logging.getLogger('AlertSystem')

    def _load_config(self, config_path):
        """
        Loads the email configuration from a YAML file.
        """
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def send_alert(self, message):
        """
        Sends an email alert with the given message.
        """
        try:
            email_msg = EmailMessage()
            email_msg.set_content(message)
            email_msg['Subject'] = 'File Integrity Alert'
            email_msg['From'] = self.config['email']['sender_email']
            email_msg['To'] = self.config['email']['recipient_email']

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(
                    self.config['email']['sender_email'],
                    self.config['email']['sender_password']
                )
                smtp.send_message(email_msg)
            
            self.logger.info('Alert sent successfully')
        except Exception as e:
            self.logger.error(f'Failed to send alert: {str(e)}')