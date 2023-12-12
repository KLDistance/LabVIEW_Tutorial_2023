import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
	df = pd.read_csv('./data1.csv', sep=',', header=None)
	mat = np.array(df.values).T
	fig1 = plt.figure(1)
	plt.plot(mat[0, :], mat[1, :])
	plt.show()