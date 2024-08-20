> [!NOTE] 
> **Attention**  
> This document is written in Github-flavoured Markdown and was meant to be read either from the Github Markdown preview or from a compatible Markdown reader.

Estudante: Marcos Vinícius Bandeira Irigoyen

Resolution of task 5 from the [Algorithms and Data Structures II course](https://github.com/ivanovitchm/datastructure) at UFRN. Context beyond this folder's content about it shall be available at the professor's repository whether he chooses to.

[Presentation video](Not yet, hi youtube!)

Task 5 is an analysis of a wikipedia pages network, made from pages up to 2 references away from three initial articles: [Pretzel](https://en.wikipedia.org/wiki/Pretzel), [Caipirinha](https://en.wikipedia.org/wiki/Caipirinha) and [Chahan (dish)](https://en.wikipedia.org/wiki/Chahan_(dish)). The network is modelled as a unweighted directed graph, whose nodes refer to wikipedia articles and edges means references from one article to another. The analysis focuses around centrality measures, in-degree distribution, and k-cores/k-shells. The analysis is mande in Portuguese, and a visualization of the network is available on https://marcos7765.github.io/AEDII/network.

## Folder Structure
- `images/` is a folder containg PNG images used in the analysis;
- `Plots.ipynb` is a jupyter notebook file that generates the matplotlib images;
- `Analysis.md` is a markdown file, just as this one, with all of the task required texts (in Portuguese);
- This `readme.md` file is the very text you are reading.

## Execution
> [!NOTE] 
> **Attention**  
> Execution isn't assured to generate the same results, as Wikipedia articles can change over time and the network layout, as well as the images made with Gephi, were done manually.

This specific task was done with two different python scripts (namely `makeGraph.py` and `joinAndFilter.py`), the tool [Gephi](https://gephi.org/), and a jupyter notebook (`Plots.ipynb`). All requirements are listed right after the step to step.

[This notebook](https://drive.google.com/file/d/176yqX3XCb4SOsYQtYFL6xZYJGTLfrYIw/view?usp=sharing) includes a step-by-step to replicate (as much as it is possible) the execution. Both python scripts have their usage and parameters described with python's `argparse`, so executing `python <SCRIPT_NAME>.py -h` should show the information to run them by themselves.

### Requirements
- Gephi;
- Python:
  - Python packages:
       - Networkx,
       - Matplotlib,
       - wikipedia;
  - Tested locally on version 3.12.4;

To replicate on Windows machines, you'll also need to call each script and their parameters as they were passed in `run.sh`. Linux and MacOS systems should be able to execute it on their shell of choice.

You might find [this tutorial video](https://youtu.be/RLYoEyIHL6A) useful for general Google Colaboratory usage. The link for the notebook is above the `Folder Structure` section and you'll need to be logged in to run the Notebook.

Manual creation of the layout, using Gephi, is necessary to make most of the images. The Week 09 of the [course repository](https://github.com/ivanovitchm/datastructure/tree/main) has some instructions for it's usage.

If you've got a better machine than Google Colab's one and is comfortable with running the program, I heavily suggest you to do so on this one.

## References
- Implementation:
    - [Wikipedia.ipynb](https://github.com/ivanovitchm/datastructure/blob/main/lessons/week_09/Wikipedia.ipynb) by Ivanovitch Silva (for generation and filtering of the networks);
    - [Hubs.ipynb](https://github.com/ivanovitchm/datastructure/blob/main/lessons/week_08/Hubs.ipynb) by Ivanovitch Silva (for plotting of the centrality measures and in-degree distribution);
- Theoretical:
    - [Algorithms and Data Structure II course repository](https://github.com/ivanovitchm/datastructure/tree/main) by Ivanovitch Silva (specifically week 8 and week 9 Gephi tutorials);
    - [The Atlas for the Aspiring Network Scientist](https://www.networkatlas.eu/) by Michele Coscia (chs. 6, 11, 14 specially, 28, 32 and 38 could've been used).