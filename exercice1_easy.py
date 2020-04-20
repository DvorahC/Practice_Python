"""
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format
The first line contains the first integer,a .
 The second line contains the second integer,b .

Constraints
1<= a <= 10**10
1<= b <= 10**10
Output Format
Print the three lines as explained above.
"""

a = int(input())
b = int(input())


def test_range(first, second):
    if first in range(1, 10 ** 10) and second in range(1, 10 ** 10):
        print(first + second,"\n", first - second,"\n", first*second)
    else:
        print("The number is outside the given range.")


test_range(a, b)
