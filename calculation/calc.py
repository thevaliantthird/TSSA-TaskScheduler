import math
from scipy import spatial
import numpy as np
import itertools
#[xc,xwt,xr,xp,diff,d,xt] parameters
#coding,watching,reading,problem solving,difficulty,remaining time(in hr),typing/writing for official submission/Notes

# d=2 #i set deadline for all tasks as d hrs, i.e 2d units of 30 min
# tasks = {
#     "outlab": {
#         # [0.8,0.4,0.6,0.1,8.0,d*2,0.1],
#         "xc" : 0.8,
#         "xwt" : 0.4,
#         "xr" : 0.6,
#         "xp" : 0.1,
#         "xt" : 0.1,
#         "diff" : 8.0,
#         "d" : 2*d
#     },
#     "ps207": { 
#         # [0,0.3,0.5,0.8,6.0,d*2,0],
#         "xc" : 0.0,
#         "xwt" : 0.3,
#         "xr" : 0.5,
#         "xp" : 0.8,
#         "xt" : 0,
#         "diff" : 6.0,
#         "d" : 2*d
#     },
#     "dsalab": {
#         # [0.9,0.1,0.3,0.2,7.0,d*2,0.1],
#         "xc" : 0.9,
#         "xwt" : 0.1,
#         "xr" : 0.3,
#         "xp" : 0.2,
#         "xt" : 0.1,
#         "diff" : 7.0,
#         "d" : 2*d
#         },
#     "qq": {
#         # [0,0.2,0.25,0.5,3.0,d*2,0],
#         "xc" : 0.0,
#         "xwt" : 0.1,
#         "xr" : 0.2,
#         "xp" : 0.5,
#         "xt" : 0.0,
#         "diff" : 3.0,
#         "d" : 2*d
#     },
#     "215lec": {
#         # [0,1.0,0.5,0.2,4.0,d*2,0.2],
#         "xc" : 0.0,
#         "xwt" : 1.0,
#         "xr" : 0.5,
#         "xp" : 0.2,
#         "xt" : 0.2,
#         "diff" : 4.0,
#         "d" : 2*d
#     },
#     "matlab": {
#         # [0.5,0.2,0.3,0.3,6.0,d*2,0.8],
#         "xc" : 0.5,
#         "xwt" : 0.2,
#         "xr" : 0.3,
#         "xp" : 0.3,
#         "xt" : 0.8,
#         "diff" : 6.0,
#         "d" : 2*d
#     },
#     "213tut": {
#         # [0.3,0.2,0.3,0.7,5.0,d*2,0],
#         "xc" : 0.3,
#         "xwt" : 0.2,
#         "xr" : 0.3,
#         "xp" : 0.7,
#         "xt" : 0.0,
#         "diff" : 5.0,
#         "d" : 2*d
#     },
#     "IEassign": {
#         # [0.1,0.2,0.3,0.8,5.0,d*2,0.5],
#         "xc" : 0.1,
#         "xwt" : 0.2,
#         "xr" : 0.3,
#         "xp" : 0.8,
#         "xt" : 0.5,
#         "diff" : 5.0,
#         "d" : 2*d
#     },
#     "207lec" : {
#         # [0,1.0,0.2,0.3,3.0,d*2,0.2]
#         "xc" : 0.0,
#         "xwt" : 1.0,
#         "xr" : 0.2,
#         "xp" : 0.3,
#         "xt" : 0.2,
#         "diff" : 3.0,
#         "d" : 2*d
#     }

# }

