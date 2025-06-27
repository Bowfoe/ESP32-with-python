def find_type(path):
    """
    Extract the file extension/type from the requested path.
    Defaults to 'html' if no extension is found.
    """
    dot_pos = path.find(".")
    if dot_pos >= 0:
        file_type = path[dot_pos + 1:]
    else:
        file_type = "html"
    print("file_type =", file_type)
    return file_type


def analyze_headers(request):
    """
    Parse the HTTP GET request header string.
    Returns the requested file name and its file type.
    Defaults to 'index.html' and 'html' if the request is root '/' or a '.form' file.
    """
    START_PAGE = "index.html"

    pos_http = request.find("HTTP/")
    pos_get = request.find("GET /")

    if pos_get >= 0 and pos_http > pos_get:
        requested_path = request[pos_get + 4: pos_http - 1]
        print("1) Requested path:", requested_path)

        file_type = find_type(requested_path)
        print("No form parameters found.")

        if requested_path == "/" or file_type == "form":
            requested_path = START_PAGE
            file_type = "html"

        print("3) Final path to serve:", requested_path)
        print("4) File type:", file_type)

        return requested_path, file_type

    else:
        return START_PAGE, "html"


def respond_to_browser(conn, file_name, file_type):
    """
    Send the requested file as an HTTP response through the socket connection.
    Supports text files (html, txt, css), binary files (images, etc.), and command files.
    """
    try:
        # Open file in the correct mode
        if file_type in ("html", "txt", "css"):
            f = open(file_name, "r")  # text mode
        elif file_type == "cmd":
            # Handle 'cmd' files here if needed
            pass
        else:
            f = open(file_name, "rb")  # binary mode

        file_content = f.read()
        f.close()

        length_response = len(file_content)
        print("\nFile length =", length_response, "bytes")

        # Start HTTP response headers
        response = "HTTP/1.1 200 OK\r\n"

        # Add cache control header for non-html/txt/cmd files
        if file_type not in ("html", "cmd", "txt"):
            response += "Cache-Control: max-age=3600\r\n"

        # Add Content-Encoding header for gzip compressed css/js files
        if file_type in ("gz.css", "gz.js"):
            response += "Content-Encoding: gzip\r\n"

        # Content-Type header based on file type
        if file_type == "html":
            response += "Content-Type: text/html\r\n"
        elif file_type == "txt":
            response += "Content-Type: text/plain\r\n"
        elif file_type == "cmd":
            response += "Content-Type: text/html\r\n"
        elif file_type == "jpg":
            response += "Content-Type: image/jpeg\r\n"
        elif file_type == "png":
            response += "Content-Type: image/png\r\n"
        elif file_type == "ico":
            response += "Content-Type: image/x-icon\r\n"
        elif file_type in ("css", "gz.css"):
            response += "Content-Type: text/css\r\n"
        elif file_type in ("js", "gz.js"):
            response += "Content-Type: application/javascript\r\n"
        else:
            print("No matching Content-Type found for:", file_type)

        response += "Content-Length: " + str(length_response) + "\r\n\r\n"

        # Send HTTP headers
        conn.sendall(response.encode("UTF-8"))

        # Send file content
        if file_type in ("html", "txt", "cmd"):
            conn.sendall(file_content.encode("UTF-8"))  # text files must be encoded to bytes
        else:
            conn.sendall(file_content)  # binary files sent as raw bytes

        conn.close()

    except Exception as e:
        print("Exception in respond_to_browser:", e)
        conn.close()
