import numpy as np

def main():
    
    result = calculate(list(range(9)))
    print(result)

def calculate(le_list):
    
    # Raise Error if the length of the list is not nine
    if len(le_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Create a dictionary with final results
    final_dict = {}
    
    # Convert the 1D list of 9 elements to a 3D list of 3 elements each
    three_matrix = np.array(le_list).reshape((3, 3, 1))

    # Make a flat version of the numpy array
    flat_matrix = three_matrix.flatten()

    # Grab mean
    mean_axis_1 = np.mean(three_matrix, axis = 0)
    mean_axis_2 = np.mean(three_matrix, axis = 1)

    # Grab mean along flat list
    mean_flat = np.mean(flat_matrix)

    # Store results on a list
    mean_1_list = convert_result_to_list(mean_axis_1)
    mean_2_list = convert_result_to_list(mean_axis_2)

    # Add the mean key to the dict
    final_dict["mean"] = [mean_1_list, mean_2_list, mean_flat]

    # Grab the variance
    var_axis_1 = np.var(three_matrix, axis = 0)
    var_axis_2 = np.var(three_matrix, axis = 1)

    # Grab flat variance
    var_flat = np.var(flat_matrix)

    # Store results on a list
    var_1_list = convert_result_to_list(var_axis_1)
    var_2_list = convert_result_to_list(var_axis_2)

    # Add the variance key to the dict
    final_dict["variance"] = [var_1_list, var_2_list, var_flat]

    # Calculate the standard deviation
    std_axis_1 = np.std(three_matrix, axis = 0)
    std_axis_2 = np.std(three_matrix, axis = 1)

    # Grab the flat std
    std_flat = np.std(flat_matrix)

    # Store results in list
    std_1_list = convert_result_to_list(std_axis_1)
    std_2_list = convert_result_to_list(std_axis_2)

    # Add the standard deviation to the dict
    final_dict["standard deviation"] = [std_1_list, std_2_list, std_flat]

    # Find the maximum
    max_axis_1 = np.amax(three_matrix, axis = 0)
    max_axis_2 = np.amax(three_matrix, axis = 1)

    # Grab flat max
    max_flat = np.amax(three_matrix)

    # Store results in list
    max_1_list = convert_result_to_list(max_axis_1)
    max_2_list = convert_result_to_list(max_axis_2)

    # Add the max to the dict
    final_dict["max"] = [max_1_list, max_2_list, max_flat]

    # Find the minimum
    min_axis_1 = np.amin(three_matrix, axis = 0)
    min_axis_2 = np.amin(three_matrix, axis = 1)

    # Grab the flat min
    min_flat = np.amin(flat_matrix)

    # Store results in list
    min_1_list = convert_result_to_list(min_axis_1)
    min_2_list = convert_result_to_list(min_axis_2)

    # Add the min to the dict
    final_dict["min"] = [min_1_list, min_2_list, min_flat]

    # Find the sum
    sum_axis_1 = np.sum(three_matrix, axis = 0)
    sum_axis_2 = np.sum(three_matrix, axis = 1)

    # Grab the flat sum
    sum_flat = np.sum(flat_matrix)

    # Store results in list
    sum_1_list = convert_result_to_list(sum_axis_1)
    sum_2_list = convert_result_to_list(sum_axis_2)

    # Add the sum to the dict
    final_dict["sum"] = [sum_1_list, sum_2_list, sum_flat]

    # Return the final dict
    return final_dict

def convert_result_to_list(result_arr):
    return [result_arr[i][0] for i in range(len(result_arr))]


if __name__ == "__main__":
    main()