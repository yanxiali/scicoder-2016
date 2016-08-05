### Your Shell and You

This is a collection of tips and tricks for working in a terminal environment. The program where you enter commands is called a shell. These commands are applicable to the bash shell (`/usr/bin/bash`) unless otherwise indicated.

##### Todo:  
differences between .bashrc, .bash_profile, .profile ?

##### Directories & Navigation

`~`: represents your home directory, e.g.

    % cd ~
    % mv ~/file_in_home_dir /some/other/place/

| Command             | Action                                   |
| ------------------- | ---------------------------------------- |
| `pwd`               | show current directory                   |
| `cd`                | alone with no arguments, go to home directory |
| `cd -`              | go to last directory you were in         |
| `pushd name_of_dir` | “bookmark” a particular directory, typically used to bookmark the current directory with `pushd .` |
| `pushd`             | alone, switches to directory *without* removing it from the stack |
| `popd`              | change directory to the last bookmarked directory (this actually works like a stack) |
| `dirs`              | list directories in the pushd/popd stack |

##### Control Characters
| Control Char             | Action                                   |
| ------------------------ | ---------------------------------------- |
| cntrl-a                  | move cursor to start of line (also works on the command line) |
| cntrl-e                  | move cursor to end of line (also works on the command line) |
| cntrl-left / cntrl-right | move cursor left/right one word, conflicts with moving between Spaces on Mac OS |
| cntrl-r                  | (r)everse search your history (forward search not yet implemented) |
| cntrl-d                  | forward delete                           |
| cntrl-k                  | delete from cursor to end of line        |
| cntrl-l                  | clear screen?                            |
| cntrl-c                  | cancel command (scrap command and go to a new prompt) |
| cntrl-u                  | delete from beginning of line to cursor  |
| cntrl-e cntrl-u          | go to end of line and delete whole line  |
| cntrl-a cntrl-k          | go to beginning of line and delete whole line |

##### Tab Completion

Start typing a few characters of a file or directory, e.g.

    % cd Docu

and then hit the `tab` key. The shell will automatically complete the file (or directory) name that matches the start of what you typed. This is very useful for files with long names. The shell will complete until there is no longer a unique match. For example, if a diectory has these files:

    plateInput_047-25_MGA_SCI_8188-output.par
    plateInput_047-25_MGA_SKY_8188-output.par
    plateInput_047-25_MGA_STA_8188-output.par

entering `ls pl` then `tab` will result in this at the prompt:

    % ls plateInput_047-25_MGA_S

One more character, then `tab` will complete the filename.

By default, tab completion is case-sensitive, but it's much more useful (and forgiving) to be case-insensitive. Place this `~/.bashrc` to ignore case in tab completion:

    set completion-ignore-case on

Same in tcsh (`~/.tcshrc`):

    set complete = enhance

After hitting `tab` to autocomplete, if the shell finds more than one file that is not unique, hit `tab` again to list them.

##### Command Completion

In addition to `tab` completion, you can customize he behavior to auto-complete from a limited list of values specific to a certain program.

Place this in your `~/.bashrc`. Typing `ssh h` plus `tab` will autocomplete host names found in your `~/.ssh/config` file. (Bonus points for anyone who can do this via Python instead.)

    function _ssh_completion() {
        perl -ne 'print "$1 " if /^Host (.+)$/' ~/.ssh/config
    }
    complete -W "$(_ssh_completion)" ssh

This can be expanded to any command, e.g.

    function _svn_completion() {
        echo "add blame cat changelist checkout cleanup commit copy delete diff export help import info list lock log merge mergeinfo mkdir move patch propdel propedit propget proplist propset relocate resolve resolved revert status switch unlock update"
    	# left out "upgrade"
    }
    complete -W "$(_svn_completion)" svn

For when typing "notebook" is just more trouble than it's worth:

    function _jupyter_completion() {
    	echo "notebook --pdb"
    }
    complete -W "$(_jupyter_completion)" jupyter

And for `ipython notebook`:

    function _ipython_completion() {
    	echo "notebook --pdb"
    }
    complete -W "$(_ipython_completion)" ipython


##### Useful Aliases

Create an alias with the command (shortcut=command)

    alias ll="ls -l"

It's recommended to put all your aliases in their own file, e.g. `~/.aliases`, which is then called from `~/.bashrc` as:

    source $HOME/.aliases

| Alias | Command            | Description                              |
| ----- | ------------------ | ---------------------------------------- |
| ll    | ls -l              | (l)ong listing                           |
| lh    | ls -lh             | (h)uman readable file sizes              |
| lla   | ls -a              | list ()a)ll files, including invisible ones |
| ltr   | ls -ltr            | show long listing + put most recent file at the bottom, helpful for the “what did this file save to?” moments or finding the most recent plot you made. |
| ipnb  | "ipython notebook" | is this still the best way to launch the nb? |

##### Other Commands (to sort as this grows)

| Command          | Action                                   |
| ---------------- | ---------------------------------------- |
| !v               | executes the most recent command in your history that begins with "v" |
| which            | show the location of the program of the given command, e.g. `which python` - finds the first one on the $PATH |
| type -a          | lists all instances of a program on the $PATH, e.g. `type -a python` |
| source filename  | execute all commands in file `filename` as if they were typed on the terminal |
| touch <filename> | if file doesn’t exist, create a blank one with that name; if it does exist, change the last modified date to now |

##### Misc

###### !!

Use `!!` to represent the last command that was run, can be used to make a new command:

    cat some_file.txt
    !! | grep string

Also very useful with sudo:

	rm file # permission denied
	sudo !!

###### Creating New Files

