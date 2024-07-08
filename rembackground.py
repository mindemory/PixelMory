import os
import numpy as np
from PIL import Image
import argparse

def main(fname):
    # file_name = 'Fig1.png'
    img = Image.open(fname)
    img_array = np.array(img)
    print(img_array.shape)

    img_new_array = img_array.copy()
    # Add an empty column for alpha values
    img_new_array = np.insert(img_new_array, 3, 255, axis=2)

    # Set the alpha value to 0 for the white pixels
    img_new_array[img_new_array[:,:,0] == 255] = [255, 255, 255, 0]
    # Change the black pixels to be white but not transparent
    img_new_array[img_new_array[:,:,0] == 0] = [255, 255, 255, 255]
    # Save the image
    img_new = Image.fromarray(img_new_array)
    img_new.save(fname[:-4] + '_transparent.png', 'PNG', quality=300)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', type=str, help='File name')
    args = parser.parse_args()
    main(args.fname)