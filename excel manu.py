from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from datetime import datetime

# Create empty lists for x and y values
x_values = []
y_values = []

# Create the plot
fig, ax = plt.subplots()

# Initialize an empty line
line, = ax.plot([], [], '-')
line_hline = ax.axhline(y=70, color='r', linestyle='--')  # Horizontal line at y=70

# Set y-axis limits
ax.set_ylim(0, 100)

# Enable gridlines
ax.grid(True)

# Function to initialize the plot
def init_plot():
    line.set_data([], [])
    return line,

# Function to update the chart with new data
def update_chart(frame):
    # Generate or fetch live data
    current_time = datetime.now()
    x = current_time  # Use current time as x value
    y = random.randint(0, 100)  # Generate a random y value

    # Append the new data to the lists
    x_values.append(x)
    y_values.append(y)

    # Update the plot data
    line.set_data(x_values, y_values)
    ax.relim()
    ax.autoscale_view()

    return line,

# Create an animation that calls the update function every 100 milliseconds
frames = range(300)
animation = FuncAnimation(fig, update_chart, frames=frames, init_func=init_plot, blit=True, interval=1000)

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Y')
ax.set_title('Real-Time Data Chart')

# Show the plot and continuously update it
plt.pause(15)

# Keep the script running
while True:
    plt.pause(15)
