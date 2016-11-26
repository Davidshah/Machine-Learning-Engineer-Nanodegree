# coding: utf-8
# Technical Interview Practice
# David Shahrestani

# In[1]:

def question1(s, t):
    """
    Return true if some anagram of t is a substring of s.
    Otherwise return false.
    """
    # Return false for None case
    if t is None or s is None:
        return False
    
    # Initialize length variables
    s_length = len(s)
    t_length = len(t)
    
    # Return false for certain edge cases
    if t_length > s_length or t == "" or s == "":
        return False
    
    # Convert both strings to lowercase
    s = s.lower()
    t = t.lower()
    
    # Initialize and sort t_list for easier comparison
    t_list = list(t)
    t_list.sort()
    
    # Iterate through slices of s of t_length (O(n^2))
    for i in xrange(s_length - t_length + 1):
        sub_string = s[i:(i + t_length)]
        
        # Concert to sorted list for easier comparison
        sub_string = list(sub_string)
        sub_string.sort()
        
        # Compare sorted sub_string with t_list
        if sub_string == t_list:
            return True
    
    return False


# Normal case Q1 tests
print question1("udacity", "ad")
# True
print question1("Batman", "tab")
# True
print question1("abcdefghijklmnopabcdefghijklmnopabcdefghijklmnopab", "xyz")
# False

# Edge case Q1 tests
print question1("apple", "superman")
# False
print question1(None, "")
# False
print question1("a", "a")
# True

# In[2]:

def question2(a):
    """
    Return the longest palindromic substring containied in a.
    """
    # Return None for certain edge cases
    if a is None or a == "":
        return None
    
    # Initialize length variables
    length = len(a)
    pal_length = len(a)
    
    # Convert string to lowercase
    a = a.lower()
    
    # Iterate through different lengths of palindrome search
    while pal_length > 1:
        
        # Iterate through slices of 'a' (O(n^2))
        for i in xrange(length - pal_length + 1):
            sub_string = a[i:(i + pal_length)]
            
            # Check if sub_string is a palindrome
            if sub_string == sub_string[::-1]:
                return sub_string
        
        # Reduce pal_length and repeat search
        pal_length -= 1
    
    return None


# Normal case Q2 tests
print question2("ioioi")
# "ioioi"
print question2("abcdxyxefgh")
# "xyx"
print question2("abcdefghijklmnopqrstuvwxyz")
# None

# Edge case Q2 tests
print question2("")
# None
print question2(None)
# None
print question2("abCcCccxy")
# "ccccc"

# In[14]:

# Import library
import heapq

def question3(G):
    """
    Return the minimum spanning tree withing G.
    Must input connected graph.
    """
    # Return None for certain edge cases
    if G is None:
        return None
    
    # Initialize variables
    new_graph = {}
    explored = set([])
    heap = []
    mst = {}
    
    # Modify G format to include edge pair information in tuple
    for vertex in G:
        new_graph[vertex] = []
        mst[vertex] = []
        for edge in G[vertex]:
            pair = (edge[1], [vertex, edge[0]])
            if pair not in new_graph[vertex]:
                new_graph[vertex].append(pair)
    
    # Pick a starting vertex
    start = list(new_graph.keys())[0]
    explored.add(start)
    
    # Begin exploration
    for tup in new_graph[start]:
        heapq.heappush(heap, tup)
    
    # Continue exploration until heap is empty (O(ElogV))
    while heap:
        w, b = heapq.heappop(heap)
        
        # Check if we already been to this node
        if b[1] not in explored:
            explored.add(b[1])
            
            # Append mst with findings
            if (b[1], w) not in mst[b[0]]:
                mst[b[0]].append((b[1],w))
            if (b[0], w) not in mst[b[1]]:
                mst[b[1]].append((b[0],w))
            
            # Add new edges to exploration
            for tup in new_graph[b[1]]:
                heapq.heappush(heap, tup)

    return mst


# Normal case Q3 tests
print question3({'A': [('B', 2)],
                 'B': [('A', 2), ('C', 5)], 
                 'C': [('B', 5)]})
# {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}

print question3({'A': [('B', 3), ('C', 4)],
                 'B': [('A', 3), ('C', 5), ('D', 6), ('E', 2)],
                 'C': [('A', 4), ('B', 5), ('E', 7)],
                 'D': [('B', 6)],
                 'E': [('B', 2), ('C', 7)]})
