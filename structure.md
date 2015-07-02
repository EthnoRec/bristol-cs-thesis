# Structure
40 pages max

## !Introduction and statement of problem (requirements analysis)
* Race recognition is "solved" (95%+ accuracy)
* Ethnicity recognition not researched widely (~75% accuracy in 1 paper)
### Datasets
* Currently available datasets are expensive and limited in scope
* Describe several potential datasets
* Solution: collect own data automatically

## !Background information including literature review
Current state of race recogntition and 1 paper on ethnicity recognition
### Different approaches used for race recognition (feature extraction)
See "Research notes" Google Doc

## !Specification and system design with a discussion of possible alternative approaches

### Data collection

### Face and landmark detection

### Feature extraction


### Classification


## !Discussion of implementation including code fragments as necessary

### Data collection
* Node.js application
* Uses a Tinder client library
* Saves images to disk
* Saves metadata to PostgreSQL database

### Face and landmark detector
* C++ application
* Takes ~7s to process a single image (may find >1 faces)

### Face detector job manager
* Additional scripts to create face detector jobs that can run concurrently
* HPC BlueCrystal used
* Saves face landmark data to PostgreSQL

### Classifier application
* Python application with numpy, scipy, scikit-learn, opencv etc

#### Preprocessing
* Affine transform to centre faces

#### Feature extraction
* LBP

#### Classifier
* SVM


## !Results and achievement - detailed discussion of results and their meaning
## !Conclusion and future work 
