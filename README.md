# SQLModifier

A command-line tool that allows users to modify SQL files based on custom regex patterns and replacements.

**drop.py** is a specific script that adds `DROP TABLE IF EXISTS` in front of every `CREATE TABLE` query, this is useful for when you get an error like:
`ERROR 1146 (42S02) at line 2500543: Table 'wp_tablename' doesn't exist`

main.py is a versatile script allowing a user to create their own patterns:

<code>Enter the path to your database file e.g. 'Users/database.sql': path_to_db.sql
Enter the name of your outputted file (include .sql): output.sql
Enter the replacement string: DROP TABLE IF EXISTS `{}`;\nCREATE TABLE `{}`
Enter the regex pattern you're looking for: CREATE TABLE `([^`]+)`
</code>

This will add `DROP TABLE IF EXISTS` in front of every `CREATE TABLE`, just like drop.py but flexible with the user's input.
