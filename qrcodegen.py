from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter import filedialog as fd 
import qrcode
import cv2
import subprocess

def generate_qrcode():
    qrcode_data = str(data_entry.get())
    qrcode_name = str(filename_entry.get())
    if qrcode_name == '':
        showerror(title='Hiba', message='Hiba lépett fel' \
                   '\nA következő lehet ' \
                    'a hiba:\n->Üresen hagyott mező\n' \
                    'A fájlnév helye legyen kitöltve!')
    else:
        if askyesno(title='Megerősítés', message=f'Biztosan készít egy QR kódot a megadott információval?'):
            try:
                qr = qrcode.QRCode(version = 1, box_size = 6, border = 4)
                qr.add_data(qrcode_data)
                qr.make(fit = True)
                name = qrcode_name + '.png'
                qrcode_image = qr.make_image(fill_color = 'black', back_color = 'white')
                qrcode_image.save(name)
                global Image
                Image = PhotoImage(file=f'{name}')
                image_label1.config(image=Image)
                reset_button.config(state=NORMAL, command=reset)
            except:
                showerror(title='Hiba', message='Adjon meg egy valós fájlnevet')
def reset():
    if askyesno(title='Újra', message='Újra kezdi a folyamatot?'):
        image_label1.config(image='')
        reset_button.config(state=DISABLED)
def open_dialog():
    name = fd.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, name)
def detect_qrcode():
    image_file = file_entry.get()
    if image_file == '':
        showerror(title='Hiba', message='Adjon meg egy valódi QR kód képfájlt!')
    else:
        try:
            qr_img = cv2.imread(f'{image_file}')  
            qr_detector = cv2.QRCodeDetector()  
            global qrcode_image
            qrcode_image = PhotoImage(file=f'{image_file}')
            image_label2.config(image=qrcode_image)
            data, pts, st_code = qr_detector.detectAndDecode(qr_img)  
            data_label.config(text=data)
        except:
            showerror(title='Hiba', message='Hiba lépett fel a fájl keresésekor' \
                   '\nA következő lehet ' \
                    'a hiba:\n->Rossz képfájl\n' \
                    'Adjon meg egy valódi képfájlt!')
def kezdooldal_menu_button_press():
    subprocess.Popen(args=['python', r'kezdőoldal.py'])
    ablak.destroy()
def akasztofa_menu_button_press():
    subprocess.Popen(args=['python', r'akasztofa.py'])
    ablak.destroy()
def valuta_menu_button_press():
    subprocess.Popen(args=['python', r'valutavalto.py'])
    ablak.destroy()
def valorant_menu_button_press():
    subprocess.Popen(args=['python', r'valorantguide.py'])
    ablak.destroy()
def qrcode_menu_button_press():
    subprocess.Popen(args=['python', r'qrcodegen.py'])
    ablak.destroy()
def jelszo_menu_button_press():
    subprocess.Popen(args=['python', r'jelszogenerator.py'])
    ablak.destroy()
def naptar_menu_button_press():
      subprocess.Popen(args=['python', r'naptar.py'])
      ablak.destroy()
def iraki_menu_button_press():
    subprocess.Popen(args=['python', r'iraki_ora.py'])
    ablak.destroy()
ablak=Tk()
ablak.geometry("665x400")
ablak.title("QR kód generátor")
menubar = Menu(ablak)
Kezdőoldalmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Kezdőoldal", command=kezdooldal_menu_button_press)
menubar.add_cascade(label="Akasztófa", command=akasztofa_menu_button_press)
menubar.add_cascade(label="Valuta Váltó", command=valuta_menu_button_press)
menubar.add_cascade(label="Valorant Line-up Guide", command=valorant_menu_button_press)
menubar.add_cascade(label="QR kód generátor", command=qrcode_menu_button_press)
menubar.add_cascade(label="Jelszó generátor", command=jelszo_menu_button_press)
menubar.add_cascade(label="Naptár", command=naptar_menu_button_press)
menubar.add_cascade(label="Iraki óra", command=iraki_menu_button_press)
akszto=Menu(menubar, tearoff=0)
valuta=Menu(menubar, tearoff=0)
valolineup=Menu(menubar, tearoff=0)
qrkodgen=Menu(menubar, tearoff=0)
jelszogen=Menu(menubar, tearoff=0)
naptar=Menu(menubar, tearoff=0)
irakiora=Menu(menubar, tearoff=0)
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 11))
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DotumChe', 10))
tab_control = ttk.Notebook(ablak)
first_tab = ttk.Frame(tab_control)
second_tab = ttk.Frame(tab_control)
tab_control.add(first_tab, text='QR kód generátor')
tab_control.add(second_tab, text='QR kód visszafejtő')
tab_control.pack(expand=1, fill="both")
first_canvas = Canvas(first_tab, width=450, height=430)
first_canvas.pack()
second_canvas = Canvas(second_tab, width=450, height=430)
second_canvas.pack()
image_label1 = Label(ablak)
first_canvas.create_window(200, 100, window=image_label1)
qrdata_label = ttk.Label(ablak, text='QR kód adat', style='TLabel')
data_entry = ttk.Entry(ablak, width=50, style='TEntry')
first_canvas.create_window(40, 300, window=qrdata_label)
first_canvas.create_window(250, 300, window=data_entry)
filename_label = ttk.Label(ablak, text='Fájlnév', style='TLabel')
filename_entry = ttk.Entry(width=50, style='TEntry')
first_canvas.create_window(60, 320, window=filename_label)
first_canvas.create_window(250, 320, window=filename_entry)
reset_button = ttk.Button(ablak, text='Újra', style='TButton', state=DISABLED)
generate_button = ttk.Button(ablak, text='QR kód generálás', style='TButton', command=generate_qrcode)
first_canvas.create_window(250, 350, window=reset_button)
first_canvas.create_window(350, 350, window=generate_button)
image_label2 = Label(ablak)
data_label = ttk.Label(ablak)
second_canvas.create_window(20, 130, window=image_label2)
second_canvas.create_window(230, 280, window=data_label)
file_entry = ttk.Entry(ablak, width=55, style='TEntry')
browse_button = ttk.Button(ablak, text='Tallózás', style='TButton', command=open_dialog)
second_canvas.create_window(180, 330, window=file_entry)
second_canvas.create_window(410, 330, window=browse_button)
detect_button = ttk.Button(ablak, text='QR kód visszafejtése', style='TButton')
second_canvas.create_window(78, 360, window=detect_button)
detect_button = ttk.Button(ablak, text='QR kód visszafejtés', style='TButton', command=detect_qrcode)
ablak.config(menu=menubar)
ablak.mainloop()