import pickle
import sys
import shutil
import os

if sys.argv[1] and sys.argv[2]:
    adv_name = sys.argv[1]
    y_origin_name = sys.argv[2]
else:
    print "adv_name and y_name is needed"
    exit

adv = pickle.load(open(adv_name,"rb"))
adv_toadd = pickle.load(open("x_adv500.pkl","rb"))

y_origin = pickle.load(open(y_origin_name,"rb"))
y_origin_toadd = pickle.load(open("y_origin500.pkl","rb"))

for i in range(len(adv_toadd)):
    adv.append(adv_toadd[i])
    y_origin.append(y_origin_toadd[i])
print len(adv)
pickle.dump(adv,open("x_adv{}.pkl".format(len(adv)),"wb"))
pickle.dump(y_origin,open("y_origin{}.pkl".format(len(adv)),"wb"))

def native_cp(path_new):
    shutil.copyfile(adv_name,"{}/{}".format(path_new,adv_name))
    shutil.copyfile(y_origin_name,"{}/{}".format(path_new,y_origin_name))
    
native_cp("old_examples")

os.remove(adv_name)
os.remove(y_origin_name)
