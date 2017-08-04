from bs4 import BeautifulSoup


def _process_string(s):
    return s.strip().replace('\n', '')


def _process_tuple(tuple):
    return map(_process_string, tuple)


def _get_parsed_row(soup):
    fields_to_get = ['age', 'aboutme', 'displayname']

    for row in soup.find_all('row'):
        yield _process_tuple(
            row.get(field, '') for field in fields_to_get
        )


def main(fname, ofname):
    with open(fname, 'r') as f:
        soup = BeautifulSoup(f, 'lxml')

    with open(ofname, 'w') as output:
        for row in _get_parsed_row(soup):
            print(','.join(row), file=output)


if __name__ == '__main__':
    fname = 'Users.xml'
    ofname = 'output.csv'
    main(fname, ofname)
