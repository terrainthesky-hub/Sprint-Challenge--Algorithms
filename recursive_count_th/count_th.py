'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, counter=0):
    if not word:
        return counter
    if word[:2] == 'th':
        counter += 1
        return count_th(word[1:], counter)
    else:
        return count_th(word[1:], counter)




    # return (if word[:2] == 'th':
    #             counter += 1) + count_th(word[2:])
    # (counter += 1 if word[:2] == 'th' else 0) + count_th(word[2:])
    # counter = 0
    # if 'th' in word:
    #     counter += 1
    #     word = word.replace('th', '', 1)
    #     count_th(word)
    # # TBC
    
    # return counter