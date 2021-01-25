def cumm_sum(a, sum1, i):
    # print(i)
    if i == 0:
        sum1.append(a[i])
        cumm_sum(a, sum1, i+1)
    else:
        sum1.append(sum1[i-1]+a[i])
        # print(sum)
        if i+1 == len(a):
            print(sum1)
            quit()
        else:
            cumm_sum(a, sum1, i+1)



sum1 = cumm_sum([5, 2, 3, 4], [], 0)
print(sum1)
