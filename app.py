from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Clock")
window.geometry("410x210")
window.configure(bg="black")  
window.resizable(False, False) 

clock_label = Label(
    window, bg="black", fg="white", font=("Sans Serif", 50, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)


def update_label():
    
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)  # to update after every 80 milliseconds
    clock_label.pack(anchor="center")


update_label()
window.mainloop()


