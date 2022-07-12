# Problem 65:
#     Convergents of e
#
# Description:
#     The square root of 2 can be written as an infinite continued fraction.
#         sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...))))
#
#     The infinite continued fraction can be written, sqrt(2) = [1;(2)],
#       (2) indicates that 2 repeats *ad infinitum*.
#     In a similar way, sqrt(23) = [4;(1,3,1,8)].
#
#     It turns out that the sequence of partial values of continued fractions
#       for square roots provide the best rational approximations.
#
#     Let us consider the convergents for sqrt(2).
#         1 + 1 / 2                             =  3 /  2
#         1 + 1 / (2 + 1/2)                     =  7 /  5
#         1 + 1 / (2 + 1 / (2 + 1/2))           = 17 / 12
#         1 + 1 / (2 + 1 / (2 + 1 / (2 + 1/2))) = 41 / 29
#
#     Hence the sequence of the first ten convergents for sqrt(2) are:
#         1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#
#     What is most surprising is that the important mathematical constant,
#         e = [ 2 ; 1, 2, 1, 1, 4, 1, 1, 6, 1,..., 1, 2k, 1, ...]
#
#     The first ten terms in the sequence of convergents for *e* are:
#         2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
#     The sum of digits in the numerator of the 10'th convergent is 1 + 4 + 5 + 7 = 17.
#
#     Find the sum of digits in the numerator of the 100'th convergent of the continued fraction for *e*.

from math import e
from typing import Tuple


def main(i: int) -> Tuple[int, int]:
    """
    Returns the numerator and denominator of the i'th convergent of e.

    Args:
        i (int): Natural number

    Returns:
        (Tuple[int, int]): Numerator/denominator of n'th convergent of e.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(i) == int and i > 0

    # Idea:
    #     Let convergent `i` of `e` be called c{i}.
    #     Then the fraction c{i} is equal to n{i} / d{i}.
    #
    #     Figured out the following (for i ≥ 2):
    #         n{i} = a{i} * n{i-1} + n{i-2}
    #         d{i} = a{i} * d{i-1} + d{i-2}
    #
    #     Base case values for the recurrence:
    #         n{0} = 2,     d{0} = 1,       c{0} = n{0} / d{0} = 2 / 1 = 2
    #         n{1} = 3,     d{1} = 1,       c{1} = n{1} / d{1} = 3 / 1 = 3
    #
    #     Wish I had a clean proof for it, but couldn't figure it out... :/

    if i == 1:
        return 2, 1
    elif i == 2:
        return 3, 1
    else:
        # Only need previous two elements to get next numerator/denominator
        ns = [2, 3]
        ds = [1, 1]
        for j in range(3, i+1):
            a = 2*j//3 if j % 3 == 0 else 1
            ns.append(a * ns[-1] + ns[-2])
            ds.append(a * ds[-1] + ds[-2])
            ns.pop(0)
            ds.pop(0)
        return ns[-1], ds[-1]


if __name__ == '__main__':
    convergent_number = int(input('Enter a natural number: '))
    convergent_numerator, convergent_denominator = main(convergent_number)
    print('Convergent #{} of e is:'.format(convergent_number))
    print('    Numerator   = {}'.format(convergent_numerator))
    print('    Denominator = {}'.format(convergent_denominator))
    print('Actual values:')
    print('    Actual e   = {:.20f}'.format(e))
    print('    Convergent = {:.20f}'.format(convergent_numerator/convergent_denominator))
    convergent_numerator_sum = sum(map(int, list(str(convergent_numerator))))
    print('Sum of numerator digits:')
    print('    {}'.format(convergent_numerator_sum))
