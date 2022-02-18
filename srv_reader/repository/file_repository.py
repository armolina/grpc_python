import json
from src.shop.dto.product import Product

class FileRepository():
    __file_path = 'src/resources/product_list.json'
    __file_open = None

    def __open_file(self) -> None:
        if(self.__file_open==None):
            self.__file_open = open(self.__file_path)

    def read_data(self):
        try:
            self.__open_file()
            data_read = json.load(self.__file_open)
            return data_read
        except Exception as exception:
            raise Exception('Error reading data: ' + str(exception))
        finally:
            self.__close_file()

    def find_by_code(self, code: str) -> Product:
        data = self.read_data()

        for item in data:
            if(item['code']==code):
                return item

        return None

    def __close_file(self) -> None:
        if(self.__file_open):
            self.__file_open.close()