#1.Read a log file and count how many times the word "ERROR" appears.
#2.Read a JSON file and print the value of a specific key.
#3.Write a list of dictionaries containing book details to a CSV file with headers.
#4.Read a CSV file with list of items and print description of items if greater than 50
#5.Read a file and replace all occurrences of a word (e.g., "Python") with another word (e.g., "Java").
#6.Detect Presence of a Keyword in a sentence.
#7.Extract Domain Names from Emails
#8.Replace all digits in a credit card number except the last 4 with *.
#9.Given strings like "2025-11-30 Report Generated", use match() to confirm if the string starts with a date in YYYY-MM-DD format. in python and give me a explanation clearly

#1.
count = 0
with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            count += 1
print("Number of ERROR messages:", count)

#2.
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data["name"])

#3.
import csv

books = [
    {"Title": "Python Basics", "Author": "Amritha", "Price": 300},
    {"Title": "Networking", "Author": "Kavya", "Price": 500}
]

with open("books.csv", "w", newline="") as file:
    headers = ["Title", "Author", "Price"]    
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(books)
print("Books written to CSV file successfully.")

#4.
import csv
with open("items.csv", "r") as file:
    reader = csv.DictReader(file)    
    for row in reader:
        if int(row["price"]) > 50:
            print(row["description"])

#5.
with open("sample.txt", "r") as file:
    content = file.read()
content = content.replace("Python", "Java")
with open("sample.txt", "w") as file:
    file.write(content)
print("Word replacement completed.")

#6.
sentence = "Python is a powerful programming language"
keyword = "Python"
if keyword in sentence:
    print("Keyword found")
else:
    print("Keyword not found")

#7.
import re
emails = "barkavi@gmail.com, test@yahoo.com"
domains = re.findall(r'@(\w+\.\w+)', emails)
print(domains)

#8.
import re
card = "1234567812345678"
hidden = re.sub(r'\d(?=\d{4})', '*', card)
print(hidden)

#9.
import re
text = "2025-11-30 Report Generated"
pattern = r"\d{4}-\d{2}-\d{2}"
if re.match(pattern, text):
    print("Starts with valid date")
else:
    print("Invalid format")