from os import scandir, getcwd
from os.path import abspath

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
print(ls("C:\PFM\SracpCalpe"))