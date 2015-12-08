import imageio
import numpy as np
from scipy.sparse import *
from sklearn.cluster import KMeans

im = imageio.imread("emily.jpeg")
n, m, _ = im.shape
X = [im[i][j] for i in range(n) for j in range(m)]
X = csr_matrix(np.array(X))
for k in range(3, 10):
    print k,
    labeler = KMeans(k)
    labeler.fit(X)
    for i in range(n):
        for j in range(m):
            im[i][j] = labeler.cluster_centers_[labeler.labels_[i*m+j]]
    imageio.imsave('emily' + str(k) + '.jpeg', im)