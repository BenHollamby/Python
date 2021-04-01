#Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in
#the first file and three names of dogs in the second file. Write a program that tries to read these
#files and print the contents of the file to the screen. Wrap your code in a try-except block to
#catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
#files to a different location on your system, and make sure the code in the except block
#executes properly.
catfile = "catfile.txt"
dogfile = "dogfile.txt"

while open(catfile, 'w') as file_object:
    cat_content = file_object.write("Pork Chop\n Tiger\n La'FaShe")

while open(dogfile, 'w') as f:
    dog_content = f.write("Barney\nJack\nDuke")




#Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if
#either file is missing.



#Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts
#you’d like to analyze. Download the text files for these works, or copy the raw text from your
#browser into a text file on your computer.
