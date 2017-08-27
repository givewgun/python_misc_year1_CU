#logistic regression
import numpy as np

data = np.array([[15,3.78],
                 [29,2.0],
                 [10,2.5],
                 [25,2.85],
                 [30,3.96]])

print("Which student's score do you want to compute?")
n = int(input('Student no.: '))
student_data = data[n-1]

def logit(row):
    return -3.98 + 0.2*student_data[0] + 0.5*student_data[1]

def p(row):
    return 1.0 / (1 + np.exp(1)**logit(row))
def pass_or_not(row):
 return p(row) > 0.5

print(logit(student_data) , p(student_data),pass_or_not(student_data))
