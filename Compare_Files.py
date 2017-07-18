#!/usr/bin/python

from optparse import OptionParser
import realine, os, sys


def main():
  t_file = ''
  t_file_dir = os.getenv('PWD')
  
  start_time = time.strftime('%Y%m%d %H:%M:%S')
  print('Start time is %s.' % start_time)
  
  p = OptionParser(usage: '%prog -t <input_file1.txt> <input_file2.txt>')
  
  p.add_option('-o', '--output',
              type='string',
              action='store',
              dest='outfile',
              nargs=1,
              help='Specifies the output file name.')
  p.add_option('-t', '--txt',
              type='string',
              action='store',
              dest='txtfile',
              nargs=1,
              help='Specifies the file with which other files are compared.')
  (args, opts) = p.parse_args()
  
  if opts.txtfile:
    t_file = opts.txtfile
    t_file_list = []
    for item in range(len(sys.argv)):
      t_file_list.append(item)
    
    for file in t_file_list:
      compare_files(t_file,t_file_list[file])
    
def compare_files(file1,file2):
  results_file = ''
  count = 0

  with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
          for row1, row2 in zip.iter(f1,f2):
            if row1 != row2:
              results_file = row1 + row2

  with open('some_output_file.txt', 'w') as FO:
    for line in same:
        FO.write(line)
  return results_file

def file_to_var(txtfile):
  for line in input.readlines(txtfile):
    var_file = var_file + line + "\n"
  return var_file

def compare_files(file1,file2):
  
def diff(a, b):
    y = []
    for x in a:
        if x not in b:
            y.append(x)
        else:
            b.remove(x)
    return y

with open('output_ref.txt', 'r') as file1:
    with open('output_ref1.txt', 'r') as file2:
        same = diff(list(file1), list(file2))
        print same
        print "\n"

if __name__ == '__main__':
    main()

Updated 7/15/2017
