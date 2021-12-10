## Video to Image

실시간 촬영이나 rosbag 실행시 ROS topic 형태로 나오는 영상을 이미지화 해주는 프로그램  </br></br>

## 사용법
### 파라미터 설정
```yaml
sub_topic: subscribe 할 토픽 이름
save_path: 이미지 파일 저장경로
frame: 몇 프레임마다 저장할건지 #(ex. sub_topic이 30Hz일때 1로 설정하면 1초에 30장 저장됨. 2로설정하면 15장 저장됨)
```
### 명령어
conda 환경설치 방법은 상위 폴더를 참조
```
(base) $ conda activate watt

(3w) $ rosrun video2img_ros video2img.py save_img_path
```