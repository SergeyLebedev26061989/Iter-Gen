class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list = []
        self.it = iter(self.list_of_list)
        return self

    def __next__(self):
        while True:
            try:
                self.cur_elem = next(self.it)
            except StopIteration:
                if not self.list:
                    raise StopIteration
                else:
                    self.it = self.list.pop()
                    continue
            if isinstance(self.cur_elem, list):
                self.list.append(self.it)
                self.it = iter(self.cur_elem)
            else:
                return self.cur_elem


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()