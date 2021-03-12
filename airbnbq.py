#an AirBnB interview question to find the first number which cannnot be made by summing any subset of an input list
#a no doubt messy and complicated way of doing it but it does work
#23 Nov 2020


input = [1, 2, 3, 8, 9, 10]

def smallest(input):
    sum_list = [i for i in input]
    for i in range(len(input)):
        for j in range(len(input)):
            sum_list.append(input[i] + input[j])
            
    sum_list.sort()
    # print(sum_list)
    answer = []
    for i in range(sum_list[len(sum_list)-1]):
        if i not in sum_list:
            answer.append(i)
            # print(answer)        
    return answer[1]

print(smallest(input))