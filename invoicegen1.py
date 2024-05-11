import tkinter as tk

root = tk.Tk()

# Store layout information
widget_layout = {}

# Create some widgets and pack/place them initially
label = tk.Label(root, text="Label")
entry = tk.Entry(root)
button = tk.Button(root, text="Button")

label.place(x=100, y=50, width=100, height=30)
entry.place(x=100, y=100, width=100, height=30)
button.place(x=100, y=150, width=100, height=30)

# Function to forget all widgets
def forget_widgets():
    global widget_layout
    widget_layout = {widget: (widget.winfo_class(), *widget.place_info().values()) for widget in root.winfo_children() if widget.winfo_manager()}
    for widget in root.winfo_children():
        widget.pack_forget()
        widget.place_forget()

# Function to repack/place widgets to their previous positions
def restore_widgets():
    global widget_layout
    for widget, args in widget_layout.items():
        widget_class, x, y, width, height = args
        if widget_class == 'Label':
            widget = tk.Label(root, text="Label")
        elif widget_class == 'Entry':
            widget = tk.Entry(root)
        elif widget_class == 'Button':
            widget = tk.Button(root, text="Button")
        widget.place(x=x, y=y, width=width, height=height)

# Create buttons to forget and restore widgets
forget_button = tk.Button(root, text="Forget Widgets", command=forget_widgets)
restore_button = tk.Button(root, text="Restore Widgets", command=restore_widgets)

forget_button.pack()
restore_button.pack()

root.mainloop()
