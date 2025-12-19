# frame.py
from tkinter import ttk
from sections import (
    HomeSection,
    CompanySection,
    PersonalMenuSection,
    PersonalInfoSection,
    AttendanceSection,
    PayslipSection,
)
from function import get_connection, TABLE_EMP


# ================== 로그인 화면 ==================
class LoginFrame(ttk.Frame):
    """
    로그인 화면 프레임.
    - 사번(emp_id), 비밀번호(emp_pw)를 DB에서 검증.
    - 성공 시 App.logged_in_emp에 정보 저장 후 MainFrame으로 전환.
    """
    def __init__(self, parent, controller):
        super().__init__(parent, style="App.TFrame")
        self.controller = controller

        wrapper = ttk.Frame(self, style="App.TFrame")
        wrapper.pack(fill="both", expand=True)

        # 중앙 카드
        card = ttk.Frame(wrapper, style="Card.TFrame")
        card.place(relx=0.5, rely=0.5, anchor="center", width=430, height=340)

        ttk.Label(card, text="사원 포털 로그인",
                  style="Title.TLabel").pack(pady=(24, 4))
        ttk.Label(card, text="사번과 비밀번호를 입력해 주세요.",
                  style="Body.TLabel").pack(pady=(0, 18))

        form = ttk.Frame(card, style="App.TFrame")
        form.pack(pady=5, padx=40, fill="x")

        ttk.Label(form, text="사번(ID)", style="Body.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 2)
        )
        self.emp_entry = ttk.Entry(form)
        self.emp_entry.grid(row=1, column=0, sticky="ew", pady=(0, 8))

        ttk.Label(form, text="비밀번호(PW)", style="Body.TLabel").grid(
            row=2, column=0, sticky="w", pady=(0, 2)
        )
        self.pw_entry = ttk.Entry(form, show="*")
        self.pw_entry.grid(row=3, column=0, sticky="ew", pady=(0, 8))

        form.columnconfigure(0, weight=1)

        self.msg = ttk.Label(card, text="", foreground="red", style="Body.TLabel")
        self.msg.pack(pady=(4, 2))

        ttk.Button(
            card,
            text="로그인",
            style="Accent.TButton",
            command=self.login_db,
        ).pack(pady=(8, 0))

    def login_db(self):
        """
        DB를 이용하여 로그인 검증.
        - 성공 시: App.logged_in_emp 채우고 MainFrame으로 이동
        - 실패 시: 에러 메시지 표시
        """
        emp = self.emp_entry.get().strip()
        pw = self.pw_entry.get().strip()

        if not emp or not pw:
            self.msg.config(text="사번과 비밀번호를 모두 입력해 주세요.")
            return

        try:
            conn = get_connection()
        except Exception as e:
            print("DB 연결 오류:", e)
            self.msg.config(text="DB 연결 오류가 발생했습니다.")
            return

        row = None
        try:
            with conn.cursor() as cur:
                sql = f"""
                    SELECT emp_id, emp_pw, name, position,
                           basic_salary, annual_leave, department
                    FROM {TABLE_EMP}
                    WHERE emp_id = %s AND emp_pw = %s
                """
                cur.execute(sql, (emp, pw))
                row = cur.fetchone()
        except Exception as e:
            print("쿼리 실행 오류:", e)
            self.msg.config(text="로그인 처리 중 오류가 발생했습니다.")
        finally:
            conn.close()

        if row:
            # 로그인 성공 → App 인스턴스에 사원 정보 저장
            self.controller.logged_in_emp = {
                "emp_id": row["emp_id"],
                "name": row["name"],
                "dept": row["department"],
                "position": row["position"],
                "basic_salary": row["basic_salary"],
                "annual_leave": row["annual_leave"],
            }
            self.controller.show_frame("MainFrame")
        else:
            self.msg.config(text="ID 또는 비밀번호가 올바르지 않습니다.")

    def reset_fields(self):
        """
        로그아웃 시 로그인 폼 초기화용.
        """
        self.emp_entry.delete(0, "end")
        self.pw_entry.delete(0, "end")
        self.msg.config(text="")


