import http.server
import socketserver
import os

# --- ESTA ES LA PARTE IMPORTANTE PARA RENDER ---
# Render te da un puerto dinámico a través de la variable de entorno PORT
# Usamos os.environ.get() para leerla, y si no existe (local), usamos 8000
PORT = int(os.environ.get('PORT', 8000))
# -----------------------------------------------

# Asegurarnos de que estamos sirviendo desde el directorio del script
script_dir = os.path.dirname(__file__)
if script_dir:
    os.chdir(script_dir)

Handler = http.server.SimpleHTTPRequestHandler

# --- AQUÍ ESTÁ LA CORRECCIÓN ---
# Debe ser TCPServer (con S mayúscula), no TCServer
with socketserver.TCPServer(("", PORT), Handler) as httpd:
# ---------------------------------
    print(f"======================================================")
    print(f"  S E R V I D O R   P Y T H O N   A C T I V O")
    print(f"======================================================")
    print(f"  Sirviendo en: http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n... Servidor detenido.")
        httpd.shutdown()
