import subprocess
import matplotlib.pyplot as plt
fig,axis=plt.subplots(2)
users=100
itr=10
throug=list()
avg_RTT=[]
noofuser=list()
for i in range(itr):
    test = subprocess.Popen(["taskset","-c","1-7","./load_gen","localhost","5000",str(users),"0.1","60"], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    ab=output.decode("ascii")
    print(ab)
    
    noofuser.append(users)
    throug.append(float(ab.split("\n")[5].split(":")[1].strip()))
    avg_RTT.append(float(ab.split("\n")[6].split(":")[1].strip()))
    print(throug)
    axis[0].plot(noofuser,throug,marker='x')
    axis[0].set_title("Throughput")
    axis[0].set_xlabel("Load")
    axis[0].set_ylabel("Throughput")
    axis[1].plot(noofuser,avg_RTT,marker='x')
    axis[1].set_title("Avg RTT")
    axis[1].set_xlabel("Load")
    axis[1].set_ylabel("Avg RTT")

    plt.tight_layout()

    plt.savefig("outputs/throughput_graph.png")
    # plt2.savefig("average_rtt_graph.png")

    users+=200