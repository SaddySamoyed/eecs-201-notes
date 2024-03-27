import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 500)  # 500 pts to ensure smoothness

y = x**3 - 7*x + 2*x + 2

# Plot
plt.plot(x, y)  # Plot the function
plt.title("Who needs MATLAB?")  # Add a title to the plot
# Save
plt.savefig('output.png')