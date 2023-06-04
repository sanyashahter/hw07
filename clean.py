import sys
from pathlib import Path
from os import *
import re
import shutil
import os

def run():
    def main():
        a = sys.argv[1]
        
        return a
    num = main()

    try:
        path_video = os.path.join(num, 'video')
        os.mkdir(os.path.join(num, 'video'))
        path_audio = os.path.join(num, 'audio')
        os.mkdir(os.path.join(num, 'audio'))
        path_archives = os.path.join(num, 'archives')
        os.mkdir(os.path.join(num, 'archives'))
        path_images = os.path.join(num, 'images')
        os.mkdir(os.path.join(num, 'images'))
        path_documents = os.path.join(num, 'documents')
        os.mkdir(os.path.join(num, 'documents'))
    except: FileExistsError

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for i, j in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(i)] = j
        TRANS[ord(i.upper())] = j.upper() 

    def translate(name):
        translated_name = ''
        
        for k in name:
            perevod = str.translate(k, TRANS)
            translated_name = translated_name + str(perevod)
            
        return translated_name

    spisok_rashirenii = set()

    def normalize(string):
        rez = translate(string)
    
        pattern_zamena = re.sub("[^A-Za-z0-9]", "_", rez)
    
        return pattern_zamena
        
    extensions = {
                    "JPEG": "images",
                    "PNG": "images",
                    "JPG": "images",
                    "SVG": "images",
                    "DOC": "documents",
                    "DOCX": "documents",
                    "TXT": "documents",
                    "PDF": "documents",
                    "XLSX": "documents",
                    "PPTX": "documents",
                    "MP3":"audio",
                    "OGG":"audio",
                    "WAV":"audio",
                    "AMR":"audio",
                    "AVI":"video",
                    "MP4":"video",
                    "MOV":"video",
                    "MKV":"video",
                    "ZIP":"",
                    "GZ":"",
                    "TAR":""
                    }
    spisok_rashir = set()

    path = Path(main())


    if path.exists():

        if path.is_dir(): 
                
            items = path.glob('**/*')
            for item in items:

                if item.is_file():
                    
                    item_file = item.name.split('.')
                    razshir_faila = item_file[1].upper()
                    nazva_faila = item_file[0]
                    nazva_faila = normalize(nazva_faila)
                
                    if razshir_faila in extensions.keys():
                        spisok_rashirenii.add(razshir_faila)
    
                    else:
                        spisok_rashir.add(razshir_faila)

                    for i in extensions.keys():
                    
                        i = i.upper()                                     
                        if i == razshir_faila:

                            if razshir_faila == 'ZIP':
                                
                                way = os.path.join(path, 'archives')
                                
                                way = os.path.join(way, nazva_faila)
                                ar_path = os.path.join(path, way)   
                                                        
                                                    
                                shutil.unpack_archive(item, ar_path)
                            elif razshir_faila == "TAR":  
                                
                                way = os.path.join(path, 'archives')
                                way = os.path.join(way, nazva_faila)
                                ar_path = os.path.join(path, way)   
                                
                            elif razshir_faila == "GZ":  
                                
                                way = os.path.join(path, 'archives')                          
                                way = os.path.join(way, nazva_faila)
                                ar_path = os.path.join(path, way)   
                            
                            else:
                                ext_v = extensions.get(i)
                                old_way = os.path.abspath(item)                             
                                new_pat = os.path.join(path, ext_v)                       
                                new_path = os.path.join(new_pat, (nazva_faila + '.' + razshir_faila))                     
                                os.replace(old_way, new_path)                   
                    
                        else:
                            pass
                                    
                else:
                    if item.name in extensions.values():
                        pass

    spisok_papok_iskluchenii = ['video', 'audio', 'documents','images', 'archives']
    pattern_parsinga = path.iterdir()
    for i in pattern_parsinga:

        if  i.is_dir():
            
            if i.name in spisok_papok_iskluchenii:
                print(f'ПАПКУ {i.name} НЕ УДАЛЯТЬ')

            else:
                print(f'ПАПКУ >>>>{i.name}<<<< УДАЛИТЬ')
                
                try:
                    os.rmdir(i)
                except: OSError
                else:
                    print(f' ПАПКА {i} УДАЛЕНА')
                finally:
                    print('DONE ------------------------------------------------')

    print(f'Не известные расширения файлов >>>>{spisok_rashir}')
    print(f'Расширения которые  известны {spisok_rashirenii}')

if __name__ == "__main__":
    run()