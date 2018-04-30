# hearst

Uses python Hearst pattern code from https://github.com/mmichelsonIF/hearst_patterns_python

USAGE: python3 hearst.py [<input file or directory>] [-o <output file>] [-s]

If no input file is given, it will process text read from stdin.  If no output file is given, it will write to stdout.  The -s flag limits the parrersn to the oritinal (simple) ones from thew 1992 paper.

Output has tab-separated lines like 'specific\tgeneral\tsource_file',
e.g., 'apple\tfruit\trecipies.txt'

From python, call hearst.hearstify(<path>, [<extended>]) to get an iterable of pairs

Works in both Python3 and 2.X

## background ##

See: Marti A. Hearst. 1992. Automatic acquisition of hyponyms from large text corpora.
In Proceedings of the 14th conference on Computational linguistics - Volume 2 (COLING '92),
Vol. 2. Association for Computational Linguistics, Stroudsburg, PA, USA, 539-545. 
DOI: https://doi.org/10.3115/992133.992154
http://people.ischool.berkeley.edu/~hearst/papers/coling92.pdf

## some sample output ##

**apt_2017** is a directory with some sample text files

**apt_sg.txt** is the output produced by hearst.py run on more than 400
APT documents where the 1st column is the specific term and the second
is the generic one.

**apt_sg_uniq.txt** are those results after processing with sort and uniq

**apt_gs.txt** is the output produced by hearst.py run on more than 400
APT documents where the 1st column is the generic term and the second
is the specific one.

**apt_gs_uniq.txt** are those results after processing with sort and uniq
