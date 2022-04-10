from tkinter import *
import Tools
import HousekeepingLog


## UI


def getData(button, product, amount):
    """ Collect the given data. """
    product = product.get()
    amount = float(amount.get())

    if Tools.checkFile(button):
        Tools.writeCSVFile(button, product, amount)
    else:
        Tools.createCSVFile(button)
        Tools.writeCSVFile(button, product, amount)


def commandB(button):
    """ Command the following categorized buttons:
        HOME, GROCERY, PERSONAL, UBER, OTHERS. """
    product = StringVar()
    amount = StringVar()

    product_label = Label(UI, text="Product:")
    product_label.grid(row=3, column=0)
    product_entry = Entry(UI)
    product_entry.grid(row=3, column=1, columnspan=5)

    amount_label = Label(UI, text="Price ($):")
    amount_label.grid(row=4, column=0)
    amount_entry = Entry(UI)
    amount_entry.grid(row=4, column=1, columnspan=5)

    enter = Button(UI, text="Enter", width=8,
                   command=lambda:getData(button, product_entry, amount_entry))
    enter.grid(row=4, column=5)


def commandQuit(UI):
    """ Command the button 'QUIT' and
        document all collected data."""
    HousekeepingLog.createHousekeepingLog(HousekeepingLog.gatherHousekeepingLog())
    UI.destroy()


def getStatistics():
    """ Get statistics of usage. """
    statistic = HousekeepingLog.analyzeHousekeepingLog(HousekeepingLog.gatherHousekeepingLog())

    stat_label = Label(UI, text="")
    stat_label.grid(row=5, column=0, rowspan=5, columnspan=6)
    
    Tools.printResult(statistic, stat_label)


if __name__ == "__main__":
    # Create an user interface
    UI = Tk()
    
    UI.title("HOUSEKEEPING LOG")
    UI.geometry("460x280")

    # Create buttons
    b1 = Button(UI, text="HOME", bg="white", fg="black", height=3, width=8,
                command=lambda: commandB(b1))
    b1.grid(row=1, column=0)
    b2 = Button(UI, text="GROCERY", bg="white", fg="black", height=3, width=8,
                command=lambda: commandB(b2))
    b2.grid(row=1, column=1)
    b3 = Button(UI, text="PERSONAL", bg="white", fg="black", height=3, width=8,
                command=lambda: commandB(b3))
    b3.grid(row=1, column=2)
    b4 = Button(UI, text="UBER", bg="white", fg="black", height=3, width=8,
                command=lambda: commandB(b4))
    b4.grid(row=1, column=3)
    b5 = Button(UI, text="OTHERS", bg="white", fg="black", height=3, width=8,
                command=lambda: commandB(b5))
    b5.grid(row=1, column=4)
    b_quit = Button(UI, text="QUIT", bg="gray", fg="red", height=3, width=8,
                    command=lambda:commandQuit(UI))
    b_quit.grid(row=1, column=5)
    b_stat = Button(UI, text="statistic", bg="gray", fg="blue", width=8,
                    command=lambda:getStatistics())
    b_stat.grid(row=2, column=5) 
