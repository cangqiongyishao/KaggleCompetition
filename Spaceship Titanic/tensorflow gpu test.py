import tensorflow as tf

# 检查 TensorFlow 版本
print("TensorFlow version:", tf.__version__)

# 检查是否有可用的 GPU
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# 如果有可用的 GPU，显示其详细信息
if tf.config.experimental.list_physical_devices('GPU'):
    print("GPU is available and will be used by TensorFlow.")
else:
    print("GPU is not available. TensorFlow will use the CPU.")