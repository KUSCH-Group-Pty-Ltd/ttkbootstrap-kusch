"""
ttkbootstrap-kusch Showcase (Standard TTK Style)

This script demonstrates how easy it is to apply ttkbootstrap-kusch theming
to a standard tkinter/ttk script. 

THE ONLY CHANGES FROM A NORMAL TTK SCRIPT:
1. Import: `import ttkbootstrap as ttk` instead of `from tkinter import ttk`
2. Window: `ttk.Window(themename="kusch_theme_dark")` instead of `tk.Tk()`

Everything else is standard ttk code - no special parameters or widgets!
"""

import tkinter as tk
# This is the only import change needed - swap ttk for ttkbootstrap
import ttkbootstrap as ttk


class TTKShowcase:
    """Showcase standard TTK widgets with ttkbootstrap theming applied."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Standard TTK Showcase (with ttkbootstrap-kusch)")
        self.root.geometry("850x900")
        
        # Build UI using standard ttk patterns
        self._create_widgets()
    
    def _create_widgets(self):
        """Create all showcase widgets using standard TTK code."""
        # Main scrollable canvas setup (standard tkinter pattern)
        canvas = tk.Canvas(self.root, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        frame_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        def configure_canvas(e):
            canvas.itemconfig(frame_id, width=e.width)
        
        canvas.bind("<Configure>", configure_canvas)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Content Container
        main_frame = ttk.Frame(scrollable_frame, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self._create_header(main_frame)
        
        # Sections
        self._create_button_section(main_frame)
        self._create_label_section(main_frame)
        self._create_input_section(main_frame)
        self._create_checkbutton_section(main_frame)
        self._create_radiobutton_section(main_frame)
        self._create_progressbar_section(main_frame)
        self._create_scale_section(main_frame)
        self._create_spinbox_section(main_frame)
        self._create_notebook_section(main_frame)
        self._create_treeview_section(main_frame)
        self._create_listbox_section(main_frame)
        
        # Enable Mousewheel scrolling
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    
    def _create_section(self, parent, title):
        """Helper to create a consistent section with a labelframe."""
        section = ttk.Labelframe(parent, text=title, padding=15)
        section.pack(fill=tk.X, pady=(0, 15))
        return section
    
    def _create_header(self, parent):
        """Create the header section."""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title label - standard ttk.Label
        title = ttk.Label(header_frame, text="Standard TTK Showcase", font=("Segoe UI", 24, "bold"))
        title.pack(anchor=tk.W)
        
        # Subtitle
        subtitle = ttk.Label(header_frame, text="All widgets below use standard ttk code - only the import changed!")
        subtitle.pack(anchor=tk.W, pady=(5, 0))
        
        # Separator
        ttk.Separator(header_frame, orient="horizontal").pack(fill=tk.X, pady=(15, 0))
    
    def _create_button_section(self, parent):
        """Demonstrate standard ttk.Button widgets."""
        section = self._create_section(parent, "Buttons (ttk.Button)")
        
        btn_frame = ttk.Frame(section)
        btn_frame.pack(fill=tk.X)
        
        # Standard buttons - no special parameters
        ttk.Button(btn_frame, text="Primary Action").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Secondary Action").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancel").pack(side=tk.LEFT, padx=5)
        
        # Disabled button
        disabled_btn = ttk.Button(btn_frame, text="Disabled")
        disabled_btn.state(["disabled"])
        disabled_btn.pack(side=tk.LEFT, padx=5)
    
    def _create_label_section(self, parent):
        """Demonstrate standard ttk.Label widgets."""
        section = self._create_section(parent, "Labels (ttk.Label)")
        
        # Standard labels with different fonts
        ttk.Label(section, text="Default Label Text").pack(anchor=tk.W, pady=2)
        ttk.Label(section, text="Bold Label", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=2)
        ttk.Label(section, text="Larger Label", font=("Segoe UI", 14)).pack(anchor=tk.W, pady=2)
        ttk.Label(section, text="Italic Label", font=("Segoe UI", 10, "italic")).pack(anchor=tk.W, pady=2)
    
    def _create_input_section(self, parent):
        """Demonstrate input widgets."""
        section = self._create_section(parent, "Input Widgets (ttk.Entry, ttk.Combobox)")
        
        # Entry widgets
        row1 = ttk.Frame(section)
        row1.pack(fill=tk.X, pady=5)
        
        ttk.Label(row1, text="Entry:", width=15).pack(side=tk.LEFT)
        entry1 = ttk.Entry(row1, width=30)
        entry1.insert(0, "Editable text here")
        entry1.pack(side=tk.LEFT, padx=5)
        
        entry2 = ttk.Entry(row1, width=30)
        entry2.insert(0, "Another entry")
        entry2.pack(side=tk.LEFT, padx=5)
        
        # Combobox widgets
        row2 = ttk.Frame(section)
        row2.pack(fill=tk.X, pady=5)
        
        ttk.Label(row2, text="Combobox:", width=15).pack(side=tk.LEFT)
        combo1 = ttk.Combobox(row2, values=["Option 1", "Option 2", "Option 3"], width=27)
        combo1.set("Select an option")
        combo1.pack(side=tk.LEFT, padx=5)
        
        combo2 = ttk.Combobox(row2, values=["A", "B", "C", "D"], width=27, state="readonly")
        combo2.set("Read-only combo")
        combo2.pack(side=tk.LEFT, padx=5)
        
        # Disabled entry
        row3 = ttk.Frame(section)
        row3.pack(fill=tk.X, pady=5)
        
        ttk.Label(row3, text="Disabled:", width=15).pack(side=tk.LEFT)
        disabled_entry = ttk.Entry(row3, width=30)
        disabled_entry.insert(0, "This is disabled")
        disabled_entry.state(["disabled"])
        disabled_entry.pack(side=tk.LEFT, padx=5)
    
    def _create_checkbutton_section(self, parent):
        """Demonstrate checkbutton widgets."""
        section = self._create_section(parent, "Checkbuttons (ttk.Checkbutton)")
        
        check_frame = ttk.Frame(section)
        check_frame.pack(fill=tk.X)
        
        var1 = tk.BooleanVar(value=True)
        var2 = tk.BooleanVar(value=False)
        var3 = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(check_frame, text="Option A (checked)", variable=var1).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(check_frame, text="Option B (unchecked)", variable=var2).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(check_frame, text="Option C (checked)", variable=var3).pack(side=tk.LEFT, padx=10)
        
        # Disabled checkbutton
        disabled_chk = ttk.Checkbutton(check_frame, text="Disabled Option")
        disabled_chk.state(["disabled"])
        disabled_chk.pack(side=tk.LEFT, padx=10)
    
    def _create_radiobutton_section(self, parent):
        """Demonstrate radiobutton widgets."""
        section = self._create_section(parent, "Radiobuttons (ttk.Radiobutton)")
        
        radio_frame = ttk.Frame(section)
        radio_frame.pack(fill=tk.X)
        
        var = tk.StringVar(value="option1")
        
        ttk.Radiobutton(radio_frame, text="Option 1", value="option1", variable=var).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(radio_frame, text="Option 2", value="option2", variable=var).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(radio_frame, text="Option 3", value="option3", variable=var).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(radio_frame, text="Option 4", value="option4", variable=var).pack(side=tk.LEFT, padx=10)
    
    def _create_progressbar_section(self, parent):
        """Demonstrate progressbar widgets."""
        section = self._create_section(parent, "Progressbars (ttk.Progressbar)")
        
        # Determinate progressbar
        row1 = ttk.Frame(section)
        row1.pack(fill=tk.X, pady=5)
        
        ttk.Label(row1, text="Determinate:", width=15).pack(side=tk.LEFT)
        pb1 = ttk.Progressbar(row1, value=70, length=300)
        pb1.pack(side=tk.LEFT, padx=5)
        ttk.Label(row1, text="70%").pack(side=tk.LEFT, padx=5)
        
        # Another progressbar
        row2 = ttk.Frame(section)
        row2.pack(fill=tk.X, pady=5)
        
        ttk.Label(row2, text="Lower value:", width=15).pack(side=tk.LEFT)
        pb2 = ttk.Progressbar(row2, value=30, length=300)
        pb2.pack(side=tk.LEFT, padx=5)
        ttk.Label(row2, text="30%").pack(side=tk.LEFT, padx=5)
        
        # Indeterminate
        row3 = ttk.Frame(section)
        row3.pack(fill=tk.X, pady=5)
        
        ttk.Label(row3, text="Indeterminate:", width=15).pack(side=tk.LEFT)
        pb3 = ttk.Progressbar(row3, mode="indeterminate", length=300)
        pb3.pack(side=tk.LEFT, padx=5)
        pb3.start(10)  # Animation
    
    def _create_scale_section(self, parent):
        """Demonstrate scale widgets."""
        section = self._create_section(parent, "Scales (ttk.Scale)")
        
        scale_frame = ttk.Frame(section)
        scale_frame.pack(fill=tk.X)
        
        # Horizontal scales
        ttk.Label(scale_frame, text="Horizontal:").pack(anchor=tk.W)
        ttk.Scale(scale_frame, from_=0, to=100, orient="horizontal", length=300).pack(anchor=tk.W, pady=5)
        
        ttk.Scale(scale_frame, from_=0, to=100, orient="horizontal", length=300, value=75).pack(anchor=tk.W, pady=5)
    
    def _create_spinbox_section(self, parent):
        """Demonstrate spinbox widgets."""
        section = self._create_section(parent, "Spinbox (ttk.Spinbox)")
        
        spin_frame = ttk.Frame(section)
        spin_frame.pack(fill=tk.X)
        
        ttk.Label(spin_frame, text="Numeric:", width=15).pack(side=tk.LEFT)
        ttk.Spinbox(spin_frame, from_=0, to=100, width=15).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(spin_frame, text="With values:", width=15).pack(side=tk.LEFT)
        ttk.Spinbox(spin_frame, values=("Low", "Medium", "High"), width=15).pack(side=tk.LEFT, padx=5)
    
    def _create_notebook_section(self, parent):
        """Demonstrate notebook (tabs) widget."""
        section = self._create_section(parent, "Notebook / Tabs (ttk.Notebook)")
        
        notebook = ttk.Notebook(section)
        notebook.pack(fill=tk.X, pady=5)
        
        # Tab 1
        tab1 = ttk.Frame(notebook, padding=15)
        notebook.add(tab1, text="First Tab")
        ttk.Label(tab1, text="This is the content of the first tab.").pack(anchor=tk.W)
        ttk.Button(tab1, text="A Button").pack(anchor=tk.W, pady=10)
        
        # Tab 2
        tab2 = ttk.Frame(notebook, padding=15)
        notebook.add(tab2, text="Second Tab")
        ttk.Label(tab2, text="This is the content of the second tab.").pack(anchor=tk.W)
        ttk.Entry(tab2, width=30).pack(anchor=tk.W, pady=10)
        
        # Tab 3
        tab3 = ttk.Frame(notebook, padding=15)
        notebook.add(tab3, text="Third Tab")
        ttk.Label(tab3, text="This is the content of the third tab.").pack(anchor=tk.W)
    
    def _create_treeview_section(self, parent):
        """Demonstrate treeview widget."""
        section = self._create_section(parent, "Treeview (ttk.Treeview)")
        
        # Create Treeview with columns
        columns = ("name", "size", "modified")
        tree = ttk.Treeview(section, columns=columns, show="headings", height=5)
        
        # Define headings
        tree.heading("name", text="Name")
        tree.heading("size", text="Size")
        tree.heading("modified", text="Modified")
        
        # Define column widths
        tree.column("name", width=200)
        tree.column("size", width=100)
        tree.column("modified", width=150)
        
        # Add sample data
        sample_data = [
            ("document.pdf", "2.5 MB", "2024-01-15"),
            ("image.png", "850 KB", "2024-01-14"),
            ("spreadsheet.xlsx", "1.2 MB", "2024-01-13"),
            ("presentation.pptx", "5.8 MB", "2024-01-12"),
            ("archive.zip", "15.3 MB", "2024-01-11"),
        ]
        
        for item in sample_data:
            tree.insert("", tk.END, values=item)
        
        tree.pack(fill=tk.X, pady=5)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(section, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
    
    def _create_listbox_section(self, parent):
        """Demonstrate a frame with multiple widgets (like a form)."""
        section = self._create_section(parent, "Sample Form Layout")
        
        # Row 1
        row1 = ttk.Frame(section)
        row1.pack(fill=tk.X, pady=5)
        
        ttk.Label(row1, text="First Name:", width=15).pack(side=tk.LEFT)
        ttk.Entry(row1, width=30).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(row1, text="Last Name:", width=15).pack(side=tk.LEFT)
        ttk.Entry(row1, width=30).pack(side=tk.LEFT, padx=5)
        
        # Row 2
        row2 = ttk.Frame(section)
        row2.pack(fill=tk.X, pady=5)
        
        ttk.Label(row2, text="Email:", width=15).pack(side=tk.LEFT)
        ttk.Entry(row2, width=30).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(row2, text="Department:", width=15).pack(side=tk.LEFT)
        dept_combo = ttk.Combobox(row2, values=["Engineering", "Sales", "Marketing", "HR"], width=27)
        dept_combo.set("Select department")
        dept_combo.pack(side=tk.LEFT, padx=5)
        
        # Row 3 - Checkboxes
        row3 = ttk.Frame(section)
        row3.pack(fill=tk.X, pady=10)
        
        var1 = tk.BooleanVar(value=True)
        ttk.Checkbutton(row3, text="Subscribe to newsletter", variable=var1).pack(side=tk.LEFT, padx=5)
        
        var2 = tk.BooleanVar(value=False)
        ttk.Checkbutton(row3, text="Accept terms and conditions", variable=var2).pack(side=tk.LEFT, padx=5)
        
        # Buttons row
        btn_row = ttk.Frame(section)
        btn_row.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(btn_row, text="Submit").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_row, text="Clear").pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_row, text="Cancel").pack(side=tk.LEFT, padx=5)


def main():
    """Run the showcase application."""
    # THIS IS THE ONLY REAL CHANGE FROM STANDARD TKINTER:
    # Instead of: root = tk.Tk()
    # We use: root = ttk.Window(themename="kusch_theme_dark")
    
    root = ttk.Window(
        title="Standard TTK Showcase",
        themename="kusch_theme_dark",  # Change to "kusch_theme_light" for light mode
        size=(850, 900)
    )
    
    app = TTKShowcase(root)
    root.mainloop()


if __name__ == "__main__":
    main()
