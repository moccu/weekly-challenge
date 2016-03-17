# 008: Dijkstras' algorithm

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. The task is to find the shortest path between Frankfurt and Munich by using [this map](https://upload.wikimedia.org/wikipedia/commons/a/ad/MapGermanyGraph.svg).

| A | B | Distance |
| --------- | ------ | --- |
| Augsburg | Karlsruhe | 250 |
| Augsburg | Munich | 84 |
| Erfurt | Wuerzburg | 186 |
| Frankfurt | Kassel | 173 |
| Frankfurt | Mannheim | 85 |
| Frankfurt | Wuerzburg | 217 |
| Karlsruhe | Mannheim | 80 |
| Kassel | Munich | 502 |
| Munich | Nuremberg | 167 |
| Nuremberg | Stuttgart | 183 |
| Nuremberg | Wuerzburg | 103 |

Source: [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra's_algorithm)

---

```python
from collections import namedtuple
from operator import attrgetter


Edge = namedtuple('Edge', ['a', 'b', 'dist'])
Section = namedtuple('Section', ['name', 'dist', 'parent'])


def parse_data(data):
    """Parse text data and return list of edges

    >>> parse_data('a b 1\\nb c 2')
    [Edge(a='a', b='b', dist=1), Edge(a='b', b='c', dist=2)]
    """
    items = [line.split(' ') for line in data.strip().split('\n')]
    return [Edge(i[0], i[1], int(i[2])) for i in items]


def edge_to_section(edge, parent):
    """Convert an edge to a section

    >>> edge_to_section(Edge('a', 'b', 2), Section('a', 1, None))
    Section(name='b', dist=3, parent=Section(name='a', dist=1, parent=None))
    """
    name = edge.a if edge.b == parent.name else edge.b
    return Section(name, edge.dist + parent.dist, parent)


def walk(target, sections, edges):
    """Find the shortest path to target and return the section

    >>> walk('a', [Section('a', 1, None)], [])
    Section(name='a', dist=1, parent=None)
    >>> walk('b', [Section('a', 1, None)], [])
    Traceback (most recent call last):
        ...
    Exception: Not found
    >>> walk('b', [Section('a', 1, None)], [Edge('a', 'b', 2)])
    Section(name='b', dist=3, parent=Section(name='a', dist=1, parent=None))
    """
    sec = sorted(sections, key=attrgetter('dist'))[0]
    sections.remove(sec)
    if sec.name == target:
        return sec
    elif not edges:
        raise Exception("Not found")
    next_edges = filter(lambda e: e.a == sec.name or e.b == sec.name, edges)
    rem_edges = filter(lambda e: e.a != sec.name and e.b != sec.name, edges)
    new_sections = [edge_to_section(e, sec) for e in next_edges]
    return walk(target, sections + new_sections, list(rem_edges))


def list_names(section):
    """Get a list with all section names

    >>> list_names(Section('b', 3, Section('a', 1, None)))
    ['a', 'b']
    """
    names = []
    while section:
        names.insert(0, section.name)
        section = section.parent
    return names


if __name__ == '__main__':
    with open('data.txt') as f:
        data = f.read()
    edges = parse_data(data)
    section = walk('Munich', [Section('Frankfurt', 0, None)], edges)
    names = list_names(section)
    print('{0}: {1}'.format(names, section.dist))
```
From: Andreas | Language: Python
