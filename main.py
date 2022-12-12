class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.element_list = 0
        self.list_of_list_element = 0
        return self

    def __next__(self):

        if self.element_list < len(self.list_of_list[self.list_of_list_element]):
            item = self.list_of_list[self.list_of_list_element][self.element_list]
            self.element_list += 1
        else:
            self.list_of_list_element +=1
            if self.list_of_list_element < len(self.list_of_list):
                self.element_list = 0
                item = self.list_of_list[self.list_of_list_element][self.element_list]
                self.element_list += 1
            else:
                raise StopIteration
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # for x in FlatIterator(list_of_lists_1):
    #     print(x)


    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()