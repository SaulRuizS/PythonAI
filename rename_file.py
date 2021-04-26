import os

def rename_img():
    """
    Resize images from 'images' directory
    """
    directory_imgs = 'C:\\AI_dev\\trafficlights_detector_yolo\\data\\custom\\images\\'
    count = 0
    jpegFileName = ''
    pngFileName  = ''

    for img in os.listdir(directory_imgs):
        
        img_filepath = directory_imgs + img
        
        filename, file_ext = os.path.splitext(img_filepath)

        count += 1

        if(file_ext == '.jpeg')
            jpegFileName = 'difjpeg' #+ str(count)
            filename = directory_imgs + jpegFileName
        elif(file_ext == 'png')
            
            filename = directory_imgs + pngFileName
        else
            filename = directory_imgs + 'img' + str(count)


        #print(filename)
        #print(file_ext)

    print('Images renamed')


rename_img()