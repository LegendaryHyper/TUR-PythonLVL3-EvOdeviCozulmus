# "Gamer" sınıfının tanımı
# Görev 2. nickname alanını ekleyin
# Görev 3. email alanını ekleyin
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Görev 4: Mesajı değiştirin
    def introduce(self):
        print(f"Merhaba, benim adım {self.name}, {self.age} yaşındayım. Bana her zaman {self.email} adresine eposta göndererek ulaşabilirsiniz. Beni oyunda {self.nickname} takma adıyla arayın.")


# Oyuncu sınıfının bir örneğini oluşturma
gamer1 = Gamer("Emre", 14, "PrensEmre", "emre@gmail.com")

# Oyunları ekleme
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")

# Bir oyuncunun mini sunumu
gamer1.introduce()

# Favori oyunların çıktısının alınması
print(f"{gamer1.name} şu oyunları seviyor: {', '.join(gamer1.games)}")
