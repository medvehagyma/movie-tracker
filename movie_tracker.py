

import tkinter as tk


def writeFormContentToFile(formTextboxes):
    with open("movies.txt", "a", encoding="utf-8") as movies_file:     # append-mód
        movies_file.write("Title: " + formTextboxes["title"].get() + "\n")  # itt fogom feliratozni
        movies_file.write("Release date: " + formTextboxes["release"].get() + "\n")
        movies_file.write("Watched date: " + formTextboxes["watched"].get() + "\n")
        movies_file.write("Seen: " + str(formTextboxes["seen"].get()) + "\n \n")  # boolean érték, ezért str-be kell konvertálni # kell-e a 2.\n az adatelemzésnél nem lesz-e akadály


formTextboxes = {}



root = tk.Tk()   # root = tk.Tk()
root.title("Movie tracker")
root.geometry("400x400")


greeting_label = tk.Label(
    root,
    text="Enikő's movie tracker",
    font=("Arial", 15)
)
greeting_label.pack(pady=20)
greeting_label.config(fg="red")



title_label = tk.Label(
    root,
    text="Enter the title",
    font=("Arial", 10)
)
title_label.pack(pady=10)

title_text_box = tk.Entry(root)
title_text_box.pack()
formTextboxes["title"] = title_text_box


releaseYear_label = tk.Label(
    root,
    text="Enter the release year",
    font=("Arial", 10)
)
releaseYear_label.pack(pady=10)

releaseYear_text_box = tk.Entry(root)
releaseYear_text_box.pack()
formTextboxes["release"] = releaseYear_text_box


watchedDate_label = tk.Label(
    root,
    text="Enter the watched year",
    font=("Arial", 10)
)
watchedDate_label.pack(pady=10)

watchedDate_label_text_box = tk.Entry(root)
watchedDate_label_text_box.pack()
formTextboxes["watched"] = watchedDate_label_text_box


seen = tk.BooleanVar()

seen_checkbox = tk.Checkbutton(
    root,
    text="I have seen it: ",
    variable=seen
)
seen_checkbox.pack()

seen_ceckbox_text_box = tk.BooleanVar()
formTextboxes["seen"] = seen


slider = tk.Scale(
    root,
    from_=0, to=10, 
    orient="horizontal"
)
slider.pack()



button = tk.Button(
    root,
    text="Save",
    command=lambda: writeFormContentToFile(formTextboxes)
)
button.pack()


root.mainloop()