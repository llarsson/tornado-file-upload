# tornado-file-upload
File uploads using Python Tornado working example.

This example is intended as a basis for "serious" file upload handling, so some error checking and logging is done. It does not stream the file contents, so make sure to use it only for small files!

## usage

 1. Clone the repo.
 2. Run "make virtualenv" to get a virtualenv.
 3. Install requirements using "make init".
 4. Run the main.py file, optionally supplying it with a port and a debug flag as options.
