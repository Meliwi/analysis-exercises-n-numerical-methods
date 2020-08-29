# We need to compare some answers
import math
def function_f(x):
    resultadof= x * (math.sqrt(x+1)-math.sqrt(x))
    print("the value is: ",resultadof)
    return 0;
function_f(500)

def function_g(x):
    resultadog= x / (math.sqrt(x+1)+math.sqrt(x))
    print("the value is: ",resultadog)
    return 0;
function_g(500)