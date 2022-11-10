from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class PersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
               
        # Label
        Label(mainFrame, text='Nilai Panjang:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Nilai Lebar:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        # Texbox
        self.txtPanjang = Entry(mainFrame) 
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)

        self.txtLebar = Entry(mainFrame) 
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)

        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)

        # Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)

    def LuasPersegi(self,panjang,lebar):
        luas = panjang * lebar
        return luas        

    def onHitung(self, event=None):
        p = int(self.txtPanjang.get())
        l = int(self.txtLebar.get())
        luas = self.LuasPersegi(p,l)

        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = PersegiPanjang(root, "Program ...")
    root.mainloop() 