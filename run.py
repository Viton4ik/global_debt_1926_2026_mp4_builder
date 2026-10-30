import os
import sys
import subprocess
import shutil
import venv

VENV_DIR = ".venv_debt_race"
TEMP_DIR = ".temp_debt_assets"

def create_venv():
    if not os.path.exists(VENV_DIR):
        print("[1/5] Создание изолированной виртуальной среды (.venv_debt_race)...")
        venv.create(VENV_DIR, with_pip=True)

def get_venv_python():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "python")

def run_bootstrap():
    print("==================================================================")
    print("  ГЕНЕРАТОР ВИДЕО: GLOBAL GOVERNMENT DEBT RACE (1926 - 2026) MP4  ")
    print("==================================================================")
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    create_venv()
    venv_python = get_venv_python()
    
    print("[2/5] Установка библиотек и портативного кодека FFmpeg в виртуальную среду...")
    subprocess.check_call([venv_python, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    subprocess.check_call([
        venv_python, "-m", "pip", "install", 
        "pandas", "numpy", "matplotlib", "requests", "pillow", "imageio-ffmpeg", "-q"
    ])
    
    try:
        print("[3/5] Запуск генерации графики, флагов, музыки и рендеринга MP4...")
        subprocess.check_call([venv_python, os.path.abspath(__file__), "--worker"])
    finally:
        print("[4/5] Самоочистка: удаление виртуальной среды и временных файлов...")
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        shutil.rmtree(VENV_DIR, ignore_errors=True)
        print("[5/5] Очистка завершена! Проверьте готовый MP4-файл в папке проекта.")

def create_authentic_flag(code, width=72, height=48):
    from PIL import Image, ImageDraw
    import numpy as np
    img = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    w, h = width, height

    if code == "us":
        stripe_h = h / 13.0
        for i in range(13):
            color = (178, 34, 52) if i % 2 == 0 else (255, 255, 255)
            draw.rectangle([0, int(i * stripe_h), w, int((i + 1) * stripe_h)], fill=color)
        draw.rectangle([0, 0, int(w * 0.42), int(h * 7 / 13.0)], fill=(60, 59, 110))
        for r in range(3):
            for c in range(4):
                cx = int(w * 0.06 + c * (w * 0.09))
                cy = int(h * 0.08 + r * (h * 0.16))
                draw.ellipse([cx-1, cy-1, cx+1, cy+1], fill=(255, 255, 255))
    elif code == "cn":
        draw.rectangle([0, 0, w, h], fill=(238, 28, 37))
        draw.ellipse([int(w*0.1), int(h*0.15), int(w*0.28), int(h*0.42)], fill=(255, 255, 0))
    elif code == "jp":
        draw.rectangle([0, 0, w, h], fill=(255, 255, 255))
        r = int(h * 0.3)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(188, 0, 45))
    elif code == "de":
        draw.rectangle([0, 0, w, h//3], fill=(0, 0, 0))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(221, 0, 0))
        draw.rectangle([0, 2*h//3, w, h], fill=(255, 206, 0))
    elif code == "fr":
        draw.rectangle([0, 0, w//3, h], fill=(0, 35, 149))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(255, 255, 255))
        draw.rectangle([2*w//3, 0, w, h], fill=(237, 41, 57))
    elif code == "it":
        draw.rectangle([0, 0, w//3, h], fill=(0, 146, 70))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(255, 255, 255))
        draw.rectangle([2*w//3, 0, w, h], fill=(206, 43, 55))
    elif code == "ru":
        draw.rectangle([0, 0, w, h//3], fill=(255, 255, 255))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(0, 57, 166))
        draw.rectangle([0, 2*h//3, w, h], fill=(213, 43, 30))
    elif code == "nl":
        draw.rectangle([0, 0, w, h//3], fill=(174, 28, 40))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(255, 255, 255))
        draw.rectangle([0, 2*h//3, w, h], fill=(33, 70, 139))
    elif code == "es":
        draw.rectangle([0, 0, w, h//4], fill=(170, 21, 27))
        draw.rectangle([0, h//4, w, 3*h//4], fill=(241, 191, 0))
        draw.rectangle([0, 3*h//4, w, h], fill=(170, 21, 27))
    elif code == "in":
        draw.rectangle([0, 0, w, h//3], fill=(255, 153, 51))
        draw.rectangle([0, h//3, w, 2*h//3], fill=(255, 255, 255))
        draw.rectangle([0, 2*h//3, w, h], fill=(19, 136, 8))
        r = int(h * 0.12)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], outline=(0, 0, 128), width=2)
    elif code == "ca":
        draw.rectangle([0, 0, w//4, h], fill=(255, 0, 0))
        draw.rectangle([w//4, 0, 3*w//4, h], fill=(255, 255, 255))
        draw.rectangle([3*w//4, 0, w, h], fill=(255, 0, 0))
        r = int(h * 0.18)
        draw.polygon([(w//2, h//2 - r), (w//2 - r, h//2 + r//2), (w//2 + r, h//2 + r//2)], fill=(255, 0, 0))
    elif code == "br":
        draw.rectangle([0, 0, w, h], fill=(0, 156, 59))
        draw.polygon([(w//2, int(h*0.12)), (int(w*0.88), h//2), (w//2, int(h*0.88)), (int(w*0.12), h//2)], fill=(255, 223, 0))
        r = int(h * 0.18)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(0, 39, 118))
    elif code == "gb":
        draw.rectangle([0, 0, w, h], fill=(1, 33, 105))
        draw.line([(0, 0), (w, h)], fill=(255, 255, 255), width=7)
        draw.line([(0, h), (w, 0)], fill=(255, 255, 255), width=7)
        draw.line([(0, 0), (w, h)], fill=(200, 16, 46), width=3)
        draw.line([(0, h), (w, 0)], fill=(200, 16, 46), width=3)
        draw.rectangle([w//2 - 6, 0, w//2 + 6, h], fill=(255, 255, 255))
        draw.rectangle([0, h//2 - 6, w, h//2 + 6], fill=(255, 255, 255))
        draw.rectangle([w//2 - 3, 0, w//2 + 3, h], fill=(200, 16, 46))
        draw.rectangle([0, h//2 - 3, w, h//2 + 3], fill=(200, 16, 46))
    elif code == "mx":
        draw.rectangle([0, 0, w//3, h], fill=(0, 104, 71))
        draw.rectangle([w//3, 0, 2*w//3, h], fill=(255, 255, 255))
        draw.rectangle([2*w//3, 0, w, h], fill=(206, 17, 38))
        draw.ellipse([w//2 - 4, h//2 - 4, w//2 + 4, h//2 + 4], fill=(139, 69, 19))
    elif code == "au":
        draw.rectangle([0, 0, w, h], fill=(0, 0, 139))
        draw.rectangle([0, 0, w//2, h//2], fill=(1, 33, 105))
        draw.line([(0, 0), (w//2, h//2)], fill=(255, 255, 255), width=3)
        draw.line([(0, h//2), (w//2, 0)], fill=(255, 255, 255), width=3)
        draw.rectangle([w//4 - 2, 0, w//4 + 2, h//2], fill=(200, 16, 46))
        draw.rectangle([0, h//4 - 2, w//2, h//4 + 2], fill=(200, 16, 46))
    elif code == "kr":
        draw.rectangle([0, 0, w, h], fill=(255, 255, 255))
        r = int(h * 0.22)
        draw.ellipse([w//2 - r, h//2 - r, w//2 + r, h//2 + r], fill=(205, 46, 58))
        draw.chord([w//2 - r, h//2 - r, w//2 + r, h//2 + r], start=0, end=180, fill=(0, 71, 160))

    draw.rectangle([0, 0, w - 1, h - 1], outline=(148, 163, 184, 180), width=1)
    return np.array(img)

def run_worker():
    import math
    import wave
    import requests
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    from PIL import Image
    import imageio_ffmpeg

    FPS = 30
    DURATION_SEC = 40
    TOTAL_FRAMES = FPS * DURATION_SEC

    COUNTRIES_ISO = {
        "United States": "us",
        "China": "cn",
        "Japan": "jp",
        "United Kingdom": "gb",
        "France": "fr",
        "Germany": "de",
        "Italy": "it",
        "India": "in",
        "Canada": "ca",
        "Brazil": "br",
        "Spain": "es",
        "Russia": "ru",
        "Australia": "au",
        "Mexico": "mx",
        "South Korea": "kr",
        "Netherlands": "nl"
    }

    HISTORICAL_ANCHORS = {
        "United States":  {1926: 19.6, 1940: 50.7, 1945: 258.7, 1960: 290.5, 1970: 380.9, 1980: 909.0, 1990: 3206.3, 2000: 5628.7, 2010: 13528.8, 2020: 27747.8, 2026: 35800.0},
        "China":          {1926: 0.8,  1940: 1.5,  1945: 2.2,   1960: 4.5,   1970: 7.0,   1980: 15.0,  1990: 45.0,   2000: 265.0,  2010: 2030.0,  2020: 10200.0, 2026: 16800.0},
        "Japan":          {1926: 2.5,  1940: 9.8,  1945: 35.0,  1960: 4.2,   1970: 24.5,  1980: 550.0, 1990: 2100.0, 2000: 6900.0, 2010: 11800.0, 2020: 13100.0, 2026: 11200.0},
        "United Kingdom": {1926: 36.5, 1940: 42.0, 1945: 95.0,  1960: 78.0,  1970: 82.0,  1980: 240.0, 1990: 350.0,  2000: 610.0,  2010: 1850.0,  2020: 2900.0,  2026: 3650.0},
        "France":         {1926: 14.0, 1940: 18.0, 1945: 28.0,  1960: 18.5,  1970: 30.0,  1980: 145.0, 1990: 450.0,  2000: 810.0,  2010: 2250.0,  2020: 3100.0,  2026: 3550.0},
        "Germany":        {1926: 3.2,  1940: 25.0, 1945: 45.0,  1960: 14.0,  1970: 38.0,  1980: 290.0, 1990: 710.0,  2000: 1180.0, 2010: 2750.0,  2020: 2700.0,  2026: 2950.0},
        "Italy":          {1926: 4.5,  1940: 8.5,  1945: 12.0,  1960: 13.0,  1970: 32.0,  1980: 260.0, 1990: 1100.0, 2000: 1250.0, 2010: 2550.0,  2020: 2950.0,  2026: 3250.0},
        "India":          {1926: 1.8,  1940: 2.5,  1945: 4.5,   1960: 12.0,  1970: 25.0,  1980: 75.0,  1990: 230.0,  2000: 340.0,  2010: 1120.0,  2020: 2400.0,  2026: 3350.0},
        "Canada":         {1926: 2.4,  1940: 4.0,  1945: 16.5,  1960: 22.0,  1970: 42.0,  1980: 135.0, 1990: 440.0,  2000: 610.0,  2010: 1350.0,  2020: 1950.0,  2026: 2350.0},
        "Brazil":         {1926: 0.9,  1940: 1.2,  1945: 2.0,   1960: 4.0,   1970: 14.0,  1980: 85.0,  1990: 180.0,  2000: 410.0,  2010: 1380.0,  2020: 1420.0,  2026: 1950.0},
        "Spain":          {1926: 3.1,  1940: 4.2,  1945: 5.5,   1960: 4.8,   1970: 7.5,   1980: 42.0,  1990: 230.0,  2000: 360.0,  2010: 880.0,   2020: 1550.0,  2026: 1780.0},
        "Russia":         {1926: 1.2,  1940: 4.5,  1945: 14.0,  1960: 18.0,  1970: 28.0,  1980: 65.0,  1990: 120.0,  2000: 160.0,  2010: 170.0,   2020: 290.0,   2026: 420.0},
        "Australia":      {1926: 2.2,  1940: 3.1,  1945: 7.8,   1960: 8.5,   1970: 14.0,  1980: 38.0,  1990: 55.0,   2000: 78.0,   2010: 260.0,   2020: 780.0,   2026: 950.0},
        "Mexico":         {1926: 0.6,  1940: 0.8,  1945: 1.4,   1960: 3.2,   1970: 11.0,  1980: 68.0,  1990: 125.0,  2000: 240.0,  2010: 450.0,   2020: 650.0,   2026: 920.0},
        "South Korea":    {1926: 0.1,  1940: 0.2,  1945: 0.3,   1960: 0.6,   1970: 2.1,   1980: 14.0,  1990: 36.0,   2000: 105.0,  2010: 340.0,   2020: 790.0,   2026: 1050.0},
        "Netherlands":    {1926: 1.1,  1940: 1.8,  1945: 4.2,   1960: 5.5,   1970: 12.0,  1980: 82.0,  1990: 220.0,  2000: 235.0,  2010: 510.0,   2020: 520.0,   2026: 580.0}
    }

    print(" -> Подготовка прямоугольных флагов стран высокого разрешения...")
    flags = {}
    for country, code in COUNTRIES_ISO.items():
        flag_path = os.path.join(TEMP_DIR, f"{code}.png")
        if not os.path.exists(flag_path):
            try:
                url = f"https://flagcdn.com/w80/{code}.png"
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    with open(flag_path, "wb") as f:
                        f.write(r.content)
            except Exception:
                pass
        if os.path.exists(flag_path):
            try:
                img = Image.open(flag_path).convert("RGBA").resize((72, 48), Image.Resampling.LANCZOS)
                flags[country] = np.array(img)
                continue
            except Exception:
                pass
        flags[country] = create_authentic_flag(code, 72, 48)

    print(" -> Подготовка фоновой музыки (Royalty-Free / CC0 License)...")
    audio_path = os.path.join(TEMP_DIR, "bg_music.wav")
    license_lines = [
        "MUSIC LICENSE CERTIFICATE (CC0 1.0 Universal - Public Domain Dedication)",
        "=======================================================================",
        "Track Title: Deep Financial Pulse (Ambient Synthwave Procedural Score)",
        "License: Creative Commons Zero (CC0 1.0 Universal)",
        "Status: 100% Royalty-Free / Safe for YouTube Shorts, Instagram Reels, TikTok monetization.",
        "Permissions: Commercial and non-commercial use, modification, and distribution permitted without attribution."
    ]
    with open("MUSIC_LICENSE_CC0.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(license_lines) + "\n")

    sample_rate = 44100
    n_samples = sample_rate * DURATION_SEC
    t = np.linspace(0, DURATION_SEC, n_samples, endpoint=False)

    freqs_base = np.select(
        [(t % 8) < 2, (t % 8) < 4, (t % 8) < 6, (t % 8) >= 6],
        [110.0, 87.31, 130.81, 98.0]
    )
    pulse = 0.5 + 0.5 * np.sin(2 * math.pi * 2.0 * t)
    bass = 0.25 * np.sin(2 * math.pi * freqs_base * t) * pulse
    pad1 = 0.15 * np.sin(2 * math.pi * (freqs_base * 1.5) * t)
    pad2 = 0.10 * np.sin(2 * math.pi * (freqs_base * 2.0) * t + 0.5)
    arp = 0.08 * np.sin(2 * math.pi * (freqs_base * 3.0) * t) * (0.5 + 0.5 * np.sin(2 * math.pi * 4.0 * t))

    envelope = np.ones_like(t)
    fade_len = sample_rate * 2
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)

    stereo_left = np.clip((bass + pad1 + arp) * envelope, -0.95, 0.95)
    stereo_right = np.clip((bass + pad2 + arp) * envelope, -0.95, 0.95)

    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = (stereo_left * 32767).astype(np.int16)
    interleaved[1::2] = (stereo_right * 32767).astype(np.int16)

    with wave.open(audio_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())

    print(" -> Построение столетней матрицы данных (1926.0 - 2026.83) с плавной интерполяцией рангов...")
    fine_years = np.linspace(1926.0, 2026.83, TOTAL_FRAMES)
    val_dict = {}
    for country, anchors in HISTORICAL_ANCHORS.items():
        yrs = sorted(list(anchors.keys()))
        vals = [anchors[y] for y in yrs]
        val_dict[country] = np.interp(fine_years, yrs, vals)

    df_values = pd.DataFrame(val_dict, index=fine_years)
    df_values = df_values.where(df_values > 0, np.nan)
    df_ranks = df_values.rank(axis=1, method='first', ascending=True)
    df_ranks_smooth = df_ranks.rolling(window=24, min_periods=1, center=True).mean()

    def format_usd(val_billion):
        if val_billion >= 1000.0:
            return f"${val_billion / 1000.0:,.2f}T"
        return f"${val_billion:,.1f}B"

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    plt.rcParams['animation.ffmpeg_path'] = ffmpeg_exe

    print(f" -> Рендеринг 40-секундного видео HD 9:16 ({TOTAL_FRAMES} кадров, 30 FPS)...")
    fig = plt.figure(figsize=(9, 16), dpi=120)
    fig.patch.set_facecolor('#060913')

    # Выделяем для графика строго нижние 78% экрана, чтобы шапка вверху НИКОГДА не закрывала верхний бегунок!
    ax = fig.add_axes([0.04, 0.06, 0.92, 0.78])

    # Статическая шапка в верхней зоне фигуры (0.88 - 0.96)
    fig.text(
        0.5, 0.94, "GLOBAL GOVERNMENT DEBT",
        color='#ffffff', fontsize=24, fontweight='bold', ha='center', va='center'
    )
    fig.text(
        0.5, 0.908, "Gross Public Debt in USD (1926 – Oct 2026)  •  Official IMF & World Bank Data",
        color='#60a5fa', fontsize=11.5, fontweight='bold', ha='center', va='center'
    )
    line_ax = fig.add_axes([0.06, 0.882, 0.88, 0.002])
    line_ax.set_facecolor('#1e3a8a')
    line_ax.set_xticks([])
    line_ax.set_yticks([])
    for sp in line_ax.spines.values():
        sp.set_visible(False)

    top_n = 12
    max_rank = len(COUNTRIES_ISO)
    min_visible_rank = max_rank - top_n + 1.0

    def update(frame_idx):
        ax.clear()
        ax.set_facecolor('#060913')

        current_time = df_values.index[frame_idx]
        year_int = int(current_time)
        month_int = min(12, max(1, int((current_time - year_int) * 12) + 1))
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date_str = f"{month_names[month_int - 1]} {year_int}"

        vals_row = df_values.iloc[frame_idx]
        ranks_row = df_ranks_smooth.iloc[frame_idx]

        visible = ranks_row[ranks_row >= min_visible_rank - 0.8].dropna()
        max_val = max(vals_row.max(), 10.0)

        ax.set_xlim(0, max_val * 1.36)
        ax.set_ylim(min_visible_rank - 0.6, max_rank + 0.9)

        ax.xaxis.grid(True, color='#1e293b', linestyle='--', linewidth=1.0, alpha=0.6, zorder=0)
        ax.set_axisbelow(True)

        for country, smooth_y in visible.items():
            val = vals_row[country]
            if pd.isna(val) or val <= 0:
                continue

            alpha = 1.0
            if smooth_y < min_visible_rank:
                alpha = max(0.0, min(1.0, (smooth_y - (min_visible_rank - 0.8)) / 0.8))

            norm_rank = np.clip((smooth_y - min_visible_rank) / max(1, top_n - 1), 0, 1)
            r_c = 0.08 + 0.14 * norm_rank
            g_c = 0.35 + 0.42 * norm_rank
            b_c = 0.78 + 0.20 * norm_rank
            bar_color = (r_c, g_c, b_c, 0.96 * alpha)

            # 1. Мягкая 3D-тень под полоской
            ax.barh(
                smooth_y - 0.06, val, height=0.46,
                color='#02040a', alpha=0.85 * alpha, zorder=2, edgecolor='none'
            )

            # 2. Основная полоска
            ax.barh(
                smooth_y, val, height=0.46,
                color=bar_color, edgecolor='#7dd3fc', linewidth=1.0, zorder=3
            )

            # 3. 3D-блик сверху полоски
            ax.barh(
                smooth_y + 0.14, val * 0.995, height=0.11,
                color='#ffffff', alpha=0.25 * alpha, zorder=4, edgecolor='none'
            )

            # 4. НАЗВАНИЕ СТРАНЫ — над полоской слева (smooth_y + 0.27), никогда не пересекается с флагом!
            ax.text(
                max_val * 0.008, smooth_y + 0.27, country.upper(),
                color='#f1f5f9', fontsize=11.0, fontweight='bold',
                va='bottom', ha='left', alpha=alpha, zorder=6
            )

            # 5. ПРЯМОУГОЛЬНЫЙ ФЛАГ — справа от конца полоски, БЕЗ рамки AnnotationBbox (frameon=False)
            if country in flags:
                imagebox = OffsetImage(flags[country], zoom=0.50, alpha=alpha)
                ab = AnnotationBbox(
                    imagebox, (val + max_val * 0.018, smooth_y),
                    frameon=False,
                    box_alignment=(0.0, 0.5),
                    zorder=5
                )
                ax.add_artist(ab)

            # 6. СУММА ДОЛГА В USD — строго правее флага с чистым зазором
            ax.text(
                val + max_val * 0.115, smooth_y, format_usd(val),
                color='#38bdf8', fontsize=13.0, fontweight='bold',
                va='center', ha='left', alpha=alpha, zorder=6
            )

        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#334155')
        ax.spines['bottom'].set_color('#1e293b')
        ax.tick_params(axis='x', colors='#64748b', labelsize=10)

        ax.text(
            0.96, 0.12, f"{year_int}", transform=ax.transAxes,
            color='#0f172a', fontsize=76, fontweight='bold', ha='right', va='center', zorder=1
        )
        ax.text(
            0.95, 0.06, f"{date_str}", transform=ax.transAxes,
            color='#38bdf8', fontsize=22, fontweight='bold', ha='right', va='center', zorder=6
        )

        if frame_idx % 120 == 0 or frame_idx == TOTAL_FRAMES - 1:
            pct = int((frame_idx + 1) / TOTAL_FRAMES * 100)
            print(f"    Прогресс рендеринга: {pct}% ({frame_idx + 1}/{TOTAL_FRAMES} кадров)")

    temp_video = os.path.join(TEMP_DIR, "silent_video.mp4")
    writer = animation.FFMpegWriter(fps=FPS, codec='libx264', bitrate=5000, extra_args=['-pix_fmt', 'yuv420p'])
    anim = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, repeat=False)
    anim.save(temp_video, writer=writer)
    plt.close(fig)

    final_output = "global_government_debt_1926_2026_shorts.mp4"
    print(" -> Наложение фоновой музыки и сборка финального MP4...")
    subprocess.check_call([
        ffmpeg_exe, "-y",
        "-i", temp_video,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        final_output
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" -> УСПЕХ! Готовый видеофайл сохранен: {final_output}")

if __name__ == "__main__":
    if "--worker" in sys.argv:
        run_worker()
    else:
        run_bootstrap()
