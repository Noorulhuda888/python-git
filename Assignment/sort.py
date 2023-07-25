animals = ['duck', 'cat', 'frog']

animals.sort()

print(animals)



animals = ['duck', 'cat', 'frog']

animals.sort(reverse=True)

print(animals)



def myFunc(e):
  return len(e)

animals = ['duck', 'crocodile', 'frog', 'cat']

animals.sort(key=myFunc)

print(animals)



def myFriends(e):
  return e['year']

friends = [
  {'friend': 'Ahmad', 'year': 1995},
  {'friend': 'Ali', 'year': 2002},
  {'friend': 'Khalid', 'year': 2006},
  {'friend': 'Shamir', 'year': 2005}
]

friends.sort(key=myFriends)

print(friends)



def myFunc(e):
  return len(e)

animals = ['duck', 'crocodile', 'frog', 'cat']

animals.sort(reverse=True, key=myFunc)

print(animals)

