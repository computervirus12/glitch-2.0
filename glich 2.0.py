import tkinter as tk
import random
import winsound

# Create window
root = tk.Tk()
canvas = tk.Canvas(root, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

# Track fullscreen state and position
is_fullscreen = False
move_direction = 1
y_position = 100

# Moving rectangles
moving_rects = [{'x': random.randint(0, 800), 'y': random.randint(0, 600),
                 'dx': random.choice([-10, 10]), 'dy': random.choice([-10, 10]),
                 'size': random.randint(30, 100)} for _ in range(50)]

# Generate random color
def random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)

# Play loud random beep
def play_sound():
    freq = random.randint(500, 4000)
    dur = random.randint(100, 300)
    winsound.Beep(freq, dur)

# Toggle fullscreen
def toggle_fullscreen():
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes('-fullscreen', is_fullscreen)

# Move window up and down
def move_window():
    global y_position, move_direction
    if not is_fullscreen:
        y_position += 20 * move_direction
        if y_position > 500 or y_position < 100:
            move_direction *= -1
        root.geometry(f"800x600+100+{y_position}")

# Update moving rectangles
def update_moving_rects():
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    for rect in moving_rects:
        rect['x'] += rect['dx']
        rect['y'] += rect['dy']
        if rect['x'] < 0 or rect['x'] > width:
            rect['dx'] *= -1
        if rect['y'] < 0 or rect['y'] > height:
            rect['dy'] *= -1

# Draw glitchy visuals
def glitch_frame():
    canvas.delete("all")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Draw static shapes
    for _ in range(300):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(10, 100)
        y2 = y1 + random.randint(10, 100)
        color = random_color()
        shape = random.choice(['oval', 'rect'])

        if shape == 'oval':
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    # Flashing lights
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(5, 30)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=random_color(), outline="")

    # Glitchy text
    for _ in range(80):
        x = random.randint(0, width)
        y = random.randint(0, height)
        text = random.choice(["GLITCH", "ERROR", "DATA", "404", "SYSTEM"])
        canvas.create_text(x, y, text=text, fill=random_color(), font=("Courier", random.randint(10, 30)))

    # Moving rectangles
    update_moving_rects()
    for rect in moving_rects:
        x = rect['x']
        y = rect['y']
        size = rect['size']
        canvas.create_rectangle(x, y, x + size, y + size, fill=random_color(), outline="")

    # Flashing overlay when not fullscreen
    if not is_fullscreen:
        canvas.create_rectangle(0, 0, width, height, fill=random_color(), outline="")

    # Background color flash
    root.configure(bg=random_color())

    # Play sound
    play_sound()

    # Toggle fullscreen occasionally
    if random.randint(0, 30) == 0:
        toggle_fullscreen()

    # Move window if not fullscreen
    move_window()

    # Safe loop
    root.after(50, glitch_frame)

# Start animation
glitch_frame()
root.mainloop()