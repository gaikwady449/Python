import psutil
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name=folder + "_" +timestamp +".zip"
    zobj=zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative= os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()

    return zip_name



def calculate_hash(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data= fobj.read(1024) 
        if not data:

            break
        else:
            hobj.update(data)

    fobj.close()


def BackupFiles(Source,Destination):
    copied_files=[]
    print("creating the backup folder for backup process")

    os.makedirs(Destination,exist_ok=True)

    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

        # copy the file if its new , updated
            if(not os.path.exists(dest_path)) or (calculate_hash(src_path) !=calculate_hash(dest_path)):
            
             #print(calculate_hash(src_path))

                shutil.copy2(src_path,dest_path)

                copied_files.append(relative)
    return copied_files

def marvellousDataSheildstart(Source="Data"):
    Backupname="MarvellousBackup"
    print("Backup process started successfull:",time.ctime())

    files= BackupFiles(Source,Backupname)

    zip_files=make_zip(Backupname)

    print("Backup completed successfully")
    print("files copied:",len(files))
    print("files gets created:",zip_files)

    BackupFiles(Source,Backupname)

def main():
    Border="-"*50
    print(Border)
    print("-----Marvellous Data sheild System-----")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to")
            print("1:takes auto backup at given time")
            print("2:backup only new and updated files")
            print("3:create and aechive a backup periodically")

        elif(sys.argv[1]=="--u"or sys.argv[1]=="--U"):
            print("use thr automation scrit as")
            print("ScriptName.py timeInterval SourceDirectory ")
            print("Timeinterval: the time in minute for perodic scheduling")
            print("Source:Name of Directory to backup")
            
  
        else:
            print("invalid number of command line argument")
            print("unable to proceed as there is no such opetion")
    # python Demo.py 5 data
    elif(len(sys.argv)==3):
        print("inside project logic") 
        print("Time interval:",sys.argv[1])
        print("Directory name:",sys.argv[2])
        
        # Apply the Schedular
        schedule.every(int(sys.argv[1])).minutes.do(marvellousDataSheildstart,sys.argv[2])
         
        print(Border)
        print("Data Sheild System started succesfully")
        print("Directory created with name:",sys.argv[2])
        print("Time interval in miniute:",sys.argv[1])
        print("press Clrl + to stop the execution ")
        print()
        # Wait till abort

        while True:
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("unable to proceed as thre is no such opetion")

    print(Border)
    print("------thank you for using script-------")

if __name__ == "__main__":
    main()