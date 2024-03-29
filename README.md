==========
 grapheap
==========

A read optimised graph (DS) library    


Read more about:   

Graph: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)    
Heap: https://en.wikipedia.org/wiki/Heap_(data_structure)   


Installation
------------

To install grapheap, simply:   

for Python2
```sh
pip install grapheap
```
for Python3
```sh
pip3 install grapheap
```

Install Memcache using Homebrew:
```sh
brew install memcached
```


Configuration
-------------

Update memcache configuration:   

```sh
sudo vim ~/grapheap_config.conf
```


Basic Use
---------

Run Memcached service:    

```sh
memcached -p 11211
```


To use grapheap, you must first create an instance of Grapheap,
and construct your nodes and edges:    

```python
# Import Grapheap
from grapheap import Grapheap

# Create a grapheap
g = Grapheap()

# Add optimisation keys
g.optimise_for('bananas')
g.optimise_for('apples')

# Create Nodes (need 'apples', 'bananas' keys in all nodes, as they have been added to optimisation_keys)
n1 = g.add_vertex({
    'name': 'Tom',
    'age': 24,
    'bananas': 5,
    'apples': 4
})
n2 = g.add_vertex({
    'name': 'Bob',
    'bananas': 0,
    'apples': 8
})
n3 = g.add_vertex({
    'name': 'Harry',
    'gender': 'Male',
    'bananas': 3,
    'apples': 1
})
n4 = g.add_vertex({
    'name': 'Jill',
    'bananas': 8,
    'apples': 1
})

# Connect them
g.add_edge(g.entry, n2) # g.entry specifies the entry point for graph
g.add_edge(g.entry, n3)
g.add_edge(n2, n3)
g.add_edge(n3, n4)
g.add_edge(n2, n1)
```

![grapheap](http://i.imgur.com/mbWiYet.png)


Then you can perform filter/sort operations on any of the node to get the required adjacent nodes from that node:

```python
# Filter By
# Get all outgoing nodes (only adjacent) from n2 which have only 1 apples
nodes1 = n2.get_outgoing().filter_by('apples', [1]).get_all_nodes()

# Sort By
# Get all incoming nodes (only adjacent) to n3 sorted by number of bananas they have
nodes2 = n3.get_incoming().sort_by('bananas').get_all_nodes()

# Get first incoming node to n1 sorted by bananas
node1 = n1.get_incoming().sort_by('bananas').get_node_indexed_at(0)
```


Also you can perform chained complex operations:

```python
# Filter By, Sort By
# Get all outgoing nodes (only adjacent) from n2 with apples less than 5 and sorted by bananas
nodes1 = n2.get_outgoing().filter_by('apples', 5, "lt").sort_by('bananas').get_all_nodes()

# Sort By, Filter By, Filter By
nodes2 = n3.get_incoming().sort_by('bananas').filter_by('bananas', [1, 5], "in").filter_by('apples', [1]).get_all_nodes()
```

Metrics 
-------

* **Filter By (equal to):** 0.0065 seconds
* **Filter By (less than):** 0.0065 seconds
* **Filter By (greater than):** 0.0099 seconds
* **Filter By (range):** 0.0115 seconds
* **Sort By:** 0.0088 seconds
* **Filter By, Filter By:** 0.0119 seconds
* **Filter By, Sort By:** 0.0155 seconds

*Operations are performed on the node which is connected to 100 nodes*

Contributing
------------

Contributions are awesome. You are most welcome to [submit issues](https://github.com/practo/grapheap/issues),
or [fork the repository](https://github.com/practo/grapheap).
