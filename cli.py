import sys
import main

args = sys.argv

for i, a in enumerate(args):

    if a == '-h'or a == '--help':
        print("usage: imagefilter\n"
              "-h, --help :\n"
              "-i,--input-dir <directory>\n"
              "-o,--output-dir <directory>\n")

    elif a == '-i' or a == '--input-dir':
        input_dir = args[i + 1]
        #mettre input_dir dans img du main
        print(input_dir)

    elif a == '-o' or a == '--output-dir':
        output_dir = args[i + 1]
        #mettre output_dir dans le fichier output du main
        print(output_dir)