
# WHAT I LEARNT

This repo is the 2nd repo of the same project. The first repo got deleted because I started it with an Anaconda virtual environment, and once I had to introduce MySQL to the project, Anaconda turned out to be non-reliable. I knew Anaconda is more skewed toward Data science and ML but I had no idea it was reluctant toward MySQL.  
Lesson learnt on my side. 

#### PROJECT DETAILS:  

VENV Manager: pipenv  
Python: v3.11  
Database: MySQL + DataGrip  

---

## Title 1

text

---

## Structure of the Data Model

The best approach consists of 2 things:  
- minimal coupling between apps
- high cohesion in each app  

By having a smaller number of apps, we decrease the need for coupling (while trying to avoid piling functionalities, which leads to the creation of a monolith-like structure).  

By not having only one app (a monolith) that does it all, we increase the cohesion of each separate app.  

It becomes obvious that there is a **fine line between these two things**, and the balance is not always clear. 

#### Our Data Structure:

So here, we decided on the following:
- store app: cart, cart items, order, customer, collections, products:  
  because all of these items are strongly related to one another
- tag app: for generic relationships (usable independently)

---

## Introduction to MYSQL

Here I only just touched the surface of Databases. Installing MYSQL and DataGrip and creating a new database in DataGrip.  
Why DataGrip? Just because the course I am following is using it. But MYSQL Workbench is an alternative (though less optimal, according to the course). 

--- 

## Title 3

Text

--- 

## How Well Did I do?

After I compared my code to the solutions: 
- **exercise **:  
  Text 

  GRADE: Text. 

- **exercise **:  
  Text. 

- **exercise **:

#### Resources:
[Code with Mosh Online Course: Ultimate Django](codewithmosh.com/courses/the-ultimate-django-part1-1)  
[DataGrip from Jetbrains](https://www.jetbrains.com/datagrip/download/download-thanks.html?platform=windows)  
[MySQL](https://dev.mysql.com/downloads/windows/)  

