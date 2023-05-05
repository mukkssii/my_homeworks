from typing import Any

everything = [12,
              'hey',
              46.8,
              'boom',
              ['bye', 14.6, 'No way'],
              {44.3, 'guitar', 33},
              ('dog', 'kitten', 34, 55),
              'notebook',
              34.5,
              'something'
              'hello',
              ('boombastik', 33, 'bye'),
              {'nof', 'yes'},
              2345,
              3.3,
              'anyone',
              ['OOH NOOO', 'OOH YEAH'],
              {'True', 'False'},
              545454234255342514542354325,
              4.7,
              'OMG',
              'Wow',
              ('Donbas', 'Lugansk'),
              'hehehehehehehe',
              ['gta', 'cyberpunk'],
              {'nice', 'yeaaah'},
              ['Spider man', 'batman'],
              'some',


              ]


def is_str(value: Any):
    if type(value) == str:
        return True
    return False


only_str = list(filter(is_str, everything))
only_str2 = list(filter(lambda value: type(value) == str, everything))


def string_plus_string(value: Any) -> str:
    if type(value) == str:
        return value + ' boom'
    return ''


only_string = list(map(string_plus_string, only_str2))
only_string_lambda = list(map(lambda value: value + ' boom', only_str2))
