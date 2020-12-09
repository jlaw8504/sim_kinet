class CompileParse:
    """
    Parse directory containing compiled images in RGB format
    """
    def __init__(self, directory):
        self.directory = directory

    def parse_dir(self, glob_pattern):
        from tensorflow.keras.preprocessing import image
        import glob
        import os
        import numpy as np

        files = glob.glob(os.path.join(self.directory, glob_pattern))
        array_list = []
        for file in files:
            img = image.load_img(file)
            im_array = image.img_to_array(img)
            array_list.append(im_array)
        im_stack = np.stack(array_list)
        return im_stack