# {'A': [('B', 3), ('C', 4)], 'C': [('A', 4)], 'B': [('A', 3), ('E', 2), ('D', 6)], 'E': [('B', 2)], 'D': [('B', 6)]}

# Edge case Q3 tests
print question3(None)
# None
print question3({'A': [('B', 1000)],
                 'B': [('A', 1000), ('C', 1000)], 
                 'C': [('B', 1000), ('D', 1000)],
                 'D': [('C', 1000), ('E', 1000)],
                 'E': [('D', 1000), ('F', 1000)],
                 'F': [('E', 1000), ('G', 1000)],
                 'G': [('F', 1000), ('H', 1000)],
                 'H': [('G', 1000), ('I', 1000)],
                 'I': [('H', 1000), ('J', 1000)],
                 'J': [('I', 1000), ('K', 1000)],
                 'K': [('J', 1000), ('L', 1000)],
                 'L': [('K', 1000), ('M', 1000)],
                 'M': [('L', 1000), ('N', 1000)],
                 'N': [('M', 1000)]})
# {'A': [('B', 1000)], 'C': [('B', 1000), ('D', 1000)], 'B': [('A', 1000), ('C', 1000)],
# 'E': [('D', 1000), ('F', 1000)], 'D': [('C', 1000), ('E', 1000)], 'G': [('F', 1000),
# ('H', 1000)], 'F': [('E', 1000), ('G', 1000)], 'I': [('H', 1000), ('J', 1000)],
# 'H': [('G', 1000), ('I', 1000)], 'K': [('J', 1000), ('L', 1000)], 'J': [('I', 1000),
# ('K', 1000)], 'M': [('L', 1000), ('N', 1000)], 'L': [('K', 1000), ('M', 1000)], 'N': [('M', 1000)]}

# In[15]:

def question4(T, r, n1, n2):
    """
    Return the least common ancestor between two nodes on a binary search tree.
    """
    # Return None for certain edge cases
    if r is None or T is None or n1 is None or n2 is None:
        return None
    if r >= len(T):
        return None
 
    # Check if n1 and n2 are both smaller than the root
    if(r > n1 and r > n2):
        return question4(T, T[r].index(1), n1, n2)
 
    # Check if n1 and n2 are both larger than the root
    elif(r < n1 and r < n2):
        return question4(T, (len(T[r]) - T[r][::-1].index(1) - 1), n1, n2)
    
    # If n1 and n2 are on different sides of root then LCA found
    else:
        return r
    
    
# Normal case Q4 tests
print question4([[0, 1, 0, 0, 0], 
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)
# 3

print question4([[0, 0, 0, 0, 0], 
                 [1, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 2,
                 1,
                 0)
# 1

print question4([[0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]],
                 2,
                 8,
                 4)
# 6

# Edge case Q4 tests
print question4(None,
                 2,
                 8,
                 4)
# None

print question4([[0, 1, 0, 0, 0], 
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 5,
                 1,
                 4)
# None

# In[24]:

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

def question5(ll, m):
    """
    Return the element in a singly linked list that's m elements form the end.
    """
    
    # Return None for certain Edge cases
    if ll is None or m is None:
        return None
    
    # Initialize variables and counter
    target_node = ll
    ref_node = ll
    count  = 0
    
    # Search while count is less than m, this
    # Will give us starting point for ref_node (O(n-m))
    while count < m:
        # If search exceeds length return None
        if ref_node is None:
            return None
        
        # Continue search to next node
        ref_node = ref_node.next
        count += 1
    
    # Continue search until ref_node reaches end
    # Moving through target nodes. (O(n-m))
    while ref_node is not None:
        target_node = target_node.next
        ref_node = ref_node.next
            
    return target_node.data


# Create linked list
link_list = LinkedList()
link_list.push(20)
link_list.push(4)
link_list.push(15)
link_list.push(35)
link_list.push(55)
link_list.push(22)
link_list.push(31)
link_list.push(25)
link_list.push(52)
link_list.push(11)

# Normal case Q5 tests
print question5(link_list.head, 5)
# 55
print question5(link_list.head, 10)
# 11

# Edge case Q5 tests
print question5(link_list.head, 11)
# None
print question5(None, 1)
# None
