#!/usr/bin/python3
"""Lists all states with a name starting with N from the database."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    # Create a cursor
    cur = db.cursor()
    # Execute SQL query to filter states starting with N
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Display results
    for row in cur.fetchall():
        print(row)
    # Close cursor and connection
    cur.close()
    db.close()