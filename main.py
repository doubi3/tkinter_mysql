from PIL import ImageTk, Image
from tkinter import *
from PIL import Image, ImageTk

# mysql components
import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    auth_plugin='mysql_native_password'
)
db_cursor = db_conn.cursor(buffered=True)
root = Tk()
root.title('Staff Database')
root.attributes('-zoomed', True)  # Invoking fullscreen window
# root.iconbitmap('ico_url_here')
# root.geometry("IntxInt")

'''load = Image.open("./images/laptop.jpg")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x = 0, y = 0) '''

# tentative form labels

staffIdLabel = Label(root, text='Staff Id:').place(x=40, y=60)
lnameLabel = Label(root, text='Surname:').place(x=40, y=90)
fnameLabel = Label(root, text='First Name:').place(x=40, y=120)
DobLabel = Label(root, text='Date of Birth:').place(x=40, y=150)
phoneLabel = Label(root, text='Phone Number:').place(x=40, y=180)
emailLabel = Label(root, text='Email Address:').place(x=40, y=210)
AddressLabel = Label(root, text='Address:').place(x=40, y=240)
genderLabel = Label(root, text='Gender:').place(x=40, y=270)
lgaLabel = Label(root, text='L.G.A.:').place(x=40, y=300)
stateLabel = Label(root, text='State:').place(x=40, y=330)

# tentative entry boxes for form lables
staffIdInput = Entry(root, width=50).place(x=150, y=60)
lnameInput = Entry(root, width=50).place(x=150, y=90)
fnameInput = Entry(root, width=50).place(x=150, y=120)
DobInput = Entry(root, width=50).place(x=150, y=150)
phoneInput = Entry(root, width=50).place(x=150, y=180)
emailInput = Entry(root, width=50).place(x=150, y=210)
AddressInput = Entry(root, width=50).place(x=150, y=240)
genderInput = Entry(root, width=50).place(x=150, y=270)
lgaInput = Entry(root, width=50).place(x=150, y=300)
stateInput = Entry(root, width=50).place(x=150, y=330)


# tentative buttons

addBtn = Button(root, text='Add Record').place(x=40, y=360)
delBtn = Button(root, text='Delete Record').place(x=180, y=360)
editBtn = Button(root, text='Update Record').place(x=320, y=360)

db_conn.commit()
db_conn.close()
mainloop()
