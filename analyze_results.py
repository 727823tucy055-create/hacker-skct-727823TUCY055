# Vishwanth - 727823TUCY055

from datetime import datetime

print("Analyzing Results")
print("Roll No: 727823TUCY055")
print("Time:", datetime.now())

with open("logs/honeypot.log", "r") as f:
    data = f.readlines()

print("Total Connections:", len(data))

