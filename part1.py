from sys import argv

file_name = argv[0]
worked_hour = argv[1]
rate = argv[2]
benefit = argv[3]

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")
