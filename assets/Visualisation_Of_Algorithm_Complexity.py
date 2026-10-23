import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

initial_n_max = 100
n = np.linspace(1, initial_n_max, 500)

y_linear = n
y_nlogn = n * np.log2(n)
y_quad = n**2

line_linear, = ax.plot(n, y_linear, label=r'$O(n)$ Linear', color='blue', linewidth=2)
line_nlogn, = ax.plot(n, y_nlogn, label=r'$O(n \log n)$ Linearithmic', color='green', linewidth=2)
line_quad, = ax.plot(n, y_quad, label=r'$O(n^2)$ Quadratic', color='red', linewidth=2)

ax.set_title("Algorithm Complexity Scaling")
ax.set_xlabel("Input Size (n)")
ax.set_ylabel("Operations")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

ax.set_xlim(1, initial_n_max)
ax.set_ylim(0, initial_n_max**2) 

ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
n_slider = Slider(
    ax=ax_slider, label='Max Input (n)',
    valmin=10, valmax=1000, valinit=initial_n_max, valstep=10
)

def update(val):
    current_n_max = n_slider.val
    new_n = np.linspace(1, current_n_max, 500)
    
    line_linear.set_xdata(new_n)
    line_linear.set_ydata(new_n)
    line_nlogn.set_xdata(new_n)
    line_nlogn.set_ydata(new_n * np.log2(new_n))
    line_quad.set_xdata(new_n)
    line_quad.set_ydata(new_n**2)
    
    ax.set_xlim(1, current_n_max)
    ax.set_ylim(0, current_n_max**2) 
    fig.canvas.draw_idle()

n_slider.on_changed(update)

vline = ax.axvline(x=0, color='black', linestyle='--', alpha=0.5, zorder=1)
vline.set_visible(False)

annot = ax.annotate(
    "", xy=(0,0), xytext=(15, 15),
    textcoords="offset points",
    bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="gray", alpha=0.95)
)
annot.set_visible(False)

def hover(event):
    if event.inaxes == ax:
        x_val = int(round(event.xdata))
        
        if x_val >= 1:
            val_linear = x_val
            val_nlogn = x_val * np.log2(x_val)
            val_quad = x_val**2
            
            text = f"Input Size (n) = {x_val}\n"
            text += f"Linear: {val_linear:,.0f} ops\n"
            text += f"Linearithmic: {val_nlogn:,.0f} ops\n"
            text += f"Quadratic: {val_quad:,.0f} ops"
            
            annot.xy = (event.xdata, event.ydata)
            annot.set_text(text)
            annot.set_visible(True)
            
            vline.set_xdata([x_val, x_val])
            vline.set_visible(True)
            
            fig.canvas.draw_idle()
    else:
        if annot.get_visible():
            annot.set_visible(False)
            vline.set_visible(False)
            fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()