import shutil
src_file_obj=open("PanTadeusz.txt", "rb")
targ_file_obj=open("testkopia.txt", 'wb')
shutil.copyfileobj(src_file_obj, targ_file_obj)

#działa