import io, sqlite3
import numpy as np
from contextlib import closing

def convert_array(text):
	out = io.BytesIO(text)
	out.seek(0)
	return np.load(out)

if __name__ == '__main__':
	sqlite3.register_converter('ARRAY', convert_array)
	with closing(sqlite3.connect('data_arr.db', detect_types=sqlite3.PARSE_DECLTYPES)) as connection:
		cursor = connection.cursor()
		rows = cursor.execute('SELECT sample_id, sample_arr FROM data').fetchall()
		print(rows)
		cursor.close()
		connection.close()