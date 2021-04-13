import numpy as np
import cv2 as cv

img_name = input("Please enter the image you want to do by average filter : ")
img_color = cv.imread(img_name)
cv.imwrite('ColoerImage_' + img_name + '.jpg', img_color)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imwrite('GrayImage_' + img_name + '.jpg', img_gray)

img_row_size, img_col_size = img_gray.shape
median_color = np.zeros((img_row_size, img_col_size, 3))
median_gray = np.zeros((img_row_size, img_col_size))
unsharp_color = np.zeros((img_row_size, img_col_size, 3))
unsharp_gray = np.zeros((img_row_size, img_col_size))

for i in range(1, img_row_size-1):
    for j in range(1, img_col_size-1):
        sort_pixel_gray = [img_gray[i-1][j-1], img_gray[i-1][j], img_gray[i-1][j+1], img_gray[i][j-1],
                           img_gray[i][j], img_gray[i][j+1], img_gray[i+1][j-1], img_gray[i+1][j], img_gray[i+1][j+1]]
        sort_pixel_gray = sorted(sort_pixel_gray)
        median_gray[i][j] = sort_pixel_gray[4]
        unsharp_gray[i][j] = img_gray[i][j] - median_gray[i][j]/255

        sort_pixel_r = [img_color[i-1][j-1][0], img_color[i-1][j][0], img_color[i-1][j+1][0], img_color[i][j-1][0],
                        img_color[i][j][0], img_color[i][j+1][0], img_color[i+1][j-1][0], img_color[i+1][j][0], img_color[i+1][j+1][0]]
        sort_pixel_g = [img_color[i-1][j-1][1], img_color[i-1][j][1], img_color[i-1][j+1][1], img_color[i][j-1][1],
                        img_color[i][j][1], img_color[i][j+1][1], img_color[i+1][j-1][1], img_color[i+1][j][1], img_color[i+1][j+1][1]]
        sort_pixel_b = [img_color[i-1][j-1][2], img_color[i-1][j][2], img_color[i-1][j+1][2], img_color[i][j-1][2],
                        img_color[i][j][2], img_color[i][j+1][2], img_color[i+1][j-1][2], img_color[i+1][j][2], img_color[i+1][j+1][2]]
        sort_pixel_r = sorted(sort_pixel_r)
        sort_pixel_g = sorted(sort_pixel_g)
        sort_pixel_b = sorted(sort_pixel_b)
        median_color[i][j][0] = sort_pixel_r[4]
        median_color[i][j][1] = sort_pixel_g[4]
        median_color[i][j][2] = sort_pixel_b[4]
        unsharp_color[i][j][0] = img_color[i][j][0] - median_color[i][j][0]/255
        unsharp_color[i][j][1] = img_color[i][j][1] - median_color[i][j][1]/255
        unsharp_color[i][j][2] = img_color[i][j][2] - median_color[i][j][2]/255


median_gray = median_gray.astype(np.uint8)
cv.imwrite('GrayImageMadeByMedianFilter_' + img_name + '.jpg', median_gray)
median_color = median_color.astype(np.uint8)
cv.imwrite('ColorImageMadeByMedianFilter_' + img_name + '.jpg', median_color)

unsharp_gray = unsharp_gray.astype(np.uint8)
cv.imwrite('GrayImageMadeByMedianFilterUnsharped_' +
           img_name + '.jpg', unsharp_gray)
unsharp_color = unsharp_color.astype(np.uint8)
cv.imwrite('ColorImageMadeByMedianFilterUnsharped_' +
           img_name + '.jpg', unsharp_color)

cv.imshow("Origianl Color Image", img_color)
cv.imshow("Original Gray Image", img_gray)
cv.imshow("Color Image Made By Median Filter", median_color)
cv.imshow("Gray Image Made By Median Filter", median_gray)
cv.imshow("Color Image Made By Median Filter & Unsharped", unsharp_color)
cv.imshow("Gray Image Made By Median Filter & Unsharped", unsharp_gray)
cv.waitKey(0)
cv.destroyAllWindows()
