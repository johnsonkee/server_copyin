import pickle
import sys

adv_name = sys.argv[1]
y_origin_name = sys.argv[2]

adv = pickle.load(open(adv_name,"rb"))
adv_toadd = pickle.load(open("x_adv500.pkl","rb"))

y_origin = pickle.load(open(y_origin_name,"rb"))
y_origin_toadd = pickle.load(open("y_origin500.pkl","rb"))

for i in range(len(adv_toadd)):
    adv.append(adv_toadd[i])
    y_origin.append(y_origin_toadd[i])

pickle.dump(adv,open("../x_adv{}.pkl".format(len(adv)),"wb"))
pickle.dump(y_origin,open("../y_origin{}.pkl".format(len(adv)),"wb"))
