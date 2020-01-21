# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:44:32 2020

@author: Srivatsan
"""

import numpy as np
import h5py
    
    
def load_dataset():
    train_dataset = h5py.File('data.he5', "r")
    train_set_x_orig = np.array(train_dataset['train_dataset'][:]) # your train set features
    train_set_y_orig = np.array(train_dataset['train_dataset][:]) # your train set labels

    test_dataset = h5py.File('data.he5', "r")
    test_set_x_orig = np.array(test_dataset['test_dataset'][:]) # your test set features
    test_set_y_orig = np.array(test_dataset['test_dataset'][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
