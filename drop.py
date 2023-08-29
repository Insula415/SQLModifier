import re

database = input("Enter the path to your database file e.g. 'Users/database.sql':")
output = input("Enter the name of your outputted file (include .sql): ")
print(f"Reading {database}...")

with open(database, 'r', encoding='utf-8') as f:
    content = f.read()


def prepend_drop_table_if_exists(match):
    table_name = match.group(1)
    return f"DROP TABLE IF EXISTS `{table_name}`;\nCREATE TABLE `{table_name}`"

content_modified = re.sub(r"CREATE TABLE `([^`]+)`", prepend_drop_table_if_exists, content)
print(f"Saving {output}...")
with open(output, 'w', encoding='utf-8') as f:
    f.write(content_modified)

print("Modification complete!")
