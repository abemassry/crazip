# Crazip
### You'd have to be crazy to use this to zip

Take a hash of file and the size and use that as information, then randomly generate the bits of the same size and compare the hash.

Uses murmur hash from: [mmh3](https://github.com/hajimes/mmh3)

This is not very practical but if you had a supercomputer it might work.  This was also an exploration in threads and multiprocessing in python.

Picture this future use case:
It takes a long time to send a message through space so you want to compress it as much as possible.  On the other planet you have a supercomputer (or quantum computer) that has trillions of cores.  You can hash the message, then figure out the original message based on that hash.  As always there is a size vs time trade-off here.

War and peace test text file from: http://www.textfiles.com/etext/FICTION/war_peace_text which I haven't dared try to decompress yet.

#### decompress_single.py
This is the single threaded test script for reference.

#### decompress_threads.py
This is the thread based test script for reference.  Because of the Python Global Interpreter Lock threads execute with the eqivalent of one core.

#### craunzip
This is the multicore decompression script and the main file.  The multiprocessing library is used that is similar to a C fork() this is one way to get true multiprocessing in python.

#### notes.txt
Here are some notes in python code to make sure I was correctly generating the bits

### Time trials / benchmarking

|Tester                                    |File      |Bits   |Bytes | Time (s)|
|------------------------------------------|----------|------:|-----:|--------:|
|[@abemassry](https://github.com/abemassry)|a.txt     |16     |2     |    0.424|
|[@abemassry](https://github.com/abemassry)|ab.txt    |24     |3     |    17.65|
|[@abemassry](https://github.com/abemassry)|abc.txt   |32     |4     |    3405 |

Test and submit a pull request with your file and add your time.

Seems like an NP hard problem, probably O(n!). A computer scientist could comment.

#### License
MIT
