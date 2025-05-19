from http.server import BaseHTTPRequestHandler, HTTPServer

class ServidorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/servidor':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), ServidorHandler)
    print('Servidor de salud corriendo en http://localhost:8000/servidor')
    server.serve_forever()
