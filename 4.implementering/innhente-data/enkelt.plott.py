import matplotlib.pyplot as plt

# x=[0,1,2,3,4,5]
# y=[]

# #plt.plot(x,y) #opretter plot
# #plt.show() #viser plottet

# #utfordring

# for i in range (0,6):
#     tall=3*i+2
#     y.append(tall)
# #plt.plot(x,y) linje
# #plt.scatter(x,y) prikker
# plt.show()


# Tegn grafen til funksjonen f(x) = 2x – 3. 

import numpy as np

# xverdier = np.linspace(0, 20, 50)
# yverdier = xverdier*2-3

# plt.title("Graf")

# plt.plot(xverdier, yverdier)

# plt.grid()
# plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2)
# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.xlim(-40, 20)
# plt.ylim(-40, 400)

# plt.show()


# Juster utseendet til grafen ved å bruke innebygde stiler. Prøv minst fem forskjellige stiler.
# Juster utseendet til grafen uten å bruke en innebygd stil. Prøv deg fram med ulike farger og andre egenskaper.



xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()

# Graf 3
yverdier = 2**2

plt.subplot(2, 2, 3)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 4
yverdier = xverdier/3

plt.subplot(2, 2, 4)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()