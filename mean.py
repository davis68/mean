def mean( num_list ):
    value = sum( num_list ) / len( num_list )
    if type(value) == complex:
        return NotImplemented
    else:
        return value
