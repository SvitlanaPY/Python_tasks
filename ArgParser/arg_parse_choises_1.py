import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')

parser.add_argument("--education", choices=["highschool", "college", "university", "other"],
                    required=True, type=str, help="Your name")

args = parser.parse_args()

ed = args.education
# if args.education == "college" or args.education == "university": ...
if ed == "college" or ed == "university":
    print("Has degree")
elif ed == "highschool":   # elif args.education == "highschool": ...
  print("Finished Highschool")
else:
    print("Does not have degree")


# run ~$ python3 arg_parse_choises_1.py --education university
# OUTPUT: Has degree


# run ~$ python3 arg_parse_choises_1.py -h
# usage: arg_parse_choises_1.py [-h] --education {highschool,college,university,other}
# A tutorial of argparse!
# optional arguments:
#   -h, --help            show this help message and exit
#   --education {highschool,college,university,other}
#                         Your name