import argparse
import os

from shutil import copyfile

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Setup script for the phpdev Docker environment.')

    parser.add_argument('-s', '--htdocs-source', type=str, required=False, help='The htdocs symlink source')

    args = parser.parse_args()

    # Get path to current directory

    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Create php.env if it doesn't already exist

    if not os.path.isfile(current_directory + '/env/php.env'):
        copyfile(current_directory + '/env/php.env.dist', current_directory + '/env/php.env')

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

    directories = [
        current_directory + '/storage',
        current_directory + '/storage/mariadb',
        current_directory + '/storage/mysql',
        current_directory + '/storage/postgres',
        current_directory + '/storage/redis',
    ]

    for directory in directories:
        if not os.path.exists(directory):
            print('Creating %s directory.' % (directory))
            os.mkdir(directory)

    # Tell the user that we're done

    print('All done!')
