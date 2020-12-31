
**Introduction** 

Among  the  set  of  search  and  optimization  techniques,  the  development  of  Evolutionary Algorithms has been very important in the last decade. These algorithms are a set of modern meta  heuristics used successfully in many applications with great complexity. Its success in solving difficult problems has been the engine of a field known as Evolutionary Computation. 

Benefits  using  such  techniques  mostly  come  from  flexibility  gains  and  their  fitness  to  the objective target in combination with a robust behavior. Nowadays, Evolutionary Computation is considered an adaptable concept for problems, specially complex optimization problems. 

Evolutionary algorithms (EAs) are inspired by the biological model of evolution and natural selection first proposed by Charles Darwin in 1859. Species change over the course of many generations. Mutations occur randomly. Some mutations will be advantageous, but many will be useless  or  detrimental.  Progress  comes  from  the  feedback  provided  by  non-random  natural selection. If a random genetic modification helps an organism to survive and to reproduce, that modification  will  itself  survive  and  spread  throughout  the  population,  via  the  organism's offspring. 

Evolutionary algorithms are based on a simplified model of this biological evolution. To solve a particular  problem  we  create  an  environment  in  which  potential  solutions  can  evolve.  The environment is shaped by the parameters of the problem and encourages the evolution of good solutions.  



**Outline of Evolutionary Algorithms** 

In  an  Evolutionary  Algorithm,  a number of artificial creatures search over the space of the problem.  They  compete  continually with each other to discover optimal areas of the search space. It is hoped that over time the most successful of these creatures will evolve to discover the optimal solution. 

The artificial creatures, known as individuals, are typically represented by fixed length strings or vectors. Each individual encodes a single possible solution to the problem under consideration. 

The basic Algorithm behind the working of such algorithms is:  

1. **Genesis:** Create an initial set (population) of n candidate solutions. This may be done entirely randomly. 

1. **Evaluation:** Evaluate each member of the population using some fitness function. 

1. **Survival  of  the  Fittest:**  Select  a  number  of  members  of  the  evaluated  population, favouring  those  with  higher  fitness  scores.  These  will  be  the  parents  of  the  next generation. 

1. **Evolution:** The evolution is performed by one or more evolutionary operators. Hence a new offspring generation is created, using the parents found in step 3, which has the best properties of the previous generations in addition to some mutation which may or may not be beneficial. 

1. **Iteration:**  Repeat  steps  2-4  until  a  satisfactory  solution  is  found  or  some  other termination condition is met (such as the number of generations or elapsed time). 

   

**Working of Evolutionary Algorithms**

Evolutionary Algorithms have some rather general properties concerning their working. To illuminate how an EA typically works we assume a one dimensional objective function to be maximised. 

![](SVM-PSO.001.png)Above figure shows three stages of the evolutionary search, exhibiting how the individuals are distributed in the beginning, somewhere halfway and at the end of the evolution. Directly after initialisation, the individuals are randomly spread over the whole search space. After a few generations this distribution changes: caused by selection and variation operators the population abandons low fitness regions and starts to climb" the hills. Close to the end of the search, the whole population is concentrated around a few peaks, where some of these peaks can be suboptimal. In principle it is possible that the population climbs the wrong hill" and all individuals are positioned around a local, but not global optimum. 

Another property worth noticing is “anytime behaviour”. We show this by plotting the development of the population's best value with time**.**  

![](SVM-PSO.002.png)

This curve is characteristic for Evolutionary Algorithms, showing rapid progress in the beginning and flattening out later on. Based on this anytime curve we can make some general observations concerning initialisation and the termination condition for Evolutionary Algorithms. 

- In general, it could be said that the typical progress curve of an evolutionary process makes it unnecessary to put extra computational efforts into applying some intelligent heuristics to seed the initial populations with better than random individuals. 
- As the figure indicates, the progress in terms of fitness increase in the first half of the run, is significantly greater than the second half. This suggests that it might 

not be worth allowing very long runs, since efforts spent after a certain time may not result in better solution quality.



**How are Evolutionary Algorithms Useful?**

