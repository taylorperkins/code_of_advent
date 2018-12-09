class Node:
    def __init__(self, ind, child_node_cnt, metadata_entry_cnt):
        """This guy can probably be removed actually. It gets used a bit more in pt 2 though."""
        self.ind = ind

        self.child_node_cnt = child_node_cnt
        self.metadata_entry_cnt = metadata_entry_cnt


class Tree:
    def __init__(self, node_stream):
        self.node_stream = node_stream

        # pull from the end and add one to get the index of the next
        self.used_indices = list()
        self.metadata_indices = list()

    def build_tree(self, start_idx=0):
        """iterates through the node stream and maps out the outline of the tree

        :param int start_idx: idx in which to begin parsing
        :return: None
        """
        # the header for the node count and also the header for the metadata count
        self.used_indices.extend([start_idx, start_idx + 1])

        child_node_cnt, metadata_entry_cnt = self.node_stream[start_idx], self.node_stream[start_idx + 1]
        node = Node(start_idx, child_node_cnt, metadata_entry_cnt)

        for i in range(node.child_node_cnt):
            child_idx = self.used_indices[-1] + 1

            self.build_tree(child_idx)

        # need to account for the indices that children have used up
        metadata_start_inx = self.used_indices[-1] + 1

        # no more children.. so now we can begin to calculate metadata schtuff.
        self.used_indices.extend(list(range(metadata_start_inx, metadata_start_inx + metadata_entry_cnt)))
        self.metadata_indices.extend(list(range(metadata_start_inx, metadata_start_inx + metadata_entry_cnt)))

    def add_up_metadata_entries(self):
        total_entries = 0
        calc = ''

        for i in self.metadata_indices:
            calc += f'+{self.node_stream[i]}'
            total_entries += self.node_stream[i]

        print(calc)
        return total_entries


if __name__ == '__main__':
    with open('./input.txt') as f:
        data = list(map(int, f.read().split(' ')))

    tree = Tree(node_stream=data)
    tree.build_tree()

    print(tree.add_up_metadata_entries())
