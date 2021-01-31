import numpy as np
import utils
from task2a import pre_process_images
np.random.seed(1)


if __name__ == "__main__":
    w = np.ones((785, 10))
    w = np.sum(w,axis = 1)
    print(w[0])
    print(w.shape)
    w.reshape(1)
    print(w.shape)