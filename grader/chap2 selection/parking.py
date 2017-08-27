#parking
#hr to minute = *60
import math
import time
start_time = time.time()


hr_in = float(input()) #ชม.นาที in
min_in = float(input())
min_all_in = 60*hr_in + min_in
#-------
hr_out = float(input()) #ชม.นาที out
min_out = float(input())
min_all_out = 60*hr_out + min_out
t = min_all_out - min_all_in #เวลาจอดรวม
pay =0

if t <= 15:
    pay+=0
    print(pay)
elif t> 6*60:
    pay+=200
    print(pay)
elif 15<  t <= 3*60:  #จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
    pay += 10*math.ceil(t/60)
    print(pay)
elif 3*60<  t <= 6*60: #จอดรถตั ้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง (รวมกรณีก่อนหน้าด้วย)
        pay += 10*3 + 20*math.ceil((t-3*60)/60)
        print(pay)


print("--- %s seconds ---" % (time.time() - start_time))

    
    
        
    
    



