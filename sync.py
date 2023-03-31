import os
os.chdir("output")
path= os.getcwd()
for  i in range(5):
    os.mkdir("folder"+str(i))
    os.chdir("folder"+str(i))
    os.system('fallocate -l 0.1k '+"file"+str(i))
    os.chdir(path)
for  i in range(5):
    os.system('fallocate -l 0.1k '+"file"+str(i))
os.chdir("/cnvrg")