Evolutionary algorithms are typically used to provide good approximate solutions to problems that cannot be solved easily using other techniques. Many optimisation problems fall into this category. It may be too computationally-intensive to find an exact solution but sometimes a near-optimal solution is sufficient. In these situations evolutionary techniques can be effective. Due to their random nature, evolutionary algorithms are never guaranteed to find an optimal solution for any problem, but they will often find a good solution if one exists. 

Evolutionary algorithms can also be used to tackle problems that humans don't really know how to  solve.  Being  free  from  any  human  preconceptions  or  biases,  it  can  generate  surprising solutions that are comparable to, or better than, the best human-generated efforts. It is merely necessary that we can recognise a good solution if it were presented to us, even if we don't know *how* to create a good solution. 

For  example,  NASA's  Evolvable  Systems  Group  has  used  evolutionary  algorithms  to successfully evolve antennas for use on satellites. These evolved antennas have irregular shapes with no obvious symmetry (one of these antennas is pictured below). It is unlikely that a human expert would have arrived at such an unconventional design. Despite this, when tested these antennas proved to be extremely well adapted to their purpose. 

![](SVM-PSO.003.png)



**Genetic Algorithm**

Genetic Algorithms (GAs) are adaptive heuristic search algorithms based on the evolutionary ideas of natural selection and genetics. They represent an intelligent application of a random search  used  to  solve  optimization  problems. Although they are randomised, GAs are by no means random, instead they exploit historical information to direct the search into the region of better performance within the search space. The basic techniques of the GAs are designed to simulate processes in natural systems necessary for evolution, especially following the principles first laid down by Charles Darwin of "survival of the fittest.". 

Since  in  nature,  competition  among  individuals  for  scanty  resources  results  in  the  fittest individuals dominating over the weaker ones. GAs simulate the survival of the fittest among individuals over consecutive generations for solving a problem. Each generation consists of a population of character strings that are analogous to the chromosome that we see in our DNA. Each individual represents a point in a search space and a possible solution. The individuals in the population are then made to go through a process of evolution. 

A fitness score is assigned to each solution representing the abilities of an individual to compete. Parents are selected to mate, on the basis of their fitness, producing offspring. Consequently highly  fit  solutions  are  given  more  opportunities  to  reproduce,  so  that  offspring  inherit characteristics  from  each  parent.  As  parents  mate  and  produce offspring, individuals in the population die and are replaced by the new solutions, eventually creating a new generation once all mating opportunities in the old population have been exhausted. In this way it is hoped that over successive generations better solutions will thrive while the least fit solutions die out. 



**Implementation of Genetic Algorithm**

The most common type of genetic algorithm works like this: 

1. **Initialization:** A population is created with a group of individuals created randomly. The individuals in the population are then evaluated. The evaluation function is provided by the programmer and gives the individuals a score based on how well they perform at the given task. 

2. **Selection:** A selection operator is defined, which gives preference to better individuals, allowing  them  to  pass  on  their  genes  to  the  next  generation.  The  goodness  of  an individual is determined from its fitness. Fitness may be defined by an objective function or subjective judgement. There are several types of selection operator such as: 

3. **Roulette wheel selection**: In this method, selection is made directly on the basis of the fitness of an individual. The higher the fitness the better the chances are of being selected. 

4. **Tournament selection:** In this method, the best individual of a randomly chosen subset is selected, and this process is carried out multiple times 

5. **Truncation  selection:**  Taking  the  best  half  ,  third,  etc  of  the  population  is truncation selection. 

6. **Crossover:** This operator is used to alter the features from one generation to the next. The individuals selected in step 2, are given to the crossover operator to produce the offsprings  of  the  next  generation.  There  are  different  types  of  crossover  techniques available: 

7. **Single  point  crossover:**  A  single  crossover  point  on  both  parents'  organism strings is selected. All data beyond that point in either organism string is swapped between the two parent organisms. The resulting organisms are the children. For example, 

   ​	**11001**011+11011**111** = **11001111** 

