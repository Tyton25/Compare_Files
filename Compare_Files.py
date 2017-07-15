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
    
    
def compare_files(txtfile1,file_list,outfile,args_length):
  results_file = ''
  count = 1
  master_file = file_to_var(txtfile1)
  
  for file in range(len(filelist)):
    compare_files(master_file,file)
  
  return results_file

def file_to_var(txtfile):
  for line in input.readlines(txtfile):
    var_file = var_file + line + "\n"
  return var_file

def compare_files(file1,file2):
  

if __NAME__ == '__MAIN__':
    main()
