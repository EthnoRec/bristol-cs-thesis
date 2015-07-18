* Features
   * Local feature-based methods
      * Local binary patterns (LBP) features
         * LBP with AdaBoost and Chi-square distance metric [2]
            * Found that LBP are comparable to Haar
      * Histogram of Orientated Gradient (HoG) features
      * Scale Invariant Feature Transform (SIFT) features
      * Weber Local Descriptor (WLD) features
      * Gabor wavelets
      * Retinal sampling (used with Gabor wavelets for other parts)
   * Holistic methods
      * PCA (outperformed by WLD and LBP)
   * 3D models of faces
      * Lu et al [1]
   * Fed  gray  scale  pixel  values  to  an  ensemble  radial basis  functions  with inductive  decision  tree
   * Biologically inspired features based on Gabor filters
      * Guo and Mu [3]
   * Multi-scale, multi-ratio LBP features extracted from 2D texture and 3D range face images
      * Zhang and Wang [4]
   * LDA-based algebraic features and an elastic model based on geometric features to classify three minor Chinese ethnic groups
      * Duan et al [5]
      * Manually constructed templates
   * LBP+WLD fusion with Kruskal-Wallis feature selection
      * Muhammad et al [6]
* Feature selection
   * Kruskal-Wallis ANOVA
* Face detection
   * Mixtures of trees
      * http://www.ics.uci.edu/~xzhu/face/
         * Uses Histogram of Oriented Gradients (HOG) Descriptor
         * trained in max-margin framework
            * e.g. 
         * Matlab code
         * Tasks
            * Face detection
            * Landmark estimation
            * Pose estimation
   * Viola-Jones
      * OpenCV implementation most commonly used
   * KLT (better than VJ?)
   * Review - http://www.academia.edu/253831/Comparative_Testing_of_Face_Detection_Algorithms


* Landmark estimation
   * Previous work uses densely-connected elastic graphs (xzhu:39,9)
      * difficult to optimise
      * most work focused on escaping local minima
   * Mixtures of trees (xzhu)
      * trained in max-margin framework (xzhu)
      * multi-view trees are an effective alternative (xzhu)
      * can be globally optimised with dynamic programming
      * they still capture much relevant global elastic structure
   * Active appearance model
   * Global spatial models built on top of local part detectors - Constrained Local Models (CLMs) (xzhu:11,35,5)
      * Notably, all such work assumes a densely connected spatial model, requiring the need for approximate matching algorithms. By using a tree model, we can use efficient dynamic programming algorithms to find globally optimal solutions.
* Pose (topological) estimation
   * Explicit 3D models (xzhu:6,17)
   * 2D view-based models (xzshu:31,10,21)
   * Mixture-of-trees model/View-models that share a central pool of parts (landmark parts) (xzhu)
      * quite slow ~ 8s




________________


[1] X. Lu, H. Chen, and A. K. Jain, Multimodal facial gender and ethnicity identification, in Proc. International Conf. on Biometrics (ICB), (Hong Kong, 2006), pp. 554–561
[2] Y. Zhiguang and A. Haizhou, Demographic classification with local binary patterns, in Proc. 
International Conf. on Biometrics (ICB), (2007), pp. 464–473.
[3] G. Guo and G. Mu, A study of large-scale ethnicity estimation with gender and age variations, IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), (June 2010), pp. 79–86.
[4] G.  Zhang  and  Y.  Wang,  Multimodal  2D  and  3D  facial  ethnicity  classification,  in
Fifth International Conference on Image and Graphics, 2009 (ICIG’09), (2009), pp. 928–932
[5] X.-dong  Duan,  C.-rui  Wang,  X.-dong  Liu,  Z.-jie  Li,  J.  Wu,  and  H.-long  Zhang, Ethnic Features extraction and recognition of human faces, (2010), pp. 125–130
[6] G. Muhammad, M. Hussain, F. Alenezy, G. Bebis, A. M. Mirza, and H. Aboalsamh, Race classification from face images using local descriptors. International Journal on Artificial Intelligence Tools, 21(05), 2012