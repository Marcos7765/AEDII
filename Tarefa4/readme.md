> [!NOTE] 
> **Attention**  
> This document is written in Github-flavoured Markdown and was meant to be read either from the Github Markdown preview or from a compatible Markdown reader.

Estudante: Marcos Vinícius Bandeira Irigoyen

Resolution of task 4 from the [Algorithms and Data Structures II course](https://github.com/ivanovitchm/datastructure) at UFRN. Context beyond this folder's content about it shall be available at the professor's repository whether he chooses to.

[Presentation video](https://youtu.be/WyP5Z5OQXhw) (It's in portuguese and not really good)

Task 4 is a brief analysis of coauthorship networks made from some UFRN articles, grouped by an common [SDG Goal](https://sdgs.un.org/goals) that they fit in. The network is modelled as a undirected, unweighted graph in which it's nodes symbolize authors and the edges the relation of coauthorship. The analysis is divided between two parts: one focused around the node degree x mean neighbour degree relation (degree-assortativity) and a broader one including also connected components, clustering, and network size.  
The analysis is made in Portuguese, with it's first and second part in the `readme.md` in folders `requisito2` and `requisito3` respectively.

Notebook link:
- [Setup data](https://colab.research.google.com/drive/13Wo-VHg1PMe0zzPL_ndRRMkSnMJrBgBz?usp=sharing).

## Folder Structure
- The `requisito<X>/` subfolder contains the necessary data (either a image or a markdown-formatted table) for a given X requirement of the task, and a `readme.md` file with an analysis of it (written in Portuguese).
- The `Setup_data.ipynb` is the jupyter notebook file that generates the aforementioned necessary data;
- This `readme.md` file in the folder's root is the very text you are reading.

## Execution
> [!NOTE] 
> **Attention**  
> Execution is only needed to replicate the results, which should already be available in this repository.

You can open `Setup_data.ipynb` using either Google Colab or Jupyter Notebook. If you don't already have Jupyter Notebook or any previous python experience I heavily suggest you to use Google Colab.  
Some commands used within the notebook might not be compatible with Windows or macOS (due to calls for external Linux commands and usage of Unix's output redirection operator `>`). It's incompatibility would only occur for those running it locally (a Jupyter Notebook instance in those OSes).  
The packages used directly on the notebooks are `pandas`, `networkx`,`matplotlib` and `seaborn`. Be sure to have them set up on your environment beforehand (Google Colab will already have all of them).  
You'll also need `curl`, `unzip` and `echo` programs/commands. The latter is assured to be in any POSIX-compliant system, while `curl` is very commonly preinstalled and `unzip` might not come by default in some linux distributions (if any of this sounds overwhelming, please consider more using Google Colab).

You might find [this tutorial video](https://youtu.be/RLYoEyIHL6A) useful for general Google Colaboratory usage. The link for the notebook is above the `Folder Structure` section and you'll need to be logged in to run the Notebook.

There's a forced raise of a `Exception` to stop earlier the execution of the whole notebook. It is meant for me, that gets lazy and just press "run all cells". The parts that don't execute are not necessary (and could even not be present there) for replicating the results.

The code was meant to be executed only once, so reexecutions will redownload the `.zip` file and try to extract it again (which will make `unzip` prompt the user). Other files are overwritten during reexecution. The results will be produced on the same folder as the notebook.

If the download link used during the `curl` execution doesn't work, the data should be a zipped folder containing `.csv` files reffering to articles' data gathered with [Scopus](https://www.scopus.com/home.uri) that fit into [SDG Goals](https://sdgs.un.org/goals) 3, 7, 15 and 17 respectively. The original data was gathered during mid-July 2024.

Do notice that this curl download is a security liability. Read the code from the notebook before executing it, be sure that the file is safe before unzipping (it could be a zip bomb) and so on.

## References
- Implementation:
    - [SDG.ipynb](https://github.com/ivanovitchm/datastructure/blob/main/lessons/week_06/SDG.ipynb) by Ivanovitch Silva (for the requirement 2 plot and graph modelling of the network);
- Theoretical:
    - [Algorithms and Data Structure II course repository](https://github.com/ivanovitchm/datastructure/tree/main) by Ivanovitch Silva (specifically weeks 05 to 07 pdfs);
    - [The Atlas for the Aspiring Network Scientist](https://www.networkatlas.eu/) by Michele Coscia (ch. 6-9, 14 e 27 specially).