def GetEnergy(tasks,task_list):
    ##Ignore this commented code

    # self_energy = {}
    # print ("Time left = "+str(d)+" hrs")
    # print ("  Task    Self Energy")
    # for i in tasks:
        
    #     E = (1+3*tasks[i]["xc"]+1.5*tasks[i]["xwt"]+tasks[i]["xr"]+2*tasks[i]["xp"]+1.25*tasks[i]["xt"])*math.exp(-tasks[i]["d"]/(4*tasks[i]["diff"]))
    #     self_energy[i] = E
    #     print(i,E)    
    # print("========================================")
    # print("       Cosine Similarity            ")

    # # cos_sim = {}
    # # for i in tasks:
    # #     for j in tasks:
    # #         if i==j:
    # #             continue
    # #         v1 = [3*tasks[i]["xc"],1.5*tasks[i]["xwt"],tasks[i]["xr"],2*tasks[i]["xp"],1.25*tasks[i]["xt"]]
    # #         v2 = [3*tasks[j]["xc"],1.5*tasks[j]["xwt"],tasks[j]["xr"],2*tasks[j]["xp"],1.25*tasks[j]["xt"]]
    # #         # print((i,j), "->", (1 - spatial.distance.cosine(v1, v2)) * math.exp(-abs(tasks[i]["d"]/(4*tasks[i]["diff"])-tasks[j]["d"]/(4*tasks[j]["diff"]))))
    # #         sim = (1 - spatial.distance.cosine(v1, v2)) * math.exp(-abs(tasks[i]["d"]/(4*tasks[i]["diff"])-tasks[j]["d"]/(4*tasks[j]["diff"])))
    # #         cos_sim[str(set([i,j]))] = self_energy[i] + self_energy[j] + 0.5*math.sqrt(self_energy[i]*self_energy[j]*sim)

    # sorted_cos = sorted(cos_sim.items(), key=lambda x: x[1], reverse=True)
    # for i in sorted_cos:
    #     print(i[0],"->",i[1])


    #--------------------------------------------------------------------------#
    
    weights = np.array([1,1.25,1.5,2,3]) #reading,typing,watching,problem solving,coding


    #vector of linear terms [xr,xt,xwt,xp,xc]
    linearity_vec = lambda i: np.array([tasks[i]["xr"], tasks[i]["xt"], tasks[i]["xwt"],tasks[i]["xp"] ,tasks[i]["xc"]])

    self_energy = lambda i: (1+3*tasks[i]["xc"]+1.5*tasks[i]["xwt"]+tasks[i]["xr"]+2*tasks[i]["xp"]+1.25*tasks[i]["xt"])*math.exp(-2*tasks[i]["d"]/(tasks[i]["diff"]))


    def cosine_sim(t1,t2):
        v1 = weights*linearity_vec(t1) #assigned weights to all dimensions
        v2 = weights*linearity_vec(t2)
        return (1 - spatial.distance.cosine(v1, v2)) #return cos(angle between them)
    
        # *math.exp(-abs(tasks[t1]["d"]/(tasks[t1]["diff"])-tasks[t2]["d"]/(tasks[t2]["diff"])))
        # i didn't use the line written above , but dont delete it yet. i may need it later



    def energy(t1,t2,dist): #t1,t2 are name of tasks
        if t1 not in tasks or t2 not in tasks:
            print("\nError:- ",t1," not a predefined task\n")
            exit
        E = math.sqrt(self_energy(t1)*self_energy(t2)*cosine_sim(t1,t2))/dist  #Mutual energy (=self if t1=t2)
        return E



    def total_energy(task_list):
        enrg = 0
        vec_list = list(map(lambda x: list(weights*linearity_vec(x)),task_list)) #map a list of tasks to their corresponding vectors
        for i in range(len(vec_list)):
            for j in range(i,i+len(vec_list[i:])):
                enrg+=energy(task_list[i],task_list[j],j-i+1) #mutual energy of all pairs (and self for same i,j)
        return enrg


    # #!!!Important Note- here i am setting deadline just for example!!!#
    # # def set_deadline(perm):
    # #     for i in range(len(perm)): 
    # #         tasks[perm[i]]["d"] = 8 -3*i #this if for vectors of size 3. i am setting deadlines as 8,5,2 half-hours (i.e  4, 2.5 ,1 hr)

    # #i just copied this code from internet, to iterate over all permutations
    # energy_of_perm = {}
    # for perm in itertools.permutations(["qq","dsalab","IEassign"]): #Note- if you change this vector, please change set_deadline function also
    #     set_deadline(perm)
    #     energy_of_perm[perm] = total_energy(perm) 



# sorted_energy_of_perm = sorted(energy_of_perm.items(), key=lambda x: x[1], reverse=True) #copied from internet
# for e in sorted_energy_of_perm:
#     print(e[0],"->",e[1])