8. **Two point crossover:** Two-point crossover calls for two points to be selected on the  parent  organism  strings.  Everything  between  the  two  points  is  swapped between the parent organisms, rendering two child organisms: For example, 

   ​	**11**0010**11** + 11**0111**11 = **11011111** 

   ​					And 

   ​	11**0010**11 + **11**0111**11** = **11001011** 

9. **Uniform crossover:** Information is randomly copied from both the parents. The amount of information inherited from either of the parents depends on the mixing ratio. If its value is 0.5, an equal amount of content from the parent is copied to the children, but the sequential order is random. For example,  

   ​	1**10**010**11** + **1**10**111**01 = **11011111** (mixing ratio = 0.5) 

10. **Arithmetic crossover:** Some arithmetic operation is carried out on the parents to produce a new offspring. For example, 

    ​	11001011 + 11011111 = 11001001 (AND) 

11. **Mutation:** Once a new offspring is created using the crossover function, the offspring is made to undergo mutation, i.e. some of the information stored is altered randomly. This is done to add diversity to the population. Also, this ensures that the new offspring is not exactly like any of its parents, thereby inhibiting premature convergence. 
12. Steps  2-4  are  repeated  until the optimal solution is found or some other termination condition is met. 



**Particle Swarm Optimization**

Particle  swarm  optimization(PSO)  is  a  population-based  stochastic  approach  for  solving continuous and discrete optimization problems. 

PSO  shares  many  similarities  with  evolutionary  computation  techniques  such  as  Genetic Algorithms(GA). The system is initialized with a population of random solutions and searches for optima by updating generations. However, unlike GA, PSO has no evolution operators such as crossover and mutation. In PSO, simple software agents, called particles, move in the search space of an optimization problem. The position of a particle represents a candidate solution to the optimization problem at hand. Each particle searches for better positions in the search space by changing its velocity according to rules originally inspired by behavioral models of bird flocking. Compared to GA, the advantages of PSO are that PSO is easy to implement and there are few parameters to adjust. 

Social psychology research was another source of inspiration in the development of the first particle swarm optimization algorithm. The rules that govern the movement of the particles in a problem's  search  space  can  also  be  seen  as  a  model  of  human  social  behavior  in  which individuals adjust their beliefs and attitudes to conform with those of their peers. 



**Fundamental Principle behind PSO**

As stated before, PSO simulates the behaviors of bird flocking. Consider the following scenario: a group of birds are randomly searching for food in an area. There is only one piece of food in the area being searched. All the birds do not know where the food is. But they know how far the food is in each iteration. An effective strategy to find the food is to follow the bird which is nearest to the food. 

PSO learned from the scenario and used it to solve the optimization problems. In PSO, each single solution is a "bird" in the search space. It is called a "particle". All of particles have fitness values which are evaluated by the fitness function to be optimized, and have velocities which direct the movement of the particles. The particles move through the problem space by following the current optimum particles. 

PSO is initialized with a group of random particles (solutions) and then searches for optima by updating generations. In every iteration, each particle is updated by following two "best" values.  

1. The first one is the best solution (fitness) it has achieved so far. (The fitness value is also stored.) This value is called pbest.  
1. Another "best" value that is tracked by the particle swarm optimizer is the best value, obtained so far by any particle in the population. This best value is a global best and called gbest. When a particle takes part of the population as its topological neighbors, the best value is a local best and is called lbest. 

After finding the two best values, the particle updates its velocity and positions with following equation (a) and (b). 

v[] = v[] + c1 \* rand() \* (pbest[] - present[]) + c2 \* rand() \* (gbest[] - present[]) (a) present[] = present[] + v[]  (b) 

Here: 

- v[] is the particle velocity 
- present[] is the current particle(solution) 
- pbest[] and gbest[] are defined as stated before 
- rand() is a random number between (0,1) 
- c1, c2 are learning factors. usually their value is set equal to 2 

After the particle positions are updated, the fitness value of the particles is recalculated and the process is repeated again until the optimal solution is found or some other terminating conditions are met.  

Particles' velocities on each dimension are clamped to a maximum velocity Vmax. If the sum of accelerations would cause the velocity on that dimension to exceed Vmax, which is a parameter specified by the user. Then the velocity on that dimension is limited to Vmax. 



