def swap(n, p1, p2):
    # Move p1'th to rightmost side
    bit1 = (n >> p1) & 1
    # Move p2'th to rightmost side
    bit2 = (n >> p2) & 1

    new1 = n >> p2 | bit1 << p2 # change p2 value
    new2 = new1 >> p1 | bit2 << p1 # change p1 value

    return new2

def swap_bits(n):
    a, b = 0, 1
    while n >> b:
        n = swap(n, a, b)
        a += 1
        b += 1
    return n