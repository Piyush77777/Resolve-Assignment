#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries
import pandas as pd
import os


# In[2]:


path = os.getcwd()
path = path + "\\Downloads\\resolve assignment"

# loop over the list of csv files
for root, dirs, filenames in os.walk(path):
    for a, f in enumerate(filenames):
        fullpath = os.path.join(path, f)
        globals()[f.split(".")[0]] = pd.read_csv(fullpath)


# In[3]:


def total_days(flights):
    """total number of days does the flights table cover"""
    #     adding year,month,day into a new column string for a date
    flights["dateInt"] = (
        flights["year"].astype(str)
        + flights["month"].astype(str).str.zfill(2)
        + flights["day"].astype(str).str.zfill(2)
    )
    #     changing string to datetime format
    flights["Date"] = pd.to_datetime(flights["dateInt"], format="%Y%m%d")
    #     return unique number of days
    return len(flights["Date"].unique())


# In[4]:


# total days flight -- 365


# In[5]:


def departure_cities(airports, flights):
    """departure cities does the flights database cover"""
    #     slice important columns
    airports = airports[["IATA_CODE", "CITY"]]
    #     rename it so that both dataframe have a common name to join on
    airports = airports.rename({"IATA_CODE": "origin"}, axis=1)
    #     merge dataframes on common column
    flights_with_cities = pd.merge(flights, airports, on="origin")
    return len(flights_with_cities["CITY"].unique())


# In[6]:


# departure cities does the flights database cover-- 2


# In[7]:


def relationship(planes, flights):

    """relationship between flights and planes tables"""
    #     loop through both database
    #     find the common columns
    #     find the common element in common columns
    common_elements=[]
    for i in planes.columns:
        for j in flights.columns:
            if i == j:
                common_elements.append(i)
    return common_elements           
                


# In[8]:


# Common column between two tables is-- tailnum and year


# In[9]:


def manufacturer_delay(planes, flights):
    """manufacturer incurred the most delays"""
    #     slice important columns
    planes = planes[["tailnum", "manufacturer"]]
    #     join dataframes on common column
    flights_with_planes = pd.merge(flights, planes, on="tailnum")
    #     groupby data on manufacturer with delay as condition
    groupby_data = flights_with_planes.groupby("manufacturer")["dep_delay"]
    #     use the sum function on grouped data
    #     filter it using using nlargest function and resetting index
    return groupby_data.sum().nlargest(1).reset_index()["manufacturer"][0]


# In[10]:


#  airplane manufacturer incurred the most delays-- EMBRAER


# In[11]:


def most_connected_cities(flights, airports):
    """two most connected cities"""
    #     slice important columns
    flights = flights[["origin", "dest"]]
    airports = airports[["IATA_CODE", "AIRPORT", "CITY", "STATE"]]
    #     rename it so that both dataframe have a common name to join on
    airports_origin = airports.rename(
        {
            "IATA_CODE": "origin",
            "AIRPORT": "origin airport",
            "CITY": "origin city",
            "STATE": "origin state",
        },
        axis=1,
    )
    airports_dest = airports.rename(
        {
            "IATA_CODE": "dest",
            "AIRPORT": "dest airport",
            "CITY": "dest city",
            "STATE": "dest state",
        },
        axis=1,
    )
    #     merge dataframes on common column
    flight1 = pd.merge(flights, airports_origin, on="origin")
    flight2 = pd.merge(flight1, airports_dest, on="dest")
    #     groupby data on origin city with delay as dest city
    groupby_data = flight2.groupby("origin city")["dest city"]
    #     use describe fumction on grouped data and resetting index
    final_data = groupby_data.describe().reset_index()
    #     return 1st row of dataframe
    list_of_cities= [final_data["origin city"][0], final_data["top"][0]]
    return list_of_cities


# In[12]:


# two most connected cities are --'New York', 'Chicago'


# In[13]:


if __name__ == '__main__':
    print(total_days(flights))
    print(departure_cities(airports, flights))
    print(relationship(planes, flights))
    print(manufacturer_delay(planes, flights))
    print(most_connected_cities(flights, airports))


# In[14]:


# how many total number of days does the flights table cover?
# how many departure cities (not airports) does the flights database cover?
# what is the relationship between flights and planes tables?
# which airplane manufacturer incurred the most delays in the analysis period?
# # which are the two most connected cities?


# In[15]:


# 365
# 2
# ['tailnum', 'year']
# EMBRAER
# ['New York', 'Chicago']

