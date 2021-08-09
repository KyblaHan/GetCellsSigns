

import SingsDetector as sd


path = r"C:\_Programming\_DataSets\Multiclass\augData\test\Monocyte\1 (125).bmp.png"


sd = sd.SingsDetector(path)

print("S=", sd.get_area())
print("P=", sd.get_perimeter())
print("SC=", sd.get_shape_coefficient())
print("!", sd.get_average_brightness_rgb())

