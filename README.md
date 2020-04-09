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
![input](https://user-images.githubusercontent.com/46081301/78917426-77bc1580-7aac-11ea-8fd2-29349c52f9dd.JPG)

#### After Threshold
![threh](https://user-images.githubusercontent.com/46081301/78917430-78ed4280-7aac-11ea-90da-84e5dc4af571.JPG)

#### Cropped Image
![crop](https://user-images.githubusercontent.com/46081301/78917438-7ab70600-7aac-11ea-9ba4-255c08a5c750.JPG)

#### Cropped Numbers from Sudoku

![c1](https://user-images.githubusercontent.com/46081301/78917446-7d196000-7aac-11ea-8e95-5435fbf2602c.JPG)
![c2](https://user-images.githubusercontent.com/46081301/78917450-7db1f680-7aac-11ea-958c-ed15de5c10d6.JPG)
![c3](https://user-images.githubusercontent.com/46081301/78917457-7ee32380-7aac-11ea-819b-c47343634082.JPG)

#### Sudoku_Algorithm_input(Not the same image from above)
![Capture1](https://user-images.githubusercontent.com/46081301/78917367-67a43600-7aac-11ea-9b6e-ccdfd1f4ca49.JPG)

#### Output
![Capture2](https://user-images.githubusercontent.com/46081301/78917393-6ffc7100-7aac-11ea-955c-42924a0e0b7b.JPG)

### Note
The final output is displayed only to show that algorithm works fine but the problem is with CNN prediction.
### I will try my best to complete it as soon as possible.
