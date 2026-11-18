def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """

    mini = [float('inf')] * len(data[0])
    maxi = [float('-inf')] * len(data[0])
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            mini[j] = min(mini[j], data[i][j])
            maxi[j] = max(maxi[j], data[i][j])

    for i in range(len(data)):
        for j in range(len(data[0])):
            if mini[j]==maxi[j]:
                data[i][j] = 0.0
            else:
                data[i][j] = (data[i][j]-mini[j])/(maxi[j]-mini[j])

    return data