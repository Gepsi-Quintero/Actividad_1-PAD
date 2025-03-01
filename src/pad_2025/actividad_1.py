import json
import requests


class actividad_1():
    def __init__(self):
        self.ruta_static="src/pad_2025/static/"
        
    def leer_json(self):
        # r read w write

        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos    
    
    def leer_txt(self):
        # r read w write

        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos 

    def leer_varios_txt(self,nombre=""):
        # r read w write

        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"r",encoding="utf-8") as f:
            datos = f.read()
        return datos   
    
    def  leer_cualquier_excel(self,nombre=""):
        pass
    
    def  leer_cualquier_csv(self,nombre=""):
        pass
    
    def  leer_html(self,url=""):
        pass
    
    def  leer_bd(self,nombre_bd="",servidor="",puerto=0000):
        pass
    
    def  leer_api(self,url=""):
     # El metodo get() de la libreria requests, permite hacer una peticion a una API
     response = requests. get("https://api.jikan.moe/v4/anime/989")
     return response.json()
        
    def  escribir_json(self, nombre, datos):
        ruta_json = "{}json/{}.json".format(self.ruta_static, nombre)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    
    def escribir_txt(self,nombre,datos):
        # r read w write
        ruta_txt = "{}.txt".format(nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f:
            #f.write(datos)
            f.writelines(datos)





inges = actividad_1() 
# datos_json = actividad_1.leer_api("https://api.jikan.moe/v4/anime/989")
#"https://api.jikan.moe/v4/anime/989"
datos_json = inges.leer_api("https://api.jikan.moe/v4/anime/989")
print("datos_json",datos_json)
#if inges.write_json (nombre_archivo="entrega_actividad_1.json" ,datos=datos_json) 
 # print("se ha cesrito el archivo json")
inges.write_txt("actividad_1.txt",datos_json)
inges.write_json("actividad_1.txt",datos_json)
print("se ha escrito el archivo txt")


#inges.escribir_txt(nombre="archivo_json",datos=datos_json)
#inges.escribir_txt(nombre="archivo_txt",datos=datos_txt)
#inges.escribir_txt(nombre="archivo_txt_copy",datos=datos_txt_dos)
    
    
    
    
