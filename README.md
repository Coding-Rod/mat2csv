# mat file to csv converter

## Example codes
~~~python
import mat2csv as m2c
m2c.convert_mat("sample.mat")
~~~

~~~python
import mat2csv as m2c
import pandas as pd
df = m2c.read_matfile("sample.mat")
print(df)
~~~