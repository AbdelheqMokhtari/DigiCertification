#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="0" # set to your desired GPU id
#import tensorflow as tf
#from keras import backend as K
#K.set_image_data_format('channels_last')
#K.tensorflow_backend.set_session(tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))))

import os
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"]= "0"
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))