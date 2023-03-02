def remove_adjacent(nums):
    return nums
nums=list(set([1,2,2,3]))
result=remove_adjacent(nums)
print(result)


def match_ends(words):
    return words
words=['aba','xyz','aa','x','bbb']
words=len(words)
result=match_ends(words)
print(result)


def front_x(words):
    return words
words=['mix','xyz','apple','xanadu','aardvark']
words=words.sort()
result=front_x(words)
print(result)



def front_x(words):
    list=sorted(list1+list2)
    list.sort(reverse=True)
    return list
list1=['mix','xyz']
list2=['apple','xanadu','aardvark']
result=front_x(list)
print(result)

def front_x(words):
    words.sort(reverse=True)
    return words
words=['mix','xyz','apple','xanadu','aardvark']
result=front_x(words)
print(result)


def sort_last(tuples):
    return tuples
tuples=[(1,7),(1,3),(3,4,5),(2,2)]
tuples.reverse()
result=sort_last(tuples)
print(result)


def linear_merge(list1,list2):
  list=sorted(list1+list2)
  return list
list1=['aa','xx','zz']
list2=['bb','cc']
result=linear_merge(list1,list2)
print(result)


def verbing(s):
  n=len(s)
  if n > 2:
    if s[-3:]=='ing':
      s+='ly'
    else:
      s+='ing'
  return s
print(verbing('ab'))
print(verbing('abc'))
print(verbing('string'))


def not_bad(s):
  m=s.find('not')
  n=s.find('bad')
  if n>m and m>0 and n>0:
    s=s.replace(s[m:(n+3)],'good')
    return s
  else:
    return s
print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad'))