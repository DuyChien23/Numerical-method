import numpy as np
from scipy.linalg import eig

def eigenvalue_euclidean_scaling(A, x, epsilon=1e-6, max_iterations=100):
    n = A.shape[0]
    
    # Initialize eigenvector
    v = np.ones(n) / np.sqrt(n)
    
    # Power iteration method
    for i in range(max_iterations):
        v_prev = v
        v = A @ v
        v = v / np.linalg.norm(v)
        
        # Compute eigenvalue
        eigenvalue = v @ A @ v / (v @ v)
        
        # Compute residual/error
        residual = np.linalg.norm(A @ v - eigenvalue * v)
        
        # Print eigenvalue and residual
        if (i % 10 == 9):
            print("Iteration", i+1)
            print("Eigenvalue:", eigenvalue)
            print("Residual/Error:", residual)
    
    return eigenvalue, residual


def eigenvalue_maximum_entry_scaling(A, x, epsilon=1e-6, max_iterations=100):
    n = A.shape[0]
    
    # Initialize eigenvector
    v = np.ones(n) / np.sqrt(n)
    
    # Power iteration method
    for i in range(max_iterations):
        v_prev = v
        v = A @ v
        v = v / np.max(np.abs(v))
        
        # Compute eigenvalue
        eigenvalue = v @ A @ v / (v @ v)
        
        # Compute residual/error
        residual = np.linalg.norm(A @ v - eigenvalue * v)
        
        # Print eigenvalue and residual
        if (i % 10 == 9):
            print("Iteration", i+1)
            print("Eigenvalue:", eigenvalue)
            print("Residual/Error:", residual)
        
    
    return eigenvalue, residual


# Example usage
line0 = [-119, 80, 0, 0, 0, 0, 0, 0, 0, 0] 
line1 = [-180, 121, 0, 0, 0, 0, 0, 0, 0, 0]
line2 = [-120, 80, -11, 18, 0, 0, 0, 0, 0, 0]
line3 = [-300, 200, -30, 49, 0, 0, 0, 0, 0, 0]
line4 = [0, 0, 2350, -3760, 2, 0, 0, 0, 0, 0]
line5 = [0, 0, 2775, -4440, 0, 2, 0, 0, 0, 0]
line6 = [0, 0, 0, 0, 0, 0, -1703, 1415, -450, 730]
line7 = [0, 0, 0, 0, 0, 0, -2046, 1700, -540, 876]
line8 = [0, 0, 0, 0, 0, 0, -608, 504, -573, 922]
line9 = [0, 0, 0, 0, 0, 0, -1520, 1260, -1500, 2413]
A = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9]
x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print("==============================Euclidean Scaling===================================")
eigenvalue_euclidean_scaling(np.array(A), x, 1e-6, 50)

print("==============================Maximum Entry Scaling===================================")
eigenvalue_maximum_entry_scaling(np.array(A), x, 1e-6, 50)

