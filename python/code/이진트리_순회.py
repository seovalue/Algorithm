import heapq as hq

heap = []
for i in range(1,8):
    hq.heappush(heap, i)

def postOrder(v):
    if v > 7:
        return
    else:
        postOrder(v*2) #왼쪽 자식 노드 호출
        postOrder(v*2+1) #오른쪽 자식 노드 호출
        print(v,end=" ")

def preOrder(v):
    if v > 7:
        return
    else:
        print(v, end=" ")
        preOrder(v*2)
        preOrder(v*2+1)

def inOrder(v):
    if v > 7:
        return
    else:
        inOrder(v*2)
        print(v, end=" ")
        inOrder(v*2+1)

if __name__ == "__main__":
    print("전위순회")
    preOrder(1)
    print("\n중위순회")
    inOrder(1)
    print("\n후위순회")
    postOrder(1)
