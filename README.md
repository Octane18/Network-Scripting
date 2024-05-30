# How to run?

Clone the files socket-client.py and socket-server.py from this repository. Then, on any terminal window(Windows terminal, Linux terminal) run these python files on separate systems using the command python3 <file path>. The IP the client would enter would be the IP of the device where the server file is running. 

The format of the instructions from client to server is as follows:

 POST_STRING: this command allows a client to send a text file to the server line by line. The client must type the text (using the standard input)   line-by-line. The first line is the command itself (i.e. POST_STRING) and subsequent lines are treated as the text. The end of the text input is signalled by  a special symbol  &. 

    Example: 

    client: POST_STRING

    client: Welcome socket programming in cs3201

    client: I start writing  an app code ABC

    client: more text.

    client: &
    server: OK

     

    Then, the message sent to the server is a string: POST_STRING\nWelcome socket programming in cs3201\nI start writing  an app code ABC\nmore text.\n&\n
    The server will acknowledge the receipt of the message with "OK"

POST_FILE: this command allows a client to send  a text file and the server responds to the command by asking the client the absolute path of the file in client machine.  You can edit the save path in server code.

    Example: Suppose  a named text file  is cs3201_project.py  whose  absolute path in the local machine is  /user/file/cs3201_project.py

     

    client: POST_FILE

    server: please send  the path name of your text file

    client: /user/file/cs3201_project.py

     
    If the file transfer is successful, the server replies with " OK"; otherwise, the operation fails, and the client needs to resend it again. For example, if the path  does not exist of path typing errors, the  server will not respond to the request.

 

GET: upon receiving this command, the server will send all previously posted messages (posted by POST_STRING command) by the client and other clients  back to the client as the standard output. 

 

EXIT: this informs the server to close the socket to the client. The server will acknowledge the receipt of the command with "OK".


After establishing the TCP connection to the socket of the server, the client program will repeatedly  wait for a command  from the user to execute until it receives command EXIT, and stops the client session. For commands GET and EXIT, the client will just send the command to the server, whereas for POST_STRING, the client will send a message line by line, where the first line is the command (i.e. POST_STRING), and the following lines include the text, and ending with a special symbol &. 

 
