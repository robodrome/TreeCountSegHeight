
import os


# Configuration of the parameters for segmentation and counting preprocessing
class Configuration:
    
    def __init__(self):
        self.training_base_dir = '/home/sizhuo/Desktop/denmark10cm/poly_rect/poly_rect_utm_test/'
        self.training_area_fn = 'rectangles.shp'
        self.training_polygon_fn = 'polygons.shp'


        # For reading multichannel images
        self.raw_image_base_dir = './raw_tif_utm_v4/' 
        self.raw_image_file_type = '.tif'
        self.raw_image_prefix = 'reset_2018_' 
        self.raw_aux_prefix = ['CHM_', 'ndvi_2018_'] 
        self.prediction_pre = 'det'
        # Channel names in order for the raw tif image
        self.raw_channel_prefixs = ['red', 'green', 'blue', 'infrared']
        # channel names in order for the auxiliary tif image
        self.aux_channel_prefixs = [['chm'], ['ndvi']]
        # All channel in one single raster file or not
        self.single_raster = False
        self.bands = list(range(len(self.raw_channel_prefixs)))
        self.aux_bands = list(list(range(len(c))) for c in self.aux_channel_prefixs) # for multi auxs

        # For writing the extracted images and their corresponding annotations and boundary file
        self.path_to_write = './extracted_data_testtest'
        self.show_boundaries_during_processing = True #False
        self.extracted_file_type = '.png'
        self.extracted_filenames = ['red', 'green', 'blue', 'infrared']
        self.extracted_annotation_filename = 'annotation'
        self.extracted_boundary_filename = 'boundary'
        self.kernel_size_svls = 15
        self.kernel_sigma_svls = 5

        # Path to write should be a valid directory
        # assert os.path.exists(self.path_to_write)
        if not os.path.exists(self.path_to_write):
            os.makedirs(self.path_to_write)

        if not len(os.listdir(self.path_to_write)) == 0:
            print('Warning: path_to_write is not empty! The old files in the directory may not be overwritten!!')

