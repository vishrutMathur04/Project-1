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

# Oct 19 8:14 pm  
So I was able to split each line into an ACTION and MESSAGE.  
also was able to skip blank lines.  
and then flush output after every write.

Next I would need to Wrap logic in a main() for clarity, validate argument count, test edge cases.

# Oct 19 8:25 pm
I was able to implement all the requirements in Logger and a main method and now it meets all these requirements  
 
 Reads stdin until QUIT.  
 Writes timestamps and actions.  
 Flushes after each entry.  
 Handles argument errors cleanly.  


Start `encrypt.py` following the same development pattern.

# Oct 19 8:45 pm
I did some more testing with logger file and now have created the encrypt.py file for the encryption program

Start working on 'encrypt.py`. This program will manage encryption/decryption using a Vigenère-style cipher and communicate via stdin/stdout.

# Oct 19 8:59 pm
I am thinking to find a way to validate input so only alphabetic text is processed.
Non-letter characters should be rejected early to avoid errors.

Write a helper function for only the letters
It should return True if text has only letters.

# Oct 19 9:20 pm
With validation ready, the next big part is actual encryption logic.

As the Vigenère cipher shifts each letter by key position so need both encrypt and decrypt versions.

So next steps will be implement vigenere_encrypt() and vigenere_decrypt() functions

I will also see if its able to iterate through characters and apply shifts using key indices.

# Oct 19 9:27 pm

Core functions work standalone, but now the program needs to interact dynamically.
It should read commands through standard input and respond immediately.


Start an infinite loop to process stdin lines.
Handle blank lines and QUIT properly.

# Oct 19 9:33 pm 
So we are ready to implement the password setup command.

Need to validate input and store the uppercase version as key for later use so for that adding handler for PASS and PASSKEY commands.
Validate input via letters_only().
Print result or error to stdout.

# Oct 19 9:40 pm
Key storage works. N
Need to validate both key and payload before calling cipher functions.

Next we will perform encryption and decryption using it.
Add blocks for ENCRYPT and DECRYPT commands.
Handle missing key and invalid input errors gracefully.

# Oct 19 9:45 pm
Added blocks for encrypt and decrypt commands

Now next I am thinking to add final else clause for unknown commands.
Ensure every output is flushed immediately.

# Oct 19 9:48 pm
Encryptor module works as expected with all commands tested manually.
No syntax errors or hangs — ready to integrate with Driver

Now for the next session I will just finalize file by adding the main method/ main() block.

And then prepare for testing with subprocess in Driver next.

# Oct 19 9:56 pm

So now both the logger and encryptor are functional individually.
Now I need a central script that coordinates them, manages I/O, and provides an interface for the user.

Create a new file driver.py

Import required modules (sys, subprocess).

# Oct 19 10:05 pm

Now that argument parsing works, I can spawn both the logger and encryptor as subprocesses.
They’ll be connected via stdin and stdout pipes.


Use subprocess.Popen to start both programs.

Configure encoding and pipes.

# Oct 19 10:26 pm
Both child processes launch fine. I now need helper functions to make the communication cleaner.
Driver should log actions and interact with encryptor easily.

So now next I will Add a write_log() function to send entries to the logger.

and then also add send_encrypt_command() to send instructions to encrypt file and read its responses.

# Oct 19 10:40 pm
With communication established, I need to build the main user interface.
Driver should let the user set passwords, encrypt/decrypt strings, and view history.

Now I will create interactive loop with menu.

Add options for password setup, encryption, and decryption.

Maintain a history list.

# Oct 19 10:50 pm

Password setup is functional.

Now I’ll handle encryption and decryption commands, and make sure all results are stored in history.
Will Add handlers for encrypt and decrypt.
Append results to history and log all actions except passwords.

# Oct 19 11:05 pm
The encrypt/decrypt logic works well. 

Now I’ll add commands to show the stored history and handle the quit case cleanly.

For that I will add a history display section.
Send QUIT to both child processes when exiting.
Ensure all processes terminate safely.

# Oct 19 11:18 pm
All core features work correctly. Driver communicates with both modules, logs all operations, and handles clean exits.

Final cleanup and comments.
Test complete workflow from password -> encrypt -> decrypt -> quit.



