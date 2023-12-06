Laboration 3
Due 2023-12-14
The purpose of this assignment is to empirically study the time complexity of the following
search tree.
• Data Structure D
— D is a binary search tree.
— For every node v in the tree D,
∗ the size of v  ́s left subtree is at most c× (the size of the subtree rooted at v),
and
∗ the size of v  ́s right subtree is at most c× (the size of the subtree rooted at v),
where c, 1
2 < c < 1, is a constant.
— An insert operation on D is performed just as in a standard binary search tree. For
all the nodes x on the search path, if
∗ either the size of x  ́s left subtree > c× (the size of the subtree rooted at x)
∗ or the size of x  ́s right subtree > c× (the size of the subtree rooted at x)
then the subtree rooted at x is replaced by a perfect balanced binary search tree
containing the same keys.
• Implementation and experiment
— Implement such a data structure and an insert operation on it.
— Conduct simulation experiments with a series of insertions on the data structure and
the standard binary search tree (considering different types of inputs and different
values of c).
• Report
Each group must turn in a report describing your implementation and illustrating experi-
mental results. The report can be written in either Swedish or English and should not be
handwritten.
Before submitting your report, you should discuss your solution to the laboration (design,
implementation, and report) with your lab-assistant.
