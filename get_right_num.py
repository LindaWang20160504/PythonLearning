"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？分别每行打印一个输出全部
"""


def get_number_performance(number):
    target_number = []
    for hundred_number in number:
        for tens_digit in number:
            for the_unit in number:
                if (hundred_number != tens_digit) and (tens_digit != the_unit) and (the_unit != hundred_number):
                    target_number.append(hundred_number * 100 + tens_digit * 10 + the_unit)
    return target_number


def print_target_number(items):
    for item in items:
        print(item)
    print('totally count is :', len(items))  # how many numbers


if __name__ == "__main__":
    init_array = [1, 2, 3, 4]
    print_target_number(get_number_performance(init_array))

"""
123
124
132
134
142
143
213
214
231
234
241
243
312
314
321
324
341
342
412
413
421
423
431
432
totally count is : 24
"""
