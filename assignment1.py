def primepartition(m):
    primelist=[]
    if m<0:
      return False
    else:
      for i in range(2,m+1):
         for n in range (2,i):
           if (i%n) == 0:
             break
      else:
        primelist.append(i)
    for a in primelist:
      diff = m - a
      if diff in primelist:
        return True
    return False

def matched(s):
  bcount = 0
  n = 0
  while bcount >= 0 and n < len(s):
    if s[n] == '(':
      bcount += 1
    elif s[n] == ')':
      bcount -= 1
    n += 1
  if bcount == 0:
    return True
  else:
    return False
print(len([1,2,3,4,5]))

#incorrect
def rotatelist(l, k):
  if k < 0:
    return (l)
  else:
    for i in range(1, k):
      if k == 1:
        return l[k:] + l[0]
      elif k < len(l):
        return l[k:] + l[0:(len(l) + 1) - k]
      elif k > len(l):
        k = k % len(l)
        return l[k:] + l[:k]


##SOLUTIONS>>
def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist.append(i)
  return(factorlist)

def prime(n):
  return(factors(n)==[1,n])

def primepartition(n):
  for i in range(1,n//2+1):
    if prime(i) and prime(n-i):
      return(True)
  return(False)

###########

def matched(s):
  nesting = 0
  for c in s:
    if c == '(':
      nesting = nesting + 1
    elif c == ')':
      nesting = nesting - 1
    if nesting < 0:
      return(False)
  return(nesting == 0)

###########

def rotatelist(l,k):
  retlist = l[:]

  if k <= 0:
    return(retlist)

  for i in range(1,k+1):
    retlist = retlist[1:] + [retlist[0]]
  return(retlist)




