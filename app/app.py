import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from logic.heap_manager import HeapManager
from logic.computer import ComputerPlayer


heap_manager = HeapManager(heap_size=15, max_count_to_take=3)
computer_player = ComputerPlayer(max_count_to_take=3)


def computer_step(label):
    tkinter.messagebox.showinfo('INFO', 'Computer step...')
    take = computer_player.step(heap_size=heap_manager.size())
    heap_manager.remove_items(count=int(take))
    label["text"] = f"Heap size: {heap_manager.size()}"

def start_window():
    window = Tk()
    window.title("Start Window")
    window.geometry("250x200")
    position = {"padx":6, "pady":6, "anchor":NW}
    select_var = StringVar(value='Computer First')
    computer_first_btn = ttk.Radiobutton(window, text='Computer First', value='Computer First', variable=select_var)
    computer_first_btn.pack(**position)
    me_first_btn = ttk.Radiobutton(window, text='Me First', value='Me First', variable=select_var)
    me_first_btn.pack(**position)
    start_button = Button(window, text='Start', command=lambda: game(window, select_var))
    start_button.pack(anchor=CENTER)
    window.mainloop()

def process_step(root, label, entry):
    try:
        heap_manager.remove_items(count=int(entry.get()))
    except Exception as err:
        tkinter.messagebox.showerror(title='ERROR', message=err)
        return

    label["text"] = f"Heap size: {heap_manager.size()}"  # получаем введенный текст
    if heap_manager.is_empty():
        tkinter.messagebox.showinfo('INFO', 'You Win')
        tkinter.messagebox.showinfo('INFO', 'Refreshing Game')
        heap_manager.refresh()
        label["text"] = f"Heap size: {heap_manager.size()}"
        root.destroy()
        start_window()
        return

    computer_step(label)

    if heap_manager.is_empty():
        tkinter.messagebox.showinfo('INFO', 'You lose')
        tkinter.messagebox.showinfo('INFO', 'Refreshing Game')
        heap_manager.refresh()
        label["text"] = f"Heap size: {heap_manager.size()}"
        root.destroy()
        start_window()


def game(window, select_var):
    window.destroy()

    root = Tk()
    root.title("B A S H E")
    root.geometry("400x400")
    label = ttk.Label()
    label["text"] = f"Heap size: {heap_manager.size()}"
    label.pack(anchor=CENTER, padx=6, pady=6)
    label_entry = ttk.Label()
    label_entry['text'] = 'Count to take'
    label_entry.pack(anchor=NW, padx=6, pady=6)
    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=6, pady=6)

    btn = ttk.Button(text="OK", command=lambda: process_step(root, label, entry))
    btn.pack(anchor=NW, padx=6, pady=6)

    if select_var.get() == 'Computer First':
        computer_step(label)

    root.mainloop()


if __name__ == '__main__':
    start_window()