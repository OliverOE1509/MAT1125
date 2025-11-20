import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle, Ellipse
import matplotlib.patches as patches

class NormVisualizer:
    def __init__(self):
        self.fig = None
        self.ax = None
        
    def p_norm(self, x, p):
        """Calculate the p-norm of vector x"""
        if p == np.inf:
            return np.max(np.abs(x))
        elif p == -np.inf:
            return np.min(np.abs(x))
        else:
            return np.sum(np.abs(x)**p)**(1/p)
    
    def plot_unit_balls_2d(self, p_values=[0.5, 1, 2, 3, 5, 10, np.inf]):
        """Plot unit balls in 2D for different p-norms"""
        fig, axes = plt.subplots(2, 4, figsize=(16, 8))
        axes = axes.flatten()
        
        # Generate points on the unit circle for each norm
        theta = np.linspace(0, 2*np.pi, 1000)
        
        for i, p in enumerate(p_values):
            if i >= len(axes):
                break
                
            ax = axes[i]
            
            if p == np.inf:
                # L-infinity norm (square)
                x = np.array([-1, 1, 1, -1, -1])
                y = np.array([-1, -1, 1, 1, -1])
                ax.plot(x, y, 'b-', linewidth=2)
                ax.fill(x, y, alpha=0.3)
            elif p == 1:
                # L1 norm (diamond)
                x = np.array([0, 1, 0, -1, 0])
                y = np.array([1, 0, -1, 0, 1])
                ax.plot(x, y, 'b-', linewidth=2)
                ax.fill(x, y, alpha=0.3)
            else:
                # General p-norm
                r = 1
                x = r * np.cos(theta)
                y = r * np.sin(theta)
                
                # Parameterize the unit ball
                points = np.column_stack([x, y])
                norms = np.array([self.p_norm(point, p) for point in points])
                scaling = 1 / norms
                
                x_scaled = x * scaling
                y_scaled = y * scaling
                
                ax.plot(x_scaled, y_scaled, 'b-', linewidth=2)
                ax.fill(x_scaled, y_scaled, alpha=0.3)
            
            ax.set_xlim(-1.2, 1.2)
            ax.set_ylim(-1.2, 1.2)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_title(f'p = {p}' if p != np.inf else 'p = ∞')
            ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Remove empty subplots
        for i in range(len(p_values), len(axes)):
            axes[i].set_visible(False)
            
        plt.suptitle('Unit Balls for Different p-Norms in 2D', fontsize=16)
        plt.tight_layout()
        return fig
    
    def plot_norm_comparison_3d(self):
        """3D visualization showing how norms compare"""
        fig = plt.figure(figsize=(15, 5))
        
        # Create sample vectors
        np.random.seed(42)
        n_vectors = 100
        vectors = np.random.randn(n_vectors, 2) * 2
        
        # Calculate different norms
        norms_l1 = np.array([self.p_norm(v, 1) for v in vectors])
        norms_l2 = np.array([self.p_norm(v, 2) for v in vectors])
        norms_linf = np.array([self.p_norm(v, np.inf) for v in vectors])
        
        # Plot 1: L1 vs L2
        ax1 = fig.add_subplot(131)
        scatter1 = ax1.scatter(norms_l1, norms_l2, c=np.arange(n_vectors), cmap='viridis')
        ax1.plot([0, max(norms_l1)], [0, max(norms_l1)], 'r--', alpha=0.7, label='y = x')
        ax1.set_xlabel('L1 Norm')
        ax1.set_ylabel('L2 Norm')
        ax1.set_title('L1 vs L2 Norms')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: L2 vs L∞
        ax2 = fig.add_subplot(132)
        scatter2 = ax2.scatter(norms_l2, norms_linf, c=np.arange(n_vectors), cmap='viridis')
        ax2.plot([0, max(norms_l2)], [0, max(norms_l2)], 'r--', alpha=0.7, label='y = x')
        ax2.set_xlabel('L2 Norm')
        ax2.set_ylabel('L∞ Norm')
        ax2.set_title('L2 vs L∞ Norms')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: All norms comparison
        ax3 = fig.add_subplot(133)
        indices = np.arange(n_vectors)
        width = 0.25
        ax3.bar(indices - width, norms_l1, width, label='L1 Norm', alpha=0.7)
        ax3.bar(indices, norms_l2, width, label='L2 Norm', alpha=0.7)
        ax3.bar(indices + width, norms_linf, width, label='L∞ Norm', alpha=0.7)
        ax3.set_xlabel('Vector Index')
        ax3.set_ylabel('Norm Value')
        ax3.set_title('Comparison of Different Norms')
        ax3.legend()
        
        plt.tight_layout()
        return fig
    
    def demonstrate_norm_equivalence(self, dimension=2):
        """Demonstrate the equivalence of norms theorem"""
        print("=== Norm Equivalence Demonstration ===")
        print(f"Dimension: {dimension}")
        print()
        
        # Generate random vectors
        np.random.seed(42)
        n_samples = 50
        vectors = np.random.randn(n_samples, dimension)
        
        # Calculate different norms
        p_values = [1, 2, np.inf]
        norm_values = {}
        
        for p in p_values:
            norm_values[p] = np.array([self.p_norm(v, p) for v in vectors])
        
        # Find equivalence constants
        print("Equivalence Constants:")
        for i, p1 in enumerate(p_values):
            for j, p2 in enumerate(p_values):
                if i < j:
                    ratio_p1_p2 = norm_values[p1] / norm_values[p2]
                    ratio_p2_p1 = norm_values[p2] / norm_values[p1]
                    
                    c1 = np.max(ratio_p1_p2)
                    c2 = np.max(ratio_p2_p1)
                    
                    p1_str = "∞" if p1 == np.inf else str(p1)
                    p2_str = "∞" if p2 == np.inf else str(p2)
                    
                    print(f"L{p1_str} ≤ {c1:.4f} * L{p2_str}")
                    print(f"L{p2_str} ≤ {c2:.4f} * L{p1_str}")
                    print(f"→ L{p1_str} and L{p2_str} are equivalent")
                    print()
    
    def plot_norm_convergence(self):
        """Show that convergence in one norm implies convergence in others"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Create a sequence converging to zero
        n_points = 100
        sequence = 1 / np.arange(1, n_points + 1)
        
        # Calculate different norms (treat each element as a 1D vector)
        norms_l1 = np.abs(sequence)  # For 1D, L1 = absolute value
        norms_l2 = np.abs(sequence)  # For 1D, L2 = absolute value
        norms_linf = np.abs(sequence)  # For 1D, L∞ = absolute value
        
        # Plot convergence
        ax1.semilogy(norms_l1, label='L1 Norm', alpha=0.7)
        ax1.semilogy(norms_l2, label='L2 Norm', alpha=0.7)
        ax1.semilogy(norms_linf, label='L∞ Norm', alpha=0.7)
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Norm Value (log scale)')
        ax1.set_title('Convergence in Different Norms')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot ratios to show boundedness
        ax2.plot(norms_l1 / norms_l2, label='L1/L2', alpha=0.7)
        ax2.plot(norms_l2 / norms_linf, label='L2/L∞', alpha=0.7)
        ax2.plot(norms_linf / norms_l1, label='L∞/L1', alpha=0.7)
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('Ratio')
        ax2.set_title('Ratios Between Different Norms')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(0, 2)
        
        plt.tight_layout()
        return fig

def main():
    visualizer = NormVisualizer()
    
    print("L² Norms Visualization and Equivalence Demonstration")
    print("=" * 50)
    
    # 1. Show unit balls for different p-norms
    print("1. Plotting unit balls for different p-norms...")
    fig1 = visualizer.plot_unit_balls_2d()
    
    # 2. Demonstrate norm equivalence
    print("2. Demonstrating norm equivalence...")
    visualizer.demonstrate_norm_equivalence(dimension=2)
    
    # 3. Show 3D comparison
    print("3. Creating 3D norm comparison...")
    fig2 = visualizer.plot_norm_comparison_3d()
    
    # 4. Show convergence behavior
    print("4. Plotting convergence in different norms...")
    fig3 = visualizer.plot_norm_convergence()
    
    plt.show()
    
    # Additional information
    print("\n=== Key Points About Norm Equivalence ===")
    print("• In finite-dimensional spaces, all norms are equivalent")
    print("• This means: ∃ constants c₁, c₂ > 0 such that c₁‖x‖ₐ ≤ ‖x‖ᵦ ≤ c₂‖x‖ₐ")
    print("• Convergence in one norm implies convergence in all norms")
    print("• The unit balls get 'squarer' as p → ∞ and more 'pointy' as p → 0+")

if __name__ == "__main__":
    main()