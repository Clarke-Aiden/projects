#2-read files 




def main():
    fname='Hackme.txt'
    content = readfile(fname)
    print_file_content(content)

def readfile(fname):
    with open(fname, 'r') as f:
        return f.read()

def print_file_content(content):
    print(content)


main()