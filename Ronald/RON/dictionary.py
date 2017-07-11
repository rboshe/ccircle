#1
d = dict()
key = 5
value = key*key
d[key] = value
#2
# import operator
def sort_by_key(dict):
    return sorted(dict)
def reverse_sort_by_key(dict):
    return sorted(dict.items(), reverse=True)
def sort_by_value(dict):
    return sorted(dict.items(), key=operator.itemgetter(1))
    # for tuple (x,y), operator.itemgetter(1) would give your y's value.

d = {
    6: 0.1,
    0: 0,
    1: 'hi',
    3:'roses',
    2:'bye',
    4:'bye2',
}
print(sort_by_key(d))
