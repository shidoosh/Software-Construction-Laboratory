# Laboratory: Linux and Emacs scavenger hunt
Instructions: Do this assignment on lnxsrv06, lnxsrv07, or lnxsrv09, with /usr/local/cs/bin prepended to your PATH. Use the commands that you learned in class to find answers to these questions. Don't use a search engine like Google, and don't ask your neighbor, don't use GitHub, etc. If you need a hint, ask the TA. When you find a new command, run it so you can see exactly how it works. In addition to turning in the answers to these questions, turn in a description of your session discovering them.

As you do actions, use Emacs to record your keystrokes and each answer in plain-text files key1.txt and ans1.txt that you will submit as part of the assignment. If you prefer, you can record and submit Org files key1.org and ans1.org instead of .txt files; see Hello Worg for Org introductions and tutorials.

What shell command uses the man program to print all the commands that have a specific word in their man page (or at least the description part of the man page)? (hint: man man)
Where are the cp and sh programs located in the file system? List any shell commands you used to answer this question.
What executable programs have names that are just one character long, and what do they do? List any shell commands you used to answer this question.
When you execute the command named by the symbolic link /usr/bin/emacs, which file actually is executed? List any shell commands you used to answer this question.
What is the version number of the /usr/bin/emacs program? of the plain emacs program? Why are they different programs?
The chmod program changes permissions on a file. What does the symbolic mode g+s,o-x mean, in terms of permissions?
Use the find command to find all directories modified in the last 30 days that are located under (or are the same as) the directory /usr/local/cs. List any shell commands you used to answer this question.
Of the files in the same directory as find, how many of them are symbolic links? List any shell commands you used to answer this question.
What is the oldest regular file in the /usr/lib64 directory? Use the last-modified time to determine age. Specify the name of the file without the /usr/lib64/ prefix. Consider files whose names start with ".". List any shell commands you used to answer this question.
Where does the locale command get its data from? List any shell commands you used to answer this question.
In Emacs, what commands have downcase in their name? List any Emacs commands you used to answer this question.
Briefly, what do the Emacs keystrokes C-M-r through C-M-v do? Can you list their actions concisely? List any Emacs commands you used to answer this question.
In more detail, what does the Emacs keystroke C-g do? List any Emacs commands you used to answer this question.
What does the Emacs yank function do, and how can you easily invoke it using keystrokes? List any Emacs commands you used to answer this question.
When looking at the directory /usr/bin, what's the difference between the output of the ls -l command, and the directory listing of the Emacs dired command? List any shell or Emacs commands you used to answer this question.

# Homework: Learning to use Emacs
Keith Waclena, A Tutorial Introduction to GNU Emacs (2009)
The Emacs editor, version 25.2 (2017)
An Introduction to Programming in Emacs Lisp, version 25.2 (2017)
For all the exercises, record the steps taken to accomplish the given tasks. Use intelligent ways of answering the questions. For example, if asked to move to the first occurrence of the word "scrumptious", do not merely use cursor keys to move the cursor by hand; instead, use the builtin search capabilities to find "scrumptious" quickly.

To start, download a copy of the web page you're looking at into a file named assign1.html. You can do this with Wget or curl. Use cp to make three copies of this file. Call the copies exer1.html, exer2.html, and exer3.html.

# Exercise 1.1: Moving around in Emacs
Use Emacs to edit the file exer1.html.
Move the cursor to just after the first occurrence of the word "HTML" (all upper-case).
Now move the cursor to the start of the first later occurrence of the word "scavenger".
Now move the cursor to the start of the first later occurrence of the word "self-referential".
Now move the cursor to the start of the first later occurrence of the word "arrow".
Now move the cursor to the end of the current line.
Now move the cursor to the beginning of the current line.
Doing the above tasks with the arrow keys takes many keystrokes, or it involves holding down keys for a long time. Can you think of a way to do it with fewer keystrokes by using some of the commands available in Emacs?
Did you move the cursor using the arrow keys? If so, repeat the above steps, without using the arrow keys.
When you are done, exit Emacs.
Exercise 1.2: Deleting text in Emacs
Use Emacs to edit the file exer2.html. The idea is to delete its HTML comments; the resulting page should display the same text as the original.
Delete the 18th line, which is an HTML comment. <!-- HTML comments look like this. -->
Delete the HTML comment containing the text "DELETE-ME DELETE-ME DELETE-ME".
Delete the HTML comment containing the text "https://en.wikipedia.org/wiki/HTML_comment#Comments".
There are three more HTML comments; delete them too.
Once again, try to accomplish the tasks using a small number of keystrokes. When you are done, save the file and exit back to the command line. You can check your work by using a browser to view exer2.html. Also, check that you haven't deleted something that you want to keep, by using the following command:

