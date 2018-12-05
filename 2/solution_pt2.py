if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        data = f.read().splitlines()

    final_diff_indices, final_minus_diff = list(), ''

    data_len = len(data)
    for i, v1 in enumerate(data):
        if i + 1 != data_len:
            for v2 in data[i + 1:]:

                minus_diff = ''
                diff_indices = list()

                for ind, v1_letter in enumerate(v1):
                    v2_letter = v2[ind]

                    if v1_letter == v2_letter:
                        minus_diff += v1_letter
                    else:
                        diff_indices.append(ind)

                if not final_diff_indices or len(diff_indices) < len(final_diff_indices):
                    final_diff_indices = diff_indices
                    final_minus_diff = minus_diff

    print(final_diff_indices, final_minus_diff)
