#biela manivela (crank connecting rod)

import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib as mpl

# time array
t0=0
t_end=2
dt=0.005
t=np.arange(t0,t_end+dt,dt)

# equações
r=1
l=4
f1=6 # Hz
alpha=2*np.pi*f1*t
x1=r*np.cos(alpha)
y1=r*np.sin(alpha)
x2=0
y2=r*np.sin(alpha)+sqrt(l**2-(r*np.cos(alpha))**2)


############################ animation ###################

frame_amount=len(t)
def update_plot(num):
    manivela.set_data([0,x1[num]],[0,y1[num]])
    biela.set_data([x1[num],x2],[y1[num],y2[num]])
    pistao_1.set_data([x2-0.6,x2-0.6],[y2[num]-0.5,y2[num]+0.5])
    pistao_2.set_data([x2+0.6,x2+0.6],[y2[num]-0.5,y2[num]+0.5])
    pistao_3.set_data([x2-0.6,x2+0.6],[y2[num]+0.5,y2[num]+0.5])
    pistao_4.set_data([x2-0.6,x2+0.6],[y2[num]-0.5,y2[num]-0.5])
    return manivela,biela,pistao_1,pistao_2,pistao_3,pistao_4

# figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,3)

# subplot 1
ax1=fig.add_subplot(gs[:,0:2],facecolor=(0.9,0.9,0.9))
manivela,=ax1.plot([],[],'b',lw=4)
biela,=ax1.plot([],[],'b',lw=4)
cilindro1,=ax1.plot([-0.7,-0.7],[2.7,5],'k',lw=4)
cilindro2,=ax1.plot([0.7,0.7],[2.7,5],'k',lw=4)
pistao_1,=ax1.plot([],[],'b',lw=1)
pistao_2,=ax1.plot([],[],'b',lw=1)
pistao_3,=ax1.plot([],[],'b',lw=1)
pistao_4,=ax1.plot([],[],'b',lw=1)
ax1.spines['left'].set_position('center') # posição eixo
ax1.spines['bottom'].set_position('center') # posição eixo
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.grid(True)

ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,
                           interval=50,repeat=True,blit=True)

plt.show()
