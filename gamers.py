# "Oyuncu" sınıfının tanımı
# Görev 2. takmaad alanını ekleyin
# Görev 3. Eposta alanını ekleyin
class Oyuncu:
    def __init__(self, ad, yas, takmaad, eposta):
        self.ad = ad
        self.yas = yas

        self.oyunlar = []

    def oyun_ekle(self, oyun):
        self.oyunlar.append(oyun)

    # Görev 4: Mesajı değiştirin
    def tanitim(self):
        print(f"Merhaba, benim adım {self.ad}, ve ben {self.yas} yaşındayım .")


# Oyuncu sınıfının bir örneğini oluşturma
oyuncu1 = Oyuncu("Emre", 14, "PrensEmre", "emre@gmail.com")

# Adding games
oyuncu1.oyun_ekle("Minecraft")
oyuncu1.oyun_ekle("Dota 2")

# Bir oyuncunun mini sunumu
oyuncu1.tanitim()

# Favori oyunların çıktısının alınması
print(f"{oyuncu1.ad} şu oyunları seviyor: {', '.join(oyuncu1.oyunlar)}")
