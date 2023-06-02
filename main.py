
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
clock = pygame.time.Clock()
words = []
score = 0
current_word = ""
word_complete = True
round_num = 1
word_speed = 2
current_word_color = BLACK
description_text_raw = ''

# Common Python words
python_words = [
    "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else",
    "except", "finally", "for", "from", "global", "if", "import", "in", "is",
    "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield", "zip", "enumerate", "random", "normal", "choice",
    "async", "await", "coroutine", "decorator", "generator", "yield", "self",
    "range", "map", "filter", "reduce", "lambda", "global", "nonlocal", "pass",
    "assert", "True", "False", "del", "with", "as", "try", "except", "finally",
    "super", "isinstance", "issubclass", "breakpoint", "continue", "bytes", "bytearray",
    "str", "int", "float", "list", "tuple", "set", "dict", "bool", "complex",
    "len", "print", "input", "open", "file", "os", "sys", "math", "random", "time"
]

# Common R programming words
r_words = [
    "if", "else", "for", "while", "repeat", "function", "return", "break", "next",
    "numeric", "integer", "double", "logical", "character", "list", "vector", "matrix",
    "data.frame", "factor", "c", "length",
    "sum", "mean", "median", "sd", "var", "quantile", "apply", "lapply", "sapply",
    "tapply", "split", "subset", "merge", "aggregate", "by", "order", "sort", "unique",
    "grep", "sub", "gsub", "paste", "sprintf",
    'filter', 'select', 'arrange', 'mutate', 'summarize',
    "ifelse", "switch", "apply", "lapply", "sapply", "tapply", "mapply", "replicate",
    "aggregate", "merge", "rbind", "cbind", "subset", "transform", "reshape", "melt",
    "cast", "grep", "gsub", "strsplit", "paste", "sprintf", "write", "read", "csv",
    "json", "xml", "data.table", "dplyr", "tidyr", "ggplot2", "reshape2", "stringr",
    "forcats", "zoo", "caret", "lm", "glm", "xgboost", "kmeans",
    "hclust", "ks.test", "t.test", "wilcox.test", "anova", "cor", "cov", "anova",
    "chisq.test", "binom.test", "poisson.test"
]

# Common VBA words
vba_words = [
    "Sub", "Function", "Dim", "As", "Integer", "String", "Double", "Long", "Boolean",
    "If", "Then", "Else", "ElseIf", "End", "For", "To", "Step", "Next", "Do", "While",
    "Loop", "Exit", "Select", "Case", "With", "Set", "Range", "Cells", "ActiveCell",
    "ActiveSheet", "Workbook", "Worksheets", "Application", "MsgBox", "InputBox",
    "MsgBox", "InputBox", "Const", "Exit", "Error", "Resume", "On", "Error", "GoTo",
    "Err", "Err.Description", "Err.Number"
]
vba_words = [word.lower() for word in vba_words]

# Common MATLAB commands
matlab_words = [
    "clc", "clear", "close", "figure", "plot", "hold", "grid", "xlabel", "ylabel",
    "title", "legend", "subplot", "axis", "xlim", "ylim", "text", "annotation",
    "gca", "gcf", "get", "set", "pause", "waitforbuttonpress", "input", "disp",
    "fprintf", "format", "fopen", "fclose", "fscanf", "fwrite", "fread", "feof",
    "ferror", "csvread", "csvwrite", "xlsread", "xlswrite", "load", "save", "whos",
    "size", "length", "numel", "find", "ismember", "unique", "sort", "min", "max",
    "sum", "mean", "median", "std", "var", "corrcoef", "cov", "fft", "ifft", "abs",
    "real", "imag", "angle", "conj", "transpose", "inv", "det", "eig", "svd", "lu",
    "qr", "chol", "polyfit", "polyval", "roots", "interp1", "lsqcurvefit", "ode45",
    "integral", "diff", "gradient", "meshgrid", "contour", "surf", "imshow", "imread",
    "imwrite", "imfilter", "imresize", "imadjust", "rgb2gray", "gray2rgb", "im2bw",
    "bwlabel", "regionprops", "imfill", "imopen", "imclose", "imerode", "imdilate",
    "bwmorph", "imregionalmax", "imregionalmin", "imhmax", "imhmin", "watershed",
    "edge", "corner", "histogram", "fspecial", "vision.VideoPlayer", "vision.VideoFileReader",
    "vision.VideoFileWriter", "vision.BlobAnalysis", "vision.ForegroundDetector",
    "vision.PeopleDetector", "vision.ShapeInserter", "vision.PointTracker"
]



