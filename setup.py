import os

from shutil import copyfile

if not os.path.isfile('.env'):
    copyfile('.env.dist', '.env')

directory = os.path.dirname(os.path.realpath(__file__))

directories = [
    directory + '/htdocs',
    directory + '/storage',
    directory + '/storage/mariadb',
    directory + '/storage/mysql',
    directory + '/storage/postgres',
    directory + '/storage/redis',
]

for directory in directories:
    if not os.path.exists(directory):
        print('Creating ' + directory + '.')
        os.mkdir(directory)
    else:
        print('The ' + directory + ' directory already exists!')
