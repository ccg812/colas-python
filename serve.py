import http.server
import socketserver
import os

PORT = 8000

# Asegurarnos de que estamos sirviendo desde el directorio del script
script_dir = os.path.dirname(__file__)
if script_dir:
    os.chdir(script_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"======================================================")
    print(f"  S E R V I D O R   P Y T H O N   A C T I V O")
    print(f"======================================================")
    print(f"  Sirviendo en: http://localhost:{PORT}")
    print(f"  Presiona Ctrl+C para detener el servidor.")
    print(f"======================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n... Servidor detenido.")
        httpd.shutdown()