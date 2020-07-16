from sklearn.datasets import load_digits
from sklearn.preprocessing import normalize, robust_scale, scale
from sklearn.cluster import KMeans
from numpy import reshape, transpose
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
digits = load_digits()

#(b)
#print(digits.DESCR)
digits_normalized = normalize(digits.data)
kmeans = KMeans(10,n_init=20)
kmeans.fit(digits_normalized)
# print(kmeans.inertia_)
# errotable =[]
# for i in range (1,21):
#     kmeans = KMeans(i,n_init=20)
#     kmeans.fit(digits_normalized)
#     errotable.append(kmeans.inertia_)
# plt.plot(errotable)
# plt.gray()
# kmeans = KMeans(10,n_init=20)
# kmeans.fit(digits_normalized)
# for i in range(0,10):
#     plt.matshow(reshape(kmeans.cluster_centers_[i],(8,8)))
pca = PCA(n_components=2)

print(digits_normalized)
print("VVVVVV",digits_normalized.shape)
transposed = transpose(digits_normalized)
print("GGGGG",transposed.shape)
print(transposed)
pca.fit(transposed)
print(pca.components_)
print("GGGGG",pca.components_.shape)
transposed = transpose(pca.components_)
print(transposed)

# plt.gray()
# plt.matshow(reshape(pca.components_[0], (8,8)))
# plt.matshow(reshape(pca.components_[1], (8,8)))
plt.show()
