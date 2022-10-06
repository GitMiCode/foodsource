# Food Source

[pydish.com](http://pydish.com) Is a web page built using PyScript, Python and JavaScript.
Please be advised that PyScript is very alpha and under heavy development. 
PyScript is a brand-new framework that works directly with Python.
Build interactive front-end apps using Python and JavaScript

Foodsource is a quck glimpse into our current food situation.  
U.S. farm outputs and food shortages and prices.

### Requirements:
The latest versions of your web browser should work.
Testing was done with Google Chrome and MS Edge.

### Setup:
- Run `git clone https://github.com/GitMiCode/foodsource.git`to clone the resposity.
  ***This may not be needed as there are minimal files to deal with.***
- The requests library is needed to run fmkt.py or fmkt.ipynb.

### Instructions:
- Start by visiting the project web page at [pydish.com](http://pydish.com), this will host most of the project.
  - The page will end with links to search for farmers makets in your area.  
    This will bring you back to the foodsource repo for files fmkt.py or fmkt.ipynb.

### Notes:
- The web page pydish.com (index.html) will take 10 - 20 seconds to load.
- Matplotlib and Seaborn plots will be displayed on page.  To view code for them please review the index.html source code.
  The libraries needed for these plots will be included with the page.  Nothing should be required to view them.
  - pandas
  - matplotlib
  - seaborn

### Project Requirements Met
- Table 1 Read data
  - Read csv for Matplotlib plot
  - Read different CSV for seaborn plot
  - WSDL request for (json) farmers market search 
- Table 2 Manipulate and clean your data
  - Created list of columns and dropped them
  - Created list of rows and dropped them
  - Used dropna to drop empty rows
- Table 3 Analyze your data
  - Difference in egg catagory
  - Average in egg catagory
  - Total in egg catagory
  - Column count for egg DF
  - Row count in for egg DF
- Table 4 Visualize you Data
  - Created one Matplotlib plot
  - Created one Seaborn plot
- Table 5 Interpret your data and graphical output.
  - Project shows that farm output in the US keeps increasing in production, but food prices is 
    on the rise. One way to combat this is to utilize farmers markets. 
