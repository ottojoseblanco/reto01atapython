from pathlib import Path
import os
import platform


def mostrardirectorio(rutaabuscar):
	print("Directorio: "+rutaabuscar)

	print(" ")

	listadirectorio=(os.listdir(rutaabuscar))

	for i in listadirectorio:

		if os.path.isdir("listadirectorio[]")==False:

			#***********************************************************
			#	La siguiente condicion permite filtrar por extensiones 	
			#
			#   if i[-3:]=="jpg":
			#***********************************************************
	
		   	print(i)


if __name__ == "__main__":
	mi_os=str(platform.system())
	print("Tu sistema operativo es :",mi_os)

	if mi_os=="Windows":
		print(Path.home())

		mostrar=0
		rutausuario=str(Path.home())
		rutadescargas=rutausuario+"\\"+"Downloads"
		print(rutadescargas)
		if mostrar==0:
			mostrardirectorio(rutadescargas)
	elif mi_os=="Linux":
		print(Path.home())
		rutausuario=str(Path.home())

		mostrar=0

		if os.path.isdir(rutausuario+"/Descargas"):
			rutacompleta=rutausuario+"/Descargas"
		elif os.path.isdir(rutausuario+"/Downloads"):
			rutacompleta=rutausuario+"/Downloads"
		else:
			rutacompleta=rutausuario+"/Downloads"
			print(rutacompleta)
			print(os.path.isdir(rutacompleta))
			print("No existe Directorio de Descargas ni Downloads")
			mostrar=1
		if mostrar==0:
			mostrardirectorio(rutacompleta)
	else:
		print("No puedo reconocer tu sistema Operativo")








