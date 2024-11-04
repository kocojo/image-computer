import tensorflow as tf
import cv2
import os
import numpy as np
def other(formula:dict,pos:list)->list:
    result = []
    pos.sort(key=lambda x: x[4][0])
    for i in pos:
        result.append(formula[i])
    is_power = False
    for i in range(1, len(pos)):
        if formula[pos[i]] == 'times':
            result[i] = '\\times'
        if pos[i][1] < pos[i - 1][4][1]:
            result[i - 1] = result[i - 1] + '^{'
            is_power = True
        if pos[i][1] > pos[i - 1][4][1] + pos[i - 1][3] and is_power:
            result[i - 1] = result[i - 1] + '}'
            is_power = False
    if is_power:
        result[-1] = result[-1] + '}'
    for i in range(len(result)):
        if 'sqrt' in result[i]:
            result[i] = result[i].replace('sqrt', '\\sqrt{')
            is_root = True
            for j in range(i + 1, len(result)):
                if pos[j][0] > pos[i][4][0] + pos[i][2]:
                    result[j] = result[j] + '}'
                    is_root = False
                    break
            if is_root:
                result[-1] = result[-1] + '}'
    return result
def div(formula: dict,pos:list)->list:
    pos1 =pos.copy()
    for i in pos:
        if formula[i] == '-':
            up = []
            down = []
            for j in pos1:
                if j[1] < i[1] and i[4][0]<j[0] and i[4][0]+i[2]>j[0]:
                    up.append(j)
                    pos1.remove(j)
                elif j[1] > i[1] and i[4][0]<j[0] and i[4][0]+i[2]>j[0]:
                    down.append(j)
                    pos1.remove(j)
            if len(up)==0 or len(down)==0:
                continue
            else:
                upper = other(formula,up)
                lower = other(formula,down)
            result = '\\frac{'+''.join(upper)+'}{'+''.join(lower)+'}'
            # X = (sum([f[0] for f in upper]) + sum([f[0] for f in lower])+i[0]) // (len(upper)+len(lower) + 1)
            # Y = (sum([f[1] for f in upper]) + sum([f[1] for f in lower])+i[1]) // (len(upper)+len(lower) + 1)
            # w = max(max([f[0] for f in upper]),max([f[0] for f in upper]),)
            # h =
            # pt1 =
            formula[i] = result
    result = other(formula,pos1)
    return result
def img_to_latex( img : np.ndarray)->str:
    cnn = tf.keras.models.load_model('mnist_cnn_model.keras')
    cla = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '[', ']', 'geq', 'gt',
           'leq', 'neq', 'pi', 'sqrt', 'sum', 'times', '{', '}']
    # print(cla)
    formula = {}
    # Applying 7x7 Gaussian Blur
    blurred = cv2.GaussianBlur(img, (7, 7), 0)
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
    output = np.zeros(img.shape, dtype="uint8")
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
            (X, Y) = (x1 + w // 2, y1 + h // 2)
            # Bounding boxes for each component
            # Create a new array to show individual component
            # Show the final images
            component = np.zeros(img.shape, dtype="uint8")
            componentMask = (label_ids == i).astype("uint8") * 255
            # Apply the mask using the bitwise operator
            component = cv2.bitwise_or(component, componentMask)
            component = component[int(y1):int(y1 + h), int(x1):int(x1 + w)]
        if h < w/2:
            top = abs(h-w) // 2
            bottom = top
            left = 0
            right = 0
            # Thêm viền màu trắng xung quanh
            white = [0, 0, 0]  # Màu trắng
            component = cv2.copyMakeBorder(component, top, bottom, left, right, cv2.BORDER_CONSTANT, value=white)
        if w < h/2:
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
    result = div(formula,pos)
    return ''.join(result)


