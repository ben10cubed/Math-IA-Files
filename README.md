# Math-IA-Files
Here are the programs and photos used for my Maths IA.
There are quite a few programs that were used. Here are some guides to run them if required.
Please note, not all the files I have used will be attached. For example, some programs used to draw sin graphs can easily be done in other software.

# Maths IA Data
This Excel spreadsheet contains the original data as well as the important sections of the processed data.
This will likely be difficult to understand as it is my own rough work along with my thought processes.
It does contain Longitude and Latitude calculations that are not shown in the IA.

# Ocean Current Picture
The pic.PNG file contains an image of the ocean currents from the Earth Nullschool website.
This has been properly credited in my IA document, but here is the citation:
Beccario, Cameron. “A Global Map of Wind, Weather, and Ocean Conditions.” A Visualization of Global Weather Conditions, earth.nullschool.net/. Accessed 28 Feb. 2024. 

# Streamline Files
These files contain programs that generate the data required to plot streamlines.
As the name of the files suggest, "Euler Polynomial" is for the polynomial model while "Euler Sin" is for the sin model.
To run this, please put each of these folders in a separate, newly created folder. These generate quite a lot of text files.
To compile the data into an Excel spreadsheet, copy the "excelCreate" file into the respective directories and run the program.

With the Excel spreadsheet, the MATLAB program "Eulers.m" can be used. This file should be in its own file as well.
pic.PNG and the Excel spreadsheet should be copied into this trajectory.
Simply run the program and the streamlines should be drawn.
I am unable to provide all iterations of this program but for some instances, the color of the lines can be changed manually.

# Other Files
There are two other files that I have included that are relatively important.
The first one is "LinearTransformation.m" which is a MATLAB program used to solve for the linear transformation matrix.
Simply run it and the matrix will be outputted which should be the same as the one in the IA.

The second one is "DrawModel.m" which is another MATLAB program used to draw vectors from the various models over the raw image.
For this, uncomment different models and run the program to view these models. 
Only leave one model uncommented, and do not touch the other sections of the code.
