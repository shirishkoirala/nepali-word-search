from trie import Trie

t = Trie()


for line in open("ne_NP_new.dic", "r", encoding="utf8"):
    t.insert(line.strip(' '))

print(t.search('विवेक\n'))
