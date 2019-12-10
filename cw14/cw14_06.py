import os, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir_name', default='new_dir')
parser.add_argument('-fn', '--file_name', default='new_file')
args = parser.parse_args()
current_dir = os.getcwd()
os.mkdir(f'{current_dir}/{args.dir_name}')
with open(f'{current_dir}/{args.dir_name}/{args.file_name}.txt', 'w') as f:
    f.write('')
