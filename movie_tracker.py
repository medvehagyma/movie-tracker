

import tkinter as tk

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


releaseYear_label = tk.Label(
    root,
    text="Enter the release year",
    font=("Arial", 10)
)
releaseYear_label.pack(pady=10)

releaseYear_text_box = tk.Entry(root)
releaseYear_text_box.pack()


watchedDate_label = tk.Label(
    root,
    text="Enter the watched year",
    font=("Arial", 10)
)
watchedDate_label.pack(pady=10)

watchedDate_label_text_box = tk.Entry(root)
watchedDate_label_text_box.pack()


seen = tk.BooleanVar()

seen_checkbox = tk.Checkbutton(
    root,
    text="I have seen it: ",
    variable=seen
)
seen_checkbox.pack()

seen_ceckbox_text_box = tk.BooleanVar()


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