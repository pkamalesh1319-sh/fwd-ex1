# EX01 Developing a Simple Webserver
## Date:16-11-2026
## Reg No:26014307

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol List</title>
</head>

<body>

    <center>
        <h1>LIST OF TCP/IP PROTOCOLS</h1>
        <hr width="70%">

        <h2>Network Communication Protocols</h2>

        <table border="1" cellpadding="12" cellspacing="0">
            <tr>
                <th>S.No</th>
                <th>Protocol</th>
                <th>Full Form</th>
                <th>Purpose</th>
            </tr>

            <tr>
                <td>1</td>
                <td>TCP</td>
                <td>Transmission Control Protocol</td>
                <td>Reliable data transfer</td>
            </tr>

            <tr>
                <td>2</td>
                <td>IP</td>
                <td>Internet Protocol</td>
                <td>Addressing and routing</td>
            </tr>

            <tr>
                <td>3</td>
                <td>HTTP</td>
                <td>Hypertext Transfer Protocol</td>
                <td>Web communication</td>
            </tr>

            <tr>
                <td>4</td>
                <td>FTP</td>
                <td>File Transfer Protocol</td>
                <td>File transfer</td>
            </tr>

            <tr>
                <td>5</td>
                <td>DNS</td>
                <td>Domain Name System</td>
                <td>Domain name resolution</td>
            </tr>

            <tr>
                <td>6</td>
                <td>UDP</td>
                <td>User Datagram Protocol</td>
                <td>Fast data transmission</td>
            </tr>

            <tr>
                <td>7</td>
                <td>SMTP</td>
                <td>Simple Mail Transfer Protocol</td>
                <td>Sending emails</td>
            </tr>

            <tr>
                <td>8</td>
                <td>SSH</td>
                <td>Secure Shell</td>
                <td>Secure remote access</td>
            </tr>
        </table>

        <br>
        <hr width="70%">
        <p>End of TCP/IP Protocol List</p>

    </center>

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
~~~
## OUTPUT:
![alt text](<Screenshot 2026-11-14 160125.png>)
![alt text](<Screenshot 2026-11-14 160146.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

