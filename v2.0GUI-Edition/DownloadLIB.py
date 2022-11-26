import pytube as YouTube
import os


def DownloadVideo(entry):
        url = entry.get()
        try:
            yt = YouTube.YouTube(url)
            video = yt.streams.get_highest_resolution(yt)
            video.download(output_path="C:/Users/muham/Desktop")

            return " İndirme Başrılı!   "

        except Exception as e:
            return " İndirme Başarısız  "


def DownloadAudio(url):
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
