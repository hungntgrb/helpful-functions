filename = 'OnGoing.txt'
n1 = 80
n2 = 101


def gen_nums(a, b):
    for i in range(a, b+1):
        if n2 < 100:
            n = f'{i:02d}'
        elif n2 < 1000:
            n = f'{i:03d}'
        t = f'{n} \n'
        yield t


def main():
    with open(filename, 'w') as f:
        nums = gen_nums(n1, n2)
        for l in nums:
            f.write(l)


if __name__ == '__main__':
    main()
