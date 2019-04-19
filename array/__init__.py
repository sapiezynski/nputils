import numpy as np

def unique_rows(arr):
	"""
	Returns a slice of array that contains only unique rows
	based on: http://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array
	"""
	b = np.ascontiguousarray(arr).view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[1])))
	_, idx = np.unique(b, return_index=True)
	return arr[idx]

def hash_rows(arr):
	"""
	given a (N, M) shaped array it returns a (N, ) shaped vector that contains numeric identifiers of unique rows
	useful for stratifying across multiple variables in sklearn StratifiedKFold
	"""
	result = np.zeros((arr.shape[0], ), dtype=np.int64)
	for idx, row in enumerate(arr):
		result[idx] = hash(tuple(row))
	return result

def groupby(arr, column, as_dict=False, presorted=True):
	"""
	returns a list of arrays grouped by specified column
	"""
	if not presorted:
		arr = arr[np.argsort(arr[:,column])]
	cp = np.concatenate(([0], np.where(np.diff(arr[:,column]))[0] + 1, [arr.shape[0]]))
	if as_dict:
		return {arr[cp[idx], column]: arr[cp[idx]:cp[idx+1]] for idx in range(0, cp.shape[0]-1)}
	else:
		return [arr[cp[idx]:cp[idx+1]] for idx in range(0, cp.shape[0]-1)]
	return result