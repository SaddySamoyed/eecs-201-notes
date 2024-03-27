# This is a more advanced version:
# Put in a function expression with "" as a command line argument and then you plot it!
import numpy as np
import matplotlib.pyplot as plt
import sys

def eval(expr, x):
    allowed_names = {k: v for k, v in np.__dict__.items() if not k.startswith("__")}
    allowed_names["x"] = x
    return eval(expr, {"__builtins__": None}, allowed_names)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please input: python3 plotter.py 'y_expression'")
        sys.exit(1)
    
    y_expression = sys.argv[1]  # y expression!

    x = np.linspace(-4, 4, 500)  # The grid

    try:
        y = eval(y_expression, x)  # Evaluate the expression safely
    except Exception as e:
        print(f"Error evaluating the expression: {e}")
        sys.exit(1)

    plt.plot(x, y)
    plt.title("Who needs MATLAB?")
    plt.savefig('output.png')