def consecutiveArrMaxSum(arr, n) :

    maxTillNow = 0;
    maxOverall = 0;

    for i in range(n) :

        maxTillNow = maxTillNow + arr[i];

        if(maxOverall < maxTillNow) :
            maxOverall = maxTillNow;

        if(maxTillNow < 0) :
            maxTillNow = 0;

    print("Maximum till now - " + str(maxOverall));

# Driver Code 
arr = [-2, -3, 4, -1, -2, 1, 8, -3]
        
consecutiveArrMaxSum(arr, len(arr))