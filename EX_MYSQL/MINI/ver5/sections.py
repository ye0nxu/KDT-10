# sections.py
from tkinter import ttk
from datetime import datetime
import tkinter as tk

from function import (
    get_employee_list,
    get_attendance_by_emp,
    get_salary_for_emp,
    get_connection,
)
from Jiyeon import checkIn_Delay, checkOut_work
from seob import insert_salary_records   # 🔹 급여 계산 함수 import


def make_card(parent, title_text: str):
    """
    섹션 공통 카드 레이아웃 생성 함수.
    - 바깥 카드 + 안쪽 패딩 + 제목 + 구분선까지 구성하고
      내부 컨텐츠를 올릴 'inner' 프레임을 반환.
    """
    card = ttk.Frame(parent, style="Card.TFrame")
    card.pack(fill="both", expand=True, padx=8, pady=6)

    inner = ttk.Frame(card, style="App.TFrame")
    inner.pack(fill="both", expand=True, padx=18, pady=14)

    title = ttk.Label(inner, text=title_text, style="SectionTitle.TLabel")
    title.pack(anchor="w", pady=(0, 8))

    sep = ttk.Separator(inner, orient="horizontal")
    sep.pack(fill="x", pady=(0, 10))

    return inner


# ================== 홈 화면 ==================
class HomeSection(ttk.Frame):
    """
    홈 화면 섹션.
    - 사내 직원 목록 Treeview로 표시.
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")
        self.main = main

        body = make_card(self, "홈")

        ttk.Label(
            body,
            text="사내 직원 목록이 아래에 표시됩니다.",
            style="Body.TLabel",
            justify="left",
            wraplength=900,
        ).pack(anchor="w", pady=(0, 12))

        # 직원 목록 테이블
        table_frame = ttk.Frame(body, style="App.TFrame")
        table_frame.pack(fill="both", expand=True, pady=(4, 4))

        columns = ("emp_id", "name", "position", "department", "email", "phone")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10,
        )

        self.tree.heading("emp_id", text="사번")
        self.tree.heading("name", text="이름")
        self.tree.heading("position", text="직급")
        self.tree.heading("department", text="부서")
        self.tree.heading("email", text="이메일")
        self.tree.heading("phone", text="전화번호")

        self.tree.column("emp_id", width=80, anchor="center")
        self.tree.column("name", width=80, anchor="center")
        self.tree.column("position", width=100, anchor="center")
        self.tree.column("department", width=120, anchor="center")
        self.tree.column("email", width=180, anchor="w")
        self.tree.column("phone", width=120, anchor="center")

        scroll_y = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        self.status_label = ttk.Label(
            body, text="", style="Body.TLabel", foreground="green"
        )
        self.status_label.pack(anchor="w", pady=(4, 0))

        ttk.Button(
            body,
            text="로그아웃",
            style="Primary.TButton",
            command=self.main.logout,
        ).pack(anchor="e", pady=(12, 0))

    def on_show(self):
        self.load_employees()

    def load_employees(self):
        """
        DB에서 직원 목록을 불러와 Treeview에 채우는 함수.
        """
        rows = get_employee_list()

        for item in self.tree.get_children():
            self.tree.delete(item)

        if rows is None:
            self.status_label.config(
                text="직원 목록을 불러오는 중 오류가 발생했습니다.", foreground="red"
            )
            return

        for row in rows:
            self.tree.insert(
                "",
                "end",
                values=(
                    row.get("emp_id", ""),
                    row.get("name", ""),
                    row.get("position", ""),
                    row.get("department", ""),
                    row.get("email", ""),
                    row.get("phone", ""),
                ),
            )

        self.status_label.config(text=f"총 {len(rows)}명 조회됨.", foreground="blue")


# ================== 회사 개요 ==================
class CompanySection(ttk.Frame):
    """
    회사 소개 섹션.
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")

        body = make_card(self, "회사 개요")

        # 왼쪽 굵은 캐치프레이즈
        headline = "세기를 뛰어넘는\n초일류 장수기업으로\n성장하겠습니다."
        ttk.Label(
            body,
            text=headline,
            style="Body.TLabel",
            justify="left",
            font=("맑은 고딕", 18, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        # SL 로고 이미지 (경로는 실제 파일 위치에 맞게 수정)
        # 이미지가 사라지지 않도록 self에 보관
        self.sl_logo = tk.PhotoImage(file="./KakaoTalk_20251119_0927444842.png")

        ttk.Label(
            body,
            image=self.sl_logo,
            style="App.TLabel",
        ).pack(anchor="w", pady=(0, 10))

        # 회사 소개 문단
        desc = (
            "에스엘은 1954년 설립 이래, 반세기 동안 자동차 헤드램프를 비롯한 각종 램프와 전동화,\n"
            "미러, FEM(Front End Module) 등 자동차 부품 생산에만 전력을 기울여온 "
            "자동차 부품 전문기업입니다.\n\n"
            "2004년 창립 50주년을 맞아 글로벌 기업으로 거듭나고 있는 회사의 위상에 맞춰 "
            "기업 이미지를 제고하고자\n사명을 옛 삼립산업에서 에스엘(SL)로 변경하고, "
            "핵심사업을 중심으로 한 내실경영을 통해 지속적인\n역량강화로 내부 구성원들에게는 "
            "미래를 제시하고, 외부적으로는 사회적인 책임을 다하는 장수기업으로\n"
            "발돋움하고자 합니다.\n"
            "감사합니다.\n"
        )

        ttk.Label(
            body,
            text=desc,
            style="Body.TLabel",
            justify="left",
            wraplength=800,  # 필요에 따라 너비 조절
        ).pack(anchor="w")


# ================== 개인 메뉴 ==================
class PersonalMenuSection(ttk.Frame):
    """
    개인 메뉴 섹션.
    - 개인정보 변경 / 근태 기록 / 급여 명세서로 이동 버튼 제공.
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")
        self.main = main

        body = make_card(self, "개인 메뉴")

        ttk.Label(
            body,
            text="개인 정보, 근태 기록, 급여 명세서를 확인·변경할 수 있습니다.",
            style="Body.TLabel",
        ).pack(anchor="w", pady=(0, 12))

        btn_frame = ttk.Frame(body, style="App.TFrame")
        btn_frame.pack(anchor="w")

        ttk.Button(
            btn_frame,
            text="개인 정보 변경",
            width=22,
            style="Primary.TButton",
            command=lambda: self.main.show_section("personal_info"),
        ).grid(row=0, column=0, padx=8, pady=8)

        ttk.Button(
            btn_frame,
            text="근태 기록",
            width=22,
            style="Primary.TButton",
            command=lambda: self.main.show_section("attendance"),
        ).grid(row=0, column=1, padx=8, pady=8)

        ttk.Button(
            btn_frame,
            text="급여 명세서 조회",
            width=22,
            style="Primary.TButton",
            command=lambda: self.main.show_section("payslip"),
        ).grid(row=1, column=0, padx=8, pady=8)


# ================== 개인 정보 변경 ==================
class PersonalInfoSection(ttk.Frame):
    """
    개인 정보 변경 섹션.
    - 비밀번호 / 이메일 / 전화번호 변경 가능.
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")
        self.main = main

        body = make_card(self, "개인 정보 변경")

        form = ttk.Frame(body, style="App.TFrame")
        form.pack(fill="x", pady=(0, 10))

        ttk.Label(form, text="새 비밀번호").grid(
            row=0, column=0, sticky="e", padx=4, pady=4
        )
        self.entry_pw = ttk.Entry(form, show="*")
        self.entry_pw.grid(row=0, column=1, sticky="ew", padx=4, pady=4)

        ttk.Label(form, text="비밀번호 재입력").grid(
            row=1, column=0, sticky="e", padx=4, pady=4
        )
        self.entry_pw2 = ttk.Entry(form, show="*")
        self.entry_pw2.grid(row=1, column=1, sticky="ew", padx=4, pady=4)

        ttk.Label(form, text="이메일").grid(
            row=2, column=0, sticky="e", padx=4, pady=4
        )
        self.entry_email = ttk.Entry(form)
        self.entry_email.grid(row=2, column=1, sticky="ew", padx=4, pady=4)

        ttk.Label(form, text="전화번호").grid(
            row=3, column=0, sticky="e", padx=4, pady=4
        )
        self.entry_phone = ttk.Entry(form)
        self.entry_phone.grid(row=3, column=1, sticky="ew", padx=4, pady=4)

        form.columnconfigure(1, weight=1)

        self.msg = ttk.Label(
            body, text="", foreground="green", style="Body.TLabel"
        )
        self.msg.pack(anchor="w", pady=(4, 4))

        btn_row = ttk.Frame(body, style="App.TFrame")
        btn_row.pack(anchor="w")

        ttk.Button(
            btn_row,
            text="저장",
            style="Accent.TButton",
            command=self.save_info,
        ).pack(side="left", padx=(0, 8))
        ttk.Button(
            btn_row,
            text="이전 화면으로",
            style="Menu.TButton",
            command=lambda: self.main.show_section("personal_menu"),
        ).pack(side="left")

    def save_info(self):
        """
        입력된 비밀번호/이메일/전화번호를 DB에 업데이트.
        """
        from function import get_connection, TABLE_EMP  # 지연 import (순환 참조 방지)

        pw1 = self.entry_pw.get().strip()
        pw2 = self.entry_pw2.get().strip()
        email = self.entry_email.get().strip()
        phone = self.entry_phone.get().strip()

        # 비밀번호 검증
        if pw1 or pw2:
            if pw1 != pw2:
                self.msg.config(text="비밀번호가 일치하지 않습니다.", foreground="red")
                return

        emp_id = self.main.controller.logged_in_emp.get("emp_id")
        if not emp_id:
            self.msg.config(text="로그인 정보가 없습니다.", foreground="red")
            return

        try:
            conn = get_connection()
            with conn.cursor() as cur:
                updates = []
                params = []

                if pw1:
                    updates.append("emp_pw = %s")
                    params.append(pw1)
                if email:
                    updates.append("email = %s")
                    params.append(email)
                if phone:
                    updates.append("phone = %s")
                    params.append(phone)

                if not updates:
                    self.msg.config(
                        text="변경할 정보가 없습니다.", foreground="red"
                    )
                    return

                sql = (
                    f"UPDATE {TABLE_EMP} SET "
                    + ", ".join(updates)
                    + " WHERE emp_id = %s"
                )
                params.append(emp_id)

                cur.execute(sql, params)
                conn.commit()

            self.msg.config(
                text="정보가 성공적으로 변경되었습니다.", foreground="green"
            )

        except Exception as e:
            print("DB 업데이트 오류:", e)
            self.msg.config(text="저장 중 오류가 발생했습니다.", foreground="red")
        finally:
            try:
                conn.close()
            except:
                pass

    def on_show(self):
        """
        섹션에 들어올 때마다 입력값 리셋.
        """
        self.msg.config(text="")
        self.entry_pw.delete(0, "end")
        self.entry_pw2.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_phone.delete(0, "end")


# ================== 근태 기록 ==================
class AttendanceSection(ttk.Frame):
    """
    근태 기록 섹션.
    - 로그인한 사원의 출퇴근 기록 조회
    - Jiyeon.checkIn_Delay() 호출하여 상태 업데이트
    - Jiyeon.checkOut_work() 호출하여 상태_2 업데이트
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")
        self.main = main

        body = make_card(self, "근태 기록")

        ttk.Label(
            body,
            text="로그인한 사원의 근무 기록입니다.",
            style="Body.TLabel",
        ).pack(anchor="w", pady=(0, 8))

        # 테이블 영역
        table_frame = ttk.Frame(body, style="App.TFrame")
        table_frame.pack(fill="both", expand=True, pady=(4, 4))

        columns = ("att_date", "check_in", "check_out", "status", "status_2")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10,
        )

        self.tree.heading("att_date", text="날짜")
        self.tree.heading("check_in", text="출근 시간")
        self.tree.heading("check_out", text="퇴근 시간")
        self.tree.heading("status", text="상태")
        self.tree.heading("status_2", text="상태_2")

        self.tree.column("att_date", width=100, anchor="center")
        self.tree.column("check_in", width=100, anchor="center")
        self.tree.column("check_out", width=100, anchor="center")
        self.tree.column("status", width=80, anchor="center")
        self.tree.column("status_2", width=80, anchor="center")

        scroll_y = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scroll_y.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        # 상태 메시지
        self.status_label = ttk.Label(
            body,
            text="",
            style="Body.TLabel",
        )
        self.status_label.pack(anchor="w", pady=(4, 6))

        # 버튼 영역
        btn_row = ttk.Frame(body, style="App.TFrame")
        btn_row.pack(fill="x")

        ttk.Button(
            btn_row,
            text="근태 상태 업데이트",
            style="Primary.TButton",
            command=self.update_attendance_status,
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            btn_row,
            text="이전 화면으로",
            style="Menu.TButton",
            command=lambda: self.main.show_section("personal_menu"),
        ).pack(side="left")

    def on_show(self):
        """
        화면 들어올 때마다 현재 로그인 사번으로 근태 목록 조회.
        """
        emp_id = self.main.controller.logged_in_emp.get("emp_id")
        self.load_attendance(emp_id)

    def load_attendance(self, emp_id):
        """
        DB에서 근태 기록 읽어서 Treeview에 채우는 함수.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not emp_id:
            self.status_label.config(text="로그인 정보가 없습니다.", foreground="red")
            return

        rows = get_attendance_by_emp(emp_id)

        if rows is None:
            self.status_label.config(
                text="근태 기록을 불러오는 중 오류가 발생했습니다.",
                foreground="red",
            )
            return

        for r in rows:
            self.tree.insert(
                "",
                "end",
                values=(
                    r.get("att_date", ""),
                    r.get("check_in_str", ""),
                    r.get("check_out_str", ""),
                    r.get("status", ""),
                    r.get("status_2"),
                ),
            )

        self.status_label.config(
            text=f"총 {len(rows)}건의 근태 기록 조회됨.", foreground="blue"
        )

    def update_attendance_status(self):
        """
        '근태 상태 업데이트' 버튼 핸들러.
        - Jiyeon.checkIn_Delay(emp_id) 실행 후 다시 목록 갱신.
        """
        emp_id = self.main.controller.logged_in_emp.get("emp_id")
        if not emp_id:
            self.status_label.config(text="로그인 정보가 없습니다.", foreground="red")
            return

        try:
            checkIn_Delay(emp_id)
            checkOut_work(emp_id)
            self.load_attendance(emp_id)
            self.status_label.config(
                text="근태 상태가 업데이트되었습니다.", foreground="green"
            )
        except Exception as e:
            print("근태 업데이트 오류:", e)
            self.status_label.config(
                text="근태 업데이트 중 오류가 발생했습니다.", foreground="red"
            )


# ================== 급여 명세서 ==================
class PayslipSection(ttk.Frame):
    """
    급여 명세서 섹션.
    - seob.insert_salary_records()로 해당 연/월 전체 직원 급여 계산/저장
    - 로그인한 사원의 선택 연/월 급여 내역 조회/표시
    """
    def __init__(self, parent, main):
        super().__init__(parent, style="App.TFrame")
        self.main = main

        body = make_card(self, "급여 명세서 조회")

        ttk.Label(
            body,
            text="해당 연/월의 급여를 계산한 후, 로그인한 사원의 급여 내역을 조회할 수 있습니다.",
            style="Body.TLabel",
            justify="left",
        ).pack(anchor="w", pady=(0, 10))

        # ── 연/월 선택 영역 ───────────────────────────
        ym_frame = ttk.Frame(body, style="App.TFrame")
        ym_frame.pack(anchor="w", pady=(0, 10))

        now = datetime.now()
        current_year = now.year
        current_month = now.month

        years = [str(current_year - 1), str(current_year), str(current_year + 1)]
        months = [f"{m:02d}" for m in range(1, 13)]

        ttk.Label(ym_frame, text="연도").grid(row=0, column=0, padx=4, pady=2, sticky="e")
        self.cb_year = ttk.Combobox(ym_frame, values=years, width=8, state="readonly")
        self.cb_year.set(str(current_year))
        self.cb_year.grid(row=0, column=1, padx=4, pady=2)

        ttk.Label(ym_frame, text="월").grid(row=0, column=2, padx=4, pady=2, sticky="e")
        self.cb_month = ttk.Combobox(ym_frame, values=months, width=6, state="readonly")
        self.cb_month.set(f"{current_month:02d}")
        self.cb_month.grid(row=0, column=3, padx=4, pady=2)

        ttk.Button(
            ym_frame,
            text="해당 월 전체 급여 계산/갱신",
            style="Primary.TButton",
            command=self.calculate_salary_for_month,
        ).grid(row=0, column=4, padx=(12, 4), pady=2)

        ttk.Button(
            ym_frame,
            text="내 급여 조회",
            style="Primary.TButton",
            command=self.load_my_salary,
        ).grid(row=0, column=5, padx=4, pady=2)

        # ── 급여 상세 표시 영역 ───────────────────────
        detail_frame = ttk.Frame(body, style="App.TFrame")
        detail_frame.pack(fill="x", pady=(10, 10))

        # 각 항목 라벨 생성 (좌측 제목 / 우측 값)
        self.salary_labels = {}  # key: 항목이름, value: 값 표시용 Label

        def add_row(row_idx, label_text, key):
            ttk.Label(detail_frame, text=label_text, style="Body.TLabel").grid(
                row=row_idx, column=0, sticky="e", padx=6, pady=3
            )
            val_label = ttk.Label(detail_frame, text="-", style="Body.TLabel")
            val_label.grid(row=row_idx, column=1, sticky="w", padx=6, pady=3)
            self.salary_labels[key] = val_label

        add_row(0, "기본급(월)", "basic_salary")
        add_row(1, "고용보험", "employment_insurance")
        add_row(2, "국민연금", "national_pension")
        add_row(3, "건강보험", "health_insurance")
        add_row(4, "장기요양", "long_term_care")
        add_row(5, "근로소득세", "income_tax")
        add_row(6, "지방소득세", "local_income_tax")
        add_row(7, "실수령액", "net_salary")

        detail_frame.columnconfigure(1, weight=1)

        # 상태 메시지
        self.status_label = ttk.Label(
            body,
            text="",
            style="Body.TLabel",
        )
        self.status_label.pack(anchor="w", pady=(4, 6))

        ttk.Button(
            body,
            text="이전 화면으로",
            style="Menu.TButton",
            command=lambda: self.main.show_section("personal_menu"),
        ).pack(anchor="w")

    # ----------------- 유틸 함수 -----------------
    def _get_selected_year_month(self):
        """
        콤보박스에서 선택된 연/월을 정수로 반환.
        - 잘못된 값일 경우 (None, None) 반환.
        """
        try:
            year = int(self.cb_year.get())
            month = int(self.cb_month.get())
            return year, month
        except ValueError:
            return None, None

    def _clear_salary_labels(self):
        """
        급여 상세 값 라벨을 모두 '-'로 초기화.
        """
        for lbl in self.salary_labels.values():
            lbl.config(text="-")

    # ----------------- 버튼 핸들러 -----------------
    def calculate_salary_for_month(self):
        """
        '해당 월 전체 급여 계산/갱신' 버튼 클릭 시 실행.
        - seob.insert_salary_records(cur, year, month)를 호출하여
          직원 전체의 해당 연/월 급여를 salary 테이블에 저장(덮어쓰기).
        """
        year, month = self._get_selected_year_month()
        if year is None:
            self.status_label.config(text="유효한 연/월을 선택해 주세요.", foreground="red")
            return

        try:
            conn = get_connection()
            with conn.cursor() as cur:
                count = insert_salary_records(cur, year, month)  # 🔹 seob 모듈 호출
                conn.commit()

            self.status_label.config(
                text=f"{year}년 {month}월 급여가 {count}명에 대해 계산·저장되었습니다.",
                foreground="blue",
            )
        except Exception as e:
            print("급여 계산 오류:", e)
            self.status_label.config(
                text="급여 계산 중 오류가 발생했습니다.", foreground="red"
            )
        finally:
            try:
                conn.close()
            except:
                pass

    def load_my_salary(self):
        """
        '내 급여 조회' 버튼 클릭 시 실행.
        - 로그인한 사원의 emp_id와 선택 연/월 기준으로 salary 테이블 조회
        - 결과를 화면에 표시
        """
        self._clear_salary_labels()

        emp_id = self.main.controller.logged_in_emp.get("emp_id")
        if not emp_id:
            self.status_label.config(text="로그인 정보가 없습니다.", foreground="red")
            return

        year, month = self._get_selected_year_month()
        if year is None:
            self.status_label.config(text="유효한 연/월을 선택해 주세요.", foreground="red")
            return

        row = get_salary_for_emp(emp_id, year, month)

        if row is None:
            self.status_label.config(
                text="급여 조회 중 오류가 발생했습니다.", foreground="red"
            )
            return

        if not row:
            self.status_label.config(
                text="해당 연/월의 급여 정보가 없습니다. 먼저 급여 계산을 실행해 주세요.",
                foreground="red",
            )
            return

        # 각 항목을 라벨에 세팅
        self.salary_labels["basic_salary"].config(
            text=f"{row.get('basic_salary', 0):,} 원"
        )
        self.salary_labels["employment_insurance"].config(
            text=f"{row.get('employment_insurance', 0):,} 원"
        )
        self.salary_labels["national_pension"].config(
            text=f"{row.get('national_pension', 0):,} 원"
        )
        self.salary_labels["health_insurance"].config(
            text=f"{row.get('health_insurance', 0):,} 원"
        )
        self.salary_labels["long_term_care"].config(
            text=f"{row.get('long_term_care', 0):,} 원"
        )
        self.salary_labels["income_tax"].config(
            text=f"{row.get('income_tax', 0):,} 원"
        )
        self.salary_labels["local_income_tax"].config(
            text=f"{row.get('local_income_tax', 0):,} 원"
        )
        self.salary_labels["net_salary"].config(
            text=f"{row.get('net_salary', 0):,} 원"
        )

        self.status_label.config(
            text=f"{year}년 {month}월 급여 내역을 조회했습니다.", foreground="green"
        )
