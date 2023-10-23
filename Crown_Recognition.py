import numpy as np
import cv2 as cv

def CrownDetection(img,template):

    temp_w = template.shape[1]
    temp_h = template.shape[0]
    result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

    # matchTemplate gives an array with the confidence value for each pixel, how close they are to match the template.
    # The threshold makes sure we only look at the best matching locations.
    threshold = 0.5

    location = np.where(result >= threshold)  # Finds the location of the pixels that is over the threshold
    locations = list(zip(*location[::-1]))  # Puts coordinates into lists to make it easier to read

    rectangles = []

    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), temp_w, temp_h]
        rectangles.append(rect)
        rectangles.append(rect)  # Twice because groupRectangles only looks at grouped rectangles

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    if len(rectangles):
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)

            cv.rectangle(img, top_left, bottom_right, line_color, line_type)

        return (len(rectangles))

    else:
        return 0


def CrownDetectionRotation(img):

    template = cv.imread('Template//TemplateUp.png', cv.IMREAD_UNCHANGED)
    rotation = CrownDetection(img, template)

    if rotation == 0:
        template = cv.imread('Template//TemplateRight.png', cv.IMREAD_UNCHANGED)
        rotation = CrownDetection(img, template)

        if rotation == 0:
            template = cv.imread('Template//TemplateDown.png', cv.IMREAD_UNCHANGED)
            rotation = CrownDetection(img, template)

            if rotation == 0:
                template = cv.imread('Template//TemplateLeft.png', cv.IMREAD_UNCHANGED)
                rotation = CrownDetection(img, template)
                return rotation
            return rotation
        return rotation
    return rotation


img = cv.imread("Rotated//FieldDown.png", cv.IMREAD_UNCHANGED)
NumbCrowns = CrownDetectionRotation(img)

print(NumbCrowns)

