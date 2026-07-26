import customtkinter as ctk
from PIL import ImageTk, Image

name ="pymate"
version_number = "0,0,0"
edition = name + version_number

class UI:
    def __init__(self, **kwargs):
        # 1. Apply Appearance and Theme Settings
        ctk.set_appearance_mode(kwargs.get("appearance_mode","System"))  # "System", "Dark","Light"
        ctk.set_default_color_theme(kwargs.get("color_theme"),"blue")        # "blue","dark-blue","green"

        # 2.window inithial dimensions
        self.win_width = kwargs.get("win_width",800)
        self.win_height = kwargs.get("win_height",600)
        
        self.win = ctk.CTk()
        win = self.win
        self.win.geometry(f"{self.win_width}x{self.win_height}") 
        self.win.title(edition)
        self.win.minsize(700, 450)

        # 3. logo for app                        icon is needed
        app_icon = ImageTk.PhotoImage(Image.open("app_icon.png"))
        self.wm_iconphoto(True, app_icon)

        # 4. Grid Configuration for Responsive Scaling
        # Row 0 expands vertically
        self.win.grid_rowconfigure(0, weight=1)
        
        # Column 0 (Sidebar) stays fixed-width; Column 1 (Content) expands horizontally
        self.win.grid_columnconfigure(0, weight=0)
        self.win.grid_columnconfigure(1, weight=1)

        # 5. Build Components
        self._build_sidebar()
        self._build_content_area()
        
        # Open default tab
        self.actions_tab()

    def _build_sidebar(self):
        """Creates a sidebar fixed to the full height (North-South)."""
        self.sidebar = ctk.CTkFrame(self.win, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=0, pady=0)

        
        title_label = ctk.CTkLabel(
            self.sidebar, 
            text=name, 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack(padx=20, pady=(20, 10))

        #icons for btns                                   actual imgs to replace place holder 
        icon_actions = ctk.CTkImage(light_image=Image.open("actions_icon.png"), size=(20, 20))
        icon_integrations = ctk.CTkImage(light_image=Image.open("integrations_icon.png"), size=(20, 20))
        icon_connect = ctk.CTkImage(light_image=Image.open("connect_icon.png"), size=(20, 20))
        icon_settings = ctk.CTkImage(light_image=Image.open("settings_icon.png"), size=(20, 20))

        # Navigation Buttons
        nav_buttons = [
        ("Actions", self.actions_tab, icon_actions),
        ("Integrations", self.integrations_tab, icon_integrations),
        ("Connect", self.connect_tab, icon_connect),
        ("Settings", self.settings_tab, icon_settings)
        ]

        #construction of butons
        for text, command, icon in nav_buttons:
            btn = ctk.CTkButton(
            self.sidebar,
            text=text,
            image=icon,
            compound="left",      # Places the icon to the left of the text
            anchor="w",           # Left-aligns the text and icon inside the button
            command=command).pack(padx=15, pady=8, fill="x")

    def _build_content_area(self):
        """Creates the main content panel that expands in all directions."""
        self.content_frame = ctk.CTkFrame(self.win, corner_radius=10)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

    def clear_content(self):
        """Clears existing widgets in the content frame when switching views."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # tabs
    def actions_tab(self):
        self.clear_content()
        

    def integrations_tab(self):
        self.clear_content()
        

    def connect_tab(self):
        self.clear_content()
        

    def settings_tab(self):
        self.clear_content()
    

    # advanced ui components

    def run(self):
        self.win.mainloop()

class ALERTS(ctk.CTkToplevel):

    inform_colour = "#0000ff"
    success_colour = "#00ff00"
    warning_colour = "#ffbb00"
    error_colour = "#ff0000"

    def __init__(self, parent, colour, message, duration_ms=2500):
        super().__init__(parent)
        
        # Hide window decorations and keep on top
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        
        # Pill Frame with custom color passed in
        self.frame = ctk.CTkFrame(
            self, 
            corner_radius=20, 
            fg_color=colour,
            border_width=0
        )
        self.frame.pack(fill="both", expand=True)

        # Alert Message
        self.label = ctk.CTkLabel(
            self.frame, 
            text=message, 
            text_color="white", 
            font=("Helvetica", 13, "bold"),
            padx=20, 
            pady=8
        )
        self.label.pack()

        # Calculate positioning relative to parent window
        self.update_idletasks()
        
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        
        toast_width = self.winfo_width()
        toast_height = self.winfo_height()

        x = parent_x + (parent_width // 2) - (toast_width // 2)
        y = parent_y + 40  # Distance from the top of the parent window

        self.geometry(f"{toast_width}x{toast_height}+{x}+{y}")

        # Auto-destroy after duration
        self.after(duration_ms, self.destroy)
