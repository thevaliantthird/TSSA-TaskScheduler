#[xc,xwt,xr,xp,diff,d] parameters
import math
d=8 #hrs
tasks = {
    "outlab": [0.8,0.4,0.6,0.1,8.0,d*2],
    "ps207": [0,0.3,0.5,0.8,6.0,d*2],
    "dsalab": [0.9,0.1,0.3,0.2,7.0,d*2],
    "qq": [0,0.2,0.25,0.5,3.0,d*2],
    "215lec": [0,1.0,0.5,0.2,4.0,d*2],
    "matlab": [0.5,0.3,0.4,0.3,6.0,d*2],
    "213tut": [0.3,0.2,0.3,0.7,5.0,d*2],
    "IEassign": [0.1,0.2,0.3,0.8,5.0,d*2]
}
print ("Time left = ",d," hrs")
print ("  Task    Self Energy")
for i in tasks:
    E = (1+3*tasks[i][0]+1.5*tasks[i][1]+tasks[i][2]+2*tasks[i][3])*math.exp(-tasks[i][5]/(4*tasks[i][4]))
    print(i,E)