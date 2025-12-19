from tkinter import *
import copy
import random
from tkinter import messagebox

ROWS = 23
COLS = 23
CURRENT_R = 11
CURRENT_C = 11

CURRENT_PR1 = 11
CURRENT_PC1 = 5

CURRENT_PR2 = 11
CURRENT_PC2 = 16

KEY_INDEX = []
KEY_COUNT = 0

CHEAK_POINT_KEY1 = 0
CHEAK_POINT_KEY2 = 0
CHEAK_POINT_KEY3 = 0




MAP=[ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,2,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0],
      [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,2,0,0,1,0,0,1,0],
      [0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,2,1,0],
      [0,1,1,1,0,1,2,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
      [0,2,0,1,1,1,0,1,1,1,0,0,0,1,1,1,2,1,1,1,1,1,0],
      [0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0],
      [0,1,0,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,2,0,1,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
      [0,1,0,2,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0,1,0],
      [0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0],
      [0,1,1,1,1,1,2,1,1,1,0,0,0,1,1,1,0,1,1,1,0,2,0],
      [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,2,1,0,1,1,1,0],
      [0,1,2,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0],
      [0,1,0,0,1,0,0,2,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
      [0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,2,1,1,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

window = Tk()
window.title("**Equal Grid**")
window.geometry("690x690")
window.resizable(False,False)

peo_img2 = PhotoImage(file="./hole.png")  # 포탈 이미지(값 2)
peo_img3 = PhotoImage(file="./hole.png")



def set_Potal():
    target_idx= []
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == 2:
                target_idx.append((i, j))
    random.shuffle(target_idx)
    data = random.sample(target_idx, 3)
    
    for d in data:
        r, c = d
        MAP[r][c] = 3

set_Potal()



# ----------------------------------------------------------------------------- 
def Theif_move():  # 타일 그리드
    for r in range(ROWS):
        window.grid_rowconfigure(r+1, weight=1, uniform="row")
    for c in range(COLS):
        window.grid_columnconfigure(c, weight=1, uniform="col")

    for r in range(ROWS):
        for c in range(COLS):
            v = MAP[r][c]
            if v == 1:
                Label(window, bg="gray", relief="solid", borderwidth=1).grid(row=r, column=c, sticky="nesw")
            elif v == 0:
                Label(window, bg="black").grid(row=r, column=c, sticky="nesw")
            elif v == 2: # 하수구
                Label(window, image=peo_img2).grid(row=r, column=c, sticky="nesw")
            elif v == 3: # 포탈(값=3로 통일)
                Label(window, image=peo_img3, bg="gray", relief="solid", borderwidth=1).grid(row=r, column=c, sticky="nesw")
            else:
                Label(window, bg="gray").grid(row=r, column=c, sticky="nesw")

def setCheckPoint():
    global KEY1_img ,KEY2_img ,KEY3_img ,DOOR_img
    global KEY_INDEX, KEY1, KEY2, KEY3, DOOR
    rand = [[1,1], [1,21], [21,1], [21,21]]
    random.shuffle(rand)
    
    KEY_INDEX = rand
    print(KEY_INDEX)
    KEY1,KEY2,KEY3,DOOR = rand


    r, c = KEY1    
    KEY1_img = PhotoImage(file="./key1.png")
    KEY1 = Label(window, image=KEY1_img,bg="gray")
    KEY1.grid(row=r, column=c, sticky="nesw",padx=3,pady=3)
    
    r, c = KEY2
    KEY2_img = PhotoImage(file="./key2.png")
    KEY2 = Label(window, image=KEY2_img,bg="gray")
    KEY2.grid(row=r, column=c, sticky="nesw",padx=3,pady=3)
    
    r, c = KEY3
    KEY3_img = PhotoImage(file="./key3.png")
    KEY3 = Label(window, image=KEY3_img,bg="gray")
    KEY3.grid(row=r, column=c, sticky="nesw",padx=3,pady=3)
    
    r, c = DOOR
    DOOR_img = PhotoImage(file="./door2.png")
    DOOR = Label(window, image=DOOR_img,bg="white")
    DOOR.grid(row=r, column=c, sticky="nesw",padx=2,pady=2)


def destory_handler(n):
    if n == 1:
        KEY1.destroy()
    if n == 2:
        KEY2.destroy()
    if n == 3:
        KEY3.destroy()


    return True



def CheckPoint_handler():
    global KEY_COUNT

    global CHEAK_POINT_KEY1, CHEAK_POINT_KEY2, CHEAK_POINT_KEY3
    key1, key2, key3 , door= KEY_INDEX
    Thief_pos = [CURRENT_R, CURRENT_C]


    if Thief_pos == key1 and CHEAK_POINT_KEY1==0 : 
        if destory_handler(1):
            CHEAK_POINT_KEY1 +=1
            KEY_COUNT += 1
    if Thief_pos == key2 and CHEAK_POINT_KEY2==0: 
        if destory_handler(2):
            KEY_COUNT += 1
            CHEAK_POINT_KEY2 +=1
    if Thief_pos == key3 and CHEAK_POINT_KEY3==0 : 
        if destory_handler(3):
            KEY_COUNT += 1
            CHEAK_POINT_KEY3 +=1

    if Thief_pos == door and KEY_COUNT >= 3 :
        messagebox.showinfo("탈출 성공!", "축하드립니다! 게임을 종료합니다.")
        window.destroy()   
    elif Thief_pos == door and KEY_COUNT < 3:
        messagebox.showinfo("탈출 실패","열쇠 개수가 부족합니다!")
    
    Potal()




def Thief_set():
    global set_peo,peo_img
    peo_img = PhotoImage(file="./Thief.png")
    set_peo = Label(window, image=peo_img, bg="gray")
    set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw")

def Police_set():
    global set_pol,pol_img
    pol_img = PhotoImage(file="./Police.png")
    set_pol = Label(window, image=pol_img, bg="gray")
    set_pol.grid(row=CURRENT_PR1, column=CURRENT_PC1, sticky="nesw", padx=2, pady=2)

def Police_set2():
    global set_pol1,pol1_img
    pol1_img = PhotoImage(file="./Police.png")
    set_pol1 = Label(window, image=pol1_img, bg="gray")
    set_pol1.grid(row=CURRENT_PR2, column=CURRENT_PC2, sticky="nesw", padx=2, pady=2)



PASSABLE = {1,2,3}  # 길/포탈 통과 가능

def check(next_r, next_c):
    if not in_bounds(next_r, next_c):
        return False
    if MAP[next_r][next_c] == 0:
        # print("벽입니다! 이동 불가!")
        return False
    return True

# -------------------- 그리디 한 칸 선택: 인접(거리1) 금지 옵션 추가 --------------------
def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def greedy_next_step(sr, sc, tr, tc, blocked=None, avoid_adjacent_to=None):
    """
    (sr, sc)에서 4방 후보 중 타깃 (tr, tc)까지 유클리드 거리(제곱)가 가장 작아지는 한 칸을 선택.
    - blocked: 이번 턴에 피해야 할 좌표 집합(예약 칸 등)
    - avoid_adjacent_to: (r, c). 이 좌표와 맨해튼 거리 1이 되는 칸은 제외
    - 예외:
        1) 후보칸 == 도둑 칸(즉시 체포 가능) -> 맨해튼 금지 무시하고 즉시 선택
        2) 후보칸이 도둑과 대각선(체비쇼프 1) -> 맨해튼 금지 무시하고 허용
    후보가 없으면 None 반환.
    """
    if (sr, sc) == (tr, tc):
        return (sr, sc)

    if blocked is None:
        blocked = set()

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    best = None
    best_dist2 = None  # sqrt 없이 제곱으로 비교

    for dr, dc in dirs:
        nr, nc = sr + dr, sc + dc
        if not in_bounds(nr, nc):
            continue
        if MAP[nr][nc] not in PASSABLE:
            continue
        if (nr, nc) in blocked:
            continue

        # ---- 캡처 우선 예외: 후보가 곧바로 도둑 칸이면 바로 선택 ----
        if (nr, nc) == (tr, tc):
            return (nr, nc)

        # --- 맨해튼 인접 금지 + 예외(체비쇼프 1 허용) ---
        if avoid_adjacent_to is not None:
            ar, ac = avoid_adjacent_to
            if abs(nr - ar) + abs(nc - ac) == 1:
                # 도둑과 대각선(체비쇼프 1)이면 금지 무시
                if not (max(abs(tr - nr), abs(tc - nc)) == 1 and
                        abs(tr - nr) == 1 and abs(tc - nc) == 1):
                    continue

        # 타깃까지의 제곱거리 (유클리드)
        dist2 = (tr - nr) * (tr - nr) + (tc - nc) * (tc - nc)

        if (best is None) or (dist2 < best_dist2):
            best = (nr, nc)
            best_dist2 = dist2

    return best  # 후보 없으면 None
# -------------------- 경찰 이동: 서로 맨해튼 거리 1 금지 --------------------
def police_move():
    global CURRENT_PR1, CURRENT_PC1, CURRENT_PR2, CURRENT_PC2, PREV_PR1, PREV_PC1

    # --- 1) 1번의 직전 칸 기억(이동 전) ---
    prev1r, prev1c = CURRENT_PR1, CURRENT_PC1

    # --- 2) 1번 경찰: 현재 2번과 인접(거리1) 금지 + 그리디 ---
    next1 = greedy_next_step(
        CURRENT_PR1, CURRENT_PC1,
        CURRENT_R, CURRENT_C,
        blocked=set(),
        avoid_adjacent_to=(CURRENT_PR2, CURRENT_PC2)  # ✅ 2번과 거리1 금지
    )
    if next1 is not None:
        n1r, n1c = next1
    else:
        n1r, n1c = CURRENT_PR1, CURRENT_PC1  # 후보 없으면 대기

    # --- 3) 2번을 위한 금지 칸(예약/기차놀이 방지) ---
    blocked_for_p2 = {(n1r, n1c), (prev1r, prev1c)}

    # 도둑 칸은 예약에서 제외(동시 체포 허용)
    if (CURRENT_R, CURRENT_C) in blocked_for_p2:
        blocked_for_p2.remove((CURRENT_R, CURRENT_C))

    # --- 4) 2번 경찰: 이동된 1번과 인접(거리1) 금지 + 그리디 ---
    next2 = greedy_next_step(
        CURRENT_PR2, CURRENT_PC2,
        CURRENT_R, CURRENT_C,
        blocked=blocked_for_p2,
        avoid_adjacent_to=(n1r, n1c)                 # ✅ 1번과 거리1 금지
    )
    if next2 is not None:
        n2r, n2c = next2
        # 혹시라도 동일 칸이면(비도둑 칸) 2번 대기
        if (n2r, n2c) == (n1r, n1c) and (n2r, n2c) != (CURRENT_R, CURRENT_C):
            n2r, n2c = CURRENT_PR2, CURRENT_PC2
    else:
        n2r, n2c = CURRENT_PR2, CURRENT_PC2  # 후보 없으면 대기

    # --- 5) 실제 이동 반영 ---
    set_pol.grid(row=n1r, column=n1c, sticky="nesw")
    set_pol1.grid(row=n2r, column=n2c, sticky="nesw")

    # --- 6) 좌표 갱신 + 1번의 직전 칸 업데이트 ---
    CURRENT_PR1, CURRENT_PC1 = n1r, n1c
    CURRENT_PR2, CURRENT_PC2 = n2r, n2c
    PREV_PR1, PREV_PC1 = prev1r, prev1c

    # --- 7) 체포 체크 ---
    if (CURRENT_PR1, CURRENT_PC1) == (CURRENT_R, CURRENT_C) or \
       (CURRENT_PR2, CURRENT_PC2) == (CURRENT_R, CURRENT_C):
        messagebox.showinfo("게임 종료", "잡힘! 게임이 종료됩니다.")
        window.destroy()


# -------------------- 도둑 이동 & 포탈(값=2) --------------------
def up(event=None):
    global CURRENT_R
    nr = CURRENT_R - 1
    if check(nr, CURRENT_C):
        CURRENT_R = nr
        set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw", padx=2, pady=2)
    CheckPoint_handler()
    police_move()

def down(event=None):
    global CURRENT_R
    nr = CURRENT_R + 1
    if check(nr, CURRENT_C):
        CURRENT_R = nr
        set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw")
    CheckPoint_handler()
    police_move()

def left(event=None):
    global CURRENT_C
    nc = CURRENT_C - 1
    if check(CURRENT_R, nc):
        CURRENT_C = nc
        set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw")
    CheckPoint_handler()
    police_move()

def right(event=None):
    global CURRENT_C
    nc = CURRENT_C + 1
    if check(CURRENT_R, nc):
        CURRENT_C = nc
        set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw")
    CheckPoint_handler()
    police_move()

def Potal():
    """플레이어가 포탈(값=2)에 서 있으면 다른 포탈로 랜덤 텔레포트"""
    global CURRENT_C, CURRENT_R
    if MAP[CURRENT_R][CURRENT_C] != 3:
        return
    # portals = [(i, j) for i in range(ROWS) for j in range(COLS) if MAP[i][j] == 3]

    potal_idx =[]

    for i in range(ROWS):
        for j in range(COLS):
            if MAP[i][j] == 3:
                potal_idx.append((i, j))
    

    cur = (CURRENT_R, CURRENT_C)

    if cur in potal_idx:
        potal_idx.remove(cur)
    if not potal_idx:
        return
    
    CURRENT_R, CURRENT_C = random.choice(potal_idx)
    set_peo.grid(row=CURRENT_R, column=CURRENT_C, sticky="nesw")






# ------------------------------------------------------------------------------------------
Theif_move()
Police_set()
setCheckPoint()






Police_set2()
Thief_set()
window.bind("<Up>", up)
window.bind("<Left>", left)
window.bind("<Down>", down)
window.bind("<Right>", right)
window.mainloop()