# Descriptions for Python commands
python_descriptions = {
    "and": "Logical operator that returns `True` if both conditions are `True`.",
    "as": "Used for aliasing a module or import statement.",
    "assert": "Used for debugging and testing code conditions.",
    "break": "Terminates the current loop and resumes execution at the next statement.",
    "class": "Defines a class.",
    "continue": "Skips the rest of the code inside a loop and continues to the next iteration.",
    "def": "Defines a function.",
    "del": "Deletes a reference or object.",
    "elif": "Used in conditional statements, similar to an else-if statement.",
    "else": "Executes if the condition in an if statement is `False`.",
    "except": "Catches exceptions that occur in try blocks.",
    "finally": "Specifies a block of code that will be executed regardless of the try and except blocks.",
    "for": "Loops over a sequence or iterable.",
    "from": "Used for importing specific attributes or functions from a module.",
    "global": "Declares a global variable inside a function.",
    "if": "Executes a block of code if a certain condition is `True`.",
    "import": "Imports a module.",
    "in": "Checks if a value is present in a sequence or collection.",
    "is": "Tests if two variables refer to the same object.",
    "lambda": "Creates an anonymous function.",
    "nonlocal": "Declares a nonlocal variable inside a nested function.",
    "not": "Returns `True` if a condition is `False`.",
    "or": "Logical operator that returns `True` if at least one condition is `True`.",
    "pass": "Placeholder statement that does nothing.",
    "raise": "Raises an exception.",
    "return": "Specifies the value to be returned from a function.",
    "try": "Specifies a block of code to be tested for errors.",
    "while": "Executes a block of code as long as a certain condition is `True`.",
    "with": "Used for efficient handling of file streams or resources.",
    "yield": "Pauses the execution of a function and yields a value to its caller.",
    "zip": "Returns an iterator that aggregates elements from multiple iterables.",
    "enumerate": "Returns an iterator of tuples containing indices and values from an iterable.",
    "random": "Generates random numbers.",
    "normal": "Generates random numbers from a normal (Gaussian) distribution.",
    "choice": "Returns a randomly selected element from a non-empty sequence.",
    "async": "Used to define a coroutine, an asynchronous function.",
    "await": "Used to pause the execution of a coroutine until it returns a result.",
    "coroutine": "Defines a coroutine, an asynchronous function.",
    "decorator": "Modifies the behavior of a function or class.",
    "generator": "Creates an iterator by defining a function with `yield` statements.",
    "self": "A reference to the instance of a class within a method.",
    "range": "Generates a sequence of numbers.",
    "map": "Applies a function to each item in an iterable and returns an iterator of the results.",
    "filter": "Filters an iterable by applying a function to each item and returning the items that evaluate to `True`.",
    "reduce": "Applies a function of two arguments cumulatively to the items of an iterable.",
    "open": "Opens a file and returns a file object.",
    "read": "Reads the contents of a file.",
    "write": "Writes data to a file.",
    "append": "Adds an element to the end of a list.",
    "extend": "Appends elements from an iterable to the end of a list.",
    "pop": "Removes and returns the last element of a list.",
    "remove": "Removes the first occurrence of a value from a list.",
    "insert": "Inserts an element at a specified position in a list.",
    "clear": "Removes all elements from a list.",
    "sort": "Sorts the elements of a list in ascending or descending order.",
    "reverse": "Reverses the order of elements in a list.",
    # Add more command descriptions here...
}



