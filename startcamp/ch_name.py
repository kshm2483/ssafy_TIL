import os

os.chdir(r'C:\Users\student\TIL\dummy')
for filename in os.listdir('.'):
    os.rename(filename, filename.replace('SAMSUNG', 'SSAFY'))