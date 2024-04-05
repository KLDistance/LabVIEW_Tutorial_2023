import sqlite3
from contextlib import closing

if __name__ == '__main__':
	with closing(sqlite3.connect('data.db')) as connection:
		cursor = connection.cursor()
		rows = cursor.execute('SELECT sample_id, sample_name FROM data').fetchall()
		print(rows)
		cursor.close()
		connection.close()