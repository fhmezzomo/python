#  Piston motion - connecting rod crank mechanism

import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib as mpl

# time array
t0=0
t_end=1
dt=0.005
t=np.arange(t0,t_end+dt,dt)

# equações básicas
r=1
l=4
f1=6 # Hz
alpha=2*np.pi*f1*t
y1=r*np.sin(alpha)
x1=r*np.cos(alpha)
y2=0
x2=r*np.cos(alpha)+sqrt(l**2-(r*np.sin(alpha))**2)

# velocidade - primeira derivada
vx=-r*np.sin(alpha)-r**2*np.sin(alpha)*np.cos(alpha)/(sqrt(l**2-(r*np.sin(alpha))**2))

# aceleracao - segunda derivada
ac_1=r*np.cos(alpha)
ac_2=(r**2*(np.cos(alpha)**2-np.sin(alpha)**2)/(sqrt(l**2-(r*np.sin(alpha))**2)))
ac_3=(r**4*(np.sin(alpha)**2*np.cos(alpha)**2)/(sqrt(l**2-(r*np.sin(alpha))**2)))
acx=-ac_1-ac_2-ac_3
#acel=-r*np.cos(alpha)-

############################ animation ###################
frame_amount=len(t)
def update_plot(num):

# 1st subplot
    manivela.set_data([0,x1[num]],[0,y1[num]])
    biela.set_data([x1[num],x2[num]],[y1[num],y2])
    pistao_1.set_data([x2[num]-0.6,x2[num]-0.6],[y2-0.5,y2+0.5])
    pistao_2.set_data([x2[num]+0.6,x2[num]+0.6],[y2-0.5,y2+0.5])
    pistao_3.set_data([x2[num]-0.6,x2[num]+0.6],[y2+0.5,y2+0.5])
    pistao_4.set_data([x2[num]-0.6,x2[num]+0.6],[y2-0.5,y2-0.5])

# 2nd subplot
    pos_x.set_data(t[0:num],x2[0:num])
    #print(x2[0:num])

# 3nd subplot
    veloc.set_data(t[0:num],vx[0:num])

# 4nd subplot
    acel.set_data(t[0:num],acx[0:num])
    
    return manivela,biela,pistao_1,pistao_2,pistao_3,pistao_4,pos_x,veloc,acel

# figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)
fig.tight_layout()

# subplot 1
ax1=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
manivela,=ax1.plot([],[],'b',lw=4)
biela,=ax1.plot([],[],'b',lw=4)
cilindro1,=ax1.plot([2.7,5],[-0.7,-0.7],'k',lw=4)
cilindro2,=ax1.plot([2.7,5],[0.7,0.7],'k',lw=4)
pistao_1,=ax1.plot([],[],'b',lw=1)
pistao_2,=ax1.plot([],[],'b',lw=1)
pistao_3,=ax1.plot([],[],'b',lw=1)
pistao_4,=ax1.plot([],[],'b',lw=1)
ax1.spines['left'].set_position('center') # posição eixo
ax1.spines['bottom'].set_position('center') # posição eixo
plt.xlim(-2,6)
plt.ylim(-4,4)
plt.grid(True)

# subplot 2
ax2=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
pos_x,=ax2.plot([],[],'b',lw=3)
plt.xlabel('tempo',fontsize=15)
plt.ylabel('posição do pistão',fontsize=15)
#plt.title('Posição em relação ao ângulo da manivela',fontsize=15)
plt.xlim(0,0.3)
plt.ylim(2.9,5.1)
plt.grid(True)

# subplot 3
ax3=fig.add_subplot(gs[0,1],facecolor=(0.9,0.9,0.9))
veloc,=ax3.plot([],[],'b',lw=3)
plt.xlabel('tempo',fontsize=15)
plt.ylabel('velocidade pistão',fontsize=15)
#plt.title('Velocidade em relação ao ângulo da manivela',fontsize=15)
plt.xlim(0,0.3)
plt.ylim(-1.1,1.1)
plt.grid(True)

# subplot 4
ax4=fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
acel,=ax4.plot([],[],'b',lw=3)
plt.xlabel('tempo',fontsize=15)
plt.ylabel('aceleração do pistão',fontsize=15)
#plt.title('Aceleração em relação ao ângulo da manivela',fontsize=15)
plt.xlim(0,0.3)
plt.ylim(-1.4,.8)
plt.grid(True)

ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,
                           interval=50,repeat=True,blit=True)

plt.show()
