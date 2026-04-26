from ultralytics import YOLO
import cv2

model = YOLO('my_model/train/weights/best.pt')
results = model.predict('test_tree.jpg', save=True, show=True, save_txt=True, conf=0.5, save_conf=True)

res_plotted = results[0].plot()

cv2.imshow("Results", res_plotted)
cv2.waitKey(0)
cv2.destroyAllWindows()