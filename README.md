# Visualizing_NRC_Allegation_Intake_Data
'''
This code was written to serve as an interface to visualize the allegations intake
processed by the NRC at nuclear reactors across the country from 2013-2017. 
The data is publicly available and can be found  at: 
    
    https://www.nrc.gov/about-nrc/regulatory/allegations/statistics.html 
    

This interface successfully run using:
Bokeh 0.12.9
Python 3.6.2


Interface written by Shadi Ghrayeb of the U.S. Nuclear Regulatory Commission (USNRC) 
contact: 
Shadi Ghrayeb
Shadi.Ghrayeb@nrc.gov / ghrays@gmail.com


Easiest way to run this interface is to download ANACONDA from www.continuum.io/downloads
Open a terminal to the directory where these file exist and enter following command: 
    
    bokeh serve --show main.py
    
After entering the above command a browser should appear displaying the interface using the following url: 
    
    http://localhost:5006/main
    
When running on windows machine there have been issues using the Internet Explorer browser. Try alternative browsers by 
entering the above url into Chrome, FireFox, etc. 

'''
