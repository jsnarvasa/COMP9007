def steps_to_n(num):
    '''
    Expects parameter num of type int.  This is the number that we try to reach to from 1
    Returns int - the least number of steps required to reach num 
    In this approach, to get the least number of steps, we are starting from num and tracing back down to 1
    '''

    step_counter = 0
    while num != 1:
        if num % 2 != 0:
            # if we know that num is not divisible by 2, the reduce by 1
            num -= 1
        else:
            num = num/2
        step_counter += 1
    
    return step_counter

print(steps_to_n(1001))