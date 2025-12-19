import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("사원 포털 시스템 (데모)")
        self.geometry("1000x650")
        self.minsize(900, 600)

        # 전체 배경색
        self.configure(bg="#f2f4f7")
        self._init_style()

        # 로그인한 사원 정보 (임시)
        self.logged_in_emp = {
            "emp_id": "2025001",
            "name": "홍길동",
            "dept": "1234",
        }
    

        container = ttk.Frame(self, style="App.TFrame")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        self.frames = {}
        for F in (LoginFrame, MainFrame):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def _init_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        # 기본 프레임/카드/헤더 스타일
        style.configure("App.TFrame", background="#f2f4f7")
        style.configure("Card.TFrame", background="#ffffff", relief="solid", borderwidth=1)
        style.configure("Header.TFrame", background="#1f3b57")

        # 라벨 스타일
        style.configure("Header.TLabel", background="#1f3b57", foreground="white",
                        font=("맑은 고딕", 14, "bold"))
        style.configure("Title.TLabel", background="#ffffff", font=("맑은 고딕", 20, "bold"))
        style.configure("SectionTitle.TLabel", background="#ffffff", font=("맑은 고딕", 16, "bold"))
        style.configure("Body.TLabel", background="#ffffff", font=("맑은 고딕", 11))

        # 버튼 스타일
        style.configure("Menu.TButton", font=("맑은 고딕", 11), padding=6)
        style.configure("Primary.TButton", font=("맑은 고딕", 11, "bold"), padding=8)
        style.configure("Accent.TButton", font=("맑은 고딕", 11, "bold"),
                        padding=8, foreground="white", background="#2d7ff9")
        style.map("Accent.TButton", background=[("active", "#1b63c8")])

    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()


# 1) 로그인 화면
class LoginFrame(ttk.Frame):
    def __init__(self, parent, controller: App):
        super().__init__(parent, style="App.TFrame")
        self.controller = controller

        # 중앙 카드
        card = ttk.Frame(self, style="Card.TFrame")
        card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=320)

        title = ttk.Label(card, text="사원 포털 로그인", style="Title.TLabel")
        title.pack(pady=(25, 10))

        subtitle = ttk.Label(card, text="사번과 비밀번호를 입력해 주세요.", style="Body.TLabel")
        subtitle.pack(pady=(0, 20))

        form = ttk.Frame(card, style="Card.TFrame")
        form.pack(pady=5, padx=40, fill="x")

        ttk.Label(form, text="사번(홍길동 입력)", style="Body.TLabel").grid(row=0, column=0,
                                                          padx=5, pady=5, sticky="w")
        self.entry_emp = ttk.Entry(form)
        self.entry_emp.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew")

        ttk.Label(form, text="비밀번호(1234 입력)", style="Body.TLabel").grid(row=2, column=0,
                                                              padx=5, pady=5, sticky="w")
        self.entry_pw = ttk.Entry(form, show="*")
        self.entry_pw.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")

        form.columnconfigure(0, weight=1)

        self.msg = ttk.Label(card, text="", foreground="red", style="Body.TLabel")
        self.msg.pack(pady=2)

        btn = ttk.Button(card, text="로그인", style="Primary.TButton",
                         command=self.fake_login)
        btn.pack(pady=(10, 0))

    def fake_login(self):
        emp = self.entry_emp.get().strip()
        pw = self.entry_pw.get().strip()

        if emp and pw:
            # TODO: 실제 DB 인증으로 교체
            self.controller.logged_in_emp["emp_id"] = emp
            self.controller.logged_in_emp["name"] = "홍길동"
            self.controller.logged_in_emp["dept"] = "개발팀"
            self.controller.show_frame("MainFrame")
        else:
            self.msg.config(text="사번과 비밀번호를 모두 입력해 주세요.")


