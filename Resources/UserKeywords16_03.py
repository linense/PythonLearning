import os

def create_folder(foldername):
    os.mkdir("C:\\Users\\a315707\\OneDrive - Deutsche Telekom AG\\Schulungen\\Programmierung\\Python\PythonLearning\\"+foldername)

def create_sub_folder(subfoldername):
    os.mkdir("C:\\Users\\a315707\\OneDrive - Deutsche Telekom AG\\Schulungen\\Programmierung\\Python\PythonLearning\\"+subfoldername)

def concatenate_two_values(val1, val2):
    val3=val1+" "+val2
    return val3
