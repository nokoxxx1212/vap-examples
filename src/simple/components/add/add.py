import argparse

def add(x, y):
    ans = x + y
    print(ans)
    return ans

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add two numbers')
    parser.add_argument('--x', type=int, required=True, help='first number')
    parser.add_argument('--y', type=int, required=True, help='second number')
    args = parser.parse_args()
    add(args.x, args.y)