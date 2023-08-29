import re

database = input("Enter the path to your database file e.g. 'Users/database.sql':")
output = input("Enter the name of your outputted file (include .sql): ")
pattern = input("Enter the regex pattern you're looking for (e.g. CREATE TABLE `([^`]+)`): ")
replacement = input("Enter the replacement string. Use {} where the matched pattern should go (e.g. DROP TABLE IF EXISTS `{}`;\\nCREATE TABLE `{}`): ")

print(f"Reading {database}...")

with open(database, 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    groups = match.groups()
    return replacement.format(*groups)

content_modified = re.sub(pattern, replacer, content)

print(f"Saving {output}...")
with open(output, 'w', encoding='utf-8') as f:
    f.write(content_modified)

print("Modification complete!")
