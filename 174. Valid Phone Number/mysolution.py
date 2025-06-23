def solve(phone):
  digits = "0123456789"
  parenthesis = False
  index = 0
  digitcount = 0
  while index < len(phone):
    if phone[index] in digits:
      digitcount += 1
    elif phone[index] == '(':
      if index == 0:
        parenthesis = True
      else:
        return False
    elif phone[index] == ')':
      if parenthesis == False or index != 4:
        return False
    elif phone[index] in " -.":
      if parenthesis == False and index != 3 and index != 7:
        return False
      elif parenthesis == True and index != 5 and index != 9:
        return False
    else:
      return False
    index += 1
      
  if digitcount != 10:
    return False
  return True
