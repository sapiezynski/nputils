# nputils
A set of convenience functions for NumPy

## IO operations
`npu.io.load_dir(path, prefix=None)` loads all files (starting with optional `prefix`) from a `path` into a single array.

## array operations
`npu.array.unique_rows(array)` returns unique rows of an `array`

`npu.array.groupby(array, column, presorted=True)` returns a list of slices of `array` grouped by the values in the specified `column`
