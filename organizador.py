from pathlib import Path
import shutil
from datetime import datetime

CATEGORIAS = {"Imagenes": [".jpg",".jpeg",".png",".gif",".bmp",".svg",".webp",".ico",".tiff"],
                "Videos": [".mp4",".avi",".mov",".mkv",".wmv",".flv",".webm"],
                "Documentos":[".pdf",".docx",".doc",".txt",".xlsx",".xls",".pptx",".ppt",".csv"],
                "Comprimidos": [".zip",".rar",".7z",".tar",".gz",".iso"]}


log_path = Path(__file__).parent / "logs" / "registro.txt"


class OrganizadorArchivos:
    def __init__(self, ruta):
        self.ruta = Path(ruta)
        self.contador = 0
        
        
    def obtener_categoria(self, extension):
        for categoria in CATEGORIAS:
            if extension in CATEGORIAS[categoria]:
                return categoria
        return "Otros"
    
    def organizar(self):
        if not self.ruta.exists():
            print("La Ruta Proporcionada No Existe.")
            return
        
        log_path.parent.mkdir(exist_ok=True)
        
        vf2 = input("¿Estás seguro? (s/n): ")
        if vf2 != "s":
            print("Saliendo del Programa...") 
            return   
                
        for archivo in self.ruta.iterdir():
            if archivo.is_file():
                carpeta = self.obtener_categoria(archivo.suffix)
                destino = self.ruta / carpeta
                
                destino.mkdir(exist_ok=True)
                shutil.move(archivo, destino)
                self.contador += 1
                
                with open(log_path, "a") as log:  
                    log.write(f"{datetime.now()}:  Archivo '{archivo.name}' movido a '{destino.name}'\n")
                
        print(f"Se Organizaron un Total de {self.contador} Archivos Exitosamente, Para Mayor Detalle Revisar el Log.")

if __name__ == "__main__":
    ruta = input("Ingrese la Ruta del Directorio a Organizar: ")
    OrganizadorArchivos(ruta).organizar()