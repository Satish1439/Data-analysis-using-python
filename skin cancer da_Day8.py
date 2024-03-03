#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install --upgrade tensorflow')


# In[3]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[4]:


IMG_SIZE=224
BATCH_SIZE=32


# In[5]:


#creating training parameter
train_datagen=ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)


# In[6]:


#creating training data with above parameters
#folder = parameters.flow_from_directory(path,ts,bs,cm,subset)
train_generator = train_datagen.flow_from_directory(r'C:\Users\hi\Downloads\archive (1)\train',
                                                    target_size=(IMG_SIZE,IMG_SIZE),
                                                    batch_size=BATCH_SIZE,
                                                    class_mode='binary',
                                                    subset='training'
                                                   )




# In[7]:


val_generator = train_datagen.flow_from_directory(r'C:\Users\hi\Downloads\archive (1)\train',
                                                    target_size=(IMG_SIZE, IMG_SIZE),
                                                    batch_size=BATCH_SIZE,
                                                    class_mode='binary',
                                                    subset='validation'
                                                   )


# In[9]:


#define the model`
model=keras.Sequential([
    layers.Conv2D(32, (3,3),activation='relu',input_shape=(IMG_SIZE,IMG_SIZE,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(128, (3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])


# In[11]:


#compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


# In[12]:


model.fit(train_generator,validation_data=val_generator,epochs=5)


# In[13]:


model.save("SKIN_CANCER.h5","label.txt")


# In[15]:


#load the saved model
model=load_model(r'C:\Users\hi\SKIN_CANCER.h5')
#load and preprocess the test image
test_image_path=r'C:\Users\hi\Downloads\archive (1)\train\malignant\99.jpg'
img=image.load_img(test_image_path,target_size=(224,224))
img_array=image.img_to_array(img)
img_array=np.expand_dims(img_array, axis=0)


#Add batch dimension
img_array /=255. #Normalize the pixel value
#Make prediction
prediction=model.predict(img_array)
#print the prediction
print(prediction)


# In[ ]:




