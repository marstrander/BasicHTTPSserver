'''
Basic HTTPS Server for testing purposes.
Do not use in production.
'''
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys

if len(sys.argv) < 4:
    print('\n(*) USAGE:\t python3 BasicHTTPSserver.py server_ip server_port key certificate')
    print('(*) Example:\t python3 BasicHTTPSserver.py 10.1.10.99 4443 cert.key cert.pem\n')
    sys.exit()

httpd = HTTPServer((sys.argv[1], int(sys.argv[2])), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile=sys.argv[3],
        certfile=sys.argv[4], server_side=True)

print('\n' + '-' * 80 + '\n')
print('Server running on https://' + sys.argv[1] + ':' + str(sys.argv[2]) + '\n')
print('-' * 80 + '\n')

httpd.serve_forever()