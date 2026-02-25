from tkinter import Tk, Label, Button, Entry, Frame, messagebox
# luo ohjelma ikkuna
window = Tk()
window.title('Hello')
# luo Frame, jonne tulee riville label ja entry
frame = Frame(window)
Label(frame, text='"Mikä on sinun nimesi?"', padx=10, pady=10) .pack(side='left')
entry = Entry(frame)
entry.pack(side='right')
# show frame and button
frame.pack(side='top')
Button(window, text='Lähetä',
       command =lambda : [messagebox.showinfo("Hello",
                          f'Hauska tavata, {entry.get()}.'), entry.delete(0, 'end')]).pack(side='bottom')
window.mainloop()
# start the event loop