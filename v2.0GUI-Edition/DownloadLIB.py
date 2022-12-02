import pytube as YouTube
import os


def DownloadVideo(entry):
    """Youtube'dan video indirir

    Args:
        entry (tkinter entry object): Giriş nesnesi. İçeriği okunur

    Returns:
        str: Sonucu döndürür. Sondaki ve baştaki boşluklar ayarlı
    """
    url = entry.get()
    try:
        yt = YouTube.YouTube(url)
        video = yt.streams.get_highest_resolution(yt)
        video.download(output_path="C:/Users/muham/Desktop")

        return " İndirme Başrılı!   "

    except Exception as e:
        return " İndirme Başarısız  "


def DownloadAudio(url):
    """Youtube mp3 indiricit

    Args:
        url (str): İndirilecek dosyanın URL'sid

    Returns:
        str: Sonucu döndürür. Sondaki ve baştaki boşluklar ayarlı
    """    
    try:
        yt = YouTube.YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path="C:/Users/muham/Desktop")

        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"

        os.rename(out_file, new_file)
        return " İndirme Başarılı!  "

    except Exception as e:
        return " İndirme Başarısız  "
