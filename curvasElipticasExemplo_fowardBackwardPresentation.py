import numpy as np
import matplotlib.pyplot as plt

# malha 2D
x = np.linspace(-10, 10, 600)
y = np.linspace(-10, 10, 600)
X, Y = np.meshgrid(x, y)

curves = [
    ("y² = x³ - 1",        lambda X, Y: Y**2 - (X**3 - 1)),
    ("y² = x³ + 1",        lambda X, Y: Y**2 - (X**3 + 1)),
    ("y² = x³ - x",        lambda X, Y: Y**2 - (X**3 - X)),
]

idx = 0
fig, ax = plt.subplots()

def draw():
    ax.clear()

    name, F = curves[idx]
    Z = F(X, Y)

    ax.contour(X, Y, Z, levels=[0], linewidths=2)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")

    ax.set_title(name)
    ax.grid(True)

    plt.draw()

def on_key(event):
    global idx
    if event.key == "right":
        idx = (idx + 1) % len(curves)
    elif event.key == "left":
        idx = (idx - 1) % len(curves)
    draw()

fig.canvas.mpl_connect("key_press_event", on_key)

draw()
plt.show()

