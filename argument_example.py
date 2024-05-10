import argparse

def main(env):
    print(f"Running in {env} environment")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run my program.")
    parser.add_argument('-d', '--env', default='prod', help='Set the environment (default: prod)')
    parser.add_argument('--optional', help='อาร์กิวเมนต์ที่ไม่จำเป็นต้องใส่', required=False)

    args = parser.parse_args()

    main(args.env)


#python argument_example.py -d test

import argparse


# def argument_Set(arg_name:str,arg_short_name:str,help_description:str="",default:any=False):
#     parser.add_argument(f'-{arg_short_name}', f'--{arg_name}', default=default, help=help_description,required=False)
#     # parser.add_argument(f'-t', f'--test', default=default, help=help_description,required=False)
   




class argument_Set():
    def __init__(self,description="My programe argument.") -> None:
        self.parser = argparse.ArgumentParser(description=description)
    def argument_add(self,arg_name:str,arg_short_name:str,help_description:str="",default:any=False,required=False):
        self.parser.add_argument(f'-{arg_short_name}', f'--{arg_name}', default=default, help=help_description,required=required)
    def argument_create(self):
        return self.parser.parse_args()