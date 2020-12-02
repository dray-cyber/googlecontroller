import socketserver
import time
import traceback
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from threading import Thread, Timer
import socket
import os
def serve_file(filename, content_type=None):
    class FileHandler(BaseHTTPRequestHandler):
        def do_GET(self):  
            try:
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                if os.path.exists(str(filename)):
                    mediapath = Path(filename)
                    length = mediapath.stat().st_size
                    mtime = mediapath.stat().st_mtime
                    with open(str(mediapath), "rb") as mediafile:
                        while True:
                            data = mediafile.read(100 * 1024)
                            if not data:
                                break
                            self.wfile.write(data)
                else:
                    self.wfile.write(filename)
            except:  
                traceback.print_exc()

            #tthToStopServer.cancel()
            #stopServer(httpd)
    def startServer(httpd):
        httpd.serve_forever()
        httpd.server_close()
    def stopServer(httpd):
        Thread(target = httpd.shutdown).start()
    if content_type is None:
        content_type = "video/mp4"
    httpd = socketserver.TCPServer(("0.0.0.0", 0), FileHandler)
    Thread(target=startServer, args=[httpd]).start()
    tthToStopServer = Timer(60.0, stopServer, args=[httpd])
    tthToStopServer.start()
    local_ip = socket.gethostbyname(socket.gethostname())
    (host, port) = httpd.server_address
    return "http://" + local_ip + ":" + str(port)

    
