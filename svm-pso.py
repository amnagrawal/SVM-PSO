# coding: utf-8

# In[1]:

import random
import sys
import numpy as np
import copy
import arff
from sklearn.decomposition import PCA
from sklearn.preprocessing import Imputer
from sklearn import svm
from sklearn.model_selection import KFold
import os.path
import pickle
import json
from tqdm import trange
from matplotlib import pyplot as plt

# get_ipython().magic(u'matplotlib inline')
from mpl_toolkits.mplot3d import Axes3D


# In[2]:

# Preprocessing data
def process_data(data):
    imp = Imputer(missing_values='NaN', strategy='mean', axis=1)
    data = imp.fit_transform(data)
    data = (data - np.mean(data, 0)) / np.std(data, 0)  # normalazing data
    pca = PCA(n_components=4)
    data_reduced = pca.fit_transform(data)
    # 	print(pca.explained_variance_ratio_)
    # 	print(data)
    return data_reduced, pca.explained_variance_ratio_


# In[3]:

# Load data
fil = arff.load(open('data/jm1a.arff', 'rb'))
data = np.array(fil['data'])
print("Loading data...")
data = np.array(random.sample(data, 500))
result = data[:, -1]
data = data[:, 0:21]
data, ratios = process_data(data)

faulty = 0
for i in result:
    if i == 'true':
        faulty += 1

while (np.sum(ratios) < 0.94) or ((faulty < 80) or (faulty > 100)):
    data = np.array(fil['data'])
    data = np.array(random.sample(data, 500))
    result = data[:, -1]
    data = data[:, 0:21]
    data, ratios = process_data(data)

    faulty = 0
    for i in result:
        if i == 'true':
            faulty += 1

print(ratios, np.sum(ratios))
print(faulty, np.mean(data, 0))


# In[4]:

def trainSVM(C, gamma, index):
    clf = svm.SVC(C=C, gamma=gamma)
    kf = KFold(len(data), n_folds=10, shuffle=True)
    means = []
    for training, testing in kf:
        clf.fit(data[training], result[training])
    prediction = clf.predict(data[testing])
    curmean = np.mean(prediction == result[testing])
    means.append(curmean)

    accuracy = np.mean(means)
    # 	print("\tMean accuracy of particle {}: {:.1%}".format(index, accuracy))
    return accuracy


# In[5]:

# PSO variables
NO_OF_INPUTS = 2
V_MAX = 180
V_MIN = -180
MAX_PARTICLES = 40
MAX_EPOCHS = 100
MAX_RANGE_C = 1000
MIN_RANGE_C = 50
MAX_RANGE_GAMMA = 100
MIN_RANGE_GAMMA = 0.001
W = 0.5
c1 = 1.5
c2 = 1.7


# In[6]:

class Particle:
    def __init__(self):
        self.params = [0] * NO_OF_INPUTS
        self.pBest = [0] * NO_OF_INPUTS
        self.velocity = [0] * NO_OF_INPUTS
        self.bestVal = 0

    def get_params(self):
        return self.params

    def set_params(self, value):
        self.params = value

    def get_pBest(self):
        return self.pBest

    def set_pBest(self, value):
        self.pBest = value

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, value):
        self.velocity = value

    def get_bestVal(self):
        return self.bestVal

    def set_bestVal(self, value):
        self.bestVal = value


# In[7]:

def initialize_particles():
    random.seed()
    particles = []
    for i in trange(MAX_PARTICLES):
        newParticle = Particle()
    params = []
    C = np.random.uniform(MIN_RANGE_C, MAX_RANGE_C)
    gamma = np.random.uniform(MIN_RANGE_GAMMA, MAX_RANGE_GAMMA)
    params.append(C), params.append(gamma)
    newParticle.set_params(params)
    newParticle.set_pBest(params)
    newParticle.set_bestVal(trainSVM(C=C, gamma=gamma, index=i))
    particles.append(copy.deepcopy(newParticle))
    return particles


