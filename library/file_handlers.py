# import os
# import shutil


# os.walk(path)  # (root, [*dirs], [*files]) 튜플을 iter 하는 제너레이터를 반환하는 함수
# os.listdir(path)  # 파일목록전달
# os.chdir(path)  # 작업하고 있는 디렉토리 변경
# os.getcwd()  # 현재 프로세스의 작업 디렉토리 얻기
# os.path.abspath(filename)  # 파일의 상대 경로를 절대 경로로 바꾸는 함수
# os.path.exists(filename)  # 주어진 경로의 파일이 있는지 확인하는 함수
# os.curdir()  # 현재 디렉토리 얻기
# os.pardir() # 부모 디렉토리 얻기
# os.sep() # 디렉토리 분리 문자 얻기
# os.path.basename(filename)  # 파일명만 추출
# os.path.dirname(filename)  # 디렉토리 경로 추출
# os.path.split(filename)  # 경로와 파일명을 분리
# os.path.join(path, path) # \\패턴으로 경로를 만들어줌
# os.path.splitdrive(filename)  # 드라이브명과 나머지 분리 (MS Windows의 경우)
# os.path.splitext(filename)  # 확장자와 나머지 분리
# os.path.exists(path)
# os.path.isdir(path)
# os.path.isfile(path)
# os.path.getsize(filename)
# os.remove
# shutil.copy(path, newPath)  # 파일 복사
# shutil.copy2(path, newPath)  # 파일 복사 (설정값도 함께 복사)
# shutil.move(path, newPath)  # 파일 이동
# shutil.copytree(path, newPath)
# shutil.remove(path)
# shutil.rmtree(path)


# Code Example
def sample():
    import os
    import shutil

    count = 0
    pivot = 22
    label_num = 14
    os.chdir('/home/nr-lab/Downloads/labeled_images/Label_' + str(label_num) + '/')
    files = os.listdir('')
    files.sort()
    file_num = []
    for file in files:
        file = file[len('L' + str(label_num) + '_'):]
        file = file.rstrip('.jpg')
        file_num.append(int(file))

    file_num.sort()
    sorted_file = []
    for fn in file_num:
        sorted_file.append('L' + str(label_num) + '_' + str(fn) + '.jpg')

    for name in sorted_file:
        if name.startswith('L' + str(label_num) + '_' + str(pivot) + '.jpg'):
            new_name = 'L' + str(label_num - 4) + '_' + str(count) + '_test.jpg'
            os.rename(name, new_name)
            shutil.move('./' + new_name, '../test/' + new_name)
            count += 1
            pivot += 1


import pickle
with open('temp.txt', 'wb') as f:
    pickle.dump({'name': 'data', 'value': 0xffffffff}, f)
    pickle.dump([1, 2, 3], f)
with open('temp.txt', 'rb') as f:
    print(pickle.load(f), pickle.load(f))


import shelve
data1 = ["elsar", 24, 171]
data2 = ["peter", 31, 175]
with shelve.open('test.db') as f:
    f['obv1'] = data1
    f['obv2'] = data2
with shelve.open('test.db') as f:
    print(f['obv1'])
    print(f['obv2'])


import tempfile
print(tempfile.mktemp())
with tempfile.TemporaryFile() as f:
    pass


import sys, os, glob

# 특별 변수
print(sys.argv)
print(sys.path)
print(os.environ)

# print(glob.glob('*.exe'))
# print(glob.glob('*.txt'))
# print(glob.glob(r'C:\U*'))

if os.name == 'nt':
    os.chdir("c:\\Windows")

    with os.popen('dir') as f:
        print(f.read())
