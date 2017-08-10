# -*- coding: utf-8 -*-

def substring(m, n, i, j):
    # 先将N中第0位到第i-1位一共i位保存下来
    part1 = (1 << i) - 1  # 1 + i个0，再减1即i个1
    part1 &= n
    # 再将N中第0位到第j位全清0，有j+1个数，通过右移加左移实现
    part2 = n >> (j + 1) << (j + 1)
    # m右边添i个0
    part3 = m << i

    return part2 | part3 | part1

if __name__ == '__main__':
  n = 10000000000
  m = 10101
  print substring(m, n, 2, 6)