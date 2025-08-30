#  LU Decomposition with Partial Pivoting + Operation Counting + Interpolation

This project demonstrates:
1. **LU Decomposition with Partial Pivoting (PP)** for solving linear systems.  
2. **Operation Counting** to measure computational cost on submatrices.  
3. **Interpolation (Newton & Cubic Spline)** to estimate the computational complexity for larger systems.  

---

##  Workflow Overview
1. **Load Matrix & Vector**  
   - Load a sample matrix `C` from `sample.txt`.  
   - Extract first `n×n` block into `A`.  
   - Define right-hand side vector `b`.  

2. **Solve System Ax = b**  
   - Perform LU decomposition with **partial pivoting**.  
   - Solve via forward & backward substitution.  

3. **Count Operations**  
   - Estimate computational effort for various submatrix sizes.  

4. **Interpolate Results**  
   - Use **Newton Interpolation** and **Cubic Splines** to predict operation counts for larger `n`.  

---

##  Functions Explained

###  `lu_decomposition_pp(A)`
Performs **LU decomposition with partial pivoting**.

- **Input:**  
  - `A`: square matrix.  
- **Output:**  
  - `P`: permutation matrix (for pivoting).  
  - `L`: lower triangular matrix.  
  - `U`: upper triangular matrix.  

  
Matrix `A` → Pivot swap → Build `L` + Update `U` → Done  

---

###  `count_ops_pp(A_sub, b_sub)`
Counts the **number of arithmetic operations** during Gaussian elimination with pivoting.

- **Input:**  
  - `A_sub`: submatrix of `A`.  
  - `b_sub`: subvector of `b`.  
- **Output:**  
  - Number of operations performed.  

  
Pick pivot → Eliminate column entries → Increase counter → Repeat   

---

###  `newton_divided_diff(x, y)`
Computes **Newton’s divided difference coefficients** for interpolation.

- **Input:**  
  - `x`: sample points.  
  - `y`: values at those points.  
- **Output:**  
  - Coefficients for Newton polynomial.  

  
Start with raw values → Apply divided differences → Build coefficient list  

---

###  `newton_eval(coef, x_data, x)`
Evaluates the **Newton interpolating polynomial** at a given point.

- **Input:**  
  - `coef`: coefficients from divided differences.  
  - `x_data`: original sample points.  
  - `x`: evaluation point.  
- **Output:**  
  - Approximated value.  

  
Plug into polynomial → Expand step by step → Get result 

---

###  `CubicSpline`
Uses **SciPy’s CubicSpline** to interpolate operation counts.

Data points → Smooth spline curve → Predict future values 

---

##  Example Outputs
- **System solution**: vector `x` for size `n×n`.  
- **Operation counts** for submatrices.  
- **Predicted operations** for `n=1000`:  
  - Newton Interpolation →  Estimate  
  - Cubic Spline →  Estimate  

---

##  Suggested Visual Animation
If you want to animate this in a presentation:
1. **Matrix Animation** → Rows/columns swap (pivot).  
2. **Operation Counter** → A live counter ticking up.  
3. **Interpolation Curves** → Points appear, Newton polynomial & spline curve drawn dynamically.  



