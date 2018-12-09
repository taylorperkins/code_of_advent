class Node:
    def __init__(self, ind):
        # basically the id of the node
        self.ind = ind

        self.node_value = 0
        self.children = list()

        self.metadata_values = list()

    def get_node_value(self):
        if not self.children:
            # sum of all metadata entries
            return sum(self.metadata_values)

        else:
            # determining the values for this case is really weird.
            # It is fully dependent on the relationship between metadata and children
            # for example, if there are 2 children and metadatta values are [1, 3]:
            # this node's value is the sum of the nodes in the metadata list {first and third children}
            # since there is not a third child, only the first child is considered.
            value = 0
            for val in self.metadata_values:
                try:
                    # + 1 accounts for python 0 indexing
                    value += self.children[val - 1].get_node_value()

                except IndexError:
                    pass

            return value


class Tree:
    def __init__(self, node_stream):
        self.node_stream = node_stream

        # pull from the end and add one to get the index of the next
        self.used_indices = list()

    def build_tree(self, start_idx=0):
        """iterates through the node stream and maps out the outline of the tree

        :param int start_idx: idx in which to begin parsing
        :return: None
        """
        # the header for the node count and also the header for the metadata count
        self.used_indices.extend([start_idx, start_idx + 1])

        child_node_cnt, metadata_entry_cnt = self.node_stream[start_idx], self.node_stream[start_idx + 1]
        node = Node(start_idx)

        for i in range(child_node_cnt):
            child_idx = self.used_indices[-1] + 1
            node.children.append(self.build_tree(child_idx))

        # need to account for the indices that children have used up
        metadata_start_inx = self.used_indices[-1] + 1

        # no more children.. so now we can begin to calculate metadata schtuff.
        self.used_indices.extend(list(range(metadata_start_inx, metadata_start_inx + metadata_entry_cnt)))

        node.metadata_values.extend([
            self.node_stream[i] for i in range(metadata_start_inx, metadata_start_inx + metadata_entry_cnt)
        ])
        return node


if __name__ == '__main__':
    with open('./input.txt') as f:
        data = list(map(int, f.read().split(' ')))

    tree = Tree(node_stream=data)
    root_node = tree.build_tree()

    print(root_node.get_node_value())
