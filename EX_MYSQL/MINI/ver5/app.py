# app.py
import tkinter as tk
from tkinter import ttk
from frame import LoginFrame, MainFrame


class App(tk.Tk):
    """
    전체 프로그램의 루트 윈도우.
    - 로그인 화면(LoginFrame)과 메인 프레임(MainFrame) 전환 관리
    - 공통 스타일(theme) 적용
    - 로그인한 사원 정보 저장 (logged_in_emp 딕셔너리)
    """
    def __init__(self):
        super().__init__()

        self.title("사원 포털 시스템 (데모)")
        self.geometry("840x700")
        self.configure(bg="#e9edf5")
        self.resizable(False, False)
        self._init_style()

        # 로그인한 사원 정보 (LoginFrame에서 DB 로그인 후 채움)
        self.logged_in_emp = {
            "emp_id": "",
            "name": "",
            "dept": "",
            "position": "",
            "basic_salary": 0,
            "annual_leave": 0,
        }

        # 바깥 여백 + 메인 컨테이너
        outer = ttk.Frame(self, style="Outer.TFrame")
        outer.pack(fill="both", expand=True, padx=12, pady=12)

        container = ttk.Frame(outer, style="App.TFrame")
        container.pack(fill="both", expand=True, padx=8, pady=8)

        # 로그인 / 메인 프레임 등록
        self.frames = {}
        for F in (LoginFrame, MainFrame):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # 시작은 로그인 화면
        self.show_frame("LoginFrame")

    def _init_style(self):
        """
        Tkinter ttk 스타일(색상, 폰트 등)을 한 곳에서 정의.
        """
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        BG_MAIN = "#e9edf5"
        BG_CARD = "#ffffff"
        BG_HEADER = "#1f3b57"
        ACCENT = "#2d7ff9"
        ACCENT_DARK = "#1b63c8"
        TEXT_BODY = "#333333"

        style.configure("TFrame", background=BG_CARD)
        style.configure("TLabel", background=BG_CARD, foreground=TEXT_BODY)

        style.configure("Outer.TFrame", background=BG_MAIN)

        style.configure("App.TFrame", background=BG_CARD, relief="flat", borderwidth=0)

        style.configure("Card.TFrame", background=BG_CARD, relief="solid", borderwidth=1)

        style.configure(
            "Header.TFrame", background=BG_HEADER
        )
        style.configure(
            "Header.TLabel",
            background=BG_HEADER,
            foreground="white",
            font=("맑은 고딕", 14, "bold"),
        )

        style.configure(
            "Title.TLabel",
            background=BG_CARD,
            foreground="#111111",
            font=("맑은 고딕", 20, "bold"),
        )

        style.configure(
            "SectionTitle.TLabel",
            background=BG_CARD,
            foreground="#111111",
            font=("맑은 고딕", 16, "bold"),
        )

        style.configure(
            "Body.TLabel",
            background=BG_CARD,
            foreground=TEXT_BODY,
            font=("맑은 고딕", 11),
        )

        style.configure("TButton", font=("맑은 고딕", 10), padding=6)

        style.configure(
            "Menu.TButton",
            font=("맑은 고딕", 11),
            padding=(14, 6),
            borderwidth=0,
            background=BG_CARD,
            foreground="#555555",
        )
        style.map(
            "Menu.TButton",
            background=[("active", "#edf1fb")],
            foreground=[("active", ACCENT)],
        )

        style.configure(
            "Primary.TButton",
            font=("맑은 고딕", 11, "bold"),
            padding=(14, 8),
            background="#f5f6fb",
            foreground="#222222",
            borderwidth=1,
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#e3e7ff")],
            foreground=[("active", ACCENT)],
        )

        style.configure(
            "Accent.TButton",
            font=("맑은 고딕", 11, "bold"),
            padding=(16, 8),
            background=ACCENT,
            foreground="white",
            borderwidth=0,
        )
        style.map("Accent.TButton", background=[("active", ACCENT_DARK)])

    def show_frame(self, name: str):
        """
        화면 전환 함수.
        - name: "LoginFrame" 또는 "MainFrame"
        - MainFrame으로 전환 시 상단 프로필 라벨 갱신
        """
        frame = self.frames[name]
        frame.tkraise()

        if name == "MainFrame" and hasattr(frame, "update_emp_label"):
            frame.update_emp_label()


if __name__ == "__main__":
    app = App()
    app.mainloop()
