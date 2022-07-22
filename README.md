Knight's Tour Puzzle
A solution solver to the classical Knight's Tour Puzzle, employing Warnsdorf's algorithm.
This program also allows you to try and solve the puzzle yourself, if there is a solution.



OUTPUT:

Enter your board dimensions:8 8
Enter the knight's starting position:5 5
2022-07-22 18:30:21,530 [INFO] Solution found. Runtime: 7.28ms
Do you want to try the puzzle? (y/n):
> n

Here's the solution!
 ---------------------------
8| 18 15 34 31 20  5 36  3 |
7| 33 30 19 16 35  2 21  6 |
6| 14 17 32 45 56 60  4 37 |
5| 47 44 29 59  1 64  7 22 |
4| 28 13 46 55 61 57 38 53 |
3| 43 48 62 58 63 54 23  8 |
2| 12 27 50 41 10 25 52 39 |
1| 49 42 11 26 51 40  9 24 |
 ---------------------------
    1  2  3  4  5  6  7  8
    
    
---------------------

Enter your board dimensions:4 4
Enter the knight's starting position:1 1
Do you want to try the puzzle? (y/n):
2022-07-22 18:33:37,715 [INFO] Solution found. Runtime: 2.22ms
y
 ---------------
4| __ __ __ __ |
3| __  3 __ __ |
2| __ __  3 __ |
1|  X __ __ __ |
 ---------------
    1  2  3  4
Enter your next move:3 3
Invalid move! Enter your next move:3 2
 ---------------
4| __  2 __  1 |
3|  2 __ __ __ |
2| __ __  X __ |
1|  * __ __ __ |
 ---------------
    1  2  3  4
Enter your next move:4 4
 ---------------
4| __ __ __  X |
3| __  2 __ __ |
2| __ __  * __ |
1|  * __ __ __ |
 ---------------
    1  2  3  4
Enter your next move:2 3
 ---------------
4| __ __ __  * |
3| __  X __ __ |
2| __ __  *  2 |
1|  * __  2 __ |
 ---------------
    1  2  3  4
Enter your next move:3 1
 ---------------
4| __ __ __  * |
3| __  * __  2 |
2|  2 __  * __ |
1|  * __  X __ |
 ---------------
    1  2  3  4
Enter your next move:1 2
 ---------------
4| __  1 __  * |
3| __  *  3 __ |
2|  X __  * __ |
1|  * __  * __ |
 ---------------
    1  2  3  4
Enter your next move:2 4
 ---------------
4| __  X __  * |
3| __  * __  1 |
2|  * __  * __ |
1|  * __  * __ |
 ---------------
    1  2  3  4
Enter your next move:4 3
 ---------------
4| __  * __  * |
3| __  * __  X |
2|  *  3  * __ |
1|  * __  * __ |
 ---------------
    1  2  3  4
Enter your next move:2 2
 ---------------
4|  1  *  2  * |
3| __  * __  * |
2|  *  X  * __ |
1|  * __  *  1 |
 ---------------
    1  2  3  4
Enter your next move:4 1
 ---------------
4| __  * __  * |
3| __  *  2  * |
2|  *  *  * __ |
1|  * __  *  X |
 ---------------
    1  2  3  4
Enter your next move:3 3
 ---------------
4| __  * __  * |
3| __  *  X  * |
2|  *  *  * __ |
1|  *  2  *  * |
 ---------------
    1  2  3  4
Enter your next move:2 1
 ---------------
4| __  * __  * |
3|  1  *  *  * |
2|  *  *  *  1 |
1|  *  X  *  * |
 ---------------
    1  2  3  4
Enter your next move:4 2
 ---------------
4| __  *  1  * |
3| __  *  *  * |
2|  *  *  *  X |
1|  *  *  *  * |
 ---------------
    1  2  3  4
Enter your next move:3 4
 ---------------
4| __  *  X  * |
3| __  *  *  * |
2|  *  *  *  * |
1|  *  *  *  * |
 ---------------
    1  2  3  4
Enter your next move:1 3
 ---------------
4| __  *  *  * |
3|  X  *  *  * |
2|  *  *  *  * |
1|  *  *  *  * |
 ---------------
    1  2  3  4
No more possible moves!
Your knight visited 15 squares
