import numpy as np

# New coefficients from the polynomial fit
new_coefficients = [-9713.9607829, 7050.2407842, -1560.07326938, 210.35347004]

# Create the new polynomial function
new_polynomial = np.poly1d(new_coefficients)

# Compute the derivative of the polynomial
new_polynomial_derivative = new_polynomial.deriv()

# Find roots of the derivative to identify critical points
new_critical_points = np.roots(new_polynomial_derivative)

# Filter the minima in the range [0.1, 0.2]
new_minima_in_range = [
    point for point in new_critical_points if 0.1 <= point <= 0.2 and new_polynomial.deriv(2)(point) > 0
]

print(new_minima_in_range[0])
