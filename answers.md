# CMPS 2200 Assignment 3
## Answers

**Name:** Jack Zemke


Place all written answers from `assignment-03.md` here for easier grading.






- **b.**
    -
    **Work:** $W(n) = W(n-1) + 1$ This recurrence is balanced, with a depth of $n$ levels and each level having a cost of $1$, thus the big oh notation of this recurrence is $\in O(n)$

    **Span:** Much the same, the recurrence for span is $S(n) = S(n-1) + 1$ which is balanced. It has a depth of $n$ levels and each level has a cost of $1$. The big oh notation of this recurrence is also $\in O(n)$




- **d.**
    - 
    `parens_match_scan()` makes one call to `map`, one call to `scan`, and one call to `reduce`. To find the big oh notation of this implimentation, we must find which of these functions dominates the work and span asymptotically. 
    |       |    work    |    span    
    |:-----:|:--------------:|:--------------:
    | **map** |    $O(n)$      |    $O(\log n)$ 
    | **scan** |    $O(n)$      |   $O(\log n)$   
    | **reduce** |    $O(n)$      |     $O(\log n)$  
    
    None of these functions dominate the work or span asymptotically, so the relation for `parens_match_scan()` can be modeled by the relation for any of the above calls. All of these recurrences will yield the same result, with **work** $\in O(n)$ and **span** $\in O(\log n)$.







- **f.**
    -
    **Work:** The work of this implimentation can be modeled by the recurrence $W(n) = 2W(n/2) + 1$. The cost of the root node of this tree is $1$, while the cost of its children is $2$. Therefore, this recurrence is leaf dominated. At the leaf level, there will be $2^{\log_{2}n}$ leaves each with a cost of $1$. Therefore, the work of this implimentation is $\in O(2^{\log_{2}n})$

    **Span:** The span of this implimentation can be modeled by the recurrence $S(n) = S(n/2) + 1$. This recurrence is balanced, because the cost of the root node and its children is both $1$. This tree has a depth of $\log n$ and each level has a cost of $1$. This, the span of this implimentation is $\in O(\log n)$