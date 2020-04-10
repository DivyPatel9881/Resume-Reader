def find_all(regex, seq):
    resultlist=[]
    pos=0

    while True:
       result = regex.search(seq, pos)
       if result is None:
          break
       resultlist.append(seq[result.start():result.end()])
       pos = result.start()+1
    return resultlist