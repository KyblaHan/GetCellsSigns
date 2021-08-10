import pathlib
import src.sings_detector as sd
import pandas as pd


class sings_worker:
    images = []
    df = []

    def __init__(self, path):
        self.path_to_folder = path
        self.get_list_images()

    def get_list_images(self):
        path = pathlib.Path(self.path_to_folder)
        all_image_paths = list(path.glob('*'))
        self.images = [str(path) for path in all_image_paths]


    def work(self):
        self.df = []
        output = []
        for img in self.images:
            app_data = sd.sings_detector(img).get_all_signs()
            app_data.append(img)
            output.append(app_data)

        cols = sd.sings_detector.columns
        cols.append("path")
        self.df = pd.DataFrame(output, columns=cols)

        return self.df

    def to_csv(self):
        if self.df is None:
            self.work()

        self.df.to_csv("data/reports/output_sings.csv")
