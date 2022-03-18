#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
from Resolve import *


# In[ ]:


def test_total_days():
    assert total_days(flights) == 365


# In[ ]:


def test_departure_cities():
    assert departure_cities(airports, flights) == 2


# In[ ]:


def test_relationship():
    assert relationship(planes, flights)== ['tailnum', 'year']


# In[ ]:


def test_manufacturer_delay():
    assert manufacturer_delay(planes, flights)== 'EMBRAER'


# In[ ]:


def test_most_connected_cities():
    assert most_connected_cities(flights, airports)== ['New York', 'Chicago']

