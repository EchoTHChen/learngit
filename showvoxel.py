from mpl_toolkits.mplot3d import Axes3D#这一句虽然显示灰色，但是去掉会报错。
import numpy as np
import matplotlib.pyplot as plt
import binvox_rw
def showVoxel(voxel):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
 
    ax.voxels(voxel, edgecolor="k")
    plt.show()
 
 
# ma = np.random.choice([0,1], size=(10,10,10), p=[0.95, 0.05])#意思是在10*10*10的空间中以一定的概率选择一部分点为1
f=open("scene0001_00_scanned.binvox", "rb")
ma = binvox_rw.read_as_3d_array(f)
showVoxel(ma.data)

# from mpl_toolkits.mplot3d import Axes3D#这一句虽然显示灰色，但是去掉会报错。
# import numpy as np
# import matplotlib.pyplot as plt
 
# def showVoxel(voxel):
#     fig = plt.figure()
#     ax = fig.gca(projection='3d')
 
#     ax.voxels(voxel, edgecolor="k")
#     plt.show()
 
 
# ma = np.random.choice([0,1], size=(10,10,10), p=[0.95, 0.05])#意思是在10*10*10的空间中以一定的概率选择一部分点为1
# showVoxel(ma)