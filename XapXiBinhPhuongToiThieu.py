import numpy as np
from scipy.optimize import minimize

def continuous_least_squares(x, y, degree):
    n = len(x)
    A = np.ones((n, degree+1))

    for i in range(1, degree+1):
        A[:, i] = x**i

    coefficients = np.linalg.lstsq(A, y, rcond=None)[0]
    return coefficients

def discrete_least_squares(x, y, model_func, initial_guess):
    def objective_func(params):
        return np.sum((model_func(x, params) - y)**2)

    result = minimize(objective_func, initial_guess)
    coefficients = result.x
    return coefficients

if __name__ == "__main__":
    # Dữ liệu mẫu
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 4, 5, 6])

    # Phương pháp bình phương tối thiểu liên tục (OLS)
    degree = 1
    coefficients_ols = continuous_least_squares(x, y, degree)
    print("OLS coefficients:", coefficients_ols)

    # Phương pháp bình phương tối thiểu rời rạc (ODR)
    def model_func(x, params):
        return params[0] + params[1] * x

    initial_guess = np.array([0, 1])
    coefficients_odr = discrete_least_squares(x, y, model_func, initial_guess)
    print("ODR coefficients:", coefficients_odr)
