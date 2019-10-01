from collections import defaultdict
from math import inf
import random
import csv
import math

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    total = []
    for minor_sum in zip(*points):
        total.append(sum(minor_sum))

    for ele in range(len(total)):
        total[ele] = total[ele]/len(points)
    return total



def update_centers(data_set, assignments, k):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    new_center_list = []
    for cluster_num in range(k):
        list_based_on_labels = []
        for label_index in range(len(assignments)):
            if assignments[label_index] == cluster_num:
                list_based_on_labels.append(data_set[label_index])
        new_center_list.append(point_avg(list_based_on_labels))
    return new_center_list


def assign_points(data_points, centers):  #np
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):  #np
    """
    Returns the Euclidean distance between a and b
    """
    if b == []:
        return 1000000
    else:
        return math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))


def generate_k(data_set, k):  #np
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # shuffled = random.shuffle(data_set, random.random)
    # return shuffled[:k]
    return random.choices(data_set, k = k)



def get_list_from_dataset_file(dataset_file):  # np
    data_list = []
    with open(dataset_file) as csv:
        for line in csv:
            line = line.strip().split(",")
            indivi_data = [float(line[0]),float(line[1])]
            data_list.append(indivi_data)
    return data_list


def cost_function(clustering):
    # total_cost = 0
    # index = 0
    # for centers in clustering:
    #     for data_point in clustering[centers]:
    #         total_cost += distance(data_point, new_c[index])
    #     index = index + 1
    # return total_cost
    total_cost = 0
    for cluster_num in clustering.keys():
        datas = clustering[cluster_num]
        centers = point_avg(datas)
        for indiv_data in datas:
            total_cost += distance(indiv_data, centers)
    return total_cost


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    new_centers = []
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments, k)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering, new_centers


