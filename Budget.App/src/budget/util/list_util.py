class ListUtil:
    @staticmethod
    def get_list_element_by_index(input_list, index, default=None):
        if len(input_list) > index:
            return input_list[index]
        return default