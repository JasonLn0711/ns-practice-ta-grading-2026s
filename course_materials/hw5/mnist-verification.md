# MNIST Verification

Source inspected: `/home/jnclaw/Downloads/TA-deep-learning/data/mnist/`

These files are MNIST IDX gzip files. The `t10k-*` pair is the MNIST test set,
not an additional training split.

| Original file | Working copy | IDX meaning | Count | Shape | MD5 |
| --- | --- | --- | ---: | --- | --- |
| `train-labels-idx1-ubyte.gz` | `renamed/mnist/hw5_reference_mnist_train-labels-idx1-ubyte.gz` | training labels | 60000 | labels | `d53e105ee54ea40749a09fcbcd1e9432` |
| `train-images-idx3-ubyte.gz` | `renamed/mnist/hw5_reference_mnist_train-images-idx3-ubyte.gz` | training images | 60000 | 28x28 | `f68b3c2dcbeaaa9fbdd348bbdeb94873` |
| `t10k-labels-idx1-ubyte.gz` | `renamed/mnist/hw5_reference_mnist_test-labels-idx1-ubyte.gz` | test labels | 10000 | labels | `ec29112dd5afa0611ce80d1b7f02629c` |
| `t10k-images-idx3-ubyte.gz` | `renamed/mnist/hw5_reference_mnist_test-images-idx3-ubyte.gz` | test images | 10000 | 28x28 | `9fb629c4189551a2d022fa330f9573f3` |
| `readme.txt` | `renamed/mnist/hw5_reference_mnist_readme.txt` | dataset note | n/a | n/a | n/a |

Verification commands used:

```bash
file /home/jnclaw/Downloads/TA-deep-learning/data/mnist/*.gz
md5sum /home/jnclaw/Downloads/TA-deep-learning/data/mnist/*.gz
```

IDX header checks:

- Label files have magic number `2049`.
- Image files have magic number `2051`.
- Image dimensions are `28x28`.
