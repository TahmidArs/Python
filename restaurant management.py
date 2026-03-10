import tkinter as tk
from tkinter import ttk,massagebox
from tkinter import messagebox

class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("REstaurant Management App")

    self.menu_items={
        "Fries Meal": 2,
        "Lunch Meal": 2,
        "Burger Meal":3,
        "Pizza Meal":4,
        "Cheese Burger":2.5,
        "Drinks":1
    }

    self.exchange_rate=82

    frame=ttk.Frame(root)
    frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    ttk.Label(frame,text="Restaurant Order Management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)

    self.menu_labels={}
    self.menu_quantities={}

    for i,(item,price) in enumerate(self.menu_items.items()):
        label=ttk.Label(frame,text=f"{item}: ${price:.2f}")
        label.grid(row=i+1,column=0,padx=10,pady=5,sticky=tk.W)
        self.menu_labels[item]=label

        quantity_var=tk.IntVar()
        quantity_entry=ttk.Entry(frame,textvariable=quantity_var)
        quantity_entry.grid(row=i+1,column=1,padx=10,pady=5)
        self.menu_quantities[item]=quantity_entry

        quantity_entry=ttk.Entry(frame,width=5)
        quantity_entry.grid(row=i,column=1,padx=10,pady=5)
        self.menu_quantities[item]=quantity_entry

    self.currency_var=tk.StringVar()
    ttk.Label(frame,text="Currency:",font=("Arial",12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)

    currency_dropdown=ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=["USD","INR"])
    currency_dropdown.grid(row=len(self.menu_items)+1,column=1,padx=10,pady=5)
    currency_dropdown.current(0)

    #Update prices when currency changes
    self.currency_var.trace("w",self.update_menu_prices)

    order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
    order_button.grid(row=len(self.menu_items)+2,columnspan=2,pady=10)

def update_menu_prices(self,*args):
    currency=self.currency_var.get()
    symbol="₹" if currency=="INR" else "$"
    for item,label in self.menu_labels.iems():
        price=self.menu_items[item]
        label.config(text=f"{item}{{symbol}{price}}:")

def place_order(self):
    total_cost=0
    order_summary="Order Summary:\n"
    currency=self.currency_var.get()
    symbol="₹" if currency=="INR" else "$"
    rate=self.exchange_rate if currency=="INR" else 1
    for item,quantity_entry in self.menu_quantities.items():
        quantity=quantity_entry.get()
        if quantity.isdigit():
        quantity=int(quantity)
        price=self.menu_items[item]*rate
        cost=quantity*rate
        total_cost+=cost
    if total_cost>0:
        order_summary+=f"Total Cost: {symbol}{total_cost:.2f}"
        mmessagebox.showinfo("Order Placed",order_summary) # Show order summary in a message box

else:

# Show error if no items are ordered
messagebox.showerror("Error", "Please order at least one item.")

root = tk.Tk ()

app = RestaurantOrderManagement(root)

root.geometry("800x600") # Set the size of the window

root.mainloop() # Start the GUI loop

