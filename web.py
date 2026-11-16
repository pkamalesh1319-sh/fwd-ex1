from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Unordered List</title>
</head>
<body>

    <h1>TCP/IP Protocols</h1>
    <h2>Unordered List</h2>

    <ul>
        <li>Application Layer
            <ul>
                <li>HTTP</li>
                <li>HTTPS</li>
                <li>FTP</li>
                <li>SMTP</li>
                <li>DNS</li>
                <li>DHCP</li>
            </ul>
        </li>

        <li>Transport Layer
            <ul>
                <li>TCP</li>
                <li>UDP</li>
            </ul>
        </li>

        <li>Internet Layer
            <ul>
                <li>IP</li>
                <li>ICMP</li>
                <li>IGMP</li>
            </ul>
        </li>

        <li>Network Access Layer
            <ul>
                <li>Ethernet</li>
                <li>Wi-Fi</li>
            </ul>
        </li>
    </ul>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()