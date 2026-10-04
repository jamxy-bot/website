with open('index.html', encoding='utf-8') as f:
    h = f.read()

import re

new_piket = """  <div class="piket-grid">
    <div class="piket-card glass reveal"><p class="piket-day">Senin</p><div class="piket-names"><div class="piket-name-item"><span class="piket-dot"></span>Adira Pratama</div><div class="piket-name-item"><span class="piket-dot"></span>Muhammad Arjuna Wibawa</div><div class="piket-name-item"><span class="piket-dot"></span>Shyva Dwi Amanda</div><div class="piket-name-item"><span class="piket-dot"></span>Syahwa Juarefi</div><div class="piket-name-item"><span class="piket-dot"></span>Alif Khairul Azzam</div></div></div>
    <div class="piket-card glass reveal"><p class="piket-day">Selasa</p><div class="piket-names"><div class="piket-name-item"><span class="piket-dot"></span>Anatasya Salsabila</div><div class="piket-name-item"><span class="piket-dot"></span>Bintang Trihadi</div><div class="piket-name-item"><span class="piket-dot"></span>Deacon Al Hakim Stefan</div><div class="piket-name-item"><span class="piket-dot"></span>Dinda Ariani Saragih</div><div class="piket-name-item"><span class="piket-dot"></span>Eka Purnama Dewi</div></div></div>
    <div class="piket-card glass reveal"><p class="piket-day">Rabu</p><div class="piket-names"><div class="piket-name-item"><span class="piket-dot"></span>Faa&#39;iq</div><div class="piket-name-item"><span class="piket-dot"></span>Faqiha Rahma Khoirunnisa</div><div class="piket-name-item"><span class="piket-dot"></span>Gracia Samaria Simanjuntak</div><div class="piket-name-item"><span class="piket-dot"></span>Irene Debora Siahaan</div><div class="piket-name-item"><span class="piket-dot"></span>Jhon Roy Samosir</div></div></div>
    <div class="piket-card glass reveal"><p class="piket-day">Kamis</p><div class="piket-names"><div class="piket-name-item"><span class="piket-dot"></span>Jihan Aprilia</div><div class="piket-name-item"><span class="piket-dot"></span>Juniarti Tampubolon</div><div class="piket-name-item"><span class="piket-dot"></span>Kasih Nur&#39;aini</div><div class="piket-name-item"><span class="piket-dot"></span>Keyna Rahzalia</div><div class="piket-name-item"><span class="piket-dot"></span>Lutfiah Sakirah</div></div></div>
    <div class="piket-card glass reveal"><p class="piket-day">Jumat</p><div class="piket-names"><div class="piket-name-item"><span class="piket-dot"></span>Mariana Jelena Sibuea</div><div class="piket-name-item"><span class="piket-dot"></span>Marvel Jala Sinaga</div><div class="piket-name-item"><span class="piket-dot"></span>Maulida Luthfiah</div><div class="piket-name-item"><span class="piket-dot"></span>Muhamad Fadhli</div><div class="piket-name-item"><span class="piket-dot"></span>Muhamad Rangga Wibowo</div></div></div>
  </div>"""

h = re.sub(r'  <div class="piket-grid">.*?  </div>', new_piket, h, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

print('Piket updated.')
