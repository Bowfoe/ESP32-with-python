from connect_wifi import s, PORT
import response
import analyse_headers


try:
    while True:
        print("Server is waiting for a connection on port", PORT)
        conn, addr = s.accept()
        print('Server got a connection from' , addr)
        
        request = (conn.recv(4096)).decode("UTF-8")
        print("len request =",len(request))
        print("message from client=",request)
        
        if len(request) > 0:
            
            full_name, type_file = analyse_headers.analyse_headers(request)
            print("name_file =", full_name,  "type_file =", type_file)
            
            response.antwoord_browser(conn, full_name, type_file)
            print("\nServer closed connection!**************************************************\n")

except Exception as e:
    print("Except in main!!", e)

