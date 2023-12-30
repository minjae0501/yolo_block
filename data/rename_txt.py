import os
import shutil

def rename_files(source_directory):
    # 새파일 디렉토리
    target_directory = os.path.join(source_directory, 'renamed_txt')
    os.makedirs(target_directory, exist_ok=True)

    # .txt 불러오기
    file_paths = [f for f in os.listdir(source_directory) if f.endswith('.txt')]

    # 이름 변경 후 이동
    i = 200
    for file_name in file_paths:
        # 새이름
        file_name_split_01 = file_name.split('_jpg')[0]
        file_no = int(file_name_split_01.split('_')[1]) + i
        new_file_name = 'image_'+ str(file_no) +'.txt'
        new_file_path = os.path.join(target_directory, new_file_name)

        # 파일 복사
        shutil.copy(os.path.join(source_directory, file_name), new_file_path)
        print(f"Renamed and moved '{file_name}' to '{new_file_path}'")

# Example Usage
source_directory = 'C:\\Users\\qnwje\\OneDrive\\바탕 화면\\zerobase\\딥러닝 팀플\\yolo_block\\data\\truck_data\\train\\labels'  # 라벨 디렉토리
rename_files(source_directory)
