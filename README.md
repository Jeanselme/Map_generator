# Map Generator
Creation of map using the diamond and square algorithm

## Execution
```
python3.4 map_generator.py [-n dimensionMap] [-o resultFileName]
```
This command creates two output files : a black and white map which is the result of the square algorithm and a colored one.  

By default :
  - n = 10
  - output = "result"

Warning : The final dimension of the image will be a square of side 2**n+1.

## Result
This is the result of the square algorithm :
![Square result](https://.github.com/images/result_diamond_square.png)

And after colorization :
![Map result](https://.github.com/images/result_map.png)

## Library
Needs PIL and random. Compiled with python3.4
