"""Clean library list"""

import argparse
import pandas as pd


def main(args):
    """Run the command line program."""
    
    df = pd.read_csv('libraries.csv')   #, index_col='participant')

    df['libraries'] = df['libraries'].str.strip()
    df['libraries'] = df['libraries'].str.lower()
    df = df.sort_values(by=['participant', 'libraries'])
    df = df.drop_duplicates(keep=False)
    
    df.to_csv(args.outfile, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=str, help="Input files")
    parser.add_argument("outfile", type=str, help="Output file")
    args = parser.parse_args()
    main(args)
    