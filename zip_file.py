from zipfile import ZipFile


file_name = "C:/Python/Journal_back/JOURNAL.zip";
with ZipFile(file_name, 'r') as zip:
	zip.printdir()
	print('Extracting files now...')
	zip.extractall();
	print('Done Extracting!!')