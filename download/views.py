from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def download_video(request):
    if request.method == 'POST':
        enlace_video = request.POST['enlace_video']
        ruta_descarga = 'static/videos/'  # Ajusta según tu configuración
        try:
            youtube = YouTube(enlace_video)
            stream = youtube.streams.get_highest_resolution()
            stream.download(ruta_descarga)
            mensaje = "¡Vídeo descargado correctamente!"
        except Exception as e:
            mensaje = f"Error al descargar: {e}"

        return render(request, 'download.html', {'mensaje': mensaje})

    return render(request, 'download.html')