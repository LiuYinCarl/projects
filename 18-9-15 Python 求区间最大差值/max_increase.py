def max_increase(seq):
    increase = 0
    num = len(seq)
    # if the elements are less than 2, return 0
    if num < 2:
        return 0
    for i in range(num):  # i is incremented as the number that appears first
        for j in range(i + 1, num):  # j is incremented on the basis of i
            diff = seq[j] - seq[i]  # Calculate the difference between i and j
            if diff > increase:
                increase = diff # use the new bigger difference replace the old one
    return increase


if __name__ == '__main__':
    seq = [226, 264, 337, 364, 485, 529]
    seq2 = (226, 264, 337, 364, 485, 529)
    print(max_increase(seq))
    print(max_increase(seq2))
