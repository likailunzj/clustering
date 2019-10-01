
import pytest

from clustering import kmeans


def clustered_all_points(clustering, dataset):
    points = []
    for assignment in clustering:
        points += clustering[assignment]
    for point in points:
        if point not in dataset:
            return False
    return True


@pytest.mark.parametrize('dataset', [
    ("tests/test_files/dataset_1.csv"),
])
def test_kmeans_when_k_is_1(dataset):
    expected_clustering = kmeans.get_list_from_dataset_file(dataset)
    clustering = kmeans.k_means(dataset_file=dataset, k=1)

    assert len(clustering.keys()) == 1
    assert clustered_all_points(clustering, kmeans.get_list_from_dataset_file(dataset)) is True

    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering]
   # return clustered == [expected_clustering]

@pytest.mark.parametrize('dataset,expected1,expected2', [
    ("tests/test_files/dataset_1.csv",
     "tests/test_files/dataset_1_k_is_2_0.csv",
     "tests/test_files/dataset_1_k_is_2_1.csv"),
])
def test_kmeans_when_k_is_2(dataset, expected1, expected2):
    expected_clustering1 = kmeans.get_list_from_dataset_file(expected1)
    expected_clustering2 = kmeans.get_list_from_dataset_file(expected2)
    clustering = kmeans.k_means(dataset_file=dataset, k=2)
    cost = kmeans.cost_function(clustering)

    for _ in range(2000):
        new_clustering = kmeans.k_means(dataset_file=dataset, k=2)
        new_cost = kmeans.cost_function(clustering)
        if new_cost < cost:
            clustering = new_clustering
            cost = new_cost

    assert len(clustering.keys()) == 2
    assert clustered_all_points(clustering, kmeans.get_list_from_dataset_file(dataset)) is True
    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering1, expected_clustering2]
    #return clustered == [expected_clustering1, expected_clustering2]

@pytest.mark.parametrize('dataset,expected1,expected2,expected3', [
    ("tests/test_files/dataset_1.csv",
     "tests/test_files/dataset_1_k_is_3_0.csv",
     "tests/test_files/dataset_1_k_is_3_1.csv",
     "tests/test_files/dataset_1_k_is_3_2.csv"),
])
def test_kmeans_when_k_is_3(dataset, expected1, expected2, expected3):
    expected_clustering1 = kmeans.get_list_from_dataset_file(expected1)
    expected_clustering2 = kmeans.get_list_from_dataset_file(expected2)
    expected_clustering3 = kmeans.get_list_from_dataset_file(expected3)
    clustering = kmeans.k_means(dataset_file=dataset, k=3)
    cost = kmeans.cost_function(clustering)

    for _ in range(2000):
        new_clustering = kmeans.k_means(dataset_file=dataset, k=3)
        new_cost = kmeans.cost_function(clustering)
        if new_cost < cost:
            clustering = new_clustering
            cost = new_cost

    assert len(clustering.keys()) == 3
    assert clustered_all_points(clustering, kmeans.get_list_from_dataset_file(dataset)) is True

    clustered = []
    for assignment in clustering:
        clustered.append(clustering[assignment])
    assert clustered == [expected_clustering1, expected_clustering2, expected_clustering3]
    #return clustered == [expected_clustering1, expected_clustering2, expected_clustering3]
# a = "/Users/AaronLee/clustering/tests/test_files/dataset_1.csv"
# b = "/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_3_0.csv"
# c = "/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_3_1.csv"
# d = "/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_3_2.csv"
# x = test_kmeans_when_k_is_3(a,b,c,d)
#
# a1 = "/Users/AaronLee/clustering/tests/test_files/dataset_1.csv"
# b1 = "/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_2_0.csv"
# c1 = "/Users/AaronLee/clustering/tests/test_files/dataset_1_k_is_2_1.csv"
# x1 = test_kmeans_when_k_is_2(a1,b1,c1)
#
# a2 = "/Users/AaronLee/clustering/tests/test_files/dataset_1.csv"
# x2 = test_kmeans_when_k_is_1(a2)