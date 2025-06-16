def count_multiples(dict):
    result={}

    for i in range(1,10):
        count=sum(1 for j in dict if j%i==0)
        result[i]=count
    return result

nums=[1,2,8,9,12,46,76,82,15,20,30]
print(count_multiples(nums))