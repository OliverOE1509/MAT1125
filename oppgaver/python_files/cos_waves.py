import numpy as np
import matplotlib.pyplot as plt

def plot_cos_sin_waves():
    # Generate x values from 0 to 2π
    x = np.linspace(0, 4 * np.pi, 1000)
    
    # Compute cosine and sine values
    t = 1
    cos_values = np.cos(2 * np.pi * t * x)

    
    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, cos_values, label='Cosine Wave', color='blue')
    #plt.plot(x, sin_values, label='Sine Wave', color='red')
    
    # Add title and labels
    plt.title('Cosine Waves')
    plt.xlabel('X values (radians)')
    plt.ylabel('Y values')
    for i in range(0, 13, 1):
        plt.vlines(i, ymin = -1, ymax = 1, colors = 'red')
    
    # Add a legend
    plt.legend()
    
    # Show grid
    plt.grid(True)
    
    # Display the plot
    plt.show()

plot_cos_sin_waves()