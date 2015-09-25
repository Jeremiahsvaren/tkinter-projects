#!/usr/bin/env python3

__author__ = 'Jeremiah'


from tkinter import *
from phones import *

class ContactList:

    def __init__(self, master):

        def whichSelected () :
            #print("At %s of %d")% (select.curselection(), len(phonelist))
            return int(select.curselection()[0])

        def addEntry () :
            phonelist.append ([nameVar.get(), phoneVar.get()])
            setSelect ()

        def updateEntry() :
            phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
            setSelect ()

        def deleteEntry() :
            del phonelist[whichSelected()]
            setSelect ()

        def loadEntry  () :
            name, phone = phonelist[whichSelected()]
            nameVar.set(name)
            phoneVar.set(phone)


        master.title("Contact List")

        frame1 = Frame(master) #frame for labels and entrys
        frame1.pack()

        Label(frame1, text="Name:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
        nameVar = StringVar()
        name = Entry(frame1, textvariable=nameVar)
        name.grid(row=0,column=1, sticky=W, pady=10, padx=10)

        Label(frame1, text="Phone").grid(row=1, column=0, sticky=W, pady=10, padx=10)
        phoneVar = StringVar()
        phone = Entry(frame1, textvariable=phoneVar)
        phone.grid(row=1, column=1, sticky=W, pady=10, padx=10)


        frame2 = Frame(master)
        frame2.pack()

        add = Button(frame2, text="Add", command=addEntry)
        update = Button(frame2, text="Update", command=updateEntry)
        delete = Button(frame2, text="Delete", command=deleteEntry)
        load = Button(frame2, text="Load", command=loadEntry)
        add.grid(row=0, column=0, padx=5)
        update.grid(row=0, column=1, padx=5)
        delete.grid(row=0, column=2, padx=5)
        load.grid(row=0, column=3, padx=5)

        frame3 = Frame(master)
        frame3.pack()

        scroll = Scrollbar(frame3, orient=VERTICAL)
        select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
        scroll.config(command=select.yview)
        scroll.pack(side=RIGHT, fill=Y, pady=5)
        select.pack(side=LEFT, fill=BOTH, expand=1, pady=5)


        def setSelect () :
            phonelist.sort()
            select.delete(0,END)
            for name,phone in phonelist :
                select.insert (END, name)


def main():

    root = Tk()
    contactList = ContactList(root)
    root.mainloop()

if __name__ == "__main__": main()