import numpy as np

input_file = "e30r0500.mtx"   # your input .mtx file
output_file = "sample.txt"  # output text file

# Read the file
with open(input_file, "r") as f:
    lines = f.readlines()

# Skip comments
data_lines = [line for line in lines if not line.startswith('%')]

# First line contains matrix dimensions
n_rows, n_cols, n_entries = map(int, data_lines[0].split())

# Initialize dense matrix
dense = np.zeros((n_rows, n_cols), dtype=float)

# Fill dense matrix with coordinate data
for line in data_lines[1:]:
    i, j, val = line.split()
    i, j = int(i) - 1, int(j) - 1  # Matrix Market uses 1-based indexing
    dense[i, j] = float(val)

# Save dense matrix to text file (each row in one line, space-separated)
np.savetxt(output_file, dense, fmt="%.18e", delimiter=' ')
print(f"Dense matrix saved to {output_file}")
