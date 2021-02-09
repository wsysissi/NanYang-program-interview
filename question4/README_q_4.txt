The working of the code is based on seed_filling method. I scan the matrix given from the first row, if a “1” has been found, regarded this “1” site as a seed, put it in to a queue, and then scan the 4 neighbors of the site(the site that current stay), if an other “1” has been found, push it in to the queue. After the 4 neighbors has already been scan, the queue pop out the site, and then repeat the above steps to operate the next site(the first element in the queue after pop action). Repeat the action until there is no element in the queue. Actions above was called filling. The next step is to continue scan from the site that we first met the “1” seed(scan the site after it). 

Repeat the scan-seed-filling action until the matrix has been all scaned.

In addition, we also need a flag to count the number of the connected components. In my code, I have a site as a class, and the flag is on of the site’s attributes, when it scanned a seed give that site’s flag attribute the value of flag, as long as the “filling” sites. Then, flag plus 1. 

According to the actions above, is the Programming idea of my code in code_question_4.py.