# In[8]:

def max_fitness(particles):
    best = 0
    for i in range(MAX_PARTICLES):
        if particles[i].get_bestVal() > particles[best].get_bestVal():
            best = i

    return best


# In[9]:

def calc_velocity(gBestIndex, particles):
    gBest = particles[gBestIndex].get_bestVal()
    for i in range(MAX_PARTICLES):
        velocity = np.multiply(W, particles[i].get_velocity()) + np.multiply(c1 * np.random.uniform(),
                                                                             np.subtract(particles[i].get_pBest(),
                                                                                         particles[i].get_params()))
    velocity = velocity + np.multiply(c2 * np.random.uniform(),
                                      np.subtract(particles[gBestIndex].get_params(), particles[i].get_params()))

    if velocity[0] > V_MAX:
        velocity[0] = V_MAX
    elif velocity[0] < V_MIN:
        velocity[0] = V_MIN

    particles[i].set_velocity(velocity)

    return particles


# In[10]:

def update_particles(gBestIndex, particles):
    random.seed()
    for i in trange(MAX_PARTICLES):
        params = particles[i].get_params()
    temp = particles[gBestIndex].get_params()
    vel = particles[i].get_velocity()
    for y in range(len(params)):
        if params[y] != temp[y]:
            params[y] += vel[y]

    if params[0] < 0:
        params[0] = np.random.uniform(MIN_RANGE_C, 20 * (MAX_RANGE_C - MIN_RANGE_C) / 100)

    if params[1] < 0:
        params[1] = np.random.uniform(MIN_RANGE_GAMMA, 20 * (MAX_RANGE_GAMMA - MIN_RANGE_GAMMA) / 100)

    acc = trainSVM(params[0], params[1], index=i)
    if acc > particles[i].get_bestVal():
        particles[i].set_pBest(params)
        particles[i].set_bestVal(acc)
    return particles


# In[11]:

def PSO_algo():
    epoch = 1
    particles = []
    result = []

    random.seed(10)

    if (os.path.isfile('PARTICLES.pk1')):
        with open('PARTICLES.pk1', 'r') as ip:
            particles = pickle.load(ip)
    else:
        print("Initializing particles:")
    sys.stdout.flush()
    particles = initialize_particles()

    with open('PARTICLES.pk1', 'w') as op:
        pickle.dump(particles, op, pickle.HIGHEST_PROTOCOL)

    if (os.path.isfile('save_pso_svm.json')):
        with open('save_pso_svm.json', 'r') as ip:
            open_data = json.load(ip)
            epoch = open_data['epoch']

    while epoch <= MAX_EPOCHS:
        gBest = max_fitness(particles)

    sys.stdout.flush()
    print("\nEpoch: " + str(epoch))
    sys.stdout.flush()

    particles = calc_velocity(gBest, particles)
    particles = update_particles(gBest, particles)

    sys.stdout.flush()
    print("\tMax accuracy achieved: {:.1%}".format(particles[gBest].get_bestVal()))
    print("\tC={:.10}, gamma={:.10}".format(particles[gBest].get_params()[0], particles[gBest].get_params()[1]))

    with open('PARTICLES.pk1', 'w') as op:
        pickle.dump(particles, op, pickle.HIGHEST_PROTOCOL)

    gBest = max_fitness(particles)
    # print("Best in epoch " + str(epoch) +": " + str(particles[gBest].get_data()))
    epoch += 1

    save_data = {}
    save_data['epoch'] = epoch
    save_data['C'] = particles[gBest].get_params()[0]
    save_data['gamma'] = particles[gBest].get_params()[1]
    save_data['accuracy'] = particles[gBest].get_bestVal()
    with open('save_pso_svm.json', 'w') as fp:
        json.dump(save_data, fp, sort_keys=True, indent=4)

    gBest = max_fitness(particles)
    return particles[gBest].get_params()[0], particles[gBest].get_params()[1]


# In[30]:

C, gamma = PSO_algo()