diff -u exer1.html exer2.html >exer2.diff
The output file exer2.diff should describe only text that you wanted to remove. Don't remove exer2.diff; you'll need it later.

# Exercise 1.3: Inserting text in Emacs
Use Emacs to edit the file exer3.html.
Change the first two instances of "Assignment 1" to "Assignment 21".
Change the first instance of "UTF-8" to "US-ASCII".
Ooops! The file is not ASCII so you need to fix that. Remove every line containing a non-ASCII character. You can find the next non-ASCII character by searching for the regular expression [^[:ascii:]].
Insert an empty line after the first line containing "</ol>".
When you finish, save the text file and exit Emacs. As before, use the diff command to check your work.
# Exercise 1.4: Other editing tasks in Emacs
In addition to inserting and deleting text, there are other common tasks that you should know, like copy and paste, search and replace, and undo.

Execute the command "cat exer2.html exer2.diff >exer4.html" to create a file exer4.html that contains a copy of exer2.html followed by a copy of exer2.diff.
Use Emacs to edit the file exer4.html. The idea is to edit the file so that it looks identical to exer1.html on a browser, but the file itself is a little bit different internally.
Go to the end of the file. Copy the new lines in the last chunk of diff output, and paste them into the correct location earlier in the file.
Repeat the process, until the earlier part of the file is identical to what was in the original.
Delete the last part of the file, which contains the diff output.
… except we didn't really want to do that, so undo the deletion.
Turn the diff output into a comment, by surrounding it with "<!--" and "-->".
Now let's try some search and replaces. Search the text document for the pattern ol tag. How many instances did you find? Use the search and replace function to replace them all with the final-caps equivalent. 
Check your work with viewing exer4.html with an HTML browser, and by running the shell command "diff -u exer1.html exer4.html >exer4.diff". The only differences should be changes from ol tag to oL tag, and a long HTML comment at the end.
# Exercise 1.5: Doing commands in Emacs
Do these tasks all within Emacs. Don't use a shell subcommand if you can avoid it.

Create a new directory named "junk" that's right under your home directory.
In that directory, create a C source file hello.c that contains the following text. Take care to get the text exactly right, with no trailing spaces or empty lines, with the initial # in the leftmost column of the first line, and with all other lines indented to match exactly as shown:
#include <stdio.h>
int
main (void)
{
  char n = '\n', b = '\\', q = '"';
  char const *p = "#include <stdio.h>%cint%cmain (void)%c{%c  char n = '%cn', b = '%c%c', q = '%c';%c  char const *p = %c%s%c;%c  printf (p, n, n, n, n, b, b, b, q, n, q, p, q, n, n, n, n);%c  return 0;%c}%c";
  printf (p, n, n, n, n, b, b, b, q, n, q, p, q, n, n, n, n);
  return 0;
}
Compile this file, using the Emacs M-x compile command.
Run the compiled program, and put its output into a new Emacs buffer named hello-out.
Copy this buffer's contents directly into the log that you're maintaining for this exercise. (You are using Emacs to maintain the log, aren't you?)
# Exercise 1.6: Running Elisp code
Visit Emacs's *scratch* buffer.
In the buffer, seed the random number generator with your student ID as a string, dashes included. For example, if your student ID is 123-456-789, evaluate (random "123-456-789"). Use C-j (eval-print-last-sexp) to evaluate the expression, and record the result that you get.
In the buffer, assign two random integers to the global variables x and y. Start by executing (setq x (random)). Again, use C-j.
What is the product of the two variables? You can find this out by evaluating (* x y). What do you observe about the result? If the answer is the correct mathematical answer, keep trying again with a different pair of random integers until you get an answer that is not mathematically correct.
Try evaluating (* x y) again, but this time with M-: (eval-expression). What difference do you observe in the output?
Are the two random integers truly random in the mathematical sense? If not, what's not random about them?
Assuming (random) is truly random, what is the probability that the two-variable product mentioned above is mathematically incorrect? Explain how you calculated this.
