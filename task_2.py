import numpy as np
import scipy.integrate as spi

def monte_carlo_integration(func, a, b, num_points):
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, func(b), num_points)
    points_under_curve = np.sum(y_random < func(x_random))
    rectangle_area = (b - a) * func(b)
    integral = (points_under_curve / num_points) * rectangle_area
    return integral


def main():
    def f(x):
        return x ** 2
    a, b = 0, 1
    num_points = 10000

    monte_carlo_result = monte_carlo_integration(f, a, b, num_points)
    print(f"Monte Carlo integration result: {monte_carlo_result}")

    quad_result, _ = spi.quad(f, a, b)
    print(f"Quad integration result: {quad_result}")

    print("Difference between Monte Carlo and quad results:", abs(monte_carlo_result - quad_result))

if __name__ == "__main__":
    main()
