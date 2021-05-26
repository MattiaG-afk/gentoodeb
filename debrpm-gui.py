#!/usr/bin/python3
import os, sys, subprocess
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo, showerror
from tkinter import *

class debrpmGUI():
    def __init__(self, **kwargs):
        self.options = {}
        self.log_dir = '/var/log/debrpm'
        self.tmp_dir = '/var/tmp/debrpm'
        
        self.root = Tk()
        self.root.title('Debrpm GUI')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='/usr/share/pixmaps/debrpm-GUI.png'))

        self.row = Frame(self.root)
        Label(self.row, text='Select the file that you want to install:').pack(side=LEFT, fill=BOTH)
        self.file = Entry(self.row)
        self.file.pack(side=LEFT, expand=YES, fill=X)
        Button(self.row, text='Browse file', command=(lambda: self.fillEntry(self.file, askopenfilename()))).pack(side=RIGHT, expand=YES, fill=BOTH)
        self.row.pack(expand=YES, fill=BOTH)

        self.row = Frame(self.root)
        Label(self.row, text='Root directory:').pack(side=LEFT, fill=BOTH)
        self.root_dir = Entry(self.row)
        self.root_dir.insert(0, '/')
        self.root_dir.pack(side=LEFT, expand=YES, fill=X)
        Button(self.row, text='Browse directory', command=(lambda: self.fillEntry(self.root_dir, askdirectory()))).pack(side=RIGHT, expand=YES, fill=BOTH)
        self.row.pack(expand=YES, fill=BOTH)

        Button(self.root, text='List', command=self.listInstalled).pack(side=LEFT, expand=NO, fill=BOTH)
        Button(self.root, text='Install', command=(lambda: self.installFile(self.file.get(), self.root_dir.get()))).pack(side=RIGHT, fill=BOTH)
        Button(self.root, text='Uninstall', command=(lambda: self.uninstallFile(self.file.get().split('/')[-1]))).pack(side=RIGHT, fill=BOTH)
        self.root.mainloop()

    def fillEntry(entry, value):
        entry.delete(0, END)
        entry.insert(0, value)

    def installFile(file, root):
        try:
            subprocess.run('sudo debrpm -i %s -/ %s' % (file, root), shell=True)
            showinfo('Debrpm GUI', 'Package installed successfully')
        except:
            showerror('Debrpm GUI', 'An error occurred:\n%s' % sys.exc_info)

    def uninstallFile(packet):
        try:
            print(packet)
            subprocess.run('sudo debrpm -u %s' % file, shell=True)
            showinfo('Debrpm GUI', 'Package uninstalled successfully')
        except:
            showerror('Debrpm GUI', 'An error occurred: \n%s' % sys.exc_info)

    def listInstalled():
        packageDescription = [['Name:', 'Type:', 'Log file:']]
        listWindow = Toplevel()
        listWindow.tk.call('wm', 'iconphoto', listWindow._w, PhotoImage(file='/usr/share/pixmaps/debrpm-GUI.png'))
        listWindow.resizable(width=0, height=0)
        index = 0
        for file in os.listdir(self.log_dir):
            if file.endswith('.log'):
                index += 1
                packageDescription.append([file.replace('.deb.log', ''), "deb" if ".deb" in file else "rpm", os.path.join(self.log_dir, file)])
        ii = 0
        for i in packageDescription:
            jj = 0
            for j in i:
                Label(listWindow, text=j).grid(row=ii, column=jj)
                jj += 1
            ii += 1
        Label(listWindow, text='Number of installed packages: %s' % index).grid()
        listWindow.grab_set()
        listWindow.focus_set()
        listWindow.wait_window()

if __name__ == '__main__':
    root = debrpmGUI()
