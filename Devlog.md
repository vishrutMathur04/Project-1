# Oct 19th 6:40 pm
I need to write 3 programs in Python named as Logger, Encryptor and Driver. The Driver is the main program which will activate the other 2 files using the Sub process module  and connects them using the input/output stream.
# Oct 19th 7:00pm
No thoughts as such from the last text

I am going to create a logger.py file to start working on my first function.
# Oct 19th 7:30 pm

I now understand that the Logger program’s only job is to read input lines from stdin, timestamp them, and write them to a log file whose name is provided as a command-line argument.


Handle command-line argument parsing with `sys.argv` and also Open the log file in append mode and test writing a static line.

# Oct 19th 7:45 pm
 
The logger file opens and writes correctly. No runtime errors so far.  


Next I am thinking to make the program read from stdin line by line instead of writing a static string and then also exit when the line "QUIT" is inputted.

# Oct 19 7:55 pm

Reading input works, but I need timestamps to identify when each action happened.

 
- Add stamp_line(action, message) that formats entries as `YYYY-MM-DD HH:MM [ACTION] message` and then test the function separately before integrating.

# Oct 19 8:00 pm  
So I was able to add time stamp that formats entries in this format `YYYY-MM-DD HH:MM

Now next I will use first token as tag (action), rest as message and also try to integrate timestamp function.


