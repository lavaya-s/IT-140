'''Word frequencies'''
sentence=input().split()
for word in sentence:
    num=len([1 for w in sentence if w == word])
    print(f'{word} {num}')