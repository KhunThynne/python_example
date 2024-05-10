import argparse

def main(env):
    print(f"Running in {env} environment")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run my program.")
    parser.add_argument('-d', '--env', default='prod', help='Set the environment (default: prod)')
    args = parser.parse_args()

    main(args.env)


#python argument_example.py -d test