import argparse

# Initialize the Parser
parser = argparse.ArgumentParser(description='Add help option')

# Adding Arguments
parser.add_argument('--hell', help="Add hell option")


args = parser.parse_args()
print(args.hell)


if __name__ == '__main__':
    args = parser.parse_args()