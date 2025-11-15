import numpy as np
import matplotlib.pyplot as plt

def plot_sin_waves():
    # Generate x values from 0 to 2π
    x = np.linspace(0, 4 * np.pi, 1000)
    
    # Compute cosine and sine values
    t = 1
    sin_values = np.sin(2 * np.pi * t * x)

    
    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, sin_values, label='Sine Wave', color='blue')
    #plt.plot(x, sin_values, label='Sine Wave', color='red')
    
    # Add title and labels
    plt.title('Sine Waves')
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

plot_sin_waves()