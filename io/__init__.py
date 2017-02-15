import os
import numpy as np

def shape(filename):
	"""
	return the tuple with the shape of the array in file
	"""
	f = open(filename).readline()
	shape = [int(dim) for dim in f.split('(')[1].split(')')[0].split(',') if dim]
	return tuple(shape)

def dtype(filename):
	"""
	return the dtype of the array in file
	"""
	f = open(filename).readline()
	type_str = f.split("descr': '")[1].split("',")[0]
	return np.dtype(type_str)



def load_dir(directory, prefix=None):
	"""
	load all .npy files from a given folder.
	optional: prefix - load only files whose name start with prefix
	works only with 2D arrays
	"""
	files = [f for f in os.listdir(directory) if lower(f).endswith('.npy')]
	if prefix is not None:
		files = [f for f in files if f.startswith(prefix)]
	print files
	shape_0 = 0
	shapes_1 = set()
	types = set()
	for f in files:
		s = shape(directory + '/' + f)
		shape_0 += s[0]
		shapes_1.add(s[1])
		t = dtype(directory + '/' + f)
		types.add(t)
	if len(shapes_1) > 1:
		raise IOError('All files must have the same 1st dimension')
	if len(types) > 1:
		raise IOError('All files must hold arrays of the same type')
	result = np.zeros((shape_0, list(shapes_1)[0]), dtype=list(types)[0])
	pointer = 0
	for f in files:
		temp = np.load(directory + '/' + f)
		result[pointer:pointer+temp.shape[0],:] = temp
		pointer += temp.shape[0]
	return result