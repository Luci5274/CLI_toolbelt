import os

def register_parser(subparsers):
    parser =  subparsers.add_parser('rename', help = 'batch rename files in a folder')
    parser.add_argument('directory', help = 'Target Directory')
    parser.add_argument('prefix', help= 'new file prefix')
    parser.set_defaults(func=main)

def main(args):
    files = [f for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory,f))]