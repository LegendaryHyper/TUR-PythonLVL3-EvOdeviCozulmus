import pytest
from gamers import Oyuncu


def test_Gorev_1_ad_ve_yas_kontrol():
    oyuncu = Oyuncu("Emre", 14, "PrensEmre", "emre@gmail.com")
    assert hasattr(oyuncu, 'ad'), "Görev 1 tamamlanmadı. 'Oyuncu' sınıfı 'ad' niteliğini içermiyor"
    assert hasattr(oyuncu, 'yas'), "Görev 1 tamamlanmadı. 'Oyuncu' sınıfı 'yas' özniteliğini içermiyor"


def test_Gorev_2_ekle_takmaad():
    oyuncu = Oyuncu("Emre", 14, "PrensEmre", "emre@gmail.com")
    assert hasattr(oyuncu, 'takmaad'), "Görev 2 tamamlanmadı. 'Oyuncu' sınıfı 'takmaad' niteliğini içermiyor"


def test_Gorev_3_ekle_eposta():
    oyuncu = Oyuncu("Emre", 14, "PrensEmre", "emre@gmail.com")
    assert hasattr(Oyuncu, 'eposta'), "Görev 3 tamamlanmadı. 'Oyuncu' sınıfı 'eposta' niteliğini içermiyor"


def test_Task_4_degistir_mesaj(capsys):
    oyuncu = Oyuncu("Emre", 14, "PrensEmre", "emre@gmail.com")
    oyuncu.tanitim()
    yakalanan = capsys.readouterr()
    beklenen_cikti = "Merhaba, benim adım Emre, 14 yaşındayım. Bana her zaman emre@gmail.com adresine eposta göndererek ulaşabilirsiniz. Beni oyunda PrensEmre takma adıyla arayın."
    assert beklenen_cikti in yakalanan.out, f"Görev 4 tamamlanmadı. Beklenen mesaj: {beklenen_cikti}, Alınan çıktı: {yakalanan.out}"


if __name__ == "__main__":
    pytest.main(["-v"])
