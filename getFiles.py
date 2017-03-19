# Find all txt files. Send to readIn.py

from subprocess import check_output

def main():
    files = check_output('ls | grep .txt', shell=True).split()
    files.remove(b'outfile.txt')
    for f in files:
        f = f.decode("utf-8")
        check_output("python3 readIn.py " + f, shell=True)

main()
