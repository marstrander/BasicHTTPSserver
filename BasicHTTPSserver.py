from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys

if len(sys.argv) < 5:
    print('\n(*) USAGE:\t python3 {0} server_ip server_port key certificate'.format(sys.argv[0]))
    print('(*) Example:\t python3 {0} 10.1.10.99 443 cert.key cert.pem\n'.format(sys.argv[0]))
    sys.exit()

handler = HTTPServer((sys.argv[1], int(sys.argv[2])), SimpleHTTPRequestHandler)
handler.socket = ssl.wrap_socket (handler.socket,
        keyfile=sys.argv[3],
        certfile=sys.argv[4], server_side=True)

with handler as httpd:
    print('\n' + '-' * 80 + '\n')
    print('Server running on https://{0}{1}\n'.format(sys.argv[1], sys.argv[2]))
    print('-' * 80 + '\n')
    httpd.serve_forever()
