#factorial methods test
import time
import matplotlib.pyplot as plt

def alt_fact(n):
    ans = 1
    start = time.time()
    for i in range(n,1,-1):
        ans = ans*i
    end = time.time()
    time_taken = end-start
    #print("Time taken to calculate factorial by alt method is ",time_taken)
    return ans, time_taken

def fact(n):
    if n>=1:
        return (n*fact(n-1))
    else:
        return 1
    
def do_fact(n):
    start = time.time()
    ans = fact(n)
    end = time.time()
    time_taken = end-start
    #print("Time taken to calculate factorial by recursion is ",time_taken)
    return ans, time_taken

def compare(num):
    fact_no_recursion, time_no_recursion = alt_fact(num)
    fact_yes_recursion, time_yes_recursion = do_fact(num)
    time_diff = 0
    if fact_no_recursion==fact_yes_recursion:
        if time_no_recursion<time_yes_recursion:
            time_diff_1 = time_yes_recursion-time_no_recursion
            return time_diff_1,"worse"
        elif time_no_recursion>time_yes_recursion:
            time_diff_2 = time_no_recursion-time_yes_recursion
            return time_diff_2,"better"
        else:
            time_diff_3 = time_no_recursion-time_yes_recursion
            return time_diff_3,"equal"
    
def plot_results():
    iterations_worse,iterations_better,iterations_equal,times_better,times_worse,times_equal = [],[],[],[],[],[]
    for i in range(1,990):
        time, string = compare(i)
        if "worse" in string:
            iterations_worse.append(i)
            times_worse.append(time)
        elif "better" in string:
            iterations_better.append(i)
            times_better.append(time)
        elif "equal" in string:
            iterations_equal.append(i)
            times_equal.append(time)

    print("Times recursion was better: ", len(times_better))
    print("Times recursion was worse: ", len(times_worse))
    print("Times recursion was equal: ", len(times_equal))
    
    plt.scatter(iterations_worse,times_worse,color="r")
    plt.scatter(iterations_better,times_better,color="b")
    plt.scatter(iterations_equal,times_equal,color="g")
    plt.show()   
    
plot_results()