**Comparison between Genetic Algorithm and PSO** 

Most of evolutionary techniques have the following procedure: 

1. Random generation of an initial population 
1. Reckoning of a fitness value for each subject. It will directly depend on the distance to the optimum. 
1. Reproduction of the population based on fitness values. 
1. If requirements are met, then stop. Otherwise go back to 2. 

From  the  procedure,  we  can  learn  that  PSO  shares  many  common  points  with  GA.  Both algorithms start with a group of a randomly generated population, both have fitness values to evaluate the population. Both update the population and search for the optimum with random techniques. Both systems do not guarantee success. 

However, PSO does not have genetic operators like crossover and mutation. Particles update themselves  with  the  internal  velocity.  They  also  have  memory,  which  is  important  to  the algorithm. 

Compared  with  genetic  algorithms  (GAs),  the  information  sharing  mechanism  in  PSO  is significantly different. In GAs, chromosomes share information with each other. So the whole population moves like a one group towards an optimal area. In PSO, only gBest gives out the information to others. It is a one -way information sharing mechanism. The evolution only looks for the best solution. Compared with GA, all the particles tend to converge to the best solution quickly even in the local version in most cases. 



**Brief Overview of Support Vector Machines** 

“Support Vector Machine” (SVM) is a supervised machine learning algorithm which can be used for  both  classification  or  regression  challenges. However, it is mostly used in classification problems. 

Unlike linear regression, the decision boundary given by the SVM is largely influenced by the “difficult” points which are close to the decision boundary. These points are known as support vectors. This can be visualised as follows:  

Define the hyperplane H such that:  ![](SVM-PSO.004.png)xi•w+b≥+1 when yi=+1 and   xi•w+b≤-1 when yi=-1  

H1 and H2 are the planes: H1:xi•w+b = +1 

H2:xi•w+b = -1 

The points on the planes 

H1 and H2 are the Support vectors 

d+ = the shortest distance to the closest positive point d- = the shortest distance to the closest negative point The margin of a separating hyperplane is d+ + d- 

Now for the determination of this hyperplane, the SVM iterates over the data points and tries to find the values of ‘w’ and ‘b’. In the process, it penalizes the hypothesis generated for every wrong prediction made. This penalizing parameter is generally used in equations as ‘C’. 



**Non-linear SVMs**

The simplest way to separate two groups of data is with a straight line (1 dimensional), flat plane (2 dimensions) or an N-dimensional hyperplane. However, there are situations where a nonlinear region can separate the groups more efficiently. SVM handles this by using a kernel function (nonlinear) to map the data into a different space where a hyperplane (linear) can be used to do the  separation.  It  means  a  nonlinear  function  is  learned  by  a  linear  learning  machine  in a high-dimensional feature space. This is called kernel trick. 

![](SVM-PSO.005.png)

As shown earlier, The SVM linear classifier relies on a dot product between data point vectors. 

![](SVM-PSO.006.png)		.....(a) 

Now, if we map every data point into a higher dimensional data space via a transformation, then the dot product becomes: 

![](SVM-PSO.007.png)		.....(b) 

Thus, the image of the inner product of the data is the inner product of the images of the data.  One such kernel function which is commonly used is Gaussian function or Radial basis function: 

![](SVM-PSO.008.png)

The value equal to 1/2σ^2 is commonly known as ‘gamma’ and it forms the second parameter of the SVM after ‘C’. 



**Effect of C and gamma on Classifier Accuracy**

As C acts as the penalizing parameter for the wrong predictions made by the SVM classifier during training, it can be shown that: 

- Larger C leads to low bias and high variance. Thereby, giving the model freedom to select more samples as support vectors. This means the decision boundary tends to overfit data making the classifier unfit to predict  the class of unknown samples. 
- Small values of C have reverse effects as that of large C i.e., it gives high bias and low variance  output.  Decision  boundary  is  prone  to  underfit  data,  thereby  making  the classifier unable to predict classes of the points near support vectors. 

