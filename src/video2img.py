#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
import numpy as np
import sys, os
from sensor_msgs.msg import Image
import image_converter as ic

import yaml


class Video2Image():
    def __init__(self):
        ### load param
        try:
            config_name = './param/' + 'video2img.yaml'
            with open(config_name) as file:
                self.yaml = yaml.load(file, Loader=yaml.FullLoader)
        except:
            exit('ERROR: video2img.yaml not defined.') 

        self.img_cvt = ic.ImageConverter()
        self.time_stamp = 0
        self.image_stamp = 0
        self.path = self.yaml['save_path']
        
    def recorder_cb(self, data):
        if self.time_stamp % self.yaml['frame'] is 0:
            img = self.img_cvt.imgmsg_to_opencv(data)
            file_full_path = str(self.path)+ '/image_' + str(self.image_stamp) + '.png'
            cv2.imwrite(file_full_path, img)
            sys.stdout.write(file_full_path + '\r')
            self.image_stamp += 1
        self.time_stamp += 1
                                                      
def main():
    vi = Video2Image()

    rospy.init_node('video2img_ros')
    rospy.Subscriber(vi.yaml['sub_topic'], Image, vi.recorder_cb)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nBye...")    

if __name__ == '__main__':
    main()