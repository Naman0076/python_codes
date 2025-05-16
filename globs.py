import glob
import os

files = glob.glob(r"C:\Users\Naman\OneDrive - ImpactQA\Desktop\python_codes\s*.py")
filenames = [os.path.basename(file) for file in files]
print(filenames)

#use PWD command in shell (Path to get current working directory)