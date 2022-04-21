def listsum(numList):

    #base case when numlist hits 1
    if len(numList) == 1:
        return numList[0]
    else:
        #python [1:] reduces the list -1 each time, so numlist[0] is a new ele
        return numList[0] + listsum(numList[1:])

listy = [1,3,5,7,9]

print(listsum(listy))

"""
java code

class Test {
    static int arr[] = { 1, 2, 3, 4, 5 };
 
    // Return sum of elements in A[0..N-1]
    // using recursion.
    static int findSum(int A[], int N)
    {
        if (N <= 0)
            return 0;
        return (findSum(A, N - 1) + A[N - 1]);
    }
 
    if(N <= 0){
    return 0;
    }
    
    return (findSum(A, N-1) + A[N - 1]);
    
    // Driver method
    public static void main(String[] args)
    {
        System.out.println(findSum(arr, arr.length));
    }
}

"""
