#!/usr/bin/python

from optparse import OptionParser
import realine, os, sys


def main():
  user_home_dir = os.getenv('HOME')
  t_file = ''
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
      file2 = t_file_list[file]
      diff = compare_files(t_file,file2)
      file_out_path = get_output_path(file2,user_home_dir)
      create_output_file(file_out_path,diff)
    
def compare_files(f1,f2):
  results_file = ''
  count = 0

  with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
          for row1, row2 in zip(f1,f2):
            if row1 != row2:
              results_file = row1 + row2

def create_output_file(outfile,diff_var):
  with open(outfile, 'wb') as FO:
    for line in diff_var:
        FO.write(line)
  return FO

def get_output_path(compfile,homedir):
  while not compfile.endswith('.'):
    compfile = compfile[:-1]
  while compfile.endswith('.'):
    compfile = compfile[:-1]
  out_file_name = compfile + "_compare.txt" 
  output_file_path = homedir + "/" + out_file_name
  output_file_path = os.path.normpath(output_file_path)
  
  return output_file_path


if __name__ == '__main__':
    main()
