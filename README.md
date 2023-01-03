
# Replication Package Comparison Defects and Code Smells

## Summary

Welcome to the Artifacts for the paper "Yet Another Model! A Study on Model's Similarities for Defect and Code Smells" published at the 26th International Conference on Fundamental Approaches to Software Engineering by Geanderson Santos, Amanda Santana, Gustavo Vale, and Eduardo Figueiredo. Our main goals for this paper were to (i) understand the similarities and differences between machine learning models for defects and code smells; and (ii) evaluate how different quality attributes contribute to the model explainability. For this purpose, our dataset is composed of 14 open-source java systems and 7 code smells at the class-level. This replication package allows the research community to replicate the results of a study comparing the defect model with several class-level code smell models. This replication package allows practitioners to (i) replicate our study to verify the reported results; (ii) train models using different smells and features, and (iii) use the available models to predict the smelliness and defectiveness of new classes. To better understand this replication package, we suggest reading the paper to understand our study setup and the decisions made during the experimentation. 

You can cite the paper as follows:

```bibtex
@inproceedings{SantosFASE2023,
  author    = {G. E. dos Santos and A. Santana and G. Vale and
               E. Figueiredo},
  title     = {Yet Another Model! A Study on Model's Similarities for Defect and Code Smells},
  booktitle = {26th International Conference on Fundamental Approaches to Software Engineering (FASE)},
  year      = {2023}
}
```

## Setup

To use the replication package, we recommend applying the dependencies included in the [requirements](requirements.txt) file. We strongly recommend using Python 3.9 Virtual Environment as follows, since Pycaret requires it.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

In case you don't have Python 3.9, you can use Pyenv to install it. As these scripts may be useful for other projects, we include them in the [scripts](scripts/) folder.


```bash
# Install dependencies
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncursed5-dev xz-utils tk-dev

# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to PATH and initialize
echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Update list of available Python versions
pyenv update

# Install Python 3.9
pyenv install 3.9.0

# Set global Python version to 3.9
pyenv global 3.9.0

# Verify installation
python --version
```

From there, you can run the notebooks in the [notebooks](notebooks/) folder.

### Code Smells Definitions

In our study, we evaluate the following smells:

| Code Smell                   | Definition                                                                                  | Reference |
| ---------------------------- | ------------------------------------------------------------------------------------------- | --------- |
| God Class                    | A large class that has too many responsibilities and centralizes the module functionality. | [3]       |
| Refused Bequest              | A class that does not want to use its parent behavior.                                      | [2]       |
| Spaghetti Code               | A class that has methods with large and unique multistage process flow.                     | [1]       |
| Class Data Should be Private | A class with too many public fields.                                                        | [4]       |
| Data Class                   | Classes that have only fields, getters, and setters.                                         | [2]       |
| Lazy Class                   | Classes that have little behavior, with few methods and fields.                             | [2]       |
| Speculative Generality       | Classes that support future behavior, usually interacting with test classes only.           | [2]       |

To identify such smells we relied on the Organic tool. If you want to run the Organic tool to asses the smell collection process, you can, for instance, for the project `ant`, execute the following command:

```bash
java -jar organic-OPT.jar -sf ../projects/ant/organic/ant.json -src "../bad-smells-defects/projects/ant"
```

You can execute the `organic-OPT.jar` included inside the [scripts](scripts/) folder. We highlight that Organic needs to be run on OpenJDK 11, so you need to change the java version in case it is not the required one. 

### Open-Source Java Projects

Our dataset is composed of the following systems and their source code can be found in the folder data/projects. 

- Ant 1.7
- Broadleaf 3.0
- Camel 1.6
- Elasticsearch 0.9
- Hazelcast 3.3
- JDT 3.4
- Jedit 4.3
- Lucene 4.3
- Neo4J 1.9
- OrientDB 1.6
- PDE 3.4
- POI 3.0
- Titan 0.5
- Xalan 2.7

## Hardware Requirements

The experiments were performed on a machine with the following specifications:
- 16 GB RAM
- 8th generation Intel Core i7 processor (or equivalent)

## Test Instructions

You can run the notebooks in the [notebooks](notebooks/) folder. Below, we describe each folder contained in the repository.

### Correlations

There is a folder called [correlations](correlations/) with the respective correlation analysis divided by each quality attribute. The blue value indicates a low correlation, while the red represents a high correlation. As the paper mention, we first set our threshold to 99% of correlation and excluded the more general metrics, for instance, Total Number of Attributes (TNA). We then remove those features that had multicollinearity higher than 85%.
### Data

All data is available under the [data](data/) folder. Below, we present the folder's working tree.

| Folder                        | Content                                            |
| ----------------------------- | -------------------------------------------------- |
| [**final**](data/final)       | Contains the final dataset with defects and smells |
| [**projects**](data/projects) | Contains the projects used in the study            |
| [**raw**](data/raw)           | Contains the raw dataset with defects              |
| [**unseen**](data/unseen)     | Contains the unseen dataset to test the models     |

Each project folder has all `csv` files with the information about the code smells. The files follow this naming pattern: `organic<code_smell>.csv`

#### Explanations

Inside the [explanations](explanations/) folder, we have all SHAP explanations for each target. 

### Features

The complete list of features is available in the [features](features/) folder. There are two files in this folder:

- [features.md](features/features.md): contains the list of features used in the study with the considered correlation.
- [OpenStaticAnalyzer-1.0-Metrics.html](features/OpenStaticAnalyzer-1.0-Metrics.html): contains the list of features with a brief description.

### Models

The models created in the study are available in the [models](models/) folder. Each target has its own `pickle` file. Note that some files are too large for GitHub storage, and you have to unzip the `zip` files to use the models (defect, gc, lc, and sc).

### Notebooks

The notebooks are organized as follows:

- [01-setup.ipynb](notebooks/01-setup.ipynb): prepares, trains and executes the data for the study.
- [02-predict.ipynb](notebooks/02-predict.ipynb): loads the models and predicts with unseen data.

### Results

The results are available in the [results](results/) folder. There, we have the performance of each model and the results of the statistical tests.

### Scripts

Inside the [scripts](scripts/) folder, we stored the [Organic](https://github.com/opus-research/organic) jar.

### Validation

Inside the [validation](validation/) folder, we have the results of the validation of the Organic tool with developers.

## Replication Instructions

If the required packages are installed according to the Setup section of this document. You should be able to run each cell of the notebooks in the [notebooks](notebooks/) folder.

##### References

- [1] Brown, W.H., Malveau, R.C., McCormick, H.W.S., Mowbray, T.J.: AntiPatterns: refactoring software, architectures, and projects in crisis. John Wiley & Sons, Inc. (1998)
- [2] Fowler, M.: Refactoring: Improving the Design of Existing Code. Addison-Wesley (1999)
- [3] Riel, A.: Object Oriented Design Heuristics. Addison-Wesley Professional (1996)
- [4] Shvets, A.: Dive into Design Patterns. Refactoring Guru (2021)
