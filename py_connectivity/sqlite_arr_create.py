import io, sqlite3
import numpy as np
from contextlib import closing

def array_gen():
	return np.random.normal(loc=0, scale=1, size=(16))

def adapt_array(arr):
	out = io.BytesIO()
	np.save(out, arr)
	out.seek(0)
	return sqlite3.Binary(out.read())

if __name__ == '__main__':
	sqlite3.register_adapter(np.ndarray, adapt_array)
	with closing(sqlite3.connect('data_arr.db', detect_types=sqlite3.PARSE_DECLTYPES)) as connection:
		cursor = connection.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS data (sample_id INTEGER PRIMARY KEY, sample_arr ARRAY)')
		cursor.execute('INSERT INTO data VALUES (0, ?)', (array_gen(),))
		connection.commit()
		cursor.close()
		connection.close()
