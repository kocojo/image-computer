import tensorflow as tf
import cv2
import os
import numpy as np
cnn = tf.keras.models.load_model('mnist_cnn_model.keras')
cla = np.sort(os.listdir('data/extracted_images'))
img = cv2.imread('data/Untitled.jpg')
formula = {}
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Applying 7x7 Gaussian Blur
blurred = cv2.GaussianBlur(gray_img, (7, 7), 0)
# Applying threshold
threshold = cv2.threshold(blurred, 0, 255,
                          cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# Apply the Component analysis function
analysis = cv2.connectedComponentsWithStats(threshold,
                                            4,
                                            cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = analysis
# Initialize a new image to
# store all the output components
output = np.zeros(gray_img.shape, dtype="uint8")
# Loop through each component

for i in range(1, totalLabels):
    # Area of the component
    area = values[i, cv2.CC_STAT_AREA]
    if True:
        # Create a new image for bounding boxes
        new_img = img.copy()
        # Now extract the coordinate points
        x1 = values[i, cv2.CC_STAT_LEFT]
        y1 = values[i, cv2.CC_STAT_TOP]
        w = values[i, cv2.CC_STAT_WIDTH]
        h = values[i, cv2.CC_STAT_HEIGHT]
        # Coordinate of the bounding box
        pt1 = (x1, y1)
        pt2 = (x1 + w, y1 + h)
        (X, Y) = centroid[i]
        # Bounding boxes for each component
        # Create a new array to show individual component
        # Show the final images
        component = np.zeros(gray_img.shape, dtype="uint8")
        componentMask = (label_ids == i).astype("uint8") * 255
        # Apply the mask using the bitwise operator
        component = cv2.bitwise_or(component, componentMask)
        component = component[int(y1):int(y1 + h), int(x1):int(x1 + w)]
        cv2.rectangle(new_img, pt1, pt2, (0, 255, 0), 3)
        cv2.circle(new_img, (int(X),int(Y)),4, (0, 0, 255), -1)
        cv2.imshow("Image", new_img)
        cv2.waitKey(0)
    if h < w/5:
        top = abs(h-w) // 2
        bottom = top
        left = 0
        right = 0
        # Thêm viền màu trắng xung quanh
        white = [0, 0, 0]  # Màu trắng
        component = cv2.copyMakeBorder(component, top, bottom, left, right, cv2.BORDER_CONSTANT, value=white)
    if w < h/5:
        left = abs(h-w) // 2
        right = left
        bottom = 0
        top = 0
        white = [0, 0, 0]
        component = cv2.copyMakeBorder(component, top, bottom, left, right, cv2.BORDER_CONSTANT, value=white)
    blank = cv2.resize(component, (45, 45))
    imgage = 1 - blank / 255.0
    imgage = np.expand_dims(imgage, axis=0)
    imgage = np.expand_dims(imgage, axis=3)
    result = cnn.predict(imgage)
    formula[(X,Y,w,h,pt1)] = cla[result.argmax()]
    print(cla[result.argmax()])
pos = list(formula.keys())
pos.sort(key=lambda x: x[4][0])
result = []
for i in pos:
    result.append(formula[i])
is_power = False
for i in range(1,len(pos)):
    if pos[i][1] < pos[i-1][4][1]:
        result[i-1] = result[i-1]+'^{'
        is_power = True
    if pos[i][1] > pos[i-1][4][1]+pos[i-1][3] and is_power:
        result[i-1] = result[i-1]+'}'
        is_power = False
if is_power:
    result[-1] = result[-1]+'}'
for i in range(len(result)):
    if 'sqrt' in result[i]:
        result[i] = result[i].replace('sqrt','\\sqrt{')
        is_root = True
        for j in range(i+1,len(result)):
            if pos[j][0] > pos[i][4][0]+pos[i][2]:
                result[j] = result[j]+'}'
                is_root = False
                break
        if is_root:
            result[-1] = result[-1]+'}'
        print(pos[i])
print(''.join(result))


