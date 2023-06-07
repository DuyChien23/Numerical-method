import math

def f(x):
    return math.sin(x)

def f_prime(x):
    return math.cos(x)

def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Cannot apply bisection method on this interval.")
        return None
    
    while (b - a) >= epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

def fixed_point_iteration(f, x0, epsilon, max_iterations):
    x = x0
    iteration = 0
    
    while True:
        x_next = f(x) + x
        if abs(x_next - x) < epsilon or iteration >= max_iterations:
            break
        x = x_next
        iteration += 1
    
    return x_next

def chord_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Cannot apply chord method on this interval.")
        return None
    
    x = a
    y = b
    
    while abs(y - x) >= epsilon:
        x = x - (f(x) * (y - x)) / (f(y) - f(x))
        y = y - (f(y) * (y - x)) / (f(y) - f(x))
    
    return x

def newton_method(f, f_prime, x0, epsilon, max_iterations):
    x = x0
    iteration = 0
    
    while True:
        x_next = x - f(x) / f_prime(x)
        if abs(x_next - x) < epsilon or iteration >= max_iterations:
            break
        x = x_next
        iteration += 1
    
    return x_next

def secant_method(f, x0, x1, epsilon, max_iterations):
    x_prev = x0
    x = x1
    iteration = 0
    
    while True:
        x_next = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))
        if abs(x_next - x) < epsilon or iteration >= max_iterations:
            break
        x_prev = x
        x = x_next
        iteration += 1
    
    return x_next

if __name__ == "__main__":
    epsilon = 1e-6
    max_iterations = 1000
    
    a = 3
    b = 4
    
    print("Bisection method:")
    result_bisection = bisection_method(f, a, b, epsilon)
    print("Result:", result_bisection)
    
    print("\nFixed-point iteration method:")
    result_fixed_point = fixed_point_iteration(f, a, epsilon, max_iterations)
    print("Result:", result_fixed_point)
    
    print("\nChord method:")
    result_chord = chord_method(f, a, b, epsilon)
    print("Result:", result_chord)
    
    print("\nNewton method:")
    result_newton = newton_method(f, f_prime, a, epsilon, max_iterations)
    print("Result:", result_newton)
    
    print("\nSecant method:")
    result_secant = secant_method(f, a, b, epsilon, max_iterations)
    print("Result:", result_secant)
