import networkx as nx
import wikipedia
import matplotlib.pyplot as plt
from queue import Queue, Empty
import threading
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("page_name", type=str, help="The name of the page you want to add")
parser.add_argument("--max_layer", type=int, default=2, help="Maximum distance to the page")
parser.add_argument("--num_threads", type=int, default=8)
args = parser.parse_args()
max_layer = args.max_layer

SEEDS = [args.page_name]
STOPS = ("International Standard Serial Number",
        "International Standard Book Number",
        "National Diet Library",
        "International Standard Name Identifier",
        "Pubmed Identifier",
        "Pubmed Central",
        "Digital Object Identifier",
        "Arxiv",
        "Proc Natl Acad Sci Usa",
        "Bibcode",
        "Library Of Congress Control Number",
        "Jstor",
        "Food",
        "Street Food",
        "Alcoholic Beverage",)

Nthreads = args.num_threads
timeout_sec = 3

threaded_queue = Queue()

g = nx.DiGraph()

for SEED in SEEDS:
    threaded_queue.put((0, SEED.title()))

todo_set = set([x.title() for x in SEEDS])
done_set = set()

def filterLink(link):
  if "(Identifier)" in link: return False
  if link in STOPS: return False
  if link.startswith("List Of"): return False
  return True

def montarGrafo(queue=threaded_queue):
    while True:
        try:
            layer, page = queue.get(timeout=timeout_sec)
        except Empty:
            return
        
        if page in done_set:
            queue.task_done()
            continue
        try:
            wiki = wikipedia.page(page)
        except:
            queue.task_done()
            continue

        for link in wiki.links:
            link = link.title()
            if filterLink(link):
                if layer < max_layer-1:
                    if link not in todo_set: #done_set <= todo_set
                        queue.put((layer+1, link))
                        todo_set.add(link)
            g.add_edge(page, link)
        
        done_set.add(page)
        queue.task_done()

threads = [threading.Thread(target=montarGrafo) for _ in range(Nthreads)]
time_before = time.time()
for i in threads: i.start()
threaded_queue.join()
time_after = time.time()
print(f"Wall time: {time_after-time_before}")
print(80*"-")
print("{} nodes, {} edges".format(len(g), nx.number_of_edges(g)))

nx.write_graphml(g, "unfiltered_{}.graphml".format(args.page_name.replace(' ', '__')))