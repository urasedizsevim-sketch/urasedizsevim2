import os
import subprocess

HTML_DOSYASI = "oyun-radari.html"
TXT_DOSYASI = "oyunlar.txt"


def radar_guncelle():
    print("🔍 UES Radar aktif... oyunlar.txt taranıyor.")

    if not os.path.exists(TXT_DOSYASI):
        with open(TXT_DOSYASI, "w", encoding="utf-8") as f:
            f.write("Epic Games | GTA V Premium | 749 | 3 Gün | https://store.epicgames.com\n")
            f.write("Steam | Half-Life 2 | 105 | 12 Saat | https://store.steampowered.com\n")
        print("📁 oyunlar.txt bulunamadı, örnek şablon oluşturuldu!")

    yeni_kartlar_html = ""
    with open(TXT_DOSYASI, "r", encoding="utf-8") as f:
        satirlar = f.readlines()

        for satir in satirlar:
            if satir.strip() == "":
                continue

            bilgiler = satir.strip().split("|")
            if len(bilgiler) >= 5:
                platform = bilgiler[0].strip()
                oyun_adi = bilgiler[1].strip()
                eski_fiyat = bilgiler[2].strip()
                sure = bilgiler[3].strip()
                link = bilgiler[4].strip()

                tag_class = "tag-epic"
                if platform.lower() == "steam":
                    tag_class = "tag-steam"
                elif platform.lower() == "gog":
                    tag_class = "tag-gog"

                kart = f"""
        <div class="game-card">
            <div>
                <span class="platform-tag {tag_class}">{platform}</span>
                <div class="game-title">{oyun_adi}</div>
                <div class="price-container">
                    <span class="old-price">₺{eski_fiyat}</span>
                    <span class="free-price">BEDAVA</span>
                </div>
                <div class="time-left">⏳ Fırsatın Bitmesine: <b>{sure}</b></div>
            </div>
            <a href="{link}" target="_blank" class="claim-btn">Hemen Kap 🚀</a>
        </div>"""
                yeni_kartlar_html += kart

    print("⚙️ HTML kartları üretildi, siteye enjekte ediliyor...")

    with open(HTML_DOSYASI, "r", encoding="utf-8") as f:
        html_icerik = f.read()

    baslangic = "<!-- GAMES_START -->"
    bitis = "<!-- GAMES_END -->"

    ilk_kisim = html_icerik.split(baslangic)[0]
    son_kisim = html_icerik.split(bitis)[1]

    yeni_html = ilk_kisim + baslangic + "\n" + yeni_kartlar_html + "\n        " + bitis + son_kisim

    with open(HTML_DOSYASI, "w", encoding="utf-8") as f:
        f.write(yeni_html)

    print("✅ Radar başarıyla güncellendi!")
git_path = r"C:\Users\Uras\AppData\Local\Programs\Git\cmd\git.exe"

def githuba_firlat():
    print("\n🚀 GitHub'a bağlanılıyor...")
    try:
        subprocess.run([git_path, "config", "--global", "user.email", "urasedizsevim@gmail.com"], check=True)
        subprocess.run([git_path, "config", "--global", "user.name", "urasedizsevim"], check=True)

        subprocess.run([git_path, "add", "."], check=True)
        subprocess.run([git_path, "commit", "-m", "Bot: Yeni bedava oyunlar radara eklendi 🎁"], check=True)
        subprocess.run([git_path, "push"], check=True)
        print("🌐 UES Terminal: Oyun radarı canlıya alındı!")
    except Exception as e:
        print(f"❌ Git isleminde hata oluştu: {e}")


if __name__ == "__main__":
    print("🤖 UES Gamer Bot Başlatıldı...\n")

    radar_guncelle()

    githuba_firlat()