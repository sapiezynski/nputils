import numpy as np

def unique_rows(array):
	"""
	Returns a slice of array that contains only unique rows
	based on: http://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array
	"""
	b = np.ascontiguousarray(array).view(np.dtype((np.void, array.dtype.itemsize * array.shape[1])))
	_, idx = np.unique(b, return_index=True)
	return array[idx]

def unique_rows_id(array):
	"""
	given a (N, M) shaped array it returns a (N, ) shaped vector that contains numeric identifiers of unique rows
	useful for stratifying across multiple variables in sklearn StratifiedKFold
	"""
	unique = unique_rows(array)
	lookup = {tuple(row): idx for idx, row in enumerate(unique)}
	result = np.zeros((array.shape[0], ), dtype=np.int32)
	for idx, row in enumerate(array):
		result[idx] = lookup[tuple(row)]
	return result 

def groupby(array, column, as_dict=False, presorted=True):
	"""
	returns a list of arrays grouped by specified column
	"""
	if not presorted:
		array = array[np.argsort(array[:,column])]
	cp = np.concatenate(([0], np.where(np.diff(array[:,column]))[0] + 1, [array.shape[0]]))
	if as_dict:
		return {array[cp[idx], column]: array[cp[idx]:cp[idx+1]] for idx in range(0, cp.shape[0]-1)}
	else:
		return [array[cp[idx]:cp[idx+1]] for idx in range(0, cp.shape[0]-1)]
	return result