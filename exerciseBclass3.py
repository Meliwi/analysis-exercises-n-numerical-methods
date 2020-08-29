
# implementation directly
def funcion_p(x):
    value_p = pow(x,3) - (3 * pow(x,2)) + (3*x) - 1
    print("the value is: ", value_p)
    return 0;

funcion_p(2.19)
# Using Horner algorithm


def function_hornerfor(x):
  coef = [1,-3,3,-1];
  value = 0
  for i in range (0,len(coef)):
    value = coef[i] + value * x
  print ( "the value is: ",value)

function_hornerfor(2.19)


