import matplotlib.pyplot as plt
import numpy as np


# Motor1_SV = np.load('data/body_Lleg.npy')
# Motor2_SV = np.load('data/body_Rleg.npy')
#
# body_SV = np.load('data/bodySV.npy')
# Rleg_SV = np.load('data/RlegSV.npy')
# Lleg_SV = np.load('data/LlegSV.npy')
#
# plt.plot(Motor1_SV, label='Motor1_SV')
# plt.plot(Motor2_SV, label='Motor2_SV')
#
# plt.plot(body_SV, label='body_SV')
# plt.plot(Rleg_SV, label='Rleg_SV')
# plt.plot(Lleg_SV, label='Lleg_SV')

JointSV = np.load('data/JointSV.npy')
plt.plot(JointSV, label='JointSV')

plt.legend()
plt.show()