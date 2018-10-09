# 显示图片
# 1.导入库
# import cv2
# # 2.加载图片
# img = cv2.imread("./face2.jpg")
# # 3.创建窗口
# cv2.namedWindow('James 窗口')
# # 4.显示图片
# cv2.imshow("jamas",img)
# # 5.暂停窗口
# cv2.waitKey(0)
# # 6.关闭窗口
# cv2.destroyAllWindows()

# 人脸识别
# 1.导入库
import cv2
# 2.加载图片
img = cv2.imread("./face2.jpg")
# 3.加载人脸模型
face1 = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
# 4.调整图片灰度
# 提升性能（没必要识别颜色，提高灰度）
gray = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

# 5.检查人脸
faces = face1.detectMultiScale(gray)
# 6.标记人脸
for (x,y,w,h) in faces:
    # 四个参数 1.图片 2.坐标原点 3.识别大小 4.颜色 5.线宽
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)

# 7.创建窗口
cv2.namedWindow('james')

# 8.显示图片
cv2.imshow('jkl',img)
# 9.暂停
cv2.waitKey(0)
# 10.关闭窗口
cv2.destroyWindow()