The gamma parameters can be seen as the inverse of the radius of influence of samples selected by the model as support vectors. The behavior of the model is very sensitive to the gamma parameter.   ![](SVM-PSO.009.png)

- If gamma is too large, the radius of the area of influence of the  support  vectors  only  includes  the  support  vector  itself  and  no  amount of regularization with C will be able to prevent overfitting.  
- When  gamma  is  very  small,  the  model  is  too  constrained  and  ![](SVM-PSO.010.png)cannot capture the complexity or “shape” of the data. The region of  influence of any selected support vector would include the whole  training set.  

Due to this bias-variance trade-off caused by C and gamma parameters, it is necessary to choose the right values so as to get the most accurate classifier. But, finding the right combination of values of these parameters can be an uphill task. Thus, in the next section PSO is used to carry out this process. 



**PSO Optimized SVM**

As  shown  in the previous section, C and gamma are the key parameters that determine the quality of the classifier. Hence, in this section PSO is used to optimize these SVM parameters to get a more accurate classifier. The dataset used here is a software reliability dataset. 

Software  reliability  prediction  has  great  significance  for  software  developers  to  allocate resources reasonably in order to lower development costs, shorten software development cycle and  improve  software  quality.  The  dataset  used in here is obtained from the NASA IV&V Facility Metrics Data Program (MDP) data repository and is named ‘JM1 dataset’. 

Project JM1 has 10878 modules. There are 21 metrics in each module, and the expected output is the boolean value if the module is fault prone or not. 

The following steps are followed before running PSO to find optimum parameters: 

1. A random sample of 1000 modules is selected from the given dataset 
1. Preprocessing  data:  the  data  is  preprocessed  to  using  Principal  Component Analysis (PCA) to reduce the 21 metric data to 4 principal components which are displayed in the table below: 



|Principal Component |Contribution rate |Cumulative Contribution Rate |Weight of Principal Component |
| - | - | :- | :-: |
|F1 |77.84% |77.84% |82.74% |
|F2 |7.33% |85.17% |7.8% |
|F3 |5.39% |90.56% |5.73% |
|F4 |3.46% |94.02% |3.73% |
The above 4 components determined by PCA represent 94% of the information. Also since, it can be observed that the component F1 is the most important component in the randomly sampled data. 



**PSO Parameters**

Following PSO parameters are initialised: 

- Number of iterations = 50 
- Number of particles = 20 
- w = 0.5, c1 = 1.5, c2 = 1.7 where w, c1 and c2 are the constants of velocity determining equation of PSO 
- Max velocity change allowed = 180 
- The  fitness  function  used  to  determine  the  fitness  values  of  the  particles  is 10-fold cross-validation accuracy of SVM. 
- Each particle contains the following information: 
- Current value of C and gamma 
- Velocity of the particle 
- Best value of C and gamma achieved by the particle so far 
- Best accuracy attained by the particle so far 



**RESULT** 

As it can be seen in the beginning i.e. at iteration 1, the accuracy of svm model is 79.1%. But by the end of 50 iterations, PSO has found the optimum parameters where the accuracy achieved is 83.6%. Thus, a gain of 5% in accuracy has been achieved during the entire run of PSO. 



**LIMITATIONS**

Hardware is the major limitation here. As it can be seen in the Output section, that each iteration takes around 30 minutes to complete. Thus, 50 iterations will take about 25 hours to complete.  

Since,  it  is  not  possible  to  run  the  system  for  such  long  stretches,  the  program  has  to be terminated periodically, and the parameters trained so far have to be reloaded again at a later stage. Thus, it takes almost 2 days to test the program run. 

However this can be solved, with the current hardware by taking a smaller sample of data. But, this can make the predictions of the classifier less accurate. Thus, with better system capabilities, we can run this algorithm on larger samples. 



**SCOPE OF IMPROVEMENT**

A better model can be trained by: 

- Considering more principal components 
- Taking larger sample of dataset 
- Increasing the number of particles in the swarm 
- Increasing the number of iterations 
- Ensuring a uniform distribution of particles in the entire search space during initialisation 
