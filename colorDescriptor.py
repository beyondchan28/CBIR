import cv2

class ColorDescriptor:
    def describe(image):
        (B, G, R) = cv2.split(image)
        features = []
        red = R.mean() 
        green = G.mean()
        blue = B.mean()
        
        features.append(red)
        features.append(green)
        features.append(blue)
        
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_blur = cv2.GaussianBlur(image_gray, (11,11), 0)
        image_edged = cv2.Canny(image_blur, 30,150)
        
        cnts = cv2.findContours(image_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) == 2:
            cnts = cnts[0]
            c= max(cnts, key=cv2.contourArea)
        elif len(cnts) == 3:
            cnts = cnts[1]
            c= max(cnts, key=cv2.contourArea)
        
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        extBot = tuple(c[c[:, :, 1].argmax()][0])
        
        vertical = max(extBot)-min(extTop)
        horizontal = max(extRight)-min(extLeft)
        if (vertical > horizontal) :
            diameter = vertical
            features.append(diameter)
        elif (horizontal > vertical) :
            diameter = horizontal
            features.append(diameter)
        
        return features