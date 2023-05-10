import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import git as gitpy
import os

class MainApplication:
    def __init__(self, master):
        self.master = master
        master.geometry("500x200")
        master.iconbitmap('animlogo.ico')


        # Sekme widget'ını oluştur
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both')

        # İlk sekme
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Pull-Push")
        
        # İlk sekme paneli
        self.label_box2 = tk.Frame(self.tab1)
        self.label_box2.pack(padx=10, pady=10, fill='x')
        ttk.Button(self.label_box2, text="Pull", command=self.pull).pack()
        ttk.Button(self.label_box2, text="Push", command=self.push).pack()

        


        # İkinci sekme
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Kurulum")

        # İkinci sekme paneli
        self.label_box = tk.Frame(self.tab2)
        self.label_box.pack(padx=10, pady=10, fill='x')

        self.label = ttk.Label(self.label_box, text="Git Kaynağı Seç").pack(side="left", anchor='w')
        self.folder_button = ttk.Button(self.label_box, text="Klasör Seç", command=self.select_folder)
        self.folder_button.pack(side='left', padx=10)

        # Klasör adı etiketi
        self.foldername_labelgit = ttk.Label(self.label_box, text="Seçilmedi")
        self.foldername_labelgit.pack(pady=10)

        # İkinci sekme paneli
        self.label_box = tk.Frame(self.tab2)
        self.label_box.pack(padx=10, pady=10, fill='x')

        self.label = ttk.Label(self.label_box, text="Kurulacak Klasör Seç").pack(side="left", anchor='w')
        self.folder_button = ttk.Button(self.label_box, text="Klasör Seç", command=self.select_folder2)
        self.folder_button.pack(side='left', padx=10)

        # Klasör adı etiketi
        self.foldername_label = ttk.Label(self.label_box, text="Seçilmedi")
        self.foldername_label.pack(pady=10)

        ttk.Button(self.tab2, text="Kur!", command=self.kurulum).pack()
        #self.progressbar = ttk.Progressbar(self.tab2, orient=tk.HORIZONTAL, length=100, mode="indeterminate")
    
    def pull(self):
        #eklenecek
        print("pull")
    def push(self):
        #eklenecek
        print("push")

    def select_folder(self):
        foldername = filedialog.askdirectory()
        self.foldername_labelgit.configure(text=foldername)
    def select_folder2(self):
        messagebox.showinfo("Uyarı", "Boş bir klasör seçmelisin!")
        foldername = filedialog.askdirectory()
        self.foldername_label.configure(text=foldername)

    def kurulum(self):
        
        if self.foldername_labelgit.cget("text") == "Seçilmedi" or self.foldername_label.cget("text") == "Seçilmedi":
            messagebox.showerror("Hata", "Lütfen klasörleri seçin!")
            return
        folder = self.foldername_label.cget("text")
        git = self.foldername_labelgit.cget("text")
        folder_name = os.path.basename(self.foldername_labelgit.cget("text"))
        window = tk.Toplevel(root)
        window.title("Yeni Pencere")
        window.title("Yükleniyor...")
        window.geometry("400x50")
        window.iconbitmap('animlogo.ico')
        ttk.Label(window, text="Lütfen bekle..\nKurulum boyunca uygulamayı kapatma kendisi kapanacak.").pack()
        window.lift()
        window.attributes("-topmost", True)
        messagebox.showwarning("Uyarı", "Kurulum başladığında biraz zaman alabilir... ")
        try:
            gitpy.Repo.init(f"{folder}/{folder_name}")
            repo = gitpy.Repo(f"{folder}/{folder_name}")
            remote = repo.create_remote('anim', git)
            remote.fetch()
            remote.pull(remote.refs[0].remote_head)
            window.destroy()
            messagebox.showinfo("Uyarı", "Kurulum başarıyla tamamlandı!")
        except Exception as error:
            window.destroy()
            messagebox.showerror("Hata", f"Kurulum ne yazikki tamamlanamadı!\n{error}")


        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Anim-Git")
    app = MainApplication(root)
    root.mainloop()
