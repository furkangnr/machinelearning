def reduce_memory_usage(dataframe, verbose = True):
    
    numerics = ["int16", "int32", "int64", "float16" ,"float32", "float64"]
    start_memory = dataframe.memory_usage(deep=True).sum() / (1024 * 1024)
    
    for col in dataframe.columns:
        print(f"operation on {col} has started.")
        col_type = dataframe[col].dtype
        if col_type in numerics:
            col_min = dataframe[col].min()
            col_max = dataframe[col].max()
            if str(col_type)[:3] == "int":
                if col_min > np.iinfo(np.int16).min and col_max < np.iinfo(np.int16).max:
                    dataframe[col] = dataframe[col].astype("int16")
                elif col_min > np.iinfo(np.int32).min and col_max < np.iinfo(np.int32).max:
                    dataframe[col] = dataframe[col].astype("int32")    
                else:
                    dataframe[col] = dataframe[col].astype("int64") 
            else:
                if col_min > np.finfo(np.float16).min and col_max < np.finfo(np.float16).max:
                    dataframe[col] = dataframe[col].astype("float16")
                elif col_min > np.finfo(np.float32).min and col_max < np.finfo(np.float32).max:
                    dataframe[col] = dataframe[col].astype("float32")    
                else:
                    dataframe[col] = dataframe[col].astype("float64")
        print(f"operation on {col} has ended.")
        
    print("\n \n Data type conversions has finished.")
    end_memory = dataframe.memory_usage(deep=True).sum() / (1024 * 1024)
    
    if verbose:
        percentage = 100 * (start_memory - end_memory) / start_memory
        print(f"\n \n Memory usage dropped {start_memory - end_memory}MB. This means %{percentage} reduction.")
    
    return dataframe