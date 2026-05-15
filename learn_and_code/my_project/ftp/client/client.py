import ftplib

# FTP server credentials
user = 'user'
password = 'password'

# connect to the FTP server
ftp = ftplib.FTP('localhost', user)
# force UTF-8 encoding
ftp.encoding = "utf-8"
# local file name you want to upload
filename = "some_file.txt"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR {filename}", file)
# list current files & directories
ftp.dir()
# quit and close the connection
ftp.quit()