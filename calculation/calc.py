#[xc,xwt,xr,xp,diff,d,xt] parameters
#coding,watching,reading,problem solving,difficulty,remaining time(in hr),typing/writing for official submission/Notes
import math
d=4 #hrs
tasks = {
    "outlab": {
        # [0.8,0.4,0.6,0.1,8.0,d*2,0.1],
        "xc" : 0.8,
        "xwt" : 0.4,
        "xr" : 0.6,
        "xp" : 0.1,
        "xt" : 0.1,
        "diff" : 8.0,
        "d" : 2*d
    },
    "ps207": { 
        # [0,0.3,0.5,0.8,6.0,d*2,0],
        "xc" : 0.0,
        "xwt" : 0.3,
        "xr" : 0.5,
        "xp" : 0.8,
        "xt" : 0,
        "diff" : 6.0,
        "d" : 2*d
    },
    "dsalab": {
        # [0.9,0.1,0.3,0.2,7.0,d*2,0.1],
        "xc" : 0.9,
        "xwt" : 0.1,
        "xr" : 0.3,
        "xp" : 0.2,
        "xt" : 0.1,
        "diff" : 7.0,
        "d" : 2*d
        },
    "qq": {
        # [0,0.2,0.25,0.5,3.0,d*2,0],
        "xc" : 0.0,
        "xwt" : 0.2,
        "xr" : 0.25,
        "xp" : 0.5,
        "xt" : 0.0,
        "diff" : 3.0,
        "d" : 2*d
    },
    "215lec": {
        # [0,1.0,0.5,0.2,4.0,d*2,0.2],
        "xc" : 0.0,
        "xwt" : 1.0,
        "xr" : 0.5,
        "xp" : 0.2,
        "xt" : 0.2,
        "diff" : 4.0,
        "d" : 2*d
    },
    "matlab": {
        # [0.5,0.2,0.3,0.3,6.0,d*2,0.8],
        "xc" : 0.5,
        "xwt" : 0.2,
        "xr" : 0.3,
        "xp" : 0.3,
        "xt" : 0.8,
        "diff" : 6.0,
        "d" : 2*d
    },
    "213tut": {
        # [0.3,0.2,0.3,0.7,5.0,d*2,0],
        "xc" : 0.3,
        "xwt" : 0.2,
        "xr" : 0.3,
        "xp" : 0.7,
        "xt" : 0.0,
        "diff" : 5.0,
        "d" : 2*d
    },
    "IEassign": {
        # [0.1,0.2,0.3,0.8,5.0,d*2,0.5],
        "xc" : 0.1,
        "xwt" : 0.2,
        "xr" : 0.3,
        "xp" : 0.8,
        "xt" : 0.5,
        "diff" : 5.0,
        "d" : 2*d
    },
    "207lec" : {
        # [0,1.0,0.2,0.3,3.0,d*2,0.2]
        "xc" : 0.0,
        "xwt" : 1.0,
        "xr" : 0.2,
        "xp" : 0.3,
        "xt" : 0.2,
        "diff" : 3.0,
        "d" : 2*d
    }

}
print ("Time left = "+str(d)+" hrs")
print ("  Task    Self Energy")
for i in tasks:
    E = (1+3*tasks[i]["xc"]+1.5*tasks[i]["xwt"]+tasks[i]["xr"]+2*tasks[i]["xp"]+1.25*tasks[i]["xt"])*math.exp(-tasks[i]["d"]/(4*tasks[i]["diff"]))
    print(i,E)