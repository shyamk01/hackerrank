#!/bin/python3
#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    s_swap=sentence.swapcase().split()
    result=' '.join(reversed(s_swap))
    return result

if __name__ == '__main__':
    sentence = input("please enter a sentences")
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)

