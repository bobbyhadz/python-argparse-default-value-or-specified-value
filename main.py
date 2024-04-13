# Python argparse: Default value or Specified value

import argparse


parser = argparse.ArgumentParser(
    description='A sample Argument Parser.'
)

parser.add_argument('-f',
                    '--fruit',
                    nargs='?',
                    const='apple',
                    type=str
                    )

args = parser.parse_args()

print(args.fruit)