from pprint import pprint

d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]


def merge_doubicate_tupels_value(tups):
    i, j = 0, 1
    while i < len(tups):
        tmp = j
        while j < len(tups):
            if tups[i][1] == tups[j][1]:
                tups[i] = (tups[i][0], *tups[j])
                tups.pop(tups.index(tups[j]))
            j += 1
        j = tmp + 1
        i += 1
    return tups


def tups_to_dict(tups):
    d = {}
    for item in tups:
        if len(item) > 2:
            d.update({item[2]: [item[0], item[1]]})
        else:
            d.update({item[1]: item[0]})
    return d


def print_dict(item):

    for k, v in item.items():
        print(k, ':', end=' ')
        if type(v) is list:
            print(*v)
        else:
            print(v)


if __name__ == '__main__':
    merged_tups = merge_doubicate_tupels_value(d)
    dictionary = tups_to_dict(merged_tups)
    sorted_dic = sorted(dictionary.items(), reverse=True)
    sorted_dic = (dict(sorted_dic))
    print_dict(sorted_dic)