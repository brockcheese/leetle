def solve(arr):
  ans = -1
  numbersDict = dict()
  print("madeithere")
  for n in arr:
    if n not in numbersDict.keys():
      numbersDict[n] = 1
    else:
      numbersDict[n] += 1
  print("madeithere2")
  for key in numbersDict:
    if key == numbersDict[key] and key > ans:
      ans = key
  print("madeithere3")
  return ans