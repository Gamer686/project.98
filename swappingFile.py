def swapFileData():

    file1 = input("entre the orginal file : ")
    file2 = input("entre the file to be swappped : ")

    with open(file1,'r') as Angel :
        data_Angel = Angel.read()
    with open(file2,'r') as jia :
        data_jia = jia.read()

    with open(file1,'w+') as Angel :
        Angel.write(data_jia) 
    with open(file2,'w+') as jia :
        Angel.write(data_Angel) 

swapFileData()


