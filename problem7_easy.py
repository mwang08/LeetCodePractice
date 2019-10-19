# Given a 32-bit signed integer, reverse digits of an integer.


def reverse(x):
    """
    reverse a int
    :param x: int
    :return: reverse
    """

    if x < 0:
        str_x = str(-x)
        result = -int(str_x[::-1])
    else:
        str_x = str(-x)
        result = int(str_x[::-1])

    # C++中，32位int是从-2的31次方到2的31次方之间的数，同理64位。（二进制）
    mina = -2 ** 31
    maxa = 2 ** 31 - 1
    if result not in range(mina, maxa):
        return 0
    else:
        return result


print(reverse(12346))