Create a new file with no editor

    % cat > delme
    Enter text here
    over several lines if needed
    that will be placed into the new file 'delme'. 

To exit the editing mode, enter `cntrl-d` on a blank line. Note if the file already exists, it will be overwritten! You can also append to a file with `cat >> filename`.

###### Working with Spaces in Filenames

Use `\` to work with spaces in filenames, e.g.

    cd Library/Application\ Support

Alternatively, you don't need to escape spaces if you put the filename in quotes:

    cd "Library/Application Support"

This works particularly well with tab completion which will do the right thing.

###### Regular Expressions

Multiple files can be selected with regular expression patterns:

    ls file[12348]

is the equivalent of

    ls file1 file2 file3 file4 file8

###### Head and Tail

| Command         | Action                                   |
| --------------- | ---------------------------------------- |
| tail -10        | list the last 10 lines of the file       |
| tail -10f       | list the last 10 lines of the file, and keep showing new lines that are being written |
| head -10        | list first 10 lines of a file (helpful to see header of a file) |
| df -h           | show the status of all disks, size, available space, used space (h is for human-readable; displays kB, MB, GB add appropriate instead of bytes) |
| du -sh dir_name | total size of directory in human-readable units |

###### Processes

The `top` command shows all processes running as well as memory and CPU usage. It's the first stop to check how your system is doing. The program Activity Monitor does a very similar thing on Mac OS X.

How to kill a process that is hanging. List all active processes:

    % ps

Identify the process ID (PID) of the program you want to force quit (from `top` or similar), and run:

    % kill -9 PID_OF_PROCESS

##### Misc.

`paste` : concatenate line-matched files by columns (<http://en.wikipedia.org/wiki/Paste_%28Unix%29>)

Truncate a file to zero length without deleting it. This allows programs using the file open to keep reading and writing it.

    % >longfile.log

After you mistype a command, use this to replace "wrong" with "right" and re-execute the command.

    % ^wrong^right

##### Screen

In you are working on a remote machine through a terminal, you can create a virtual window using the screen command. This virtual window will continue to run even if your connection with that machine dies or you shut down your laptop (as long as you detach the screen first). Works in Unix and Mac OS X. 

| Command   | Action                     |
| --------- | -------------------------- |
| screen    | instantiates a new session |
| ctrl-a d  | detaches the session       |
| screen -r | re-attaches the session    |

(There are other commands, but these are the only three you need, google “Unix screen”.)

##### Mac Tricks

| Command                                  | Action                                   |
| ---------------------------------------- | ---------------------------------------- |
| some_output &#124; pbcopy                | Put the output onto the Mac clipboard    |
| pbpaste &#124; some_input                | Paste the Mac clipboard to some other input |
| say “text that will be spoken by the speech synthesizer” | Useful to let you know a long process is done |

Examples:

    % pbpaste | gzip > data.gz
    % long_running_script ; say "Hey, the confrabulation analysis is done."

From the Finder (or any open/save dialog box), type `command-shift-g`. A navigation box will appear where you can type the path you want to go to, complete with tab completion. (Not perfect tab completion; if you complete on the first match it finds, even if there are others). You can also use `~` to specify the home directory.

##### Pipes and Redirection

Direct output to a file, e.g.

    ls -l > listing.txt

gzip output on the fly:

    some process that produces output | gzip > output_file.gz

app 2>&1 : combine standard out with standard error when running app, useful if you are piping the output for example

Script to customize (and color) your prompt

    # See link for full reference:
    #
    # http://bash-hackers.org/wiki/doku.php/scripting/terminalcodes
    #
    # \033 indicates a control character is to follow
    #
    # For full list, "man bash" and search to 2nd "PROMPTING" or see:
    # http://tldp.org/HOWTO/Bash-Prompt-HOWTO/bash-prompt-escape-sequences.html
    # also: http://www.yolinux.com/HOWTO/Bash-Prompt-HOWTO.html
    #
    # \u : username
    # \h : host to first "."
    # \w : current full working directory
    # \W : last part of path
    
    # ALL control sequences (i.e. non-printing characters)
    # MUST start with a \[ and end with a \]. This tells
    # the shell that these are control characters.
    # One set of escaped brackets can be used for several
    # in a row, but can be done for each alone as defined
    # below. If this is not done the line wrap will not
    # function properly (since the shell doesn't know how
    # long the prompt is).
    
    COL_BLACK=$'\[\033[30m\]'
    COL_RED=$'\[\033[31m\]'
    COL_GREEN=$'\[\033[32m\]'
    COL_YELLOW_ORANGE=$'\[\033[33m\]'
    COL_BLUE=$'\[\033[34m\]'
    COL_MAGENTA=$'\[\033[35m\]'
    COL_CYAN=$'\[\033[36m\]'
    COL_NORM=$'\[\033[39m\]'
    PMPT_BOLD=$'\[\033[1m\]'
    PMPT_NORM=$'\[\033[0m\]'
    
    # See: http://networking.ringofsaturn.com/Unix/Bash-prompts.php
    # for a longer list of colours.
    
    # actual command that sets prompt
    
    PS1="${PMPT_BOLD}${COL_CYAN}\h${COL_NORM} [\w] %${PMPT_NORM} "

Example result (but in color):

    MacBook-Air [~/Documents/Repositories/] %




#### Links with more tips

<http://stackoverflow.com/questions/68372/what-is-your-single-most-favorite-command-line-trick-using-bash>  
<http://unix.stackexchange.com/questions/6/what-are-your-favorite-command-line-features-or-tricks>  
<http://www.reddit.com/r/bashtricks>  
<http://www.linuxjournal.com/article/7385>  
