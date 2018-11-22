# Python program to find the maximum for  
# each and every contiguous subarray of 
# size k 
  
# Method to find the maximum for each 
# and every contiguous subarray of s  
# of size k 
def subArrayMaximum(arr, n, k) :

    for i in range(n - k + 1):
        max = arr[i];
        for j in range(1, k) :
            if arr[i+j] > max :
                max = arr[i+j]
        print(max)  

        

# Driver Code 
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
        
sub_array_size = 3;
subArrayMaximum(arr, len(arr), sub_array_size)

