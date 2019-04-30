#Author Thivahar Ajay Thennarasu(22221279)
# project Computing world happiness index
# Date 29/04/2019

import os

#function read_file is used read the input file given by the user
def read_file(file_name):
    #os module provides way of using opreating system dependent functionality
    #if statement check whether file exists or not
    if not os.path.isfile(file_name):
        print("File % doesnt exists in the list ")
        return []

    #here csv file will be changed into list of list by using readlines function
    else:
        fh=open(file_name,"r")
        new_array = []
        for line in fh.readlines():
            data=line.replace("\n","").split(",")
            new_array.append(data)
    return new_array

#in float_conversion function used to convert all the numerical string into flaot values
def float_conversion(files):

    lenrow=len(files)
    lencolumn=len(files[0])
    for i in range(1,lenrow):
        for j in range(1,lencolumn):
            if files[i][j]=="":
                files[i][j]=None
            else:
                files[i][j] = float(files[i][j])
    return files

#min_max function used to find the minimum and maximum number out of all the list
def min_max(float_value):

    for i in range (0,len(float_value)):  
        # loop though each column
        min_col = []
        max_col = []
        if i != 0:
            for j in range(1,len(float_value[0])):
                if j != 0 and j != 1:
                    min_col.append(float_value[i][j])
                    max_col.append(float_value[i][j])

            if i == 1:
                # temporary variable as the first list were we can check with upcoming list
                temp_min = min_col
                temp_max = max_col

            else:
                for k in range(len(min_col)):
                    # print(temp_min[k], min_col[k], 'vs')
                    if min_col[k] != None:
                        #min() to print the minimum numbers in that list
                        temp_min[k] = min(temp_min[k], min_col[k])#temp_min[k] is the temporary variable to find min
                        #max() mto return the maximum number in the list
                        temp_max[k] = max(temp_max[k], max_col[k])#temp_max[k] is the temporary variable to find max

    return temp_min, temp_max

#mormalize function used to normalize the values from 2 column till end between o to 1
def normalize(files, min_v, max_v):
    lenrow=len(files)
    lencolumn=len(files[0])
    for i in range(1,lenrow):
        for j in range(2,lencolumn): 
            # print(i, j)
            # print(files[i][j])
            if files[i][j] != None:
                files[i][j] = (files[i][j]-min_v[j-2]) / (max_v[j-2] - min_v[j-2])#To find normalizaation
    return files

#comp_min function used to find the minimum in all the list ans append to a new list
def comp_min(files):
    lenrow=len(files)
    lencolumn=len(files[0])
    min_list = []
    for i in range(1,lenrow):
        min_val = min(x for x in files[i][2:] if isinstance(x, float))
        min_list.append(min_val)
    return min_list

#comp_median used to find median in the each list of file and append to a new list
def comp_median(files):
    median_list = []
    for i in files[1:]:
        sorted_values = sorted(x for x in i[2:] if x != None)
        len_files = len(sorted_values)
        if len_files % 2 == 0:
            first_value = sorted_values[len_files // 2]
            second_value = sorted_values[(len_files // 2) - 1]
            median = (first_value+second_value) / 2
            median_list.append(median)
        else:
            median_value = sorted_values[len_files // 2]
            median_list.append(median_value)
    #print (median_list)
    return median_list

#comp_mean used to find mean in the each list of file and append to a new list
def comp_mean(files):

    mean_list = []
    for i in files[1:]:
        meanval = (x for x in i[2:] if x != None)
        counter = i[2:].count(None)
        finavalue = 2 + counter
        n = len(i) - finavalue
        mean_list1 = sum(meanval) / n
        mean_list.append(mean_list1)
    return mean_list

#comp_harmonic used to find harmonic mean in the each list of file and append to a new list
def comp_harmonic(files):

    harmonic_list = []
    for i in files[1:]:
        harmonic_value = ((1 / x) for x in i[2:] if (x != None and x != 0))
        # counter used as n(used to measure the length of the file where x should be not equal to none and 0)
        counter = (1 for x in i[2:] if x != None and x != 0)
        mean_list1 = sum(counter) / sum(harmonic_value)#harmonic_meaN formula
        harmonic_list.append(mean_list1)
    return harmonic_list

#order_list is used to sort the values with their respective country name
def order_list(files, values, ops):
    print("Ranked list of countries' happiness scores based the "+ ops + " metric")
    idx = sorted(range(len(values)), key=lambda k: values[k], reverse=True)#reverse function is used sort from desending order
    for k in range(len(idx)):
        idx[k] = idx[k] + 1
    name_list = []
    value_list = sorted(values, reverse=True)#values are sorted
    for i in range(len(idx)):
        name_list.append(files[idx[i]][0])#country names are arranged according to their sorted values
    for j in range(len(values)):
        print(name_list[j], '{0:.4f}'.format(value_list[j]))

#correlation_list used t find the correlation for the given value
def correlation_list(files, values, ops):
    lenrow=len(files)
    lencolumn=len(files[0])
    life_ladder = []
    for i in range(1,lenrow):
        life_ladder.append(files[i][1])
    idx1 = sorted(range(len(values)), key=lambda k: values[k], reverse=True)#idx1 is index for values
    idx2 = sorted(range(len(life_ladder)), key=lambda k: life_ladder[k], reverse=True)#idx12 is index for life_ladder
    d_square = []
    for j in range(len(idx1)):
        d_square.append((idx1[j]-idx2[j])**2)
    #sum_d_squar = statistics.mean(x for x in d_square) * len(idx1)
    sum_d_squar = (sum(x for x in d_square) * len(idx1)/len(idx1))#correlation formula
    sp_rank = 1 - (6*sum_d_squar) / (len(idx1) * ((len(idx1) * len(idx1))-1))
    print('The correlation coefficient between the study ranking and the ranking using the ' + ops + ' metric is {0:.4f}'.format(sp_rank))
    return sp_rank

#main function for computing world happiness index
def main():
    filename = input("Enter name of file containing World Happiness computation data: \n")#geeting input file from user
    input_file = read_file(filename)    #read the file
    float_file = float_conversion(input_file)   #convert string values into float
    min_v, max_v = min_max(float_file)  #finding minimum and maximun from the files
    files = normalize(float_file, min_v, max_v) #normalise the values between 0 to 1
    # ops options for min,mean,median and harmonic mean
    ops = input("Choose metric to be tested from:min, mean, median, harmonic_mean ")
    if ops == 'min':
        values = comp_min(files)
    elif ops == 'mean':
        values = comp_mean(files)
    elif ops == 'median':
        values = comp_median(files)
    elif ops == 'harmonic_mean':
        values = comp_harmonic(files)
    else:
        print('No this option!')
    #choice is option for list and correlation
    choice = input("Choose action to be performed on the data using the specific metric. Options are list, correlation ")
    if choice == 'list':
        order_list(files, values, ops)
    elif choice == 'correlation':
        correlation_list(files, values, ops)
    else:
        print('No this ranking option! ')

#main()
