def sum_and_average(numbers):
    pos_sum = 0  
    neg_sum = 0  
    pos_count = 0  
    neg_count = 0 

    for num in numbers:
        if num > 0:
            pos_sum += num
            pos_count += 1
        elif num < 0:
            neg_sum += num
            neg_count += 1
              pos_avg = pos_sum / pos_count if pos_count > 0 else 0
    neg_avg = neg_sum / neg_count if neg_count > 0 else 0
 return pos_sum, pos_avg, neg_sum, neg_avg
nums = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)
pos_sum, pos_avg, neg_sum, neg_avg = sum_and_average(nums)
print(f"Sum of positive numbers: {pos_sum}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {neg_sum}")
print(f"Average of negative numbers: {neg_avg:.2f}")




def sum_and_avg():
    positive_sum = 0
    negative_sum = 0
    positive_count = 0
    negative_count = 0
    for _ in range(4):
        num = int(input("Enter an integer: "))
        if num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1
    if positive_count > 0:
        positive_avg = positive_sum / positive_count
    else:
        positive_avg = 0
    if negative_count > 0:
        negative_avg = negative_sum / negative_count
    else:
        negative_avg = 0
    print(f"Positive sum: {positive_sum}, Negative sum: {negative_sum}")
    print(f"Positive average: {positive_avg}, Negative average: {negative_avg}")
sum_and_avg()
