import tkinter as tk
from tkinter import ttk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Paint App")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")

        # Variables
        self.canvas_width = 900
        self.canvas_height = 650

        self.selected_tool = "pen"
        self.selected_color = "black"
        self.selected_size = 4
        self.selected_pen_type = "line"

        self.prev_x = None
        self.prev_y = None

        # Main Canvas
        self.canvas = tk.Canvas(
            root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white",
            bd=0,
            highlightthickness=3,
            highlightbackground="#444"
        )

        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Sidebar
        self.sidebar = tk.Frame(root, bg="#2b2b2b", width=250)
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        self.setup_tools()
        self.setup_events()

    def setup_tools(self):

        title = tk.Label(
            self.sidebar,
            text="🎨 Paint Tools",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        # Pen Button
        self.pen_btn = tk.Button(
            self.sidebar,
            text="Pen",
            command=self.select_pen_tool,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=10,
            pady=8
        )
        self.pen_btn.pack(fill=tk.X, padx=15, pady=5)

        # Eraser Button
        self.eraser_btn = tk.Button(
            self.sidebar,
            text="Eraser",
            command=self.select_eraser_tool,
            bg="#e53935",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=10,
            pady=8
        )
        self.eraser_btn.pack(fill=tk.X, padx=15, pady=5)

        # Brush Size
        tk.Label(
            self.sidebar,
            text="Brush Size",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 11)
        ).pack(pady=10)

        self.size_combo = ttk.Combobox(
            self.sidebar,
            values=[2,4,6,8,10,12,15,20],
            state="readonly"
        )
        self.size_combo.current(1)
        self.size_combo.pack(padx=15, fill=tk.X)

        self.size_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.select_size(int(self.size_combo.get()))
        )

        # Colors
        tk.Label(
            self.sidebar,
            text="Choose Color",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 11)
        ).pack(pady=10)

        self.color_combo = ttk.Combobox(
            self.sidebar,
            values=[
                "black", "red", "blue", "green",
                "yellow", "purple", "orange",
                "pink", "brown", "gray"
            ],
            state="readonly"
        )

        self.color_combo.current(0)
        self.color_combo.pack(padx=15, fill=tk.X)

        self.color_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.select_color(self.color_combo.get())
        )

        # Pen Types
        tk.Label(
            self.sidebar,
            text="Pen Type",
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 11)
        ).pack(pady=10)

        self.pen_combo = ttk.Combobox(
            self.sidebar,
            values=["line", "round", "square", "diamond"],
            state="readonly"
        )

        self.pen_combo.current(0)
        self.pen_combo.pack(padx=15, fill=tk.X)

        self.pen_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.select_pen_type(self.pen_combo.get())
        )

        # Shape Buttons
        tk.Button(
            self.sidebar,
            text="Draw Circle",
            command=self.draw_circle,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT
        ).pack(fill=tk.X, padx=15, pady=15)

        tk.Button(
            self.sidebar,
            text="Draw Rectangle",
            command=self.draw_rectangle,
            bg="#9C27B0",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT
        ).pack(fill=tk.X, padx=15, pady=5)

        # Clear Button
        tk.Button(
            self.sidebar,
            text="Clear Canvas",
            command=self.clear_canvas,
            bg="#ff9800",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT
        ).pack(fill=tk.X, padx=15, pady=20)

        # Status
        self.status = tk.Label(
            self.sidebar,
            text="Current Tool: Pen",
            bg="#2b2b2b",
            fg="#bbbbbb",
            font=("Arial", 10)
        )
        self.status.pack(pady=10)

    def setup_events(self):
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.release)

    def select_pen_tool(self):
        self.selected_tool = "pen"
        self.status.config(text="Current Tool: Pen")

    def select_eraser_tool(self):
        self.selected_tool = "eraser"
        self.status.config(text="Current Tool: Eraser")

    def select_size(self, size):
        self.selected_size = size

    def select_color(self, color):
        self.selected_color = color

    def select_pen_type(self, pen_type):
        self.selected_pen_type = pen_type

    def draw(self, event):

        color = self.selected_color

        if self.selected_tool == "eraser":
            color = "white"

        if self.prev_x is not None and self.prev_y is not None:

            if self.selected_pen_type == "line":

                self.canvas.create_line(
                    self.prev_x,
                    self.prev_y,
                    event.x,
                    event.y,
                    fill=color,
                    width=self.selected_size,
                    smooth=True,
                    capstyle=tk.ROUND
                )

            elif self.selected_pen_type == "round":

                self.canvas.create_oval(
                    event.x - self.selected_size,
                    event.y - self.selected_size,
                    event.x + self.selected_size,
                    event.y + self.selected_size,
                    fill=color,
                    outline=color
                )

            elif self.selected_pen_type == "square":

                self.canvas.create_rectangle(
                    event.x - self.selected_size,
                    event.y - self.selected_size,
                    event.x + self.selected_size,
                    event.y + self.selected_size,
                    fill=color,
                    outline=color
                )

            elif self.selected_pen_type == "diamond":

                s = self.selected_size

                self.canvas.create_polygon(
                    event.x - s, event.y,
                    event.x, event.y - s,
                    event.x + s, event.y,
                    event.x, event.y + s,
                    fill=color,
                    outline=color
                )

        self.prev_x = event.x
        self.prev_y = event.y

    def release(self, event):
        self.prev_x = None
        self.prev_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw_circle(self):

        self.canvas.create_oval(
            300, 200, 500, 400,
            outline=self.selected_color,
            width=self.selected_size
        )

    def draw_rectangle(self):

        self.canvas.create_rectangle(
            250, 180, 550, 420,
            outline=self.selected_color,
            width=self.selected_size
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()