# Descriptions for R commands
r_descriptions = {
    "ifelse": "Applies a condition to each element of a vector or array, and returns values based on the condition.",
    "for": "Creates a loop that iterates over a sequence of values.",
    "while": "Creates a loop that continues until a certain condition is met.",
    "repeat": "Creates an infinite loop that can be stopped using the `break` statement.",
    "break": "Stops the execution of a loop.",
    "next": "Skips the current iteration of a loop and continues to the next iteration.",
    "function": "Defines a function.",
    "return": "Specifies the value to be returned from a function.",
    "print": "Displays output on the console.",
    "cat": "Concatenates and prints strings or objects.",
    "paste": "Concatenates strings.",
    "length": "Returns the number of elements in a vector or the number of characters in a string.",
    "class": "Displays the class of an object or assigns a class to an object.",
    "typeof": "Returns the type of an object.",
    "is.na": "Checks if an object is `NA` (missing value).",
    "is.null": "Checks if an object is `NULL`.",
    "is.vector": "Checks if an object is a vector.",
    "is.list": "Checks if an object is a list.",
    "is.matrix": "Checks if an object is a matrix.",
    "is.data.frame": "Checks if an object is a data frame.",
    "is.function": "Checks if an object is a function.",
    "is.character": "Checks if an object is a character vector.",
    "is.numeric": "Checks if an object is a numeric vector.",
    "is.logical": "Checks if an object is a logical vector.",
    "is.integer": "Checks if an object is an integer vector.",
    "is.factor": "Checks if an object is a factor.",
    "is.numeric": "Checks if an object is a numeric vector.",
    "c": "Concatenates values into a vector or combines multiple vectors into a single vector.",
    "seq": "Generates a sequence of values.",
    "rep": "Replicates values or vectors.",
    "sum": "Calculates the sum of values in a vector.",
    "mean": "Calculates the mean (average) of values in a vector.",
    "median": "Calculates the median of values in a vector.",
    "max": "Finds the maximum value in a vector.",
    "min": "Finds the minimum value in a vector.",
    "sort": "Sorts the elements of a vector in ascending order.",
    "rev": "Reverses the order of elements in a vector.",
    "unique": "Returns the unique elements of a vector.",
    "subset": "Extracts a subset of a vector or a data frame based on specified conditions.",
    "attach": "Attaches a data frame to the search path.",
    "detach": "Detaches a data frame from the search path.",
    "read.csv": "Reads a CSV file and returns a data frame.",
    "write.csv": "Writes a data frame to a CSV file.",
    # Add more command descriptions here...
}


