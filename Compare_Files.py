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
    
    
def compare_files(txtfile1,outfile,args_length):
  results_file = ''
  master_file = file_to_var(txtfile1)
  comp_file = 
  
  return results_file

def file_to_var():
  for line in input.readlines(txtfile1):
    var_file = master_file + line + "\n"
  
  return var_file

if __NAME__ == '__MAIN__':
    main()
