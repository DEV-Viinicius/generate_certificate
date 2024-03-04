import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from backend import generate_certificates

class CertificadoGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Certificados")
        self.root.geometry("400x200")

        self.btn_select_excel = tk.Button(root, text="Selecionar Planilha", command=self.select_excel)
        self.btn_select_excel.pack(side='left', padx=10, pady=10)
        
        self.btn_generate_certificates = tk.Button(root, text="Gerar Certificados", command=self.generate_certificates)
        self.btn_generate_certificates.pack(side='left', padx=10, pady=80)

    def select_excel(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        messagebox.showinfo("Planilha Selecionada", f"Planilha selecionada: {self.filepath}")

    def generate_certificates(self):
        if not hasattr(self, 'filepath') or not self.filepath:
            messagebox.showerror("Erro", "Selecione a planilha primeiro!")
            return

        success, message = generate_certificates(self.filepath)
        if success:
            messagebox.showinfo("Concluído", message)
        else:
            messagebox.showerror("Erro", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CertificadoGeneratorGUI(root)
    root.mainloop()
