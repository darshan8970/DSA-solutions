if __name__ == '__main__':
    # Read dimensions and the target sum restriction
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Generate coordinates where the sum of i, j, k is not equal to n
    result = [
        [i, j, k] 
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1) 
        if i + j + k != n
    ]
    
    print(result)
