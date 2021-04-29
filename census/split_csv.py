"""Split csv cells"""

import argparse
import csv


def main(args):
    """Run the command line program."""
    
    delimiters = {'semicolon': ';', 'newline': '\n'}
    delim = delimiters[args.cell_delim]
    
    outdata = []
    with open(args.infile, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                outdata.append(row)
            else:
                pnum = row[0]
                for item in row[1].split(delim):
                    if 'import' in item:
                        if item[0:6] == 'import':
                            item = item[7:]
                        elif item[0:4] == 'from':
                            item = item[5:]
                    if item:
                        outdata.append([pnum, item])    
            line_count += 1
            
    with open(args.outfile, mode='w') as outfile:
        writer = csv.writer(outfile)
        for row in outdata:
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=str, help="Input files")
    parser.add_argument("outfile", type=str, help="Output file")
    parser.add_argument("--cell_delim", type=str,
                        choices=('semicolon', 'newline'),
                        default='semicolon', 
                        help="Delimiter within cell")
    args = parser.parse_args()
    main(args)
    