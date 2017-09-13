contours, hierarchy = cv2.findContours(img_dilate.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

points=[]
i=0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 10 and area < 800:
        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(img_dilate,(x,y),(x+w,y+h),(0,255,0),2)
        center = (int(x),int(y))
        position = (center[0], center[1])
        points.append(position)
        print position,i
        text_color = (255,0,255)
        cv2.putText(resized,str(i+1), position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 2)
        i=i+1
pnts = np.array(points)
rect = cv2.minAreaRect(pnts)
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
cv2.drawContours(resized,[box],0,(0,255,0),2)

root_mat = cv2.getRotationMatrix2D(rect[0], angle , 1)
rotated = cv2.warpAffine(resized, root_mat, dim, flags=cv2.INTER_CUBIC)
cv2.getRectSubPix(rotated, dim, center) 