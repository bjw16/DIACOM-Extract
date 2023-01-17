import os
import pydicom
import shutil
from nullsafe import undefined, _

#List Patient IDs (Folder Names)
imaging_list = os.listdir()
for a in imaging_list:
	#Change directory to patient
	print(os.listdir("."))
	if os.path.isdir(a) == 0:
		continue
	os.chdir(a)

	#List Studies
	dir_list = os.listdir(".")
	for x in dir_list:
		if os.path.isdir(x) == 0:
			continue
		#Change Directory to Studies
		os.chdir(x)
		#List Series
		series_list = os.listdir(".")
		for y in series_list:
			if os.path.isdir(y) == 0:
				continue
			os.chdir(y)
			filename = os.listdir(".")
			#(0008, 1030) Study Description                   LO: 'Preop X-ray'
			#(0008, 103e) Series Description                  LO: 'SHOULDER Y-VIEW'
			if filename == []:
				os.chdir("..")
				continue
			else:
				for n in filename:
					ds = pydicom.dcmread(n)
					try:
						ds.StudyDescription
						for z in range(0,10000):
							filename2 = a+" "+ds.StudyDescription +"img"+str(z)+".dcm"
							if os.path.isfile("../../" + filename2):
								continue
							else:
								print(x + y)
								os.rename(n,filename2)
								shutil.move(filename2, "../../")
								break

					except AttributeError:
						for z in range(0,10000):
							if z == 0:
								filename2 = a+" "+"image" + ".dcm"
							else:
								filename2 = a+" "+"img"+str(z)+".dcm"
							if os.path.isfile("../../" + filename2):
								continue
							else:
								os.rename(n,filename2)
								shutil.move(filename2, "../../")
								break
				#Goes back to series
				os.chdir("..")
		#Take us back to study
		os.chdir("..")
	#Take us back to studies
	os.chdir("..")
