# Checking if the score archive exists
import os.path


def check_archive(name):
    try:
        archive = open(name, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Creating the score archive
def create_archive(name):
    try:
        archive = open(name, 'wt+')
        archive.close()
        with open(name, 'at') as first_score:
            first_score.write('0')
    except FileExistsError:
        pass


# Reading the high score
def read_archive(name):
    try:
        archive = open(name, 'rt')
    except FileNotFoundError:
        check_archive(name)
    else:
        for line in archive:
            return line


# High score registration
def score_registration(name, points):
    try:
        archive = open(name, 'at')
    except FileNotFoundError:
        create_archive(name)
    else:
        if points > int(read_archive(name)):
            archive.truncate(0)
            archive.write(str(points))
