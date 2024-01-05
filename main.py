import cv2
def resigeimage(image):
    imagesrc = cv2.imread(image,cv2.IMREAD_UNCHANGED)
    # cv2.imshow(image,imagesrc)

    # percent by which the image is resized
    scale_percent = 20

    # calculate the 50 percent of original dimensions
    new_height = int(imagesrc.shape[0] * scale_percent / 100)
    new_width = int(imagesrc.shape[1] * scale_percent / 100)

    # dsize tupple
    dsize = (new_width, new_height)

    # resize image
    output = cv2.resize(imagesrc, dsize)

    # save resiged image
    cv2.imwrite(f'Resiged_{image}', output)

    # display resiged image
    newimagesrc = cv2.imread(f'Resiged_{image}', cv2.IMREAD_UNCHANGED)
    cv2.imshow(f'Resiged_{image}', newimagesrc)

    cv2.waitKey(0)

if __name__ == '__main__':
    resigeimage('RoseImage.jpg')
