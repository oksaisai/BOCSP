import pickle
import sys
sys.setrecursionlimit(1000000)

def load_variable(filename):
    f = open(filename, 'rb')
    r = pickle.load(f)
    f.close()
    return r

collection_ins = []
collection_scale = load_variable("Ins_For_Scale.txt")
for ind_ins in collection_scale:
    collection_ins.append(ind_ins)
collection_te = load_variable("Ins_For_TE.txt")
for ind_ins in collection_te:
    collection_ins.append(ind_ins)
collection_var = load_variable("Ins_For_Var.txt")
for ind_ins in collection_var:
    collection_ins.append(ind_ins)

# the key attributes of the instances
for ins in collection_ins:
    print(ins.M_num)  # the number of the machines
    print(ins.J_num)  # the number of the jobs
    print(ins.O_num)  # the number of the operations
    print(ins.Processing_time)  # the processing time list of each operation of each job
    print(ins.Travel_time)  # the travelling matrix between each position
    print(ins.get_inf())  # An list consisting of seven elements: [tt_tp, mean_tp, var_tt, var_tp, et_ep, mean_ep, var_ep]
    # tt_tt: the ratio of the mean travelling time and mean processing time
    # mean_tp: the mean value of processing time
    # var_tt: the variance value of travelling time
    # var_tp: the variance value of processing time
    # et_ep: the energy ratio of the traveling stages and processing stages
    # mean_ep: the mean energy value of the processing time
    # var_ep: the variance energy value of the processing time