# Descriptions for VBA commands
vba_descriptions = {
    "Sub": "Defines a subroutine, a block of code that performs a specific task.",
    "Function": "Defines a function, a block of code that returns a value.",
    "Dim": "Declares a variable or an array.",
    "As": "Specifies the data type of a variable or a function's return type.",
    "Integer": "Specifies a variable or array of whole numbers (integers).",
    "String": "Specifies a variable or array of text values (strings).",
    "Double": "Specifies a variable or array of double-precision floating-point numbers.",
    "Long": "Specifies a variable or array of long integer numbers.",
    "Boolean": "Specifies a variable or array of Boolean (True/False) values.",
    "If": "Performs a conditional execution of code based on a specified condition.",
    "Then": "Indicates the code to be executed if a condition is true.",
    "Else": "Indicates the code to be executed if a condition is false.",
    "ElseIf": "Indicates an alternative condition to be checked if the previous conditions are false.",
    "End": "Indicates the end of a block of code or terminates a statement.",
    "For": "Creates a loop that executes a block of code a specified number of times.",
    "To": "Specifies the upper limit of a `For` loop.",
    "Step": "Specifies the increment or decrement value for a `For` loop.",
    "Next": "Indicates the end of a `For` loop or advances the loop to the next iteration.",
    "Do": "Creates a loop that continues until a certain condition is met.",
    "While": "Creates a loop that continues while a certain condition is true.",
    "Loop": "Indicates the end of a `Do` or `While` loop.",
    "Exit": "Terminates a loop or a block of code.",
    "Select": "Executes one of many possible blocks of code, depending on the value of an expression.",
    "Case": "Specifies a value or a range of values to be tested in a `Select` statement.",
    "With": "Specifies a particular object and allows access to its properties and methods without explicitly qualifying the object.",
    "Set": "Assigns an object reference to a variable.",
    "Range": "Represents a cell, a range of cells, or a collection of ranges in Excel.",
    "Cells": "Represents a range of cells in Excel.",
    "ActiveCell": "Represents the currently active cell in Excel.",
    "ActiveSheet": "Represents the currently active worksheet in Excel.",
    "Workbook": "Represents an Excel workbook.",
    "Worksheets": "Represents the collection of worksheets in an Excel workbook.",
    "Application": "Represents the Excel application.",
    "MsgBox": "Displays a message box with a specified message.",
    "InputBox": "Displays an input box to prompt the user for input.",
    "Const": "Declares a constant variable with a fixed value.",
    "Error": "Provides information about the most recent error that occurred.",
    "Resume": "Resumes execution at a specified point in code after an error has occurred.",
    "On": "Enables or disables error handling for a specific type of error.",
    "GoTo": "Transfers control to a specified line label or line number.",
    "Err": "Returns an error object that provides information about the most recent error that occurred.",
    "Err.Description": "Returns a string that describes the error that occurred.",
    # Add more command descriptions here...
}
vba_descriptions = {key.lower(): value for key, value in vba_descriptions.items()}

# Descriptions for Matlab commands

