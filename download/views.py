from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def download_video(request):
    if request.method == 'POST':
        enlace_video = request.POST['enlace_video']
        ruta_descarga = 'videos/'  # Ajusta según tu configuración
        try:
            youtube = YouTube(enlace_video)
            stream = youtube.streams.get_highest_resolution()
            stream.download(ruta_descarga)
            mensaje = "¡Vídeo descargado correctamente!"
        except Exception:
            mensaje = "ingrese la url"

        return render(request, 'download.html', {'mensaje': mensaje})

    return render(request, 'download.html')