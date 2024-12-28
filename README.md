# File Integrity Monitor

A Python-based file monitoring system that tracks file changes, generates checksums, and sends alerts when modifications are detected.

## Features

- Real-time file monitoring using watchdog
- MD5 and SHA-256 checksum generation
- Email notifications for file modifications
- Configurable monitoring rules
- Detailed change logging

## Requirements

```
Python 3.9+
watchdog
pyyaml
cryptography
```

## Installation

```bash
git clone https://github.com/boderebesec/file_monitor.git
cd file_monitor
pip install -r requirements.txt
```

## Configuration

Edit the `monitor_config.yaml` file to set up your monitoring preferences:

```yaml
email:
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  sender_email: "your-email@domain.com"
  sender_password: "your-app-password"
  recipient_email: "recipient@domain.com"

monitoring:
  recursive: true
  ignore_patterns: ["*.tmp", "*.log"]
  paths:
    - "/path/to/monitor"
```

## Usage

Run the monitor with:

```bash
python main.py
```

## Features in Detail

### File Monitoring

The system monitors specified directories for:

- File creation
- File modification
- File deletion
- File movement

### Checksum Generation

Generates and maintains:

- MD5 checksums
- SHA-256 checksums

### Alert System

Sends email notifications when:

- Files are modified
- New files are created
- Files are deleted
- Checksums don't match

## Project Structure

```
file_monitor/
├── src/
│   ├── __init__.py
│   ├── alert_system.py
│   ├── hash_generator.py
│   ├── monitor.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_monitor.py
├── config/
│   └── monitor_config.yaml
├── logs/
│   └── changes.log
├── main.py
└── requirements.txt
```

## Security Considerations

- Store sensitive information like email credentials securely
- Use app-specific passwords for email services
- Regularly update dependencies
- Monitor log files for suspicious activities

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Jason Boderebe - [GitHub Profile](https://github.com/boderebesec)
