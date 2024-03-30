import argparse

def multiply(z, w):
    ans = z * w
    print(ans)
    return ans

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add two numbers')
    parser.add_argument('--z', type=int, required=True, help='first number')
    parser.add_argument('--w', type=int, required=True, help='second number')
    args = parser.parse_args()
    multiply(args.z, args.w)