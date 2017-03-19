# Read in a file and return a wordcount

import sys
import subprocess

def main():
    file = sys.argv[1]
    wcount = subprocess.check_output('wc ' + file, shell=True).split()
    with open('outfile.txt', 'a') as f:
        c = wcount[1].decode("utf-8")
        f.write(file + ' ' + c + '\n')

main()