# 2) 메인 프레임 (홈/회사개요/개인)
class MainFrame(ttk.Frame):
    def __init__(self, parent, controller: App):
        super().__init__(parent, style="App.TFrame")
        self.controller = controller

        # 상단 헤더
        header = ttk.Frame(self, style="Header.TFrame", height=60)
        header.pack(fill="x", side="top")

        title = ttk.Label(header, text="♥♥♥♥♥", style="Header.TLabel")
        title.pack(side="left", padx=20)

        self.emp_label = ttk.Label(header, text="", style="Header.TLabel")
        self.emp_label.pack(side="right", padx=20)

        # 상단 메뉴 바
        menu_bar = ttk.Frame(self, style="App.TFrame")
        menu_bar.pack(fill="x", pady=(10, 5))

        self.btn_home = ttk.Button(menu_bar, text="홈", style="Menu.TButton",
                                   command=lambda: self.show_section("home"))
        self.btn_home.pack(side="left", padx=5)

        self.btn_company = ttk.Button(menu_bar, text="회사 개요", style="Menu.TButton",
                                      command=lambda: self.show_section("company"))
        self.btn_company.pack(side="left", padx=5)

        self.btn_personal = ttk.Button(menu_bar, text="개인", style="Menu.TButton",
                                       command=lambda: self.show_section("personal_menu"))
        self.btn_personal.pack(side="left", padx=5)

        # 메인 콘텐츠 카드
        self.content_card = ttk.Frame(self, style="Card.TFrame")
        self.content_card.pack(fill="both", expand=True, pady=(5, 0))

        self.content_card.grid_rowconfigure(0, weight=1)
        self.content_card.grid_columnconfigure(0, weight=1)

        # 섹션들
        self.sections = {
            "home": HomeSection(self.content_card, self),
            "company": CompanySection(self.content_card, self),
            "personal_menu": PersonalMenuSection(self.content_card, self),
            "personal_info": PersonalInfoSection(self.content_card, self),
            "leave_info": LeaveInfoSection(self.content_card, self),
            "attendance": AttendanceSection(self.content_card, self),
            "payslip": PayslipSection(self.content_card, self),
        }

        for name, frame in self.sections.items():
            frame.grid(row=0, column=0, sticky="nsew")

        self.update_emp_label()
        self.show_section("home")

    def update_emp_label(self):
        info = self.controller.logged_in_emp
        self.emp_label.config(
            text=f"{info.get('dept','')} {info.get('name','')}님"
        )

    def show_section(self, name: str):
        frame = self.sections[name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()


# --- 섹션들 --- #

class HomeSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        label = ttk.Label(self, text="홈", style="SectionTitle.TLabel")
        label.pack(anchor="w", padx=25, pady=(25, 10))

        desc = ttk.Label(
            self,
            text="좌측 상단 메뉴에서 [회사 개요] 또는 [개인] 버튼을 눌러 기능을 선택하세요.",
            style="Body.TLabel",
        )
        desc.pack(anchor="w", padx=25, pady=5)


class CompanySection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="회사 개요", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 10))

        info_text = (
            "회사명: OO주식회사\n"
            "설립연도: 20XX년\n"
            "주요 사업: 예) 소프트웨어 개발, 솔루션 제공 등\n"
            "주소: 서울특별시 ○○구 ○○로 ○○\n"
            "\n"
            "※ 실제 회사 소개 내용은 추후 채워 넣을 예정입니다."
        )
        lbl = ttk.Label(self, text=info_text, style="Body.TLabel", justify="left")
        lbl.pack(anchor="w", padx=25, pady=5)


class PersonalMenuSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="개인 메뉴", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 20))

        btn_frame = ttk.Frame(self, style="Card.TFrame")
        btn_frame.pack(padx=25, pady=10, anchor="w")

        ttk.Button(
            btn_frame,
            text="개인 정보 변경",
            style="Primary.TButton",
            width=22,
            command=lambda: main.show_section("personal_info")
        ).grid(row=0, column=0, padx=10, pady=8)

        ttk.Button(
            btn_frame,
            text="사원별 휴가정보",
            style="Primary.TButton",
            width=22,
            command=lambda: main.show_section("leave_info")
        ).grid(row=0, column=1, padx=10, pady=8)

        ttk.Button(
            btn_frame,
            text="근태 기록",
            style="Primary.TButton",
            width=22,
            command=lambda: main.show_section("attendance")
        ).grid(row=1, column=0, padx=10, pady=8)

        ttk.Button(
            btn_frame,
            text="급여 명세서 조회",
            style="Primary.TButton",
            width=22,
            command=lambda: main.show_section("payslip")
        ).grid(row=1, column=1, padx=10, pady=8)


class PersonalInfoSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="개인 정보 변경", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 10))

        form = ttk.LabelFrame(self, text="정보 수정", padding=15)
        form.pack(padx=25, pady=10, fill="x")

        ttk.Label(form, text="새 비밀번호").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_pw = ttk.Entry(form, show="*")
        self.entry_pw.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(form, text="주소").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_addr = ttk.Entry(form)
        self.entry_addr.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(form, text="이메일").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = ttk.Entry(form)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(form, text="계좌번호").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_account = ttk.Entry(form)
        self.entry_account.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        form.columnconfigure(1, weight=1)

        btn_row = ttk.Frame(self, style="Card.TFrame")
        btn_row.pack(padx=25, pady=10, anchor="w")

        ttk.Button(btn_row, text="저장", style="Accent.TButton",
                   command=self.save_info).pack(side="left", padx=5)
        ttk.Button(btn_row, text="개인 메뉴로", style="Menu.TButton",
                   command=lambda: main.show_section("personal_menu")).pack(side="left", padx=5)

        self.msg = ttk.Label(self, text="", style="Body.TLabel", foreground="green")
        self.msg.pack(anchor="w", padx=25, pady=5)

    def save_info(self):
        # TODO: 실제 DB 저장 로직
        self.msg.config(text="(예시) 변경 내용이 저장되었습니다.")

    def on_show(self):
        self.msg.config(text="")
        # TODO: 기존 정보 불러와서 Entry에 세팅


class LeaveInfoSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="사원별 휴가정보", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 10))

        self.info_label = ttk.Label(
            self,
            text="사용 연차: 5일\n잔여 연차: 10일\n\n(예시 텍스트, 실제 데이터는 나중에 연동)",
            style="Body.TLabel",
            justify="left"
        )
        self.info_label.pack(anchor="w", padx=25, pady=5)

        btn_row = ttk.Frame(self, style="Card.TFrame")
        btn_row.pack(anchor="w", padx=25, pady=10)
        ttk.Button(btn_row, text="개인 메뉴로", style="Menu.TButton",
                   command=lambda: main.show_section("personal_menu")).pack(side="left")

    def on_show(self):
        # TODO: 실제 DB 연차 정보 조회
        pass


class AttendanceSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="근태 기록", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 10))

        # TODO: 기간 선택 / 조회 버튼 / Treeview 구성
        dummy = ttk.Label(self,
                          text="여기에 출퇴근 기록(근태 내역) 테이블이 표시될 예정입니다.",
                          style="Body.TLabel")
        dummy.pack(anchor="w", padx=25, pady=5)

        btn_row = ttk.Frame(self, style="Card.TFrame")
        btn_row.pack(anchor="w", padx=25, pady=10)
        ttk.Button(btn_row, text="개인 메뉴로", style="Menu.TButton",
                   command=lambda: main.show_section("personal_menu")).pack(side="left")

    def on_show(self):
        # TODO: 근태 데이터 조회 및 표시
        pass


class PayslipSection(ttk.Frame):
    def __init__(self, parent, main: MainFrame):
        super().__init__(parent, style="Card.TFrame")
        self.main = main

        title = ttk.Label(self, text="급여 명세서 조회", style="SectionTitle.TLabel")
        title.pack(anchor="w", padx=25, pady=(25, 10))

        # TODO: 급여월 선택, 조회 버튼, 명세 내역, 합계 표시 등
        dummy = ttk.Label(self, text="여기에 급여 명세서 조회 화면이 들어갑니다.",
                          style="Body.TLabel")
        dummy.pack(anchor="w", padx=25, pady=5)

        btn_row = ttk.Frame(self, style="Card.TFrame")
        btn_row.pack(anchor="w", padx=25, pady=10)
        ttk.Button(btn_row, text="개인 메뉴로", style="Menu.TButton",
                   command=lambda: main.show_section("personal_menu")).pack(side="left")

    def on_show(self):
        # TODO: 급여 데이터 조회 및 표시
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
