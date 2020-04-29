import sys, getopt
from PIL import Image

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('day1.py -i inputfile -o outputfile')

    infilepath = ''
    outfilepath = ''
    for opt , arg in opts:
        if opt == '-h':
            print('day1.py -i inputfile -o outputfile')
            sys.exit(2)
        elif opt == '-i':
            infilepath = arg
        elif opt == '-o':
            outfilepath = arg
    try:
        with Image.open(infilepath) as infile:
            if (outfilepath != infilepath):
                infile.save(outfilepath,'PNG')
    except IOError:
        print('Cannot convert from from JPEG to PNG')


if __name__ == '__main__':
    main(argv=sys.argv[1:])

