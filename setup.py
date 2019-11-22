import argparse
import os

from shutil import copyfile

parser = argparse.ArgumentParser(description='Setup script for the phpdev Docker environment.')

parser.add_argument('-s', '--htdocs-source', type=str, required=False, help='The htdocs symlink source')

args = parser.parse_args()

# Create .env if it doesn't already exist

if not os.path.isfile('.env'):
    copyfile('.env.dist', '.env')

# Create htdocs if it doesn't already exist

htdocs = '%s/htdocs' % (os.path.dirname(os.path.realpath(__file__)))

if not os.path.exists(htdocs):
    if args.htdocs_source is not None:
        htdocs_source = os.path.realpath(args.htdocs_source)

        if not os.path.isdir(htdocs_source):
            print('The htdocs symlink source (%s) does not exist!' % (htdocs_source))
            exit(1)

        print('Symlinking htdocs to %s.' % (htdocs_source))
        os.symlink(htdocs_source, htdocs)
    else:
        print('Creating %s directory.' % (htdocs))
        os.mkdir(htdocs)

# Create the required storage directories

directory = os.path.dirname(os.path.realpath(__file__))

directories = [
    directory + '/storage',
    directory + '/storage/mariadb',
    directory + '/storage/mysql',
    directory + '/storage/postgres',
    directory + '/storage/redis',
]

for directory in directories:
    if not os.path.exists(directory):
        print('Creating %s directory.' % (directory))
        os.mkdir(directory)

# Tell the user that we're done

print('All done!')
