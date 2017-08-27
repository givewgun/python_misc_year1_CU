import numpy as np

def read_height_weight():
    list_hw = []
    for k in range(int(input())) :
        h,w = input().split()
        list_hw.append((int(h),int(w)))
    return np.array(list_hw)

def cm_to_m(x):
    return x / 100
def cal_bmi(hw): #[h,w]
    hw = np.array(hw,float)#type ต้องเหมือนกัน
    hw[:,0] =  cm_to_m(hw[:,0])#ความสูง
    #print(hw)
    bmi = []
    for d in hw:
        bmi.append(d[1]/(d[0]**2))
    return np.array(bmi,float)
        
def main():
    hw = read_height_weight()
    bmi = cal_bmi(hw)
    avg_bmi = np.mean(bmi, axis=0)#[a b c]
    count_underweight = sum([1 for i in bmi if i < 18.5])
    print('average bmi =', avg_bmi)
    print('#bmi < 18.5 =', count_underweight)
exec(input().strip())
