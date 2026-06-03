import tkinter as tk
from tkinter import ttk, font
import random

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# ── 데이터 ──────────────────────────────────────────────
GENRES = [
    {"name": "액션",   "icon": "⚔️",  "color": "#E50914"},
    {"name": "로맨스", "icon": "💕",  "color": "#FF69B4"},
    {"name": "공포",   "icon": "👻",  "color": "#6A0DAD"},
    {"name": "코미디", "icon": "😂",  "color": "#FF8C00"},
    {"name": "SF",     "icon": "🚀",  "color": "#00BFFF"},
    {"name": "스릴러", "icon": "🔪",  "color": "#DC143C"},
    {"name": "판타지", "icon": "🧙",  "color": "#9370DB"},
    {"name": "드라마", "icon": "🎭",  "color": "#20B2AA"},
    {"name": "다큐",   "icon": "🎬",  "color": "#DAA520"},
    {"name": "애니",   "icon": "✨",  "color": "#FF6347"},
    {"name": "범죄",   "icon": "🕵️", "color": "#B22222"},
    {"name": "가족",   "icon": "👨‍👩‍👧", "color": "#32CD32"},
]

CONTENT = [
    {"title": "오징어 게임",       "genres": ["스릴러","드라마","액션"],    "rating": 4.9, "year": 2021,
     "desc": "456명의 참가자가 상금을 위해 생존 게임에 참여하는 이야기",
     "badge": "🔥 HOT", "color": "#E50914", "image": "images/squidgame.png"},
    {"title": "기묘한 이야기",     "genres": ["SF","판타지","공포"],        "rating": 4.8, "year": 2016,
     "desc": "초자연적 존재들이 나타나는 마을에서 일어나는 미스터리",
     "badge": "⭐ TOP", "color": "#00BFFF", "image": "images/strangerthings.png"},
    {"title": "브리저튼",          "genres": ["로맨스","드라마"],           "rating": 4.5, "year": 2020,
     "desc": "19세기 런던 상류사회를 배경으로 한 로맨스 드라마",
     "badge": "💕 인기", "color": "#FF69B4", "image": "images/bridgerton.png"},
    {"title": "위쳐",              "genres": ["판타지","액션","드라마"],    "rating": 4.6, "year": 2019,
     "desc": "돌연변이 괴물 사냥꾼 게롤트의 모험을 그린 판타지",
     "badge": "🏆 수상", "color": "#9370DB", "image": "images/thewitcher.png"},
    {"title": "머니 하이스트",     "genres": ["범죄","스릴러","액션"],      "rating": 4.7, "year": 2017,
     "desc": "완벽한 강도 계획으로 조폐국을 점거하는 스페인 드라마",
     "badge": "🔥 HOT", "color": "#DC143C", "image": "images/moneyheist.png"},
    {"title": "나르코스",          "genres": ["범죄","드라마","스릴러"],    "rating": 4.6, "year": 2015,
     "desc": "콜롬비아 마약왕 파블로 에스코바르의 실화 기반 드라마",
     "badge": "📺 실화", "color": "#B22222", "image": "images/narcos.png"},
    {"title": "블랙 미러",         "genres": ["SF","스릴러","드라마"],      "rating": 4.7, "year": 2011,
     "desc": "기술 발전이 인류에게 미치는 영향을 다룬 SF 앤솔로지",
     "badge": "🤖 SF",  "color": "#1C1C2E", "image": "images/blackmirror.png"},
    {"title": "에밀리, 파리에 가다","genres": ["로맨스","코미디","드라마"], "rating": 4.2, "year": 2020,
     "desc": "파리로 이주한 미국 여성의 사랑과 커리어 이야기",
     "badge": "🗼 트렌디","color": "#FF6347", "image": "images/emilyinparis.png"},
    {"title": "지구의 밤",         "genres": ["다큐"],                     "rating": 4.9, "year": 2020,
     "desc": "지구 곳곳의 야생동물들의 야간 생활을 담은 다큐멘터리",
     "badge": "🌍 다큐", "color": "#228B22", "image": "images/nightonearth.png"},
    {"title": "아케인",            "genres": ["애니","판타지","액션"],      "rating": 4.9, "year": 2021,
     "desc": "리그 오브 레전드 세계관을 배경으로 한 최고의 애니메이션",
     "badge": "🏆 수상", "color": "#6A0DAD", "image": "images/arcane.png"},
    {"title": "길모어 걸스",       "genres": ["가족","코미디","로맨스"],    "rating": 4.5, "year": 2000,
     "desc": "싱글맘과 딸의 특별한 유대를 그린 따뜻한 드라마",
     "badge": "❤️ 감동", "color": "#32CD32", "image": "images/gilmoregirls.png"},
    {"title": "유 (YOU)",          "genres": ["스릴러","로맨스","범죄"],    "rating": 4.5, "year": 2018,
     "desc": "사랑에 집착하는 스토커의 시선으로 펼쳐지는 심리 스릴러",
     "badge": "😨 충격", "color": "#8B0000", "image": "images/you.png"},
    {"title": "루시퍼",            "genres": ["판타지","코미디","범죄"],    "rating": 4.6, "year": 2016,
     "desc": "악마가 LA 형사와 함께 범죄를 해결하는 판타지 수사물",
     "badge": "😈 인기", "color": "#FF4500", "image": "images/lucifer.png"},
    {"title": "더 크라운",         "genres": ["드라마","다큐"],             "rating": 4.7, "year": 2016,
     "desc": "영국 왕실 엘리자베스 2세의 삶을 다룬 역사 드라마",
     "badge": "👑 프리미엄","color": "#B8860B", "image": "images/thecrown.png"},
]

