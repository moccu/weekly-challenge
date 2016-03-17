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

---

*The data strucure*

```JavaScript
// An instance of this class describes a directional
// connection between two nodes by a distance
// between them.
function Path(node, distance) {
	this.node = node;
	this.distance = distance;
}

//  An instance of this class is a node. A node can be
// connected with other nodes by pathes.
function Node(name) {
	this.name = name;
	this.neighbours = [];
	this.reset();
}

Node.prototype.addNeighbour = function(node, distance) {
	this.neighbours.push(new Path(node, distance));
};

Node.prototype.reset = function() {
	this.previous = null;
	this.total = Number.MAX_VALUE;
};

Node.prototype.toString = function() {
	return this.name;
};
```

*The algorithm*

```JavaScript
function calculate(start, end, nodes) {
	// Clone nodes to not touch given nodes list...
	nodes = nodes.concat();

	// Reset all nodes, start node has a total distance of 0...
	nodes.forEach(function(node) { node.reset(); });
	start.total = 0;

	// As long as nodes are available...
	while (nodes.length > 0) {
		var current = null;
		var index = 0;

		// Get smallest node in nodes...
		nodes.forEach(function(node, at) {
			current = !current ? node : node.value < current.value ? node : current;
			index = current === node ? at : index;
		});

		// Remove smallest node from nodes...
		nodes.splice(index, 1);

		// Calculate distance to neighbours...
		current.neighbours.forEach(function(path) {
			var neighbour = path.node;

			// when in list of nodes...
			if (nodes.indexOf(neighbour) > -1) {
				var distance = current.total + path.distance;

				if (distance < neighbour.total) {
					neighbour.previous = current;
					neighbour.total = distance;
				}
			}
		});
	}

	// Build way from end to start node....
	var way = [end];
	end = end.previous;
	while (end) {
		way.unshift(end);
		end = end.previous;
	}

	return way;
}
```

*Usage*

```JavaScript
// Create nodes...
var
	Augsburg = new Node('Augsburg'),
	Erfurt = new Node('Erfurt'),
	Frankfurt = new Node('Frankfurt'),
	Karlsruhe = new Node('Karlsruhe'),
	Kassel = new Node('Kassel'),
	Mannheim = new Node('Mannheim'),
	Munich = new Node('Munich'),
	Nuremberg = new Node('Nuremberg'),
	Wuerzburg = new Node('Wuerzburg'),
	Stuttgart = new Node('Stuttgart'),
	
	// Store all cities in a list
	cities = [
		Augsburg, Erfurt, Frankfurt, Karlsruhe, Kassel,
		Mannheim, Munich, Nuremberg, Stuttgart, Wuerzburg
	]
;

// Connect nodes...
Augsburg.addNeighbour(Karlsruhe, 250);
Augsburg.addNeighbour(Munich, 84);
Erfurt.addNeighbour(Wuerzburg, 186);
Frankfurt.addNeighbour(Kassel, 173);
Frankfurt.addNeighbour(Mannheim, 85);
Frankfurt.addNeighbour(Wuerzburg, 217);
Karlsruhe.addNeighbour(Mannheim, 80);
Kassel.addNeighbour(Munich, 502);
Munich.addNeighbour(Nuremberg, 167);
Nuremberg.addNeighbour(Stuttgart, 183);
Nuremberg.addNeighbour(Wuerzburg, 103);

// Calculate the path from frankfurt to munich
calculate(Frankfurt, Munich, cities).join(' -> '); // "Frankfurt -> Kassel -> Munich"
```
From: Norman | Language: :heart:-script
