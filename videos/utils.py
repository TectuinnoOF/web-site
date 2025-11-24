import re

def obtener_id_youtube(url):
    # Casos: youtu.be/<id> | youtube.com/watch?v=<id> | youtube.com/embed/<id>
    patron = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
    match = re.search(patron, url)
    return match.group(1) if match else None