# ================== 메인 프레임 ==================
class MainFrame(ttk.Frame):
    """
    상단 헤더 + 상단 메뉴 + 콘텐츠 영역(섹션들)을 가진 메인 화면.
    - Home / 회사 개요 / 개인 메뉴 / 근태 / 급여명세서 등 섹션 전환.
    """
    def __init__(self, parent, controller):
        super().__init__(parent, style="App.TFrame")
        self.controller = controller

        wrapper = ttk.Frame(self, style="App.TFrame")
        wrapper.pack(fill="both", expand=True)

        # --- 헤더 영역 ---
        header = ttk.Frame(wrapper, style="Header.TFrame", height=64)
        header.pack(fill="x", side="top")

        title_box = ttk.Frame(header, style="Header.TFrame")
        title_box.pack(side="left", padx=20)

        ttk.Label(title_box, text="SL 사원 포털",
                  style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            title_box,
            text="Smart Lamp · Smart Life",
            style="Header.TLabel",
            font=("맑은 고딕", 9),
        ).pack(anchor="w", pady=(2, 0))

        self.emp_label = ttk.Label(header, text="", style="Header.TLabel")
        self.emp_label.pack(side="right", padx=20)

        # --- 상단 메뉴 ---
        top_box = ttk.Frame(wrapper, style="App.TFrame")
        top_box.pack(fill="x")

        menu_bar = ttk.Frame(top_box, style="App.TFrame")
        menu_bar.pack(fill="x", pady=(10, 0), padx=16)

        ttk.Button(
            menu_bar,
            text="홈",
            style="Menu.TButton",
            command=lambda: self.show_section("home"),
        ).pack(side="left", padx=(0, 6))

        ttk.Button(
            menu_bar,
            text="회사 개요",
            style="Menu.TButton",
            command=lambda: self.show_section("company"),
        ).pack(side="left", padx=6)

        ttk.Button(
            menu_bar,
            text="개인",
            style="Menu.TButton",
            command=lambda: self.show_section("personal_menu"),
        ).pack(side="left", padx=6)

        ttk.Separator(wrapper, orient="horizontal").pack(
            fill="x", padx=16, pady=(6, 4)
        )

        # --- 콘텐츠 영역 ---
        self.content = ttk.Frame(wrapper, style="App.TFrame")
        self.content.pack(fill="both", expand=True, padx=16, pady=(0, 10))

        # 섹션 등록
        self.sections = {
            "home": HomeSection(self.content, self),
            "company": CompanySection(self.content, self),
            "personal_menu": PersonalMenuSection(self.content, self),
            "personal_info": PersonalInfoSection(self.content, self),
            "attendance": AttendanceSection(self.content, self),
            "payslip": PayslipSection(self.content, self),
        }

        for sec in self.sections.values():
            sec.grid(row=0, column=0, sticky="nsew")

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.update_emp_label()
        self.show_section("home")

    def update_emp_label(self):
        """
        헤더 우측 상단에 '부서 이름님' 형식으로 표시.
        """
        info = self.controller.logged_in_emp
        dept = info.get("dept", "") or ""
        name = info.get("name", "") or ""
        if dept or name:
            self.emp_label.config(text=f"{dept} {name}님")
        else:
            self.emp_label.config(text="")

    def show_section(self, name):
        """
        섹션 전환 함수.
        - name: sections 딕셔너리 키
        """
        frame = self.sections[name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()

    def logout(self):
        """
        로그아웃 버튼에서 호출.
        - 로그인 정보 초기화
        - 로그인 프레임으로 전환
        """
        self.controller.logged_in_emp = {
            "emp_id": "",
            "name": "",
            "dept": "",
            "position": "",
            "basic_salary": 0,
            "annual_leave": 0,
        }

        login_frame = self.controller.frames["LoginFrame"]
        if hasattr(login_frame, "reset_fields"):
            login_frame.reset_fields()

        self.controller.show_frame("LoginFrame")
