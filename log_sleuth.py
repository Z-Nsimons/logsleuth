from datetime import datetime
import re
from collections import defaultdict

# log_sleuth.py
log_path = "/var/log/auth.log"
ip_fail_count = defaultdict(int)

# opens log file
with open(log_path, "r") as file:
	# reads each line
	for line in file:
		# if it contains "Failed password", it prints it
		if "Failed password" in line:
			# use regex to pull out username (2nd match group) and IP address (3rd match group)
			match = re.search(r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)", line)
			if match:
				username = match.group(2)
				ip = match.group(3)
				# stores number of failed attempts per IP
				ip_fail_count[ip] += 1
				# print warning for each failed attempt
				alert = f"[!] Failed login attempt by '{username}' from IP {ip}"
				print(alert)

				with open("logsleuth_output.log", "a") as out:
					out.write(f"{datetime.now()} {alert}\n")
# print summary table
print("\nSummary of Failed Attempts:")
for ip, count in ip_fail_count.items():
	summary = f"IP {ip} had {count} failed attempt(s)"
	print(summary)
	
	with open("logsleuth_output.log", "a") as out:
		out.write(f"{datetime.now()} {summary}\n")

# check if any IP has 5 or more failed attempts and alerts
print("\nPossible Brute-Force Attacks Detected:")
threshold = 5  # can change to be more or less strict

for ip, count in ip_fail_count.items():
	if count >= threshold:
		warning = f"IP {ip} has {count} failed attempts - possible brute-force attack!"
		print(warning)

		with open("logsleuth_output.log", "a") as out:
			out.write(f"{datetime.now()} {warning}\n")

