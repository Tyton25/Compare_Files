#!/usr/bin/python


def main():
  t_file = ''
  t_file_input = ''
  t_file_dir = ''
  
  p = parseArguments()
  
  p.addOption('-o', '--output',
              type='string',
              action='store',
              dest='outfile',
              nargs=1,
              help='Specifies the output file name.')
  p.addOption('-t', '--txt',
              type='string',
              action='store',
              dest='txtfile',
              nargs=1,
              help='Specifies the file with which other files are compared.')
  
if __NAME__ == '__MAIN__':
    main()
