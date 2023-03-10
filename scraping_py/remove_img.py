import os
import re


## GFPGAN으로 생성된 이미지 파일로부터 

remove_list = ""   
 
def to_list(remove_list):
    new_list = remove_list.split(" ")
            
    return new_list
        
def remove_img_func(remove_list, cmp_path, restored_path):
    remove_img = to_list(remove_list)
    
    c_path = os.listdir(cmp_path)
    r_path = os.listdir(restored_path)
    
    for c, r in zip(c_path, r_path):
        c_img = c.split(".png")[0]
        r_img = r.split(".png")[0]

        if c_img in remove_img and r_img in remove_img:
            print(c_img, r_img)
            os.remove(f'{cmp_path}\\{c}')
            os.remove(f'{restored_path}\\{r}')

remove_img_func(remove_list, 
                r"compare\여고단체사진cmp\cmp",
                r"compare\여고단체사진restored\restored_faces")
