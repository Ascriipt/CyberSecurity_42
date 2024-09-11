from datetime import datetime
from PIL.ExifTags import TAGS
from PIL import Image

import tkinter as tk
import customtkinter
import pytz
import sys
import os

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
class ImageMetadata:
    def __init__(self, image_path):
        self.file = image_path
        self.format = None
        self.mode = None
        self.size = None
        self.exif_data = {}

class App(customtkinter.CTk):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.current_index = 0

        # configure window
        self.title("Metadata Visualizer")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scorpion", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Next", command=self.sidebar_button_next)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Last", command=self.sidebar_button_last)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=600)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), rowspan=4, sticky="nsew")

        # create tabview
        self.sidebar_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Display initial metadata
        self.display_metadata(self.current_index)

    def display_metadata(self, index):
        self.textbox.delete("1.0", tk.END)

        if self.data[index] is None:
            self.textbox.insert(tk.END, f"No metadata available for image {index + 1}")
            return

        metadata = self.data[index]
        self.textbox.insert(tk.END, f"File: {metadata.file}\n")
        self.textbox.insert(tk.END, f"Format: {metadata.format}\n")
        self.textbox.insert(tk.END, f"Mode: {metadata.mode}\n")
        self.textbox.insert(tk.END, f"Size: {metadata.size}\n")

        if metadata.exif_data is not None:
            for tag, value in metadata.exif_data.items():
                self.textbox.insert(tk.END, f"{tag}: {value}")
                self.textbox.insert(tk.END, "\n")

    def sidebar_button_next(self):
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.display_metadata(self.current_index)

    def sidebar_button_last(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_metadata(self.current_index)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    

def get_metadata(image_path):
    try:
        metadata = ImageMetadata(image_path)
        with Image.open(image_path) as img:
            metadata.format = img.format
            metadata.mode = img.mode
            metadata.size = img.size

            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata.exif_data[tag_name] = value

                date_time = exif_data.get(36867, "Not available")
            else:
                metadata.exif_data = None

        return metadata

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None


def main():
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    if len(sys.argv) < 2:
        print("Usage: ./scorpion FILE1 [FILE2 ...]")
        sys.exit(1)

    data = []

    for file in sys.argv[1:]:
        if not os.path.isfile(file):
            print(f"File {file} does not exist.")
            continue

        if not file.lower().endswith(valid_extensions):
            print(f"File {file} has an invalid extension. Valid extensions are {valid_extensions}.")
            continue

        data.append(get_metadata(file))

    gui = App(data)
    gui.mainloop()


if __name__ == "__main__":
    main()
