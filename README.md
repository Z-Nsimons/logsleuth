# LogSleuth
Python-based Linux log monitoring tool that detects failed SSH login attempts and identifies brute-force attacks by analyzing /var/log/auth.log.

# Features
* Scans authentication logs for failed SSH login attempts
* Detects brute-force attack patterns by counting failed attempts per IP
* Logs suspicious activity with timestamps
* Scheduled to run automatically via cron for continuous monitoring
* Easy to customize and extend

# Installation
1. Clone this repository:
  git clone https://github.com/Z-Nsimons/logsleuth.git
  cd logsleuth
2. Ensure Python 3 is installed:
   python3 --version
3. Run the script:
   python3 log_sleuth.py

# Usage
* Run manually or set up a cron job for regular scans
* Ouput is logged in logsleuth_output.log

Example of detected suspicious activity:
[2025-07-15 13:45:12] ALERT: 5 failed login attempts from IP 192.168.1.100

# How It Works
The script parses the Linux auth log file /var/log/auth.log, looks for failed SSH login attempts, groups attempts by IP address, and flags IPs exceeding a threshold within a timeframe as possible brute-force attackers.

# Contributing
Feel free to fork and submit pull requests!
Suggestions and improvements are welcome!

# License
MIT License © Zerlyne Nandwani-Simons
