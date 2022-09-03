import time
hora = time.strftime("%H:%M",time.localtime())
print(hora)

def clockWork(clock):
    if clock > (time.strftime("%H:%M",time.localtime()) == 19):
        print("Hora de ir a Casa son las ", clock)
    else:
        print("Todavia te faltan", clock - time.localtime)

clockWork(hora)