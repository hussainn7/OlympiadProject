import subprocess
import time
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

window = Tk()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_button(window, image_path, command):
    image = PhotoImage(file=relative_to_assets(image_path))
    button = Button(
        window,
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=command,
        relief="flat"
    )
    button.image = image  # Keep a reference to prevent garbage collection
    return button

def create_canvas(window, bg_color="#3E36B0", width=1440, height=1024):
    canvas = Canvas(
        window,
        bg=bg_color,
        height=height,
        width=width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    return canvas

def frame1_button3():
    frame0()

def on_button_3_click():
    create_gui1()

def frame2_button():
    create_gui2()

def urok2_button():
    urok2()

def urok3_button():
    urok3()
def frame0():
    window.geometry("1440x1024")
    window.configure(bg = "#3E36B0")


    canvas = create_canvas(window)

    canvas.create_rectangle(
        128.0,
        12.0,
        1428.0,
        1012.0,
        fill="#FFFFFF",
        outline="")

    button_1 = create_button(window, "home_main.png", lambda: print("DOM ACTIV"))
    button_1.place(x=27.0, y=58.0, width=71.0, height=66.0)

    canvas.create_text(
        184.0,
        61.0,
        anchor="nw",
        text="Good morning Koshel ! ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    canvas.create_text(
        184.0,
        545.0,
        anchor="nw",
        text="cool events this week  ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("Kubik.png"))
    image_1 = canvas.create_image(
        569.0,
        326.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("Kub2.png"))
    image_2 = canvas.create_image(
        345.0,
        426.0,
        image=image_image_2
    )

    canvas.create_text(
        199.0,
        161.0,
        anchor="nw",
        text="level of progress ",
        fill="#040404",
        font=("Poppins Regular", 40 * -1)
    )

    canvas.create_text(
        216.0,
        363.0,
        anchor="nw",
        text="Days in streak\n",
        fill="#040404",
        font=("Poppins Regular", 32 * -1)
    )

    canvas.create_text(
        199.0,
        227.0,
        anchor="nw",
        text="14 lesson",
        fill="#040404",
        font=("Noto Sans", 48 * -1)
    )

    canvas.create_text(
        216.0,
        400.0,
        anchor="nw",
        text="11",
        fill="#3E36B0",
        font=("Poppins Medium", 64 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("profile-photo.png"))
    image_3 = canvas.create_image(
        787.0,
        300.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("firebig.png"))
    image_4 = canvas.create_image(
        309.0,
        442.4174499511719,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("firesmall.png"))
    image_5 = canvas.create_image(
        309.6666564941406,
        455.87249755859375,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("plakat.png"))
    image_6 = canvas.create_image(
        325.0,
        801.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("plakat1.png"))
    image_7 = canvas.create_image(
        658.0,
        805.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("plakat2.png"))
    image_8 = canvas.create_image(
        1009.0,
        804.0,
        image=image_image_8
    )
    button_2 = create_button(window, "AI_BUTTON.png", frame2_button)
    button_2.place(x=27.0, y=233.0, width=71.0, height=66.0)

    button_3 = create_button(window, "knopka_2.png", on_button_3_click)
    button_3.place(x=27.0, y=141.0, width=69.0, height=66.0)

    window.resizable(False, False)
    window.mainloop()

def open_url(url):
    webbrowser.open(url)

def create_gui1():

    window.geometry("1440x1024")
    window.configure(bg="#3E36B0")

    canvas = create_canvas(window)

    button_1 = create_button(window, "home_main.png", lambda: print("button_1 clicked"))
    button_1.place(x=26.0, y=142.0, width=71.0, height=66.0)

    button_2 = create_button(window, "frame1_activ.png", lambda: print("button_2 clicked"))
    button_2.place(x=26.0, y=142.0, width=71.0, height=66.0)

    canvas.create_rectangle(
        128.0,
        12.0,
        1428.0,
        1012.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        225.0,
        62.0,
        anchor="nw",
        text="Good morning Koshel ! ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    button_3 = create_button(window, "domik_frame1.png", frame1_button3)
    button_3.place(x=26.0, y=56.0, width=71.0, height=66.0)

    button_4 = create_button(window, "tree_bg.png", lambda: open_url("https://youtu.be/KlOD43f6Dfk"))
    button_4.place(x=225.0, y=149.0, width=1105.0, height=790.0)

    button_5 = create_button(window, "AI_BUTTON.png", frame2_button)
    button_5.place( x=26.0, y=234.0, width=71.0, height=66.0)

    button_6 = create_button(window, "strelka vlevo.png", lambda: print("LEVO"))
    button_6.place(x=140.0, y=477.0, width=70.0, height=70.0)

    button_7 = create_button(window, "strelka pravo.png", urok2_button)
    button_7.place(x=1345.0, y=477.0, width=70.0, height=70.0)


    window.resizable(False, False)
    window.mainloop()


# $$$$$$$$$$$$$$$$$$$$$$$$ AI PART $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def open_voice_script():
    subprocess.Popen(["python", "voice.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(2)
    window.destroy()
# FUNCTION TO ADD AI
def create_gui2():
    window.geometry("1440x1024")
    window.configure(bg="#3E36B0")

    canvas = create_canvas(window)
    canvas.create_rectangle(
        128.0,
        12.0,
        1428.0,
        1012.0,
        fill="#FFFFFF",
        outline="")
    button_1 = create_button(window, "AI_ACTIV.png",lambda: print("AI BUTTON ACTIV clicked"))
    button_1.place(x=26.0, y=232.0, width=71.0, height=66.0)

    canvas.create_text(
        184.0,
        61.0,
        anchor="nw",
        text="Eve is your assistant in all matters ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    button_2 = create_button(window, "TREE FRAME2.png", on_button_3_click)
    button_2.place(x=27.0, y=141.0, width=69.0, height=66.0)

    canvas.create_rectangle(
        1214.0,
        818.0,
        1303.0,
        939.0,
        fill="#A6DFF7",
        outline="")

    button_3 = create_button(window, "mic.png", open_voice_script)
    button_3.place(x=1159.0, y=782.0, width=200.0, height=200.0)

    button_4 = create_button(window, "house_fram2.png", frame1_button3)
    button_4.place(x=26.0, y=61.0, width=71.0, height=66.0)

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        677.5,
        578.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#F1F1F1",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=196.0,
        y=149.0,
        width=963.0,
        height=857.0
    )
    window.resizable(False, False)
    window.mainloop()


def urok2():
    window.geometry("1440x1024")
    window.configure(bg="#3E36B0")

    canvas = create_canvas(window)

    button_1 = create_button(window, "frame1_activ.png", lambda: print("fr1 clicked"))
    button_1.place(x=26.0, y=142.0, width=71.0, height=66.0)

    button_2 = create_button(window, "frame1_activ.png", lambda: print("fr1 clicked"))
    button_2.place(x=26.0, y=142.0, width=71.0, height=66.0)

    canvas.create_rectangle(
        128.0,
        12.0,
        1428.0,
        1012.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        225.0,
        62.0,
        anchor="nw",
        text="Good morning Koshel ! ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    button_3 = create_button(window, "house_fram2.png", frame1_button3)
    button_3.place(x=26.0, y=56.0, width=71.0, height=66.0)

    button_4 = create_button(window, "bytilka.png", lambda: open_url("https://youtu.be/P95BtgO3o68"))
    button_4.place(x=225.0, y=149.0, width=1105.0, height=790.0)

    button_5 = create_button(window, "AI_BUTTON.png", frame2_button)
    button_5.place(x=26.0, y=234.0, width=71.0, height=66.0)

    button_6 = create_button(window, "strelka vlevo.png", on_button_3_click)
    button_6.place(x=140.0, y=477.0, width=70.0, height=70.0)

    button_7 = create_button(window, "strelka pravo.png", urok3_button)
    button_7.place(x=1345.0, y=477.0, width=70.0, height=70.0)

    window.resizable(False, False)
    window.mainloop()

def urok3():
    window.geometry("1440x1024")
    window.configure(bg="#3E36B0")

    canvas = create_canvas(window)

    button_1 = create_button(window, "frame1_activ.png", lambda: print("DOM clicked"))
    button_1.place(x=26.0, y=142.0, width=71.0, height=66.0)

    button_2 = create_button(window, "frame1_activ.png", lambda: print("TRRe clicked"))
    button_2.place(x=26.0, y=142.0, width=71.0, height=66.0)

    canvas.create_rectangle(
        128.0,
        12.0,
        1428.0,
        1012.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        225.0,
        62.0,
        anchor="nw",
        text="Good morning Koshel ! ",
        fill="#040404",
        font=("Inter", 40 * -1)
    )

    button_3 = create_button(window, "house_fram2.png", frame1_button3)
    button_3.place(x=26.0, y=56.0, width=71.0, height=66.0)

    button_4 = create_button(window, "SORTIROVKA.png", lambda: open_url("https://youtu.be/Krf79TC6ZDw"))
    button_4.place(x=225.0, y=149.0, width=1105.0, height=790.0)

    button_5 = create_button(window, "AI_BUTTON.png", frame2_button)
    button_5.place(x=26.0, y=234.0, width=71.0, height=66.0)

    button_6 = create_button(window, "strelka vlevo.png", urok2_button)
    button_6.place(x=140.0, y=477.0, width=70.0, height=70.0)

    button_7 = create_button(window, "strelka pravo.png", lambda: print("PRAVO clicked"))
    button_7.place(x=1345.0, y=477.0, width=70.0, height=70.0)

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    frame0()