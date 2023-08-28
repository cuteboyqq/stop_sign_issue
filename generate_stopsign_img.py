import os
import glob
import shutil
import cv2
import random
import numpy as np
def Generate_StopSign_Img(args=None):

    img_path_list = glob.glob(os.path.join(args.img_dir,"*.jpg"))
    roi_path_list = glob.glob(os.path.join(args.roi_dir,"*.jpg"))
    
    for img_path in img_path_list:
        img = cv2.imread(img_path)

        random_index = random.randint(0, (len(roi_path_list)-1))
        random_roi_path = roi_path_list[random_index]
        roi = cv2.imread(random_roi_path)

        ##filter small size roi, roi size needs > 100*100
        while(roi.shape[0]*roi.shape[1]<100*100):
            random_index = random.randint(0, (len(roi_path_list)-1))
            random_roi_path = roi_path_list[random_index]
            roi = cv2.imread(random_roi_path)
        


        x = random.randint(0+roi.shape[1], img.shape[1]-roi.shape[1])
        y = random.randint(0+roi.shape[0], img.shape[0]-roi.shape[0])
        print(x)
        print(y)
        mask = 255 * np.ones(roi.shape, roi.dtype)
        center = (x,y)                
        #for i in range(100):
        output = cv2.seamlessClone(roi, img, mask, center, cv2.MIXED_CLONE)   

        show_img=True
        if show_img:
            cv2.imshow("img",img)
            cv2.imshow("output",output)
            cv2.imshow("roi",roi)
            cv2.waitKey(1500)
            cv2.destroyAllWindows()
    
    return NotImplementedError


def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-imgdir','--img-dir',help='image dir',default="/home/ali/Projects/datasets/BDD100K-ori/images/100k/train")
    parser.add_argument('-roidir','--roi-dir',help='roi dir',default="/home/ali/Projects/GitHub_Code/ali/landmark_issue/stop_sign")
    parser.add_argument('-savedir','--save-dir',help='save img dir',default="/home/ali/Projects/GitHub_Code/ali/landmark_issue/stopsign_images")
    parser.add_argument('-saveimg','--save-img',type=bool,default=True,help='save stopsign fake images')
    parser.add_argument('-show','--show',type=bool,default=False,help='show images result')
    return parser.parse_args()  
  
if __name__=="__main__":
    args = get_args()
    Generate_StopSign_Img(args)