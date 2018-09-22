# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:38:02 2018

@author: Lynn Dai
"""

"""
PROJECT 2 - Recursion
Name:
PID:
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """
    Insert the given value into the linked list that has head node
    :param value: value to insert
    :param node: head node for the the remaining list
    :return: head node
    """
    if node:
        if node.value >= value:
            node = LinkedNode(value, node)
        elif node.next_node:
            if node.next_node.value >= value:
                tmp = LinkedNode(value, node.next_node)
                node.next_node = tmp
            else:
                # Recursively find the nodes that meet the criteria
                insert(value, node.next_node)
        else:
            tmp = LinkedNode(value, None)
            node.next_node = tmp
    else:
        node = LinkedNode(value, None)
        return node
    return node


def string(node):
    """
    Generate and return a string representation of the list, starting at node
    :param node: head node for the the remaining list
    :return: string of all nodes
    """
    if node:
        if node.next_node:
            tmp_words = string(node.next_node)
            # Composite string
            return str(node.value) + ', ' + tmp_words
        else:
            return str(node.value)
    else:
        return ''


def reversed_string(node):
    """
    Generate and return a string representation of the list with head node, in reverse order
    :param node: head node for the the remaining list
    :return: string of all nodes in reverse order
    """
    if node:
        if node.next_node:
            tmp_words = reversed_string(node.next_node)
            # Composite string
            return tmp_words + ', ' + str(node.value)
        else:
            return str(node.value)
    else:
        return ''


def remove(value, node):
    """
    Remove the first node in the list with the given value starting at head node
    :param value:
    :param node: head node for the the remaining list
    :return: head node
    """
    if node:
        if node.value == value:
            if node.next_node:
                node.value = node.next_node.value
                node.next_node = node.next_node.next_node
            else:
                return None
        elif node.next_node:
            if node.next_node.value == value:
                node.next_node = node.next_node.next_node
            else:
                # Recursively find the value to delete
                remove(value, node.next_node)
        return node
    else:
        return None


def remove_all(value, node):
    """
    Remove all nodes in the list with the given value starting at head node
    :param value:
    :param node: head node for the the remaining list
    :return: head node
    """
    if node:
        if node.value == value:
            if node.next_node:
                node.value = node.next_node.value
                node.next_node = node.next_node.next_node
                remove_all(value, node)
                if node.next_node:
                    remove_all(value, node.next_node)
            else:
                return None
        elif node.next_node:
            if node.next_node.value == value:
                if node.next_node.next_node:
                    node.next_node = node.next_node.next_node
                else:
                    node.next_node = None
                # Recursively the remained nodes to find the value to delete
                remove_all(value, node)
            # Recursively the remained nodes to find the value to delete
            remove_all(value, node.next_node)
        return node
    return None


def search(value, node):
    """
    Looks for value in list starting with head node
    :param value:
    :param node: head node for the the remaining list
    :return: Return True if have the value in LinkList or return False
    """
    if node:
        if node.value == value:
            return True
        else:
            # Recursively look for the remaining nodes and find the matching nodes
            return search(value, node.next_node)
    else:
        return False


def length(node):
    """
    Calculates and returns the length of the list starting with head node
    :param node: head node for the the remaining list
    :return: The length of the LinkList
    """
    if node:
        # The length is computed recursively and each new node is incremented by 1
        return length(node.next_node) + 1
    else:
        return 0


def sum_all(node):
    """
    Calculates and returns the sum of the list starting with head node
    :param node: head node for the the remaining list
    :return: The sum value
    """
    if node:
        # The value is computed recursively and each new node is incremented by its value
        return sum_all(node.next_node) + node.value
    else:
        return 0


def count(value, node):
    """
    Counts how many times the given value occurs in the list starting at head node
    :param value:
    :param node: head node for the the remaining list
    :return: the number of nodes who's value is the value searched
    """
    if node:
        if node.value == value:
            # add 1 if the node is needed
            return count(value, node.next_node) + 1
        else:
            # Recurse to the next node
            return count(value, node.next_node)
    else:
        return 0


# a = LinkedNode(1, None)
#
# print(string(a))
# l = remove(1, a)
# print(string(l))
