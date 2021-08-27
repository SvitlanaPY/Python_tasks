import sys

try:
    if sys.argv[1] == 'rain':
        print("Take an umbrella")
    elif sys.argv[1] == 'sunny':
        print("Hot day is today. You can go swimming!")
    else:
        print("Please, provide valid argument")
except IndexError:
    print("WARNING: You need to provide an argument")

# run ~$ python3 sys_2.py rain
# OUTPUT: Take an umbrella

# run ~$ python3 sys_2.py sunny
# OUTPUT: Hot day is today. You can go swimming!

# run ~$ python3 sys_2.py
# OUTPUT: WARNING: You need to provide an argument

# run ~$ python3 sys_2.py
# OUTPUT: Please, provide valid argument
