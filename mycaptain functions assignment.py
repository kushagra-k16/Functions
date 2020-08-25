import operator
def most_frequent():
    n = input("Please enter a String: ")
    a = {}
    for i in n:
        keys = a.keys()
        if i in keys:
            a[i] += 1
        else:
            a[i] = 1
    ordered_answer = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
    print(ordered_answer)
most_frequent()
