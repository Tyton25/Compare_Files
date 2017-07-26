#!/usr/bin/python

from optparse import OptionParser
import realine, os, sys


def main():
  user_home_dir = os.getenv('HOME')
  t_file = ''  start_time = time.strftime('%Y%m%d %H:%M:%S')
 

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
  else:
    print "Please include a file for comparison."
    p.print_help()
    sys.exit()

  if opts.outfile:
    output_dir = os.path.normpath(opts.outfile) + "/"
  else:
    output_dir = os.getenv('HOME') + "/"

  compare_files(t_file,t_file_list,output_file_path)
  
      
def compare_files(file1,file_list,output_file):
  with open(file1, 'r') as f1:
      for item in range(len(file_list))
        with open(file2, 'r') as f2:
          file_to_compare = t_file_list[file]
          output_file_path = get_output_path(file_to_compare,output_dir)
          os.system('diff -B %s %s >' %(f1,f2,output_file))
          
def get_output_path(compfile,outdir):
  while not compfile.endswith('.'):
    compfile = compfile[:-1]
  while compfile.endswith('.'):
    compfile = compfile[:-1]
  out_filename = compfile + "_compare_results_.txt"
  out_file_path = outdir + out_filename
  out_file_path = os.path.normpath(out_file_path)

  return out_file_path


if __name__ == '__main__':
    main()
