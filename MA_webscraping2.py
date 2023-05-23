import re
import requests
import phonenumbers

# Send an HTTP request to the website URL
url = 'https://www.yellowpages.com/'
response = requests.get(url)

# Extract all text from the response
text = response.text

# Find all email addresses using regular expression
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Z|a-z]{2,}\b', text)

# Find phone numbers using regular expression pattern
raw_phone_numbers = re.findall(r'\b(?:\+?1[-.\s]?)?\(?(?:[2-9][0-9]{2})\)?[-.\s]?(?:[2-9][0-9]{2})[-.\s]?(?:[0-9]{4})\b', text)

# Format the phone numbers using the phonenumbers library
formatted_phone_numbers = set()  # Use a set instead of a list to eliminate duplicates
for number in raw_phone_numbers:
    parsed_number = phonenumbers.parse(number, "CA")
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    formatted_phone_numbers.add(formatted_number)  # Use the add() method of set to add unique phone numbers

# Print the extracted email addresses
print("Email addresses:")
print(emails)

# Print the extracted phone numbers in the correct format
print("Phone numbers:")
for number in formatted_phone_numbers:
    print(number)
