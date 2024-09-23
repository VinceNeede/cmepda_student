import argparse         #import from standard library goes first in alphaabetical order
import string

from loguru import logger



def count_chars(file_path):
    """
    Count the relative frequency of each character in the input data.
    """
    out = {char : 0 for char in string.ascii_lowercase}
    logger.debug(f"initialize dictionary: {out}")
    with open(file_path, "r") as file:
        logger.debug(f"Reading input data from: {file_path}")
        data = file.read()          #future: read each line and process it
        logger.debug(f"Done, there are {len(data)} characters")
    logger.info("Counting characters...")

    for char in data.lower():
        if char in out:
            out[char] += 1
    num_chars = sum(out.values())
    logger.info(f"Total umber of characters: {num_chars}")
    for key, value in out.items():
        out[key] = value/num_chars*100
    logger.info(f"Frequency of characters: {out}")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="This script reads a text file\
        and counts the relative frequency of each character in it.")
    parser.add_argument("file_path",metavar='string',type=str, help="Path to the input file")
    parser.add_argument("--plot_hist", metavar='bool', type=bool, 
                        help="Plot histogram of character frequencies, default False", default=False)
    parser.add_argument("--skip_preamble", metavar='bool', type=bool,help="Skip preamble\
        of the file, default False", default=False)
    parser.add_argument("--print_stats", metavar='bool', type=bool, help="Print statistics\
        of the file (number of characters, number of words, number of lines)\
        , default False", default=False)
    args = parser.parse_args()
    
    count_chars(args.file_path)

