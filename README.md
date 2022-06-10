# EasyPyPdf
 
a collection of small pdf tools in python\
they are intended to be used on windows with the "send to" context menu option

## combine front and back

looks for `*.front.pdf` and `*.back.pdf` (with the same name as *)\
and combines them into a single file

```
    Front page 1
    Back page  1
    Front page 2
    Back page  2
    
```

## reverse

reverses the pages of the file and overwrites it

## split pages

saves every page in a single pdf

# requirements

```console
pip install pikepdf
```

# installation (manual)

press [Win]+[R]\
enter `shell:sendto`\
a folder will open\

here you need to create a link for every `main_*.py` script

Important: the links need to point to `python.exe "C:\path\to\your\scripts\main_*.py"`\
they cannot directly point to the scripts

the filename of the link will appear in the send to menu

# todo

- installation script