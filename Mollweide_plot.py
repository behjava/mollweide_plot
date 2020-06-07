import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

########## inputs #############
print('')
inputfile=raw_input("Name of the input data file (must be tab-separated) = ")
print('')
output_image_name=raw_input("Name of the output image file with extension (default: out_image.jpg) = ")
if output_image_name=='':
    output_image_name='out_image.jpg'
print('')
color_label=raw_input("Label of the third column for the colorbar (default: color_label) = ")
if color_label=='':
    color_label='color_label'
print('')
color_map=raw_input("A valid matplotlib cmap (default: jet) = ")
if color_map=='':
    color_map='jet'
print('')

######### data file ############
data=pd.read_csv(inputfile, sep='\s+', header=0)
longt=data[data.columns[0]]
lat=data[data.columns[1]]
color=data[data.columns[2]]

############# converting degrees to radians between -pi and pi, and -pi/2 to pi/2 ###########
l=np.zeros(len(longt))
b=np.zeros(len(longt))
for i in range(len(longt)):
    b[i]=lat[i]*math.pi/180.0
    if longt[i]<180:
        l[i]=-(longt[i]*math.pi/180.0)
    else:
        l[i]=2*math.pi-(longt[i]*math.pi/180.0)


######## plotting the figure ##########
fig = plt.figure(figsize=(16,10))
ax = fig.add_subplot(111, projection="mollweide")
plt.setp(ax.get_yticklabels(), visible=False)
plt.setp(ax.get_xticklabels(), visible=False)
plt.grid(True)
ax.grid(color='black', linestyle='-', linewidth=1)
im=ax.scatter(l,b,c=color,s=10,edgecolors='none',cmap=color_map)
cbar=fig.colorbar(im,cax=None,shrink=0.7,orientation="horizontal",pad=0.02)
cbar.set_label(color_label, size=25)
cbar.ax.tick_params(labelsize=25)
ax.text(0,-1.5,"(0,-90)",fontsize=25)
ax.text(0,1.4,"(0,90)",fontsize=25)
ax.text(-math.pi/2.0,0,"(90,0)",fontsize=25)
ax.text(math.pi/2.0,0,"(270,0)",fontsize=25)
ax.text(0,0,"(0,0)",fontsize=25)
plt.tight_layout(pad=0.9)
plt.savefig(output_image_name)
plt.close()
