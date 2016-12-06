'''
Created on Jul 12, 2015

@author: Daniel Bruce
'''

if __name__ == '__main__':
    pass

from tkinter import *
from tkinter import ttk

from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCSTR, UINT
prototype = WINFUNCTYPE(c_int, HWND, LPCSTR, LPCSTR, UINT)
paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", None), (1, "flags", 0)
MessageBox = prototype(("MessageBoxA", windll.user32), paramflags)

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def rubbish():
    MessageBox(text="This button has no functionality.")

root = Tk()
root.title("Store your passwords securely.")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)

vaultSelectFrame = ttk.Frame(mainframe)
chooseKeyFrame = ttk.Frame(mainframe)
credentialFrame = ttk.Frame(mainframe)
passwordSearchFrame = ttk.Frame(mainframe)
modificationFrame = ttk.Frame(mainframe)

feet = StringVar()
meters = StringVar()
lclVaultValue = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(vaultSelectFrame, text="Create New Vault", command=rubbish).grid(row=1, sticky=W)
ttk.Label(vaultSelectFrame, textvariable="Enter your vault information:").grid(row=2, sticky=(W, E))
ttk.Entry(mainframe, width=7, textvariable=lclVaultValue)
# 
# ttk.Button(vaultSelectFrame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# 
# ttk.listbox = Listbox(root)
# 
# ttk.Label(vaultSelectFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(vaultSelectFrame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# 
# ttk.Label(vaultSelectFrame, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(vaultSelectFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(vaultSelectFrame, text="meters").grid(column=3, row=2, sticky=W)

#for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()