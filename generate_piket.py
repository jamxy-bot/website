with open('index.html', encoding='utf-8') as f:
    h = f.read()

import re

# We will replace the entire Piket section to use the new names
new_names = [
    "Adira Pratama",
    "Muhammad Arjuna Wibawa",
    "Shyva Dwi Amanda",
    "Syahwa Juarefi",
    "Alif Khairul Azzam",
    "Anatasya Salsabila",
    "Bintang Trihadi",
    "Deacon Al Hakim Stefan",
    "Dinda Ariani Saragih",
    "Eka Purnama Dewi",
    "Faa'iq",
    "Faqiha Rahma Khoirunnisa",
    "Gracia Samaria Simanjuntak",
    "Irene Debora Siahaan",
    "Jhon Roy Samosir",
    "Jihan Aprilia",
    "Juniarti Tampubolon",
    "Kasih Nur'aini",
    "Keyna Rahzalia",
    "Lutfiah Sakirah",
    "Mariana Jelena Sibuea",
    "Marvel Jala Sinaga",
    "Maulida Luthfiah",
    "Muhamad Fadhli",
    "Muhamad Rangga Wibowo"
]

days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
piket_html = ""
for i, day in enumerate(days):
    piket_html += f'    <div class="piket-card glass reveal"><p class="piket-day">{day}</p><div class="piket-names">'
    day_names = new_names[i*5 : (i+1)*5]
    for name in day_names:
        # Escape single quotes just in case
        name_esc = name.replace("'", "&#39;")
        piket_html += f'<div class="piket-name-item"><span class="piket-dot"></span>{name_esc}</div>'
    piket_html += '</div></div>\n'

print(piket_html)
