"""
เครื่องคิดเลขสีแดงสวยๆ (Red Calculator)
สร้างด้วย Python + tkinter (ไม่ต้องติดตั้งไลบรารีเพิ่มเติม)

วิธีรัน:
    python red_calculator.py
"""

import tkinter as tk

# ---------------------------------------------------------------
# ชุดสี (Red Theme)
# ---------------------------------------------------------------
COLOR_BG = "#7a0c0c"          # แดงเข้ม - พื้นหลังหลัก
COLOR_DISPLAY_BG = "#4a0505"  # แดงเข้มมาก - พื้นหลังจอแสดงผล
COLOR_DISPLAY_FG = "#ffffff"  # ขาว - ตัวเลขบนจอ
COLOR_NUM_BG = "#c62828"      # แดงสด - ปุ่มตัวเลข
COLOR_NUM_FG = "#ffffff"
COLOR_NUM_ACTIVE = "#e53935"  # แดงสว่างขึ้นตอนกด
COLOR_OP_BG = "#ffb300"       # ส้ม/ทอง - ปุ่มคำนวณ (ตัดกับแดง)
COLOR_OP_FG = "#4a0505"
COLOR_OP_ACTIVE = "#ffca28"
COLOR_EQUAL_BG = "#2e7d32"    # เขียว - ปุ่ม =
COLOR_EQUAL_FG = "#ffffff"
COLOR_EQUAL_ACTIVE = "#43a047"
COLOR_CLEAR_BG = "#424242"    # เทาเข้ม - ปุ่ม C / ⌫
COLOR_CLEAR_FG = "#ffffff"
COLOR_CLEAR_ACTIVE = "#616161"

FONT_DISPLAY = ("Segoe UI", 32, "bold")
FONT_BTN = ("Segoe UI", 18, "bold")


class RedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("เครื่องคิดเลขสีแดง 🔴")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg=COLOR_BG)

        self.expression = ""
        self._build_display()
        self._build_buttons()

    # -------------------------------------------------------
    def _build_display(self):
        frame = tk.Frame(self, bg=COLOR_DISPLAY_BG, bd=0)
        frame.pack(fill="both", padx=15, pady=(20, 10))

        self.display_var = tk.StringVar(value="0")
        entry = tk.Label(
            frame,
            textvariable=self.display_var,
            anchor="e",
            bg=COLOR_DISPLAY_BG,
            fg=COLOR_DISPLAY_FG,
            font=FONT_DISPLAY,
            padx=15,
            pady=25,
        )
        entry.pack(fill="both")

    # -------------------------------------------------------
    def _build_buttons(self):
        btn_frame = tk.Frame(self, bg=COLOR_BG)
        btn_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        buttons = [
            ("C", 0, 0, COLOR_CLEAR_BG, COLOR_CLEAR_FG, COLOR_CLEAR_ACTIVE, self.clear),
            ("⌫", 0, 1, COLOR_CLEAR_BG, COLOR_CLEAR_FG, COLOR_CLEAR_ACTIVE, self.backspace),
            ("%", 0, 2, COLOR_OP_BG, COLOR_OP_FG, COLOR_OP_ACTIVE, lambda: self.add("%")),
            ("÷", 0, 3, COLOR_OP_BG, COLOR_OP_FG, COLOR_OP_ACTIVE, lambda: self.add("/")),

            ("7", 1, 0, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("7")),
            ("8", 1, 1, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("8")),
            ("9", 1, 2, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("9")),
            ("×", 1, 3, COLOR_OP_BG, COLOR_OP_FG, COLOR_OP_ACTIVE, lambda: self.add("*")),

            ("4", 2, 0, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("4")),
            ("5", 2, 1, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("5")),
            ("6", 2, 2, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("6")),
            ("−", 2, 3, COLOR_OP_BG, COLOR_OP_FG, COLOR_OP_ACTIVE, lambda: self.add("-")),

            ("1", 3, 0, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("1")),
            ("2", 3, 1, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("2")),
            ("3", 3, 2, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("3")),
            ("+", 3, 3, COLOR_OP_BG, COLOR_OP_FG, COLOR_OP_ACTIVE, lambda: self.add("+")),

            ("0", 4, 0, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add("0")),
            (".", 4, 1, COLOR_NUM_BG, COLOR_NUM_FG, COLOR_NUM_ACTIVE, lambda: self.add(".")),
            ("=", 4, 2, COLOR_EQUAL_BG, COLOR_EQUAL_FG, COLOR_EQUAL_ACTIVE, self.calculate),
        ]

        for (text, row, col, bg, fg, active_bg, cmd) in buttons:
            colspan = 1
            if text == "=":
                colspan = 2  # ให้ปุ่ม = กว้างขึ้นเล็กน้อย

            btn = tk.Button(
                btn_frame,
                text=text,
                font=FONT_BTN,
                bg=bg,
                fg=fg,
                activebackground=active_bg,
                activeforeground=fg,
                bd=0,
                relief="flat",
                command=cmd,
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                sticky="nsew", padx=6, pady=6, ipady=8
            )

    # -------------------------------------------------------
    def add(self, char):
        # แปลงสัญลักษณ์การคูณ/หารให้อ่านง่ายบนจอ แต่เก็บของจริงไว้คำนวณ
        self.expression += char
        display_text = (
            self.expression.replace("*", "×").replace("/", "÷")
        )
        self.display_var.set(display_text if display_text else "0")

    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        display_text = self.expression.replace("*", "×").replace("/", "÷")
        self.display_var.set(display_text if display_text else "0")

    def calculate(self):
        try:
            # แทน % ด้วยการหาร 100 แบบง่ายๆ
            expr = self.expression.replace("%", "/100")
            result = eval(expr, {"__builtins__": {}}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except Exception:
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    app = RedCalculator()
    app.mainloop()