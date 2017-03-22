# Initial conditions: Sumatoria de tiempo de salida, llegada, cantidad de
# llegadas, sumatoria de tiempo ocioso
STS, STLL, CLL, STO = 0, 0, 0, 0


# TPS/TPLL : Tiempo proxima salida/llegada
# NS : Numero de personas en el sistema
t = 0
ITO = 0
NS = 0
TPLL = 0
# TPS = High Value
TPS = 10000000000000000000
# Cantidad de tiempo que va a correr
TF = 1000

# Vector Tiempo de Atencion, es decir TPS = VTA[0]
VTA = [15, 20, 5, 20, 5, 15, 10, 10]

# Vector Intervalo entre Arribos, es decir TPLL = VIA[0]
VIA = [10, 5, 35, 10, 25, 45, 10, 5]
i, j = 0, 0
while t <= TF:
    if TPLL <= TPS:
        if i < len(VTA):
            print "Entrada\n"
            t = TPLL
            TPLL = t + VIA[i]
            NS = NS + 1
            print "Numero de personas en el sistema es :" + str(NS) + "\n"
            STLL = STLL + t

            CLL = CLL + 1
            print "Cantidad total de personas que vinieron es :" + str(CLL) + "\n"
            i = i + 1
            if NS == 1:
                TPS = t + VTA[j]
                STO = STO + t - ITO
                j = j + 1
    else:
        t = TPS
        print "Salida\n"
        print "time is :\n" + str(t)

        STS = STS + t

        if NS > 0:
            TPS = t + VTA[i]
            print "Tiempo de proxima salida es: " + str(TPS) + "\n"
            NS = NS - 1
            print "Numero de personas en el sistema es :" + str(NS) + "\n"
            print "Cantidad total de personas que vinieron es :" + str(CLL) + "\n"
# Get results

PPS = (STS - STLL) / CLL
PTO = STO * 100 / t
print "results: \n"
print "PTO = " + str(PTO) + "\n"
print "PPS = " + str(PPS) + "\n"
