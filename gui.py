import tkinter as tk

def power_on():
    # Placeholder for power-on functionality
    status_var.set("Powering on...")

def home_motors():
    # Placeholder for homing motors functionality
    status_var.set(f"Homing motors in {direction_var.get()} direction...")

def grasp():
    # Placeholder for grasp functionality
    status_var.set("Grasping...")

def release():
    # Placeholder for release functionality
    status_var.set("Releasing...")

def extend():
    # Placeholder for extending functionality
    status_var.set("Extending...")

def retract():
    # Placeholder for retracting functionality
    status_var.set("Retracting...")

def flex_wrist():
    # Placeholder for wrist flex functionality
    status_var.set("Flexing wrist...")

def emergency_stop():
    # Placeholder for emergency stop functionality
    status_var.set("Emergency stop activated!")

# Create the main window
root = tk.Tk()
root.title("Stepper Motor Control")

# Global variables
direction_var = tk.StringVar(value="正")

# Power On button
power_btn = tk.Button(root, text="上电", command=power_on)
power_btn.grid(row=0, column=0, padx=5, pady=5)

# Home Motors button
home_btn = tk.Button(root, text="回零", command=home_motors)
home_btn.grid(row=0, column=1, padx=5, pady=5)

# Homing Direction radio buttons
direction_label = tk.Label(root, text="回零方向")
direction_label.grid(row=0, column=2, padx=5, pady=5)
direction_frame = tk.Frame(root)
direction_frame.grid(row=0, column=3, padx=5, pady=5)

direction_positive = tk.Radiobutton(direction_frame, text="正", variable=direction_var, value="正")
direction_positive.pack(side=tk.LEFT, padx=5)
direction_negative = tk.Radiobutton(direction_frame, text="负", variable=direction_var, value="负")
direction_negative.pack(side=tk.LEFT, padx=5)

# Status text box
status_var = tk.StringVar()
status_label = tk.Label(root, text="状态")
status_label.grid(row=1, column=0, padx=5, pady=5)
status_text = tk.Label(root, textvariable=status_var, relief=tk.SUNKEN, width=50)
status_text.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# Control buttons
grasp_btn = tk.Button(root, text="抓紧", command=grasp)
grasp_btn.grid(row=2, column=0, padx=5, pady=5)

release_btn = tk.Button(root, text="放松", command=release)
release_btn.grid(row=2, column=1, padx=5, pady=5)

extend_btn = tk.Button(root, text="伸长", command=extend)
extend_btn.grid(row=2, column=2, padx=5, pady=5)

retract_btn = tk.Button(root, text="缩短", command=retract)
retract_btn.grid(row=2, column=3, padx=5, pady=5)

flex_wrist_btn = tk.Button(root, text="屈腕", command=flex_wrist)
flex_wrist_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Emergency Stop button
emergency_btn = tk.Button(root, text="急停", command=emergency_stop, bg="red", fg="white")
emergency_btn.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()