# ── 메인 앱 ──────────────────────────────────────────────
class NetflixApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎬 OTT Recommender")
        self.geometry("1100x720")
        self.configure(bg="#141414")
        self.resizable(False, False)
        self.selected_genres = []
        self._frame = None
        self._show_frame(SplashScreen)

    def _show_frame(self, FrameClass, **kw):
        new = FrameClass(self, **kw)
        if self._frame:
            self._frame.destroy()
        self._frame = new
        new.pack(fill="both", expand=True)

# ── 스플래시 화면 ──────────────────────────────────────────
class SplashScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#141414")
        self._alpha = 0.0
        master.attributes("-alpha", 0.0)

        center = tk.Frame(self, bg="#141414")
        center.place(relx=0.5, rely=0.5, anchor="center")

        logo_frame = tk.Frame(center, bg="#E50914", padx=20, pady=8)
        logo_frame.pack(pady=(0, 30))
        tk.Label(logo_frame, text="4 F L I X", font=("Arial Black", 36, "bold"),
                 fg="white", bg="#E50914").pack()

        tk.Label(center, text="맞춤형 콘텐츠 추천",
                 font=("Arial", 18), fg="#aaaaaa", bg="#141414").pack(pady=(0, 8))
        tk.Label(center, text="당신의 취향으로 시작하세요",
                 font=("Arial", 12), fg="#555555", bg="#141414").pack()

        btn = tk.Button(center, text="  시작하기  ",
                        font=("Arial", 14, "bold"),
                        bg="#E50914", fg="white", relief="flat",
                        cursor="hand2", padx=24, pady=12, bd=0,
                        command=lambda: master._show_frame(GenreSelectScreen))
        btn.pack(pady=40)
        btn.bind("<Enter>", lambda e: btn.config(bg="#ff1f1f"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#E50914"))

        tk.Label(self, text="✦ Powered by Smart Algorithm ✦",
                 font=("Arial", 9), fg="#333333", bg="#141414").place(
                 relx=0.5, rely=0.97, anchor="center")

        self._fade_in()

    def _fade_in(self):
        self._alpha = min(self._alpha + 0.05, 1.0)
        self.master.attributes("-alpha", self._alpha)
        if self._alpha < 1.0:
            self.after(30, self._fade_in)

# ── 장르 선택 화면 ──────────────────────────────────────────
class GenreSelectScreen(tk.Frame):
    CARD_W, CARD_H = 140, 80
    COLS = 6

    def __init__(self, master):
        super().__init__(master, bg="#141414")
        self.master = master
        self._selected = set()
        self._buttons = {}
        self._build()

    def _build(self):
        header = tk.Frame(self, bg="#1a1a1a", pady=20)
        header.pack(fill="x")

        tk.Label(header, text="4FLIX", font=("Arial Black", 22, "bold"),
                 fg="#E50914", bg="#1a1a1a").pack()
        tk.Label(header, text="좋아하는 장르를 선택하세요 (최소 1개, 최대 5개)",
                 font=("Arial", 13), fg="#cccccc", bg="#1a1a1a").pack(pady=(6, 0))
        tk.Label(header, text="선택할수록 더 정확한 추천을 받을 수 있어요 ✨",
                 font=("Arial", 10), fg="#666666", bg="#1a1a1a").pack()

        tk.Frame(self, bg="#E50914", height=2).pack(fill="x")

        grid_frame = tk.Frame(self, bg="#141414")
        grid_frame.pack(fill="both", expand=True, padx=60, pady=30)

        for idx, genre in enumerate(GENRES):
            row, col = divmod(idx, self.COLS)
            self._make_card(grid_frame, genre, row, col)

        bottom = tk.Frame(self, bg="#141414", pady=20)
        bottom.pack(fill="x")

        self.status_label = tk.Label(bottom, text="0개 선택됨",
                                     font=("Arial", 11), fg="#888888", bg="#141414")
        self.status_label.pack()

        self.next_btn = tk.Button(bottom, text="추천받기  →",
                                  font=("Arial", 14, "bold"),
                                  bg="#333333", fg="#666666",
                                  relief="flat", padx=30, pady=12,
                                  bd=0, state="disabled", cursor="hand2",
                                  command=self._go_recommend)
        self.next_btn.pack(pady=(10, 0))

    def _make_card(self, parent, genre, row, col):
        card = tk.Frame(parent, bg="#1e1e1e",
                        width=self.CARD_W, height=self.CARD_H,
                        cursor="hand2", relief="flat", bd=0)
        card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
        card.grid_propagate(False)
        parent.grid_columnconfigure(col, weight=1)

        icon_lbl = tk.Label(card, text=genre["icon"], font=("Arial", 22),
                             bg="#1e1e1e", fg="white")
        icon_lbl.place(relx=0.5, rely=0.38, anchor="center")

        name_lbl = tk.Label(card, text=genre["name"], font=("Arial", 11, "bold"),
                             bg="#1e1e1e", fg="#cccccc")
        name_lbl.place(relx=0.5, rely=0.74, anchor="center")

        self._buttons[genre["name"]] = {
            "frame": card, "icon": icon_lbl, "name": name_lbl,
            "color": genre["color"], "selected": False
        }

        for w in [card, icon_lbl, name_lbl]:
            w.bind("<Button-1>", lambda e, g=genre["name"]: self._toggle(g))
            w.bind("<Enter>",    lambda e, g=genre["name"]: self._hover(g, True))
            w.bind("<Leave>",    lambda e, g=genre["name"]: self._hover(g, False))

    def _toggle(self, name):
        info = self._buttons[name]
        if info["selected"]:
            info["selected"] = False
            self._selected.discard(name)
            self._set_card_style(name, False)
        else:
            if len(self._selected) >= 5:
                self._shake_button(); return
            info["selected"] = True
            self._selected.add(name)
            self._set_card_style(name, True)
        self._update_status()

    def _set_card_style(self, name, selected):
        info = self._buttons[name]
        color = info["color"] if selected else "#1e1e1e"
        info["frame"].config(bg=color,
                             highlightthickness=2 if selected else 0,
                             highlightbackground=info["color"])
        info["icon"].config(bg=color)
        info["name"].config(bg=color, fg="white")

    def _hover(self, name, on):
        info = self._buttons[name]
        if not info["selected"]:
            bg = "#2a2a2a" if on else "#1e1e1e"
            fg = "white"   if on else "#cccccc"
            info["frame"].config(bg=bg)
            info["icon"].config(bg=bg)
            info["name"].config(bg=bg, fg=fg)

    def _update_status(self):
        n = len(self._selected)
        self.status_label.config(
            text=f"✓ {n}개 선택됨" if n else "0개 선택됨",
            fg="#E50914" if n else "#888888")
        if n >= 1:
            self.next_btn.config(state="normal", bg="#E50914", fg="white",
                                 text=f"추천받기")
            self.next_btn.bind("<Enter>", lambda e: self.next_btn.config(bg="#ff1f1f"))
            self.next_btn.bind("<Leave>", lambda e: self.next_btn.config(bg="#E50914"))
        else:
            self.next_btn.config(state="disabled", bg="#333333", fg="#666666",
                                 text="추천받기  →")

    def _shake_button(self):
        self.next_btn.config(text="최대 5개까지 선택 가능", bg="#ff4400")
        self.after(1200, lambda: self.next_btn.config(
            text=f"추천받기", bg="#E50914"))

    def _go_recommend(self):
        self.master.selected_genres = list(self._selected)
        self.master._show_frame(RecommendScreen)

# ── 추천 화면 ──────────────────────────────────────────────
class RecommendScreen(tk.Frame):
    HERO_IMAGE_SIZE = (360, 220)
    CARD_IMAGE_SIZE = (220, 120)

    def __init__(self, master):
        super().__init__(master, bg="#141414")
        self.master   = master
        self.selected = master.selected_genres
        self._image_cache = {}
        self.results  = self._score_content()
        self._build()

    def _resolve_image_path(self, item):
        if item.get("image"):
            return item["image"]
        title = item.get("title", "").strip().lower()
        safe = "".join(ch if ch.isalnum() or ch.isspace() else "" for ch in title)
        safe = "_".join(safe.split())
        return f"images/{safe}.png"

    def _load_image(self, path, size):
        if not path:
            return None
        cache_key = (path, size)
        if cache_key in self._image_cache:
            return self._image_cache[cache_key]
        try:
            if PIL_AVAILABLE:
                img = Image.open(path)
                img = self._resize_cover(img, size)
                photo = ImageTk.PhotoImage(img)
            else:
                photo = tk.PhotoImage(file=path)
                if size and (photo.width() != size[0] or photo.height() != size[1]):
                    photo = self._scale_photoimage(photo, size)
            self._image_cache[cache_key] = photo
            return photo
        except Exception:
            return None

    def _update_hero_thumbnail(self, canvas, item):
        w = max(canvas.winfo_width(), 10)
        h = max(canvas.winfo_height(), 10)
        canvas.delete("all")
        image_path = self._resolve_image_path(item)
        hero_img = self._load_image(image_path, (w, h))
        if hero_img:
            canvas.create_image(0, 0, image=hero_img, anchor="nw")
            canvas.image = hero_img
        else:
            canvas.create_rectangle(0, 0, w, h, fill="#0d0d0d", outline="")
            canvas.create_text(w // 2, h // 2, text=item["title"],
                               font=("Arial Black", 14), fill="white",
                               width=w - 20, justify="center")

    def _update_card_thumbnail(self, canvas, item):
        w = max(canvas.winfo_width(), 10)
        h = max(canvas.winfo_height(), 10)
        canvas.delete("all")
        canvas.create_rectangle(0, 0, w, h, fill="#1e1e1e", outline="")
        image_path = self._resolve_image_path(item)
        card_img = self._load_image(image_path, (w, h))
        if card_img:
            canvas.create_image(w // 2, h // 2, image=card_img, anchor="center")
            canvas.image = card_img
        else:
            canvas.create_text(w // 2, h // 2, text=item["title"],
                               font=("Arial Black", 13), fill="white",
                               width=w - 20, justify="center")
        badge_font = font.Font(family="Arial", size=8, weight="bold")
        badge_width = badge_font.measure(item["badge"]) + 14
        canvas.create_rectangle(8, 8, 8 + badge_width, 28,
                                fill="#E50914", outline="")
        canvas.create_text(12 + badge_width / 2, 18,
                           text=item["badge"], font=("Arial", 8, "bold"), fill="white")

    def _resize_cover(self, img, size):
        target_w, target_h = size
        src_w, src_h = img.size
        scale = max(target_w / src_w, target_h / src_h)
        new_w = int(src_w * scale + 0.5)
        new_h = int(src_h * scale + 0.5)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - target_w) // 2
        top = (new_h - target_h) // 2
        right = left + target_w
        bottom = top + target_h
        return img.crop((left, top, right, bottom))

    def _scale_photoimage(self, photo, size):
        target_w, target_h = size
        orig_w, orig_h = photo.width(), photo.height()
        if orig_w == 0 or orig_h == 0:
            return photo
        x_ratio = target_w / orig_w
        y_ratio = target_h / orig_h
        scale = max(x_ratio, y_ratio)
        if scale >= 1:
            factor = int(scale + 0.5)
            return photo.zoom(factor, factor)
        factor = int(1 / scale + 0.5)
        return photo.subsample(factor, factor)

    # ── 추천 알고리즘 (장르 매칭 × 10 + 평점 × 5 + 다양성 노이즈) ──
    def _score_content(self):
        sel = set(self.selected)
        scored = []
        for c in CONTENT:
            match = len(set(c["genres"]) & sel)
            if match == 0:
                continue
            score = match * 10 + c["rating"] * 5 + random.uniform(0, 3)
            scored.append({**c, "score": score, "match": match})
        scored.sort(key=lambda x: -x["score"])
        if not scored:   # 매칭 없으면 평점 순
            scored = sorted(CONTENT,
                            key=lambda x: -(x["rating"] + random.uniform(0, 1)))
        return scored[:8]

    def _build(self):
        # 헤더
        header = tk.Frame(self, bg="#1a1a1a")
        header.pack(fill="x")
        nav = tk.Frame(header, bg="#1a1a1a", pady=14, padx=30)
        nav.pack(fill="x")

        back = tk.Button(nav, text="다시선택", font=("Arial", 10),
                         bg="#1a1a1a", fg="#888888", relief="flat", bd=0,
                         cursor="hand2",
                         command=lambda: self.master._show_frame(GenreSelectScreen))
        back.pack(side="left")
        back.bind("<Enter>", lambda e: back.config(fg="white"))
        back.bind("<Leave>", lambda e: back.config(fg="#888888"))

        tk.Label(nav, text="4FLIX", font=("Arial Black", 20, "bold"),
                 fg="#E50914", bg="#1a1a1a").pack(side="left", padx=20)

        badge_f = tk.Frame(nav, bg="#1a1a1a")
        badge_f.pack(side="left", padx=10)
        for g in self.selected:
            gi = next((x for x in GENRES if x["name"] == g), None)
            color = gi["color"] if gi else "#E50914"
            tk.Label(badge_f, text=f" {g} ", font=("Arial", 9, "bold"),
                     bg=color, fg="white", padx=6, pady=3).pack(side="left", padx=3)

        tk.Frame(self, bg="#E50914", height=2).pack(fill="x")

        # 히어로 섹션 (1위 콘텐츠)
        if self.results:
            self._build_hero(self.results[0])

        # 추천 리스트 타이틀
        title_f = tk.Frame(self, bg="#141414", pady=16)
        title_f.pack(fill="x", padx=40)
        tk.Label(title_f, text="취향 기반 추천 콘텐츠",
                 font=("Arial Black", 15), fg="white", bg="#141414").pack(side="left")
        tk.Label(title_f, text=f"총 {len(self.results)}편",
                 font=("Arial", 10), fg="#666666", bg="#141414").pack(side="right")

        # 스크롤 카드 영역
        outer = tk.Frame(self, bg="#141414", height=340)
        outer.pack(fill="x", padx=40, pady=(0, 20))

        canvas = tk.Canvas(outer, bg="#141414", highlightthickness=0, height=320)
        canvas.pack(fill="both", expand=True)

        inner = tk.Frame(canvas, bg="#141414")
        win = canvas.create_window((0, 0), window=inner, anchor="nw")

        inner.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(win, width=e.width))
        canvas.bind("<MouseWheel>",
                    lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        for i, item in enumerate(self.results):
            r, c = divmod(i, 4)
            self._build_card(inner, item, r, c)
            inner.grid_columnconfigure(c, weight=1)

    def _build_hero(self, item):
        hero = tk.Frame(self, bg="#0d0d0d", pady=28)
        hero.pack(fill="x", padx=40)

        left = tk.Frame(hero, bg="#0d0d0d")
        left.pack(side="left", padx=(20, 0), pady=0)


        tk.Label(left, text=item["title"], font=("Arial Black", 30, "bold"),
                 fg="white", bg="#0d0d0d").pack(anchor="w")

        tag_f = tk.Frame(left, bg="#0d0d0d")
        tag_f.pack(anchor="w", pady=8)
        for g in item["genres"]:
            gi = next((x for x in GENRES if x["name"] == g), None)
            color = gi["color"] if gi else "#444"
            tk.Label(tag_f, text=f" {g} ", font=("Arial", 9),
                     bg=color, fg="white", padx=5, pady=2).pack(side="left", padx=3)

        tk.Label(left, text=item["desc"],
                 font=("Arial", 12), fg="#aaaaaa", bg="#0d0d0d",
                 wraplength=440, justify="left").pack(anchor="w", pady=4)

        stars = "★" * int(item["rating"]) + "☆" * (5 - int(item["rating"]))
        tk.Label(left, text=f"{stars}  {item['rating']} / 5.0   ({item['year']})",
                 font=("Arial", 12), fg="#F5C518", bg="#0d0d0d").pack(anchor="w", pady=4)

        match_pct = min(100, int(item.get("match", 1) / max(len(self.selected), 1) * 100))
        tk.Label(left, text=f"취향 일치도  {match_pct}%",
                 font=("Arial", 11, "bold"), fg="#4CAF50", bg="#0d0d0d").pack(anchor="w")

        btn_f = tk.Frame(left, bg="#0d0d0d")
        btn_f.pack(anchor="w", pady=16)

        play = tk.Button(btn_f, text="  ▶  지금 보기  ",
                         font=("Arial", 12, "bold"),
                         bg="white", fg="#141414", relief="flat",
                         padx=16, pady=8, bd=0, cursor="hand2")
        play.pack(side="left", padx=(0, 12))
        play.bind("<Enter>", lambda e: play.config(bg="#dddddd"))
        play.bind("<Leave>", lambda e: play.config(bg="white"))

        plus = tk.Button(btn_f, text="  ＋  내 리스트  ",
                         font=("Arial", 12),
                         bg="#333333", fg="white", relief="flat",
                         padx=16, pady=8, bd=0, cursor="hand2")
        plus.pack(side="left")
        plus.bind("<Enter>", lambda e: plus.config(bg="#444444"))
        plus.bind("<Leave>", lambda e: plus.config(bg="#333333"))

        # 썸네일 (오른쪽)
        right = tk.Frame(hero, bg="#0d0d0d")
        right.pack(side="left", padx=(40, 60), fill="both", expand=True)
        hero_canvas = tk.Canvas(right, bg="#0d0d0d", highlightthickness=0)
        hero_canvas.pack(fill="both", expand=True)
        hero_canvas.bind("<Configure>",
                         lambda e, canvas=hero_canvas, item=item: self._update_hero_thumbnail(canvas, item))

    def _build_card(self, parent, item, row, col):
        outer = tk.Frame(parent, bg="#141414", padx=6, pady=6)
        outer.grid(row=row, column=col, sticky="nsew", padx=5, pady=8)

        card = tk.Frame(outer, bg="#1e1e1e", cursor="hand2")
        card.pack(fill="both", expand=True)

        # 썸네일 캔버스
        thumb = tk.Canvas(card, width=self.CARD_IMAGE_SIZE[0], height=self.CARD_IMAGE_SIZE[1],
                          bg="#1e1e1e", highlightthickness=0)
        thumb.pack(fill="both", expand=True)
        thumb.bind("<Configure>",
                   lambda e, canvas=thumb, item=item: self._update_card_thumbnail(canvas, item))

        # 정보
        info = tk.Frame(card, bg="#1e1e1e", padx=12, pady=10)
        info.pack(fill="x")

        tk.Label(info, text=item["title"], font=("Arial", 11, "bold"),
                 fg="white", bg="#1e1e1e", anchor="w").pack(fill="x")

        tag_f = tk.Frame(info, bg="#1e1e1e")
        tag_f.pack(fill="x", pady=4)
        for g in item["genres"][:2]:
            gi = next((x for x in GENRES if x["name"] == g), None)
            color = gi["color"] if gi else "#444"
            tk.Label(tag_f, text=g, font=("Arial", 8),
                     bg=color, fg="white", padx=4, pady=1).pack(side="left", padx=(0, 4))

        bot = tk.Frame(info, bg="#1e1e1e")
        bot.pack(fill="x")
        stars = "★" * int(item["rating"])
        tk.Label(bot, text=stars,            font=("Arial", 9),        fg="#F5C518", bg="#1e1e1e").pack(side="left")
        tk.Label(bot, text=f" {item['rating']}", font=("Arial", 9, "bold"), fg="#F5C518", bg="#1e1e1e").pack(side="left")
        tk.Label(bot, text=f"  {item['year']}", font=("Arial", 9),         fg="#555555", bg="#1e1e1e").pack(side="left")

        # 호버 효과
        all_w = [card, info, bot, tag_f]

        def on_enter(e):
            for w in all_w:
                try: w.config(bg="#2a2a2a")
                except: pass
            for w in info.winfo_children() + bot.winfo_children() + tag_f.winfo_children():
                try: w.config(bg="#2a2a2a")
                except: pass

        def on_leave(e):
            for w in all_w:
                try: w.config(bg="#1e1e1e")
                except: pass
            for w in info.winfo_children() + bot.winfo_children() + tag_f.winfo_children():
                try: w.config(bg="#1e1e1e")
                except: pass

        for w in [card, info]:
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)

# ── 실행 ──────────────────────────────────────────────────
if __name__ == "__main__":
    app = NetflixApp()
    app.mainloop()
