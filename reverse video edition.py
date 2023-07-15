#!/usr/bin/env python
# coding: utf-8

# ### importing libraries

# In[1]:


import cv2


# #### passing location of the file
# 

# In[2]:


cap = cv2.VideoCapture("C:\\Users\\rajpu\\Downloads\\Untitled video - Made with Clipchamp (1).mp4")
cap


# ### hold each frame of video

# In[3]:


#Grab the current frame.
check , vid = cap.read()


# ### summing up all the frames into a single list

# In[4]:


counter = 0
  
# Initialize the value
# of check variable
check = True
  
frame_list = []
  


# ### By default, video will play and at the end, it will reverse the frame

# In[5]:


# If reached the end of the video 
# then we got False value of check.
  
# keep looping until we
# got False value of check.
while(check == True):
      
    # imwrite method of cv2 saves the 
    # image to the specified format.
    cv2.imwrite("frame%d.jpg" %counter , vid)
    check , vid = cap.read()
      
    # Add each frame in the list by
    # using append method of the List
    frame_list.append(vid)
      
    # increment the counter by 1
    counter += 1
  


# #####  last value in the frame_list is None ,because when video reaches to the end then false value store in check variable and None value is store in vide variable.

# In[ ]:


# removing the last value from the 
# frame_list by using pop method of List
frame_list.pop()
  
# looping in the List of frames.
for frame in frame_list:
      
    # show the frame.
    cv2.imshow("Frame" , frame)
      
    # waitkey method to stopping the frame
    # for some time. q key is presses,
    # stop the loop
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break


# #### Apply reverse method for each frame rate.

# In[ ]:


# release method of video 
# object clean the input video
cap.release()
  
# close any open windows
cv2.destroyAllWindows()
  
# reverse the order of the element 
# present in the list by using
# reverse method of the List.
frame_list.reverse()
  
for frame in frame_list:
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break
  
cap.release()
cv2.destroyAllWindows()


# ## A pop of window will appear and u can watch your video in reversing frame rates.
