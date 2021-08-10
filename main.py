import src.sings_worker as sw
import src.segment as sg

#
# sw_1 = sw.sings_worker(r"data/segmented_cells_images")
# sw_1.work()
# sw_1.to_csv()

seg = sg.segment(r"C:/_Programming/GetCellsSigns/data/input_images/18бласт.png")
seg.create_histogram()
