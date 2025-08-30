import numpy as np

input_file = "e30r0500.mtx"   
output_file = "sample.txt"  

with open(input_file, "r") as f:
    lines = f.readlines()

data_lines = [line for line in lines if not line.startswith('%')]

n_rows, n_cols, n_entries = map(int, data_lines[0].split())

dense = np.zeros((n_rows, n_cols), dtype=float)

for line in data_lines[1:]:
    i, j, val = line.split()
    i, j = int(i) - 1, int(j) - 1  
    dense[i, j] = float(val)

np.savetxt(output_file, dense, fmt="%.18e", delimiter=' ')
print(f"Dense matrix saved to {output_file}")