matlab_descriptions = {
    "clc": "Clears the command window.",
    "clear": "Removes variables from memory.",
    "close": "Closes a figure window.",
    "figure": "Creates a new figure window.",
    "plot": "Plots a 2D graph.",
    "hold": "Holds the current graph on the figure.",
    "grid": "Displays gridlines on the graph.",
    "xlabel": "Labels the x-axis.",
    "ylabel": "Labels the y-axis.",
    "title": "Adds a title to the graph.",
    "legend": "Adds a legend to the graph.",
    "subplot": "Creates subplots within a figure.",
    "axis": "Sets or gets the axis limits.",
    "xlim": "Sets or gets the x-axis limits.",
    "ylim": "Sets or gets the y-axis limits.",
    "text": "Adds text annotations to the graph.",
    "annotation": "Adds annotations to the graph.",
    "gca": "Gets the current axes handle.",
    "gcf": "Gets the current figure handle.",
    "get": "Gets the value of a property.",
    "set": "Sets the value of a property.",
    "pause": "Pauses program execution.",
    "waitforbuttonpress": "Waits for a mouse or keypress.",
    "input": "Prompts the user for input.",
    "disp": "Displays output in the command window.",
    "fprintf": "Formats and displays text.",
    "format": "Controls screen output format.",
    "fopen": "Opens a file.",
    "fclose": "Closes a file.",
    "fscanf": "Reads formatted data from a file.",
    "fwrite": "Writes binary data to a file.",
    "fread": "Reads binary data from a file.",
    "feof": "Checks end-of-file status.",
    "ferror": "Checks for file I/O errors.",
    "csvread": "Reads data from a CSV file.",
    "csvwrite": "Writes data to a CSV file.",
    "xlsread": "Reads data from an Excel file.",
    "xlswrite": "Writes data to an Excel file.",
    "load": "Loads variables from a MAT file.",
    "save": "Saves variables to a MAT file.",
    "whos": "Lists variables in memory.",
    "size": "Returns the size of an array.",
    "length": "Returns the length of a vector.",
    "numel": "Returns the number of elements in an array.",
    "find": "Finds indices of nonzero elements.",
    "ismember": "Checks if elements are members of a set.",
    "unique": "Returns unique elements in an array.",
    "sort": "Sorts an array in ascending order.",
    "min": "Finds the minimum value.",
    "max": "Finds the maximum value.",
    "sum": "Calculates the sum of elements.",
    "mean": "Calculates the mean of elements.",
    "median": "Calculates the median of elements.",
    "std": "Calculates the standard deviation of elements.",
    "var": "Calculates the variance of elements.",
    "corrcoef": "Calculates the correlation coefficient.",
    "cov": "Calculates the covariance matrix.",
    "fft": "Computes the discrete Fourier transform.",
    "ifft": "Computes the inverse discrete Fourier transform.",
    "abs": "Computes the absolute value.",
    "real": "Extracts the real part of a complex number.",
    "imag": "Extracts the imaginary part of a complex number.",
    "angle": "Computes the phase angle of a complex number.",
    "conj": "Computes the complex conjugate.",
    "transpose": "Transposes an array.",
    "inv": "Computes the inverse of a matrix.",
    "det": "Computes the determinant of a matrix.",
    "eig": "Computes the eigenvalues and eigenvectors of a matrix.",
    "svd": "Computes the singular value decomposition.",
    "lu": "Computes the LU decomposition.",
    "qr": "Computes the QR decomposition.",
    "chol": "Computes the Cholesky decomposition.",
    "polyfit": "Fits a polynomial to data points.",
    "polyval": "Evaluates a polynomial.",
    "roots": "Finds the roots of a polynomial.",
    "interp1": "Interpolates 1-D data.",
    "lsqcurvefit": "Fits a curve to data points.",
    "ode45": "Solves ordinary differential equations.",
    "integral": "Calculates the integral of a function.",
    "diff": "Calculates the derivative of a function.",
    "gradient": "Calculates the gradient of a function.",
    "meshgrid": "Creates coordinate matrices.",
    "contour": "Creates contour plot.",
    "surf": "Creates surface plot.",
    "imshow": "Displays an image.",
    "imread": "Reads an image from file.",
    "imwrite": "Writes an image to file.",
    "imfilter": "Applies a filter to an image.",
    "imresize": "Resizes an image.",
    "imadjust": "Adjusts image intensity values.",
    "rgb2gray": "Converts RGB image to grayscale.",
    "gray2rgb": "Converts grayscale image to RGB.",
    "im2bw": "Converts image to binary (black and white).",
    "bwlabel": "Labels connected components in a binary image.",
    "regionprops": "Measures properties of image regions.",
    "imfill": "Fills image regions.",
    "imopen": "Performs morphological opening.",
    "imclose": "Performs morphological closing.",
    "imerode": "Performs morphological erosion.",
    "imdilate": "Performs morphological dilation.",
    "bwmorph": "Applies morphological operations to binary images.",
    "imregionalmax": "Finds regional maxima in an image.",
    "imregionalmin": "Finds regional minima in an image.",
    "imhmax": "Enhances regional maxima in an image.",
    "imhmin": "Enhances regional minima in an image.",
    "watershed": "Performs image segmentation using watershed algorithm.",
    "edge": "Detects edges in an image.",
    "corner": "Detects corners in an image.",
    "histogram": "Computes the histogram of an image.",
    "fspecial": "Creates predefined filters.",
    "vision.VideoPlayer": "Plays video streams.",
    "vision.VideoFileReader": "Reads video data from a file.",
    "vision.VideoFileWriter": "Writes video data to a file.",
    "vision.BlobAnalysis": "Analyzes connected components in a binary image.",
    "vision.ForegroundDetector": "Detects foreground objects in a video sequence.",
    "vision.PeopleDetector": "Detects people in an image or video sequence.",
    "vision.ShapeInserter": "Inserts shapes into an image.",
    "vision.PointTracker": "Tracks points in an image sequence."
}



# Combine all the words
common_words = []

