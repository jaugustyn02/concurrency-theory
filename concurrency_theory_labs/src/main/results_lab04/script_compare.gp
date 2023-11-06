# Set the terminal to PNG with a specific resolution
set terminal pngcairo enhanced size 1000,600   # Adjust the size as needed
set output 'output.png'


# Set properties for the plot
set style fill solid 0.25 border
set style boxplot outliers pointtype 7

# Define the data files and columns
datafiles = "BOTH_100.csv ASYMMETRIC_100.csv ARBITER_100.csv MODIFIED_ARBITER_100.csv"
column_average_time = 2

# Create a function to clean up the plot titles
clean_title(filename) = system(sprintf("echo %s | sed 's/_/ /g'", filename))

# Label the y-axis
set ylabel "Average Waiting Time (ns)"

# Move the legend to the right-down corner
set key right bottom

# Create the box plot with names underneath
plot for [i=1:words(datafiles)] word(datafiles, i) using (i):column_average_time with boxplot title clean_title(word(datafiles, i))

set output
