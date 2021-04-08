from matplotlib import pyplot as plt


file_Mn = open('1800011716.txt', mode='r')
lines_Mn = file_Mn.readlines()
file_Mn.close()

file_Co = open('1600011744.txt', mode='r')
lines_Co = file_Co.readlines()
file_Co.close()

file_Ni = open('1800011758.txt', mode='r')
lines_Ni = file_Ni.readlines()
file_Ni.close()

wave_length = []
intensity_Mn = []
intensity_Co = []
intensity_Ni = []

for i in range(len(lines_Mn)):
    wl, it_Mn = lines_Mn[i].split(",")
    _, it_Ni = lines_Ni[i].split(",")
    _, it_Co = lines_Co[i].split(",")
    wave_length.append(eval(wl))
    intensity_Co.append(eval(it_Co))
    intensity_Mn.append(eval(it_Mn))
    intensity_Ni.append(eval(it_Ni))

plt.plot(wave_length, intensity_Mn, label="Fe-Mn")
plt.plot(wave_length, intensity_Co, label="Fe-Co")
plt.plot(wave_length, intensity_Ni, label="Fe-Ni")
plt.xlabel("wave length(nm)")
plt.ylabel("intensity")
plt.legend()
plt.savefig("compare.pdf")

