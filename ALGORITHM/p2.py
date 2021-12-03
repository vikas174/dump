def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if 1<n and arr[i]<arr[1]:
        largest=1
    if r<n and arr[largets]<arr[r]:
        laregst=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
def heapsort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,1,0)
arr=[12,11,13,5,6,7,]
heapsort(arr)
n=len(arr)
print("sorted array is")
for i in  range(n):
    print("%d"%arr[i])
