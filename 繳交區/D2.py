
# coding: utf-8

# 作業目標<br>
# 熟悉陣列維度轉換，並且會擷取需要資料<br>
# 作業重點<br>
# 使用reshap須注意order用法<br>
# where可以運用邏輯條件擷取資料

# 題目:<br>
# 1.將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")<br>
# 2.呈上題的array，找出被6除餘1的數的索引<br>

# In[1]:


import numpy as np


# In[20]:


#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
a = np.array(range(30))
a = a.reshape(5,6,order="F")
a


# In[30]:


#2.呈上題的array，找出被6除餘1的數的索引
np.where(a % 6 ==1)

