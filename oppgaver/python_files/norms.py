import matplotlib.pyplot as plt
import numpy as np

def norms():
    n = 3
    x1 = np.random.randint(0, 10, size=n)
    x2 = np.random.randint(0, 10, size=n)

    x1_norm = np.linalg.norm(x1, ord=2)
    x2_norm = np.linalg.norm(x2, ord=2)

    x_minus_y = x1 - x2
    x_minus_y_norm = np.linalg.norm(x_minus_y, ord=2)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot vectors from origin
    ax.quiver(0, 0, 0, x1[0], x1[1], x1[2], 
              color='blue', label=f'x1 (norm: {x1_norm:.2f})', 
              arrow_length_ratio=0.1, linewidth=2)
    
    ax.quiver(0, 0, 0, x2[0], x2[1], x2[2], 
              color='red', label=f'x2 (norm: {x2_norm:.2f})', 
              arrow_length_ratio=0.1, linewidth=2)
    
    # Plot difference vector (from x2 to x1)
    ax.quiver(x2[0], x2[1], x2[2], 
              x_minus_y[0], x_minus_y[1], x_minus_y[2],
              color='green', label=f'x1 - x2 (norm: {x_minus_y_norm:.2f})', 
              arrow_length_ratio=0.1, linewidth=2)
    
    # Set plot limits
    max_val = max(np.max(np.abs(x1)), np.max(np.abs(x2))) + 2
    ax.set_xlim([-max_val, max_val])
    ax.set_ylim([-max_val, max_val])
    ax.set_zlim([-max_val, max_val])
    
    # Labels and title
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Vector Visualization\nTriangle Inequality Demonstration')
    
    # Add legend
    ax.legend()
    
    # Add grid
    ax.grid(True, alpha=0.3)
    
    # Show the inequality
    lower_bound = abs(x1_norm - x2_norm)
    upper_bound = x1_norm + x2_norm
    
    print(f"\nTriangle Inequality Check:")
    print(f"| ||x1|| - ||x2|| | = {lower_bound:.2f}")
    print(f"||x1 - x2|| = {x_minus_y_norm:.2f}")
    print(f"||x1|| + ||x2|| = {upper_bound:.2f}")
    print(f"Inequality holds: {lower_bound <= x_minus_y_norm <= upper_bound}")
    
    plt.tight_layout()
    plt.show()

norms()
