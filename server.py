


# server = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
# server.serve_forever()

import http.server
import socketserver

def run_server():
  PORT = 8001
  Handler = http.server.SimpleHTTPRequestHandler
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

run_server()
