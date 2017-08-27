import math

class Circle:

    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    
    def contain_point(self,px,py): 
        # ทดสอบว่าจุดอยู่ในวงกลมหรือไม่ ถ้าอยู่จะคืน True ถ้าไม่อยู่ จะคืน False
        if distance(self.x,self.y,px,py) <= self.r:
            return True
        return False

    def touch(self,other):
        # ทดสอบว่าวงกลมสองวง ซ้อนทับกัน หรือว่า แตะกัน หรือไม่
        if distance(self.x,self.y,other.x,other.y) < self.r+other.r :
            return 'Overlap'
        elif distance(self.x,self.y,other.x,other.y) == self.r+other.r:
            return 'Touch'
        return 'Free'

    def area(self):
        return math.pi*(self.r**2) # คืนพื้นที่วงกลม

def distance(x1,y1,x2,y2): 
    # หาระยะห่างระหว่างจุดสองจุด
    return ((x1-x2)**2+(y1-y2)**2)**0.5

#----------------------------------------------------------------------------

class Cluster: # แทนแต่ละลิสต์ย่อยของวงกลม

    def __init__(self,c):
        self.circles = [c] # สร้างลิสต์ของวงกลมที่มีสมาชิกเป็นวงกลม c
 
    def add_circle(self,c):
        self.circles.append(c) # เพิ่มวงกลม c เข้าไปใน self.circles

    def merge_cluster(self,other):
        self.circles.extend(other.circles) # รวมลิสต์วงกลมจาก other เข้าไปใน self
        other.circles = []

    def is_empty(self): # ใช้ตรวจสอบว่า cluster นี้ว่างหรือไม่
        if self.circles == list():
            return True
        return False

    def contain_circle(self,c): # ใช้ตรวจสอบว่าวงกลม c ควรจะเข้าไปอยู่ใน cluster นี้หรือไม่
        for circle in self.circles:
            if c.touch(circle) != 'Free':
                return True
        return False

#----------------------------------------------------------------------------

def build_clusters(Cs): # สร้างลิสต์ของ Cluster จากลิสต์ของวงกลม Cs
    clusters = []
    for i in range(len(Cs)):
        found_in_cluster = False
        active_cluster = -1
        for j in range(len(clusters)):
            if clusters[j].contain_circle(Cs[i]):
                if active_cluster == -1:
                    clusters[j].add_circle(Cs[i])
                    active_cluster = j
                else: 
                    clusters[active_cluster].merge_cluster(clusters[j])
                found_in_cluster = True
        if found_in_cluster == False:
            clusters.append(Cluster(Cs[i]))
        new_clusters = []
        for k in range(len(clusters)):
            if not clusters[k].is_empty():
                new_clusters.append(clusters[k])
        clusters = new_clusters
    return clusters

#----------------------------------------------------------------------------

# ส่วนของโปรแกรมหลักให้เขียนต่อเอง
n = int(input().strip())
px,py = [float(e) for e in input().strip().split()]
c_list = []
for i in range(n):
    c_data = [float(e) for e in input().strip().split()]
    c_data = Circle(c_data[0],c_data[1],c_data[2],c_data[3]) #[x,y,r,ส]
    c_list.append(c_data)

c_cluster = build_clusters(c_list)


p_in_cl = False
for c_l in c_cluster:
    for c in c_l.circles: #cl มันยังเป็นclassอยู่ ต้องเรียกmethodเพื่อแปลงเป็นlist
        #print(c.r,c.color)
        if c.contain_point(px,py):
            #print("--check--")
            p_in_cl = True
            break
    if p_in_cl:
        area_t = 0
        light_t = 0
        for c in c_l.circles:
            #print(c.r,c.color)
            area = math.pi*(c.r**2)
            area_t += area
            light_t += area*(c.color)
        print(light_t/area_t)
        break
if not p_in_cl:
    print(1.0)
            
            
