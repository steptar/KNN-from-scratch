import unittest

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

from knn import knn_wrap
from knn import get_euclidean_distance
from knn import get_sorted_list
from knn import predict
from knn import tie_breaker
from knn import k_selection


class TestKNNWrap(unittest.TestCase):
    df1 = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [.5, 0, .5]])
    df2 = pd.DataFrame([[-1, 0, 5], [1, 2, -1], [.5, 0, 8]])

    def test_smoke(self):
        # smoke test
        df1 = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [.5, 0, .5]])
        df2 = pd.DataFrame([[-1, 0, 5], [1, 2, -1], [.5, 0, 8]])
        knn_wrap(df1, 5, df2)

    # test for correct inputs
    def test_type1(self):
        df1 = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [.5, 0, .5]])
        with self.assertRaises(TypeError):
            knn_wrap(np.array([1, 2]), 5, df1)

    def test_type2(self):
        df1 = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [.5, 0, .5]])
        df2 = pd.DataFrame([[-1, 0, 5], [1, 2, -1], [.5, 0, 8]])
        with self.assertRaises(TypeError):
            knn_wrap(df2, 'ten', df1)

    def test_type3(self):
        df1 = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [.5, 0, .5]])
        df2 = pd.DataFrame([[-1, 0, 5], [1, 2, -1], [.5, 0, 8]])
        with self.assertRaises(TypeError):
            knn_wrap(df2, 'ten', df1)


class TestGetEuclideanDistance(unittest.TestCase):

    def test_distance_calc(self):
        # test that the calculation is accurate
        u = pd.DataFrame(data=(2, 3, 4, 2))
        v = np.array((1, -2, 1, 3))
        with self.assertRaises(ValueError):
            get_euclidean_distance(u, v)
            return 6


class TestGetSortedList(unittest.TestCase):

    def test_inputs(self):
        # test that inputs are of the correct size
        x_test_row = pd.DataFrame(data=(2, 3, 4, 2))
        X_train = pd.DataFrame([[-1, 0, 4], [1, 0, -1], [9, 0, 1]])
        y_train = pd.DataFrame([[-1, 0, 8]])

        with self.assertRaises(ValueError):
            get_sorted_list(x_test_row, X_train, y_train, 5)


class TestPredict(unittest.TestCase):

    def test_x_test_input(self):
        # test that the dataframe has the indexes of y_train
        knn_list = pd.DataFrame(data=(2, 3, 4))
        y_train = pd.DataFrame([[-1, 0, 3]])

        with self.assertRaises(ValueError):
            predict(knn_list, y_train)


class TestTieBreaker(unittest.TestCase):

    def test_num_modes(self):
        # test that knn_list returns an error if only one mode exists
        knn_list = pd.DataFrame(data={'distance': [20, 21, 19, 18],
                                      'y_train': [20, 20, 19, 18]})

        with self.assertRaises(ValueError):
            tie_breaker(knn_list)


class TestKSelection(unittest.TestCase):

    def test_k_types(self):
        # test that k list contains only integers
        k_list = [2, 3, 4, 5, 'R', 7]
        df_train = pd.DataFrame(data={'random': [20, 21, 19, 18]})
        df_test = pd.DataFrame(data={'random': [20, 20, 19, 18]})

        with self.assertRaises(TypeError):
            k_selection(df_train, df_test, k_list)
