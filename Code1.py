import tkinter as tk
from tkinter import messagebox

def button_click(item):
    """ฟังก์ชันเมื่อกดปุ่มตัวเลขหรือเครื่องหมาย"""
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    """ฟังก์ชันเคลียร์หน้าจอ"""
    display_var.set("")

def button_equal():
    """ฟังก์ชันคำนวณผลลัพธ์"""
    try:
        # ใช้ eval เพื่อคำนวณประโยคสัญลักษณ์ทางคณิตศาสตร์
        result = str(eval(display_var.get()))
        display_var.set(result)
    except ZeroDivisionError:
        messagebox.showerror("ข้อผิดพลาด", "ไม่สามารถหารด้วยศูนย์ได้")
        display_var.set("")
    except Exception:
        messagebox.showerror("ข้อผิดพลาด", "รูปแบบการคำนวณไม่ถูกต้อง")
        display_var.set("")

# 1. ตั้งค่าหน้าต่างหลัก (Main Window)
root = tk.Tk()
root.title("เครื่องคิดเลขสีแดง (Red Calculator)")
root.geometry("340x460")
root.configure(bg="#8B0000") # พื้นหลังสีแดงเข้ม (Dark Red)
root.resizable(False, False) # ล็อกขนาดหน้าต่าง

display_var = tk.StringVar()

# 2. สร้างหน้าจอแสดงผล
display = tk.Entry(
    root, 
    textvariable=display_var, 
    font=('Helvetica', 28, 'bold'), 
    bg="#FFE4E1",      # สีชมพูอ่อนๆ ให้เข้ากับธีมแดง
    fg="#8B0000",      # ตัวหนังสือสีแดงเข้ม
    bd=10, 
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=15, pady=20)

# 3. กำหนดชุดสีและฟอนต์สำหรับปุ่ม
btn_font = ('Helvetica', 16, 'bold')
btn_bg_num = "#FF4D4D"   # สีแดงสว่าง สำหรับตัวเลข
btn_bg_op = "#CC0000"    # สีแดงเข้มปานกลาง สำหรับเครื่องหมาย (+, -, *, /)
btn_bg_sp = "#660000"    # สีแดงเข้มมาก สำหรับปุ่ม C และ =
btn_fg = "white"         # ตัวอักษรสีขาว

# 4. สร้างปุ่มต่างๆ 
buttons = [
    ('7', 1, 0, btn_bg_num), ('8', 1, 1, btn_bg_num), ('9', 1, 2, btn_bg_num), ('/', 1, 3, btn_bg_op),
    ('4', 2, 0, btn_bg_num), ('5', 2, 1, btn_bg_num), ('6', 2, 2, btn_bg_num), ('*', 2, 3, btn_bg_op),
    ('1', 3, 0, btn_bg_num), ('2', 3, 1, btn_bg_num), ('3', 3, 2, btn_bg_num), ('-', 3, 3, btn_bg_op),
    ('C', 4, 0, btn_bg_sp),  ('0', 4, 1, btn_bg_num), ('=', 4, 2, btn_bg_sp),  ('+', 4, 3, btn_bg_op)
]

# 5. นำปุ่มไปจัดเรียงบนหน้าจอ
for (text, row, col, color) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=btn_font, bg=color, fg=btn_fg, width=5, height=2, 
                        activebackground="#990000", activeforeground="white", command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=btn_font, bg=color, fg=btn_fg, width=5, height=2, 
                        activebackground="#990000", activeforeground="white", command=button_clear)
    else:
        btn = tk.Button(root, text=text, font=btn_font, bg=color, fg=btn_fg, width=5, height=2, 
                        activebackground="#FF9999", activeforeground="white", command=lambda t=text: button_click(t))
    
    # วางปุ่มลงใน Grid พร้อมเว้นระยะห่างให้สวยงาม
    btn.grid(row=row, column=col, padx=5, pady=5)

# เริ่มการทำงานของโปรแกรม
root.mainloop()