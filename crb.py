import tkinter as tk
from tkinter import messagebox
import math

def calculate_rcb():
    try:
        # Girişleri al
        D1 = float(entry_d1.get())
        D2 = float(entry_d2.get())
        C = float(entry_c.get())
        PIS = float(entry_pis.get())
        pN = float(entry_pn.get())
        dmet = float(entry_dmet.get())
        
        # Girişlerin kontrolü
        if not (0 <= C <= 100):
            messagebox.showerror("Hata", "Genel Kanser Sellülaritesi (%) 0 ile 100 arasında olmalıdır.")
            return
        if not (0 <= PIS <= 100):
            messagebox.showerror("Hata", "In situ Hastalığa Sahip Kanser Yüzdesi (%) 0 ile 100 arasında olmalıdır.")
            return
        if D1 <= 0 or D2 <= 0:
            messagebox.showerror("Hata", "Tümör çapları pozitif bir değer olmalıdır.")
            return
        if pN < 0:
            messagebox.showerror("Hata", "Pozitif lenf nodu sayısı sıfır veya daha büyük olmalıdır.")
            return
        if dmet <= 0:
            messagebox.showerror("Hata", "En Büyük Metastaz Çapı (mm) pozitif bir değer olmalıdır.")
            return
        
        # Hesaplamalar
        dprim = math.sqrt(D1 * D2)
        finv = (1 - (PIS / 100)) * (C / 100)
        term1 = 1.4 * math.pow((finv * dprim), 0.17)
        term2 = math.pow((4 * (1 - math.pow(0.75, pN)) * dmet), 0.17)
        RCB = term1 + term2

        if RCB < 1.36:
            category = "RCB-I: Minimal Rezidüel Hastalık"
        elif RCB < 3.28:
            category = "RCB-II: Orta Rezidüel Hastalık"
        else:
            category = "RCB-III: Yaygın Rezidüel Hastalık"

        # Sonuçları göster
        result_rcb.config(state='normal')
        result_rcb.delete(0, tk.END)
        result_rcb.insert(0, f"{round(RCB, 3)}")
        result_rcb.config(state='readonly')

        result_category.config(state='normal')
        result_category.delete(0, tk.END)
        result_category.insert(0, category)
        result_category.config(state='readonly')

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        messagebox.showerror("Hata", f"Hesaplamada hata oluştu: {str(e)}")

def reset_form():
    entry_d1.delete(0, tk.END)
    entry_d2.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_pis.delete(0, tk.END)
    entry_pn.delete(0, tk.END)
    entry_dmet.delete(0, tk.END)
    result_rcb.config(state='normal')
    result_rcb.delete(0, tk.END)
    result_rcb.config(state='readonly')
    result_category.config(state='normal')
    result_category.delete(0, tk.END)
    result_category.config(state='readonly')

# Tkinter arayüzü oluştur
window = tk.Tk()
window.title("RCB Hesaplayıcı")
window.geometry("550x500")  # Pencere boyutu

# Başlık
tk.Label(window, text="Rezidüel Kanser Yükü Hesaplayıcı", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Çizgi ekle
tk.Frame(window, height=2, bd=1, relief="sunken").grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=5)

# Primary Tumor Bed Bölümü
tk.Label(window, text="Primer Tümör Yatağı", font=("Arial", 12, "italic")).grid(row=2, column=0, columnspan=2, sticky="w", pady=5)

tk.Label(window, text="Primer Tümör Yatağı Alanı:", anchor="w", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=5)
frame_tumor_area = tk.Frame(window)
frame_tumor_area.grid(row=3, column=1)
entry_d1 = tk.Entry(frame_tumor_area, width=8, font=("Arial", 10), justify="center")
entry_d1.grid(row=0, column=0)
tk.Label(frame_tumor_area, text="(mm) X", font=("Arial", 10)).grid(row=0, column=1)
entry_d2 = tk.Entry(frame_tumor_area, width=8, font=("Arial", 10), justify="center")
entry_d2.grid(row=0, column=2)
tk.Label(frame_tumor_area, text="(mm)", font=("Arial", 10)).grid(row=0, column=3)

tk.Label(window, text="Genel Kanser Sellülaritesi (%):", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=5)
entry_c = tk.Entry(window, font=("Arial", 10), justify="center")
entry_c.grid(row=4, column=1, padx=10, pady=5)

tk.Label(window, text="In situ Hastalığa Sahip Kanser Yüzdesi (%):", font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=5)
entry_pis = tk.Entry(window, font=("Arial", 10), justify="center")
entry_pis.grid(row=5, column=1, padx=10, pady=5)

# Çizgi ekle
tk.Frame(window, height=2, bd=1, relief="sunken").grid(row=6, column=0, columnspan=2, sticky="we", padx=10, pady=5)

# Lymph Nodes Bölümü
tk.Label(window, text="Lenf Nodları", font=("Arial", 12, "italic")).grid(row=7, column=0, columnspan=2, sticky="w", pady=5)

tk.Label(window, text="Pozitif Lenf Nodu Sayısı:", font=("Arial", 10)).grid(row=8, column=0, padx=10, pady=5)
entry_pn = tk.Entry(window, font=("Arial", 10), justify="center")
entry_pn.grid(row=8, column=1, padx=10, pady=5)

tk.Label(window, text="En Büyük Metastaz Çapı (mm):", font=("Arial", 10)).grid(row=9, column=0, padx=10, pady=5)
entry_dmet = tk.Entry(window, font=("Arial", 10), justify="center")
entry_dmet.grid(row=9, column=1, padx=10, pady=5)

# Çizgi ekle
tk.Frame(window, height=2, bd=1, relief="sunken").grid(row=10, column=0, columnspan=2, sticky="we", padx=10, pady=5)

# Sonuçlar ve düğmeler
result_frame = tk.Frame(window)
result_frame.grid(row=11, column=0, columnspan=2, pady=10)

tk.Label(result_frame, text="Rezidüel Kanser Yükü:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5)
result_rcb = tk.Entry(result_frame, state='readonly', width=20, font=("Arial", 10), justify="center")
result_rcb.grid(row=0, column=1, padx=10, pady=5)

tk.Label(result_frame, text="Rezidüel Kanser Yükü Sınıfı:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5)
result_category = tk.Entry(result_frame, state='readonly', width=30, font=("Arial", 10), justify="center")
result_category.grid(row=1, column=1, padx=10, pady=5)

# Butonlar
button_frame = tk.Frame(window)
button_frame.grid(row=12, column=0, columnspan=2, pady=10)

reset_button = tk.Button(button_frame, text="Sıfırla", command=reset_form, bg="#FF5733", fg="white", width=10, font=("Arial", 10))
reset_button.grid(row=0, column=0, padx=5)

calculate_button = tk.Button(button_frame, text="Hesapla", command=calculate_rcb, bg="#007BFF", fg="white", width=10, font=("Arial", 10))
calculate_button.grid(row=0, column=1, padx=5)

# Tkinter ana döngüsü
window.mainloop()
