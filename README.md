# Sudoku_Solver
The following project aims to develop the gui based app that can be used to solve sudoku by just taking the image from user's mobile camera and give the 
solution instantly.

### Why this project is important?
This project is good enough to be in someone's resume because it comprises of algorithms(backtracking), Image processing(extraction of sudoku and numbers) 
machine learning (CNN) for digit recognition and finally GUI.

### Methodology
* Algorithm for solving the sudoku - we have used backtracking with recursive function concept in order to solve the given sudoku.
* Extraction the sudoku from given image - opencv is used in order to detect sudoku and extract it.
* Extracting numbers image from sudoku - grid is sliced in order to get image of each number and then enhanced for furthur work.
* Predicting each image - CNN model is trained on mnist daatset of handwritten digits and 98% acracy is achieved on validation set but somehow
the model is not giving perfect predictions. Hence,project is not completed yet.

### Results
#### Input Image

#### After Threshold

#### Cropped Image

#### Cropped Numbers from Sudoku

#### Sudoku_Algorithm_input(array)

#### Output
