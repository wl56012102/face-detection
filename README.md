# face-detection

### **使用环境**

- Python 3.5
- OpenCV 3
- imutils
- PIL
- flask



### **代码结构**

```
face-detection/
├── data/
├── test-dir/
├── web/
│   └── web-steam.py
├── get_face.py/	
├── train-face-model.py
└── face_detect.py
```



### **代码使用**

1. `python get_face.py` 

    输入人物id，名字，获取人脸图像并保存在data/face-data目录下

2. `python train-face-model.py`

   使用face-data目录下的人脸数据训练模型保存为model.yaml

3. `python face_detect.py`

   使用model.yaml识别人脸，显示可信度和ID

   ​

### **联系方式**

QQ:735382689

微信：wl735382689