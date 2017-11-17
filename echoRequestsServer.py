from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request_path = self.path

        print("\n !! ~~~~~~~~~~~~~ REQUEST START ~~~~~~~~~~~~ !!\n")
        print(request_path)
        print(self.headers)
        print("\n !! ~~~~~~~~~~~~~ REQUEST END ~~~~~~~~~~~~ !!\n")

        self.send_response(200)
        # self.send_header("v", "k")

    def do_POST(self):
        request_path = self.path

        print("\n !! ~~~~~~~~~~~~~ REQUEST START ~~~~~~~~~~~~ !!\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        clength = 0
        if content_length:
            clength = content_length[0]

        print(request_headers)
        print(self.rfile.read(clength))
        print("\n !! ~~~~~~~~~~~~~ REQUEST END ~~~~~~~~~~~~ !!\n")

        self.send_response(200)

    def do_DELETE(self):
        request_path = self.path

        print("\n !! ~~~~~~~~~~~~~ REQUEST START ~~~~~~~~~~~~ !!\n")
        print(request_path)
        print(self.headers)
        print("\n !! ~~~~~~~~~~~~~ REQUEST END ~~~~~~~~~~~~ !!\n")

        self.send_response(200)
        # self.send_header("v", "k")

    def do_PUT(self):
        request_path = self.path

        print("\n !! ~~~~~~~~~~~~~ REQUEST START ~~~~~~~~~~~~ !!\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        clength = 0
        if content_length:
            clength = content_length[0]

        print(request_headers)
        print(self.rfile.read(clength))
        print("\n !! ~~~~~~~~~~~~~ REQUEST END ~~~~~~~~~~~~ !!\n")

        self.send_response(200)

def main():
    port = 5000
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()