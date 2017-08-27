import numpy as np
import matplotlib.pyplot as plt
def read_sum_scores():
   data = np.loadtxt('Bargraph.csv' ,dtype=float , skiprows=3,
                     delimiter=',' , usecols = (i for i in range(1,7)))
   return np.sum(data ,axis=1).tolist()

def get_grade_stat(sum_scores):
   grades =[]
   freq = [0]*5
   grade_set = [[] for _  in range(5)]
   mean_set= []
   sd_set= []
   for x in sum_scores:
      if x < 50:
         grades.append(('F' , x))
         freq[0] += 1
         grade_set[0].append(x)
      elif 50<=x<60:
         grades.append(('D' , x))
         freq[1] += 1
         grade_set[1].append(x)
      elif 60<=x<70:
         grades.append(('C' , x))
         freq[2] += 1
         grade_set[2].append(x)
      elif 70<=x<80:
         grades.append(('B' , x))
         freq[3] += 1
         grade_set[3].append(x)
      elif 80<=x:
         grades.append(('A' , x))
         freq[4] += 1
         grade_set[4].append(x)
#check ;ว่ามีเกรดไรไม่มีมั่ง
   all_grade = 'FDCBA'
   index = 0
   while index < 5:
      if freq[index] == 0:
         print( 'Grade: ' + str(all_grade[index]) +\
                                   ' is missing')
      index +=1
#แต่ละชุดคะแนนของแต่ละเกรด(grade_set)ปลงเป็นarrayเป็นอันๆแล้วดำเนินการเป็นอันๆ
   for i in range(5):
      if len(grade_set[i]) ==0:
         mean_set.extend([0])
         sd_set.extend([0])
      else:
         arr = np.array([grade_set[i]])
         mean_set.extend(np.mean(arr, axis=1).tolist())
         sd_set.extend(np.std(arr, axis=1).tolist())
#-----------------------------------------------------------
   return freq,sd_set,mean_set

#ล่างนี้ผืดเพราะมันจะเพิ่มmatrixให้เท่ากัน ตัวหารเลยเกินจริง
'''#สร้าง array 
    for item in grade_set:
        diff = len(max(grade_set , key=len)) - len(item)
        if diff > 0:
            item.extend([0]*diff)
    grade_cal = np.array(grade_set) 
#หาmean
    avg = np.mean(grade_cal , axis = 1).tolist()
#หาSD
    sd  = np.std(grade_cal , axis = 1).tolist()
    return freq, sd, avg
'''

 
sum_scores = read_sum_scores() # อ่านแฟ้มเพื่อหาคะแนนรวมของนิสิตแต่ละคน 
freq, std, mean = get_grade_stat(sum_scores) #หาสถิติที่ต้องการ
print(freq)
print(std)
print(mean)
print('meanดูตรง*')

fig, ax = plt.subplots(1, 1)
ax2 = ax.twinx()
grades = ('F', 'D', 'C', 'B', 'A')
x_pos = np.arange(len(grades))
plt.xticks(x_pos, grades)
ax.set_xlabel("Grade distribution")
ax.set_ylabel("Number of students")
ax.bar(x_pos, np.array(freq),  align='center', alpha=0.4)
ax2.set_ylabel("Mean scores")
ax2.set_ylim(0, 100)
plt.errorbar(x_pos, np.array(mean), np.array(std), \
             linestyle='None', marker='*')
plt.show()

