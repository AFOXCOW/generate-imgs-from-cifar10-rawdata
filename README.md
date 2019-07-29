# purpose
generate 32*32*3 images from cifar-10 raw data include train and test set
# cifar-10 raw data python
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# usage
python make_cifar10.py -h  to see the help
# demo
python make_cifar10.py -r -d "/home/cifar_10/cifar-10-python/cifar-10-batches-py"
# folder arch
.
└── cifar-10-batches-py
    ├── batches.meta
    ├── data_batch_1
    ├── data_batch_2
    ├── data_batch_3
    ├── data_batch_4
    ├── data_batch_5
    ├── readme.html
    └── test_batch