# Game mode selection
while not common_words:
    screen.fill(WHITE)
    mode_text = font.render("Select a Game Mode", True, RED)
    python_text = font.render("1 Python", True, BLUE)
    r_text = font.render("2 R", True, BLUE)
    vba_text = font.render("3 VBA", True, BLUE)
    matlab_text = font.render("4 Matlab", True, BLUE)
    screen.blit(mode_text, (WIDTH/3, HEIGHT/2 - 80))
    screen.blit(python_text, (WIDTH/3, HEIGHT/2 - 40))
    screen.blit(r_text, (WIDTH/3, HEIGHT/2))
    screen.blit(vba_text, (WIDTH/3, HEIGHT/2 + 40))
    screen.blit(matlab_text, (WIDTH/3, HEIGHT/2 + 80))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == '1':
                common_words = python_words
                descriptions = python_descriptions
            elif event.unicode == '2':
                common_words = r_words
                descriptions = r_descriptions
            elif event.unicode == '3':
                common_words = vba_words
                descriptions = vba_descriptions
            elif event.unicode == '4':
                common_words = matlab_words
                descriptions = matlab_descriptions

# Helper function to generate a random word starting with a different letter
def generate_word():
    used_letters = [word["word"][0] for word in words]
    available_words = [word for word in common_words if word[0] not in used_letters]
    if not available_words:
        return None
    word = random.choice(available_words)
    x = random.randint(10, WIDTH - 100)
    y = -random.randint(50, 250)
    return {"word": word, "position": (x, y), "typed_letters": []}


# Function to display the description of the current word
def display_description(word):
    if word in descriptions.keys():
        description_text = descriptions[word]
    else:
        description_text = "No description available"
    #description_text = font.render(description_text, True, BLACK)
    #screen.blit(description_text, (50,50))
    return(description_text)
    # screen.blit(description_text, (10, HEIGHT - description_text.get_height() - 10))


# Game loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                if word_complete:
                    # Start typing a new word
                    current_word = pygame.key.name(event.key)
                    word_complete = False
                else:
                    # Continue typing the current word
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_BACKSPACE:
                        pass
                    else:
                        if event.key == pygame.K_RETURN and current_word != '':
                            current_word = ''
                            for word in words:
                                word["typed_letters"] = []
                        else:
                            letter = pygame.key.name(event.key)
                            current_word += letter

                for word in words:
                    if word["word"].startswith(current_word):
                        if word["word"][len(current_word)-1] == pygame.key.name(event.key):
                            word["typed_letters"].append(pygame.key.name(event.key))
                            current_word_color = RED
                            display_description(word["word"])
                            description_text_raw = display_description(word["word"])

                            if len(word["typed_letters"]) == len(word["word"]):
                                words.remove(word)
                                score += 1
                                word_complete = True
                                current_word_color = GREEN
                            break

    # Update game state
    for word in words:
        x, y = word["position"]
        word["position"] = (x, y + word_speed)
        if word["position"][1] > HEIGHT:
            words.remove(word)
            score -= 1
            if not word_complete and current_word:
                current_word = ""
                word_complete = True

    # Generate new words
    if len(words) < 5 and word_complete:
        new_word = generate_word()
        if new_word:
            words.append(new_word)

    # Increase word speed every round
    if len(words) == 5 and not words and word_complete:
        round_num += 1
        word_speed += 1

    # Render the game
    screen.fill(WHITE)
    for word in words:
        word_text = font.render(word["word"], True, BLACK)
        screen.blit(word_text, word["position"])

    # Display the current word at the top middle of the screen
    current_word_text = font.render(current_word, True, current_word_color)
    screen.blit(current_word_text, (WIDTH/2 - current_word_text.get_width()/2, 10))

    score_text = font.render("Score: " + str(score), True, BLACK)
    #round_text = font.render("Round: " + str(round_num), True, RED)
    description_text = pygame.font.Font(None, 24).render(description_text_raw, True, RED)
    screen.blit(score_text, (10, 10))
    #screen.blit(round_text, (WIDTH - round_text.get_width() - 10, 10))
    screen.blit(description_text, (10,HEIGHT-50))

    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()