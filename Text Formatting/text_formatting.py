import sys
import argparse


class InputDataError(Exception):
    pass


def text_formatting(fin, fout, w, b):
    new_par = True
    paragraphs = []
    cur_string = ''
    for lines in fin:
        if lines == "\n":
            if not new_par:
                new_par = True
                paragraphs.append(cur_string)
                cur_string = ''
        else:
            cur_string += lines
            new_par = False
    if len(cur_string) > 0:
        paragraphs.append(cur_string)
    for paragraph in paragraphs:
        par = ' '.join(paragraph.split())
        add_par = ''
        space = False
        for i in par:
            if i.isspace():
                space = True
            elif ",.?!-:'".find(i) != -1:
                add_par += i
                space = True
            else:
                if space:
                    add_par += ' ' + i
                    space = False
                else:
                    add_par += i
        words = add_par.split(' ')
        cur_string = b * ' '
        for i in words:
            if len(i) > w:
                raise InputDataError("too long sequence - '" + i + "'")
            elif len(i) + len(cur_string) < w:
                cur_string += ' ' + i
            else:
                fout.write(cur_string[1:] + '\n')
                cur_string = ' ' + i
        if len(cur_string) > 1:
            fout.write(cur_string[1:] + '\n')


def main():
    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input', default=None,
        help='the name of the input file')
    parser.add_argument(
        '-o', '--output', default=None,
        help='the name of the output file')
    parser.add_argument(
        '-l', '--line-length', type=int, default=30,
        help='maximum string length')
    parser.add_argument(
        '-p', '--paragraph-spaces', type=int, default=4,
        help='amount of indent at the beginning of a paragraph')
    args = parser.parse_args()
    # opening files
    if args.input is not None:
        file_in = open(args.input)
    else:
        file_in = sys.stdin

    if args.output is not None:
        file_out = open(args.output, 'w')
    else:
        file_out = sys.stdout
    # formatting and writing
    text_formatting(file_in, file_out, args.line_length, args.paragraph_spaces)
    # closing files
    file_in.close()
    file_out.close()


if __name__ == '__main__':
    main()
