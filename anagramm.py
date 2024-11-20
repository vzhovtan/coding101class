'''func to verify if two given strings are anagramm'''

def anagramm(s1, s2: str) -> bool:
  if len(s1) != len(s2):
    return False
  for i in s1:
    if i not in s2:
      return False
  return True