from tkinter import ttk, StringVar
from ttkthemes import ThemedTk
from watermarker import Watermarker

# The constant variables are fonts and font colors.
STEP_FONT = "Helvetica"
BACKGROUND_COLOR = "#DCEEEF"
TEXT_COLOR = "#000000"
SELECTED_COLOR = "#FF6100"


def upload_photo():
    """Calls the Watermarker upload photo function, and enables/disables
    the buttons on the GUI to direct the user to the next step. This also
    changes the font colors of the GUI labels to provide even more direction
    to the user as to the current step."""
    watermarker.upload_photo()
    upload_image_button.config(state="disabled")
    upload_watermark_button.config(state="!disabled")
    watermark_text.config(state="!disabled")
    color_choice.config(state="!disabled")
    confirm_text_button.config(state="!disabled")
    step_one.config(foreground=TEXT_COLOR)
    step_two_a.config(foreground=SELECTED_COLOR)
    or_label.config(foreground=SELECTED_COLOR)
    step_two_b.config(foreground=SELECTED_COLOR)


def upload_mark_photo():
    """Calls the Watermarker upload watermark photo function, and enables/disables
    the buttons on the GUI to direct the user to the next step. This also
    changes the font colors of the GUI labels to provide even more direction
    to the user as to the current step."""
    watermarker.upload_watermark_photo()
    upload_watermark_button.config(state="disabled")
    confirm_text_button.config(state="disabled")
    watermark_text.config(state="disabled")
    color_choice.config(state="disabled")
    step_two_a.config(foreground=TEXT_COLOR)
    or_label.config(foreground=TEXT_COLOR)
    step_two_b.config(foreground=TEXT_COLOR)

    confirm_mark.config(state="!disabled")
    final_step.config(foreground=SELECTED_COLOR)


def get_text():
    """If the user wants to use text instead of an image for their watermark, this gets the text from
    the entry in the GUI, and also gets the text color from the GUI, and passes it to the Watermarker class instance.
    This also enables/disables buttons on the GUI, and changes the GUI label font colors, to provide direction to the
    user as to what the current step is."""
    text = watermark_text.get()
    if len(text) == 0:
        raise Exception("You didn't input any text.")
    color = text_color.get()
    watermarker.get_text(text)
    watermarker.set_text_color(color)
    upload_watermark_button.config(state="disabled")
    color_choice.config(state="disabled")
    confirm_text_button.config(state="disabled")
    watermark_text.config(state="disabled")
    step_two_a.config(foreground=TEXT_COLOR)
    or_label.config(foreground=TEXT_COLOR)
    step_two_b.config(foreground=TEXT_COLOR)

    confirm_mark.config(state="!disabled")
    final_step.config(foreground=SELECTED_COLOR)


def mark_image():
    """Calls the Watermarker mark image function, finishes running the app, and closes the GUI window."""
    window.destroy()
    watermarker.mark_image()


# Creation of the main GUI window using a Tk theme.
window = ThemedTk(theme="breeze")
window.title("The Watermark App - by Liem Tran, based on Corey Ellis'")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Creation of the Watermarker class instance.
watermarker = Watermarker()

# The app's title heading.
app_heading = ttk.Label(
    text="Watermark app",
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
    font=("Helvetica", 40)
)
app_heading.grid(column=0, row=0, pady=(0, 30))

# Step one - upload image label and button.
step_one = ttk.Label(
    text="Step 1. Upload your image",
    background=BACKGROUND_COLOR,
    foreground=SELECTED_COLOR,
    font=(STEP_FONT, 14)
)
step_one.grid(column=0, row=1, pady=10, sticky="w")
upload_image_button = ttk.Button(text="Upload photo", command=upload_photo)
upload_image_button.grid(column=0, row=2, sticky="w")

# Step two - a and b - choose to either upload a watermark image, or input text as a watermark.
step_two_a = ttk.Label(
    text="Step 2a. Upload your watermark",
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
    font=(STEP_FONT, 14)
)
step_two_a.grid(column=0, row=3, pady=(20, 10), sticky="w")
upload_watermark_button = ttk.Button(text="Upload watermark", command=upload_mark_photo)
upload_watermark_button.grid(column=0, row=4, sticky="w")
upload_watermark_button.config(state="disabled")
or_label = ttk.Label(
    text="-OR-",
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
    font=(STEP_FONT, 20)
)
or_label.grid(column=0, row=5, pady=20, sticky="w")
step_two_b = ttk.Label(
    text="Step 2b. Watermark with text",
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
    font=(STEP_FONT, 14)
)
step_two_b.grid(column=0, row=6, pady=(0, 10), sticky="w")
watermark_text = ttk.Entry(width=35)
watermark_text.grid(column=0, row=7, sticky="w")
watermark_text.config(state="disabled")
text_color = StringVar()
color_choice = ttk.Combobox(window, textvariable=text_color)
color_choice.config(values=("White text", "Black text"), state="readonly")
color_choice.config(state="disabled")
color_choice.set("White text")
color_choice.grid(column=0, row=7, sticky="e")
confirm_text_button = ttk.Button(text="Confirm text", command=get_text)
confirm_text_button.grid(column=0, row=9, pady=(10, 0), sticky="w")
confirm_text_button.config(state="disabled")

# The final step is to click the button to retrieve your now watermarked image. The watermarked image is saved in your
# current directory as "watermarked_image.png".
final_step = ttk.Label(
    text="Step 3. Click the button below to get your image",
    background=BACKGROUND_COLOR,
    foreground=TEXT_COLOR,
    font=(STEP_FONT, 14)
)
final_step.grid(column=0, row=17, pady=(20, 10), sticky="w")
confirm_mark = ttk.Button(text="Mark my image!", command=mark_image)
confirm_mark.grid(column=0, row=18, sticky="w")
confirm_mark.config(state="disabled")



window.mainloop()