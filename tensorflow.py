# map on the list of tensors unpacked from `elems` on dimension 0.
tf.map_fn

#######################
# image augmentation  #
#######################
image = tf.random_crop(image, size=[img_size_cropped, img_size_cropped, num_channels])

# Randomly flip the image horizontally.
image = tf.image.random_flip_left_right(image)

# Randomly adjust hue, contrast and saturation.
image = tf.image.random_hue(image, max_delta=0.05)
image = tf.image.random_contrast(image, lower=0.3, upper=1.0)
image = tf.image.random_brightness(image, max_delta=0.2)
image = tf.image.random_saturation(image, lower=0.0, upper=2.0)

# Limit the image pixels between [0, 1] in case of overflow.
image = tf.minimum(image, 1.0)
image = tf.maximum(image, 0.0)



