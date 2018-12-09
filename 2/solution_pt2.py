if __name__ == '__main__':
    """Had to take a step back for this one! 
    
    We are comparing each line to one another and keeping track of the same values at each index.
    For the lines that are most similar, what are the values between the two lines that are the same?
    """

    with open('./input.txt', 'r') as f:
        data = f.read().splitlines()

    final_diff_indices, final_minus_diff = list(), ''

    data_len = len(data)

    # I dont want to do multiple checks, so there is this nestted loop
    for i, v1 in enumerate(data):
        if i + 1 != data_len:  # next value exists..
            for v2 in data[i + 1:]:

                minus_diff = ''
                diff_indices = list()

                # check values at each corresponding index, and record the findings
                for ind, v1_letter in enumerate(v1):
                    v2_letter = v2[ind]

                    if v1_letter == v2_letter:
                        minus_diff += v1_letter
                    else:
                        diff_indices.append(ind)

                # keep track of the smallest comparison
                if not final_diff_indices or len(diff_indices) < len(final_diff_indices):
                    final_diff_indices = diff_indices
                    final_minus_diff = minus_diff

    print(final_diff_indices, final_minus_diff)
