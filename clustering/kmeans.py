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
    dimi = len(points[0])
    total_num = len(points)
    new_center = []
    for dim in range(dimi):
        sum_of_this_dim = 0
        for pt in points:
            sum_of_this_dim += pt[dim]
        ave = sum_of_this_dim/total_num
        new_center.append(ave)
    return new_center



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


def assign_points(data_points, centers):
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


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # shuffled = random.shuffle(data_set, random.random)
    # return shuffled[:k]
    return random.choices(data_set, k = k)



def get_list_from_dataset_file(dataset_file):
    data_list = []
    with open(dataset_file) as csv:
        for line in csv:
            indivi_data = [int(line[0]),int(line[1])]
            data_list.append(indivi_data)
    return data_list


def cost_function(clustering):
    raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments, k)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering

#result = k_means("/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_2_1.csv", 2)