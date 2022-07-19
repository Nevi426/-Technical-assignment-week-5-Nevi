import dht11
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = []
    for i in range(5):
        x.append(dht11.ambil())
        time.sleep(0.4)
    
    print(x)
    plt.plot(x)
    plt.show()


def panasDingin(suhu):
        if suhu < 30:
            return "masih Dingin"
        else :
            return "sudah Panas"
        
while True:
    hm = dht11.ambil()
    
    #meanmpilkan hasil
    print("%0.1f*C, kondisi "%(hm) + panasDingin(hm))