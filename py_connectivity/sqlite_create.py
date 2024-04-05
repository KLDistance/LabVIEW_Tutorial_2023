import sqlite3
from contextlib import closing

if __name__ == '__main__':
	with closing(sqlite3.connect('data.db')) as connection:
		cursor = connection.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS data (sample_id INTEGER PRIMARY KEY, sample_name TEXT)')
		cursor.execute('INSERT INTO data VALUES (1, "data_point1")')
		cursor.execute('INSERT INTO data VALUES (3, "blahblah")')
		connection.commit()
		cursor.close()
		connection.close()
