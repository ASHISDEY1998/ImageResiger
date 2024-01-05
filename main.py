import cv2
import os

def split_file_name_and_file_path(file_path):
  """Splits a file path into the file name and file path.

  Args:
    file_path: The file path to split.

  Returns:
    A tuple containing the file name and file path.
  """

  drive, file_path = os.path.splitdrive(file_path)
  path, file_name = os.path.split(file_path)
  file_name, extension = os.path.splitext(file_name)
  return file_name, path, extension


def resigeimage(image,scale):
    file_name, path ,extension= split_file_name_and_file_path(image)


    imagesrc = cv2.imread(f'C:{path}/{file_name}{extension}',cv2.IMREAD_UNCHANGED)
    # percent by which the image is resized
    scale_percent = scale

    # calculate the 50 percent of original dimensions
    new_height = int(imagesrc.shape[0] * scale_percent / 100)
    new_width = int(imagesrc.shape[1] * scale_percent / 100)

    # dsize tupple
    dsize = (new_width, new_height)

    # resize image
    output = cv2.resize(imagesrc, dsize)

    # save resiged image
    cv2.imwrite(f'Resiged_{file_name}{extension}', output)

    # display resiged image
    newimagesrc = cv2.imread(f'Resiged_{file_name}{extension}', cv2.IMREAD_UNCHANGED)
    cv2.imshow(f'Resiged_{file_name}{extension}', newimagesrc)

    cv2.waitKey(0)

if __name__ == '__main__':
    image_path = input("Enter the path to the image: ")
    scale= int(input('Please give the scale % you want to reduce :'))
    resigeimage(image_path,scale)
    # resigeimage('RoseImage.jpg',20)
