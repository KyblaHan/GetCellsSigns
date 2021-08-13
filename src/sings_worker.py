import pathlib
import sings_detector as sd
import pandas as pd


class sings_worker:
    """
    Класс построения отчетов и поиска признаков.
    """
    images = []
    df = []

    def __init__(self, path):
        self.path_to_folder = path
        self.get_list_images()

    def get_list_images(self):
        """
        Получение списка всех изображений в папке path_to_folder.
        :return:
        """
        path = pathlib.Path(self.path_to_folder)
        all_image_paths = list(path.glob('*'))
        self.images = [str(path) for path in all_image_paths]

    def create_report(self):
        """
        Поиск признаков для всех изображений в папке и генерация отчета.
        :return:
        """
        self.get_all_sings()
        self.to_csv()

    def get_all_sings(self):
        """
        Поиск признаков для всех изображений в папке.
        :return: DataFrame - перечень признаков для каждой клетки
        """
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
        """
        Запись в CSV.
        :return:
        """
        if self.df is None:
            self.get_all_sings()

        self.df.to_csv("data/reports/output_sings.csv")
