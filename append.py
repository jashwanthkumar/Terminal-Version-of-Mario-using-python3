from Matrix import *
from alien import *

pis.append(pipe(108,28,13))
pis.append(pipe(138,28,13))
pis.append(pipe(-50,34,12))
pis.append(pipe(-15,34,7))
pis.append(pipe(-15,34,7))
pis.append(pipe(28,28,13))
pis.append(pipe(300,34,7))
pis.append(pipe(360,34,7))
pis.append(pipe(367,29,12))
pis.append(pipe(374,24,17))
pis.append(pipe(381,19,22))

hols.append(Holes(-27,41))
hols.append(Holes(-18,41))
hols.append(Holes(9,41))
hols.append(Holes(0,41))
hols.append(Holes(-9,41))
hols.append(Holes(250,41))
hols.append(Holes(259,41))
hols.append(Holes(310,41))
hols.append(Holes(319,41))
for i in range(1,20):
    hols.append(Holes(510+i*10,41))
for i in range(1,20):
    pis.append(pipe(450+i*14,28,3))
for i in range(1,50):
    if i % 2:
        alis.append(Alien(1000+i*10,1))
    else:
        alis.append(Alien(1000+i*10,-1))
alis.append(Alien(700,-1))
alis.append(Alien(580,-1))
alis.append(Alien(520,-1))
alis.append(Alien(200,-1))
alis.append(Alien(210,-1))
tpis.append(Tpipe(824,15,26))
tpis.append(Tpipe(831,19,22))
tpis.append(Tpipe(838,23,18))
tpis.append(Tpipe(845,27,14))
tpis.append(Tpipe(852,31,5))
tpis.append(Tpipe(859,31,5))
tpis.append(Tpipe(866,27,14))
tpis.append(Tpipe(873,23,18))
tpis.append(Tpipe(880,19,22))
tpis.append(Tpipe(887,15,26))
for i in range(1,100):
    clouds.append(cloud(i*15,3))
    clouds.append(cloud(i*15+1,8))
