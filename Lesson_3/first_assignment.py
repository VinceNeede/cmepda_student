import argparse         #import from standard library goes first in alphaabetical order


import charcpy    
        
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="This script reads a text file\
        and counts the relative frequency of each character in it.")
    parser.add_argument("file_path",metavar='string',type=str, help="Path to the input file")
    parser.add_argument("--plot_hist", metavar='bool', type=bool, 
                        help="Plot histogram of character frequencies, default False", default=False)
    parser.add_argument("--skip_lines", metavar='int', type=int,help="number of lines to skip, default 0", default=0)
    parser.add_argument("--print_stats", metavar='bool', type=bool, help="Print statistics\
        of the file (number of characters, number of words, number of lines)\
        , default False", default=False)
    args = parser.parse_args()

    counter = charcpy.CharacterCounter(args.file_path, args.skip_lines, args.print_stats)
    counter.run()
    print(counter.result)
    if args.plot_hist:
        counter.result.plot_hist()
    
