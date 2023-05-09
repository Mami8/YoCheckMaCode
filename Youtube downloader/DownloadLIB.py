import pytube as YouTube
import os


def DownloadVideo(url):
        try:
            # Video indiriliyor. Yol belirtilmediği için kodun çalıştırıldığı dizine indirecek
            yt = YouTube.YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()

            return "İndirme Başrılı!"

        except Exception as e:
            print(e)
            return "İndirme Başarısız"


def DownloadAudio(url):
    try:
        yt = YouTube.YouTube(url)
        
        # Ses dosyaları mp3 olarak kaydedilmeli. Dolayısıyla linkten sadece sesi filtreliyoruz 
        # Ardından çıktı yolunu bir değişkene atıyoruz. Bu daha sonra uzantıyı mp3 yapmak için
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download()

        # Dosya yolundan uzantı ayırıyoruz.
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"

        # Uzantısı düzelmiş haliyle yeniden adlandırıyoruz.
        os.rename(out_file, new_file)
        return "İndirme Başarılı!"
    # Hatayı konsola yazdırıyoruz. VSCode gibi bir uygulamadan çalıştırıldığında konsola erişmek mümkün.
    # NOT: Bunu bir txt dosyasına yazdırsan daha kullanışlı olur. Lakin hatalar sıralanmalı. Hataları biraz daha öğrenince yabarsin
    except Exception as e:
        print(e)
        return "İndirme Başarısız"