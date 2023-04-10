def dumps(pickled_objs={}, **kwargs):
    """Serializes objects."""
    import pickle
    pickled_objs.update(kwargs)
    return pickle.dumps(pickled_objs)


def dump(b_str):
    """Loads serialized objects."""
    import pickle
    pickled_objs = pickle.loads(b_str)
    if pickled_objs.get("info", 0) !=0:
        path_or_name = pickled_objs["info"]
    else:
        path_or_name = "pickled_objs.pkl"
    with open(path_or_name, mode="wb") as file_bin:
        pickle.dump(pickled_objs, file_bin)
        
        
def load(path_or_name):
    """Load pickled objects."""
    import pickle
    with open(path_or_name, "rb") as file_bin:
        pickled_objs = pickle.load(file_bin)
    return pickled_objs