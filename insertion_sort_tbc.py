def insertion_sort(A):
  N = len(A)
  for i in range(1,N):           
    for j in range(i,0,-1):      
      if A[j-1] <= A[j]:         
        break
      A[j],A[j-1] = A[j-1],A[j]
  return A 