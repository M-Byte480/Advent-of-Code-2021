from collections import Counter
import string

lines = [line.strip() for line in open('AdventOfCodeDay14.txt', 'r').readlines()]
print(lines)
template = lines[0]
rules = [rule.split(' ') for rule in lines[2:]]
print(rules)
rules = {a: (a[0]+c,c+a[1]) for a,b,c in rules}
print(rules)
pairs = [''.join(p) for p in zip(template, template[1:])]
print(pairs)
# total the pairs created by substitution
def run(steps):
    ctr = Counter(pairs)
    for i in range(steps):
        newCtr = {key : 0 for key in rules.keys()}
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value
        ctr = newCtr

    letterTotals = {letter : 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letterTotals[key[0]] += value

    # the last character in the template gets another count
    letterTotals[template[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    return lmax - lmin

# print('part 1:', run(10))
# print('part 2:', run(40))