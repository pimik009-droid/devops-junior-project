from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Это наше "блюдо"
        message = "<h1>Привет! Это мой первый DevOps проект!</h1><p>Я запустил это в Docker контейнере.</p>"
        self.wfile.write(message.encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Сервер запущен на порту 8080...")
    server.serve_forever()