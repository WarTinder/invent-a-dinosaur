from Bio import Phylo

tree = Phylo.read("sauropoda.txt", "newick")
Phylo.draw(tree)