"""Serve the math classroom on an automatically allocated slot 7 port."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess


class Handler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(404)
        return None

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()


if __name__ == '__main__':
    public = Path(__file__).resolve().parent / 'public'
    with ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(public))) as server:
        port = server.server_address[1]
        (Path.home() / '.service_port7').write_text(f'{port}\n')
        subprocess.run(['/usr/bin/sudo', '-n', '/usr/local/bin/set-stu-nginx.sh', 'stu60', '7'], check=True)
        print(f'Math classroom listening on 127.0.0.1:{port}', flush=True)
        server.serve_forever()
