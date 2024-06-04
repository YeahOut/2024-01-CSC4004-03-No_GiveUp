#aws에 파일 업로드하기
import os
import boto3
from django.conf import settings
from .models import UserMaxMinFile

def upload_to_s3(min_file, max_file,user):
    ##파일 이름 변경##
    # 파일 이름에서 확장자 분리하기
    mySound_name, mySound_ext = os.path.splitext(min_file.name)
    compareSound_name, compareSound_ext = os.path.splitext(max_file.name)    
    
    # 새 파일 이름 설정
    new_minSound_name = f'{user}'+'_min' + mySound_ext 
    new_maxSound_name = f'{user}'+ '_max' + compareSound_ext ##org.mp4 이런식으로 변경 
        
    min_file.name = new_minSound_name
    max_file.name = new_maxSound_name
    #인스턴스 중복되는거 방지하기
    upload = UserMaxMinFile(min_file=min_file,
                            max_file=max_file,
                            user=user,
                            min_file_name=min_file.name,
                            max_file_name=max_file.name)
    upload.save()

#aws에서 파일 다운로드하기
def downloadFile(min_file_name,max_file_name) :
    s3 = boto3.resource('s3')
    
    #s3 버킷 정보 가져오기
    bucket_name = 'myv-aws-bucket'
    bucket = s3.Bucket(bucket_name)
    print("###test###")
    print(bucket)

    #파일 다운로드 진행하기
    min_obj_file= 'userVoice/' + min_file_name #디렉토리 버킷 접근하기
    max_obj_file='userVoice/' + max_file_name
    print("###버킷 접근 성공###")
    print('##min file name:',min_obj_file)
    save_file = os.path.join(os.getcwd(), 'media', 'maxminSrc', min_file_name) #저장위치 및 파일 다른 이름으로 저장하기 but 이름변경 안할거임
    bucket.download_file(min_obj_file,save_file)

    save_file = os.path.join(os.getcwd(), 'media', 'maxminSrc',max_file_name) #저장위치 및 파일 다른 이름으로 저장하기 but 이름변경 안할거임
    bucket.download_file(max_obj_file,save_file)
    return 1;

#사용자마다 S3 디렉토리 버킷 생성하는 함수 (올리고, 다운받는 용도로 만든 후 음역대 저장하면 삭제할 함수)
def makingBucket():
    s3 = boto3.client('s3',
                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    # 디렉토리 버킷 생성
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    userId='userid' #db 연결후 사용자 아이디로 디렉토리 버킷 만들 예정!
    directory_path = f'{userId}/'

    s3.put_object(Bucket=bucket_name, Key=(directory_path))
    return directory_path

#버킷 삭제
def deleteBucket(): #매개변수로 userId 받을 예정
    s3 = boto3.client('s3',
                      aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    userId = 'userid'  # 매개변수로 받을 버킷 이름을 담을 예정
    directory_path = f'{userId}/'

    s3.delete_object(Bucket=bucket_name, Key=directory_path)