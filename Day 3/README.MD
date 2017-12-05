My initial solution satisfied the first part of the problem, but was difficult to scale to the second part. As a result I went back and improved on my previous code.  

The biggest improvement I made was changing how I THOUGHT about the puzzle. I initially recognized the issues of having one side shorter than the other when starting the next row, however I eventually came up with a way to fix this. By modifing the distance traveled goign right and up, I was able to successfully spiral.  

The second part of the puzzle was made easier by using a dictionary to store the information. I do feel bad about the try catches in the calc_sum function, but I couldn't quickly come up with a way to make that cleaner. I may go back and try to refactor that.
