# Sudoku_Solver
The following project aims to develop the gui based app that can be used to solve sudoku by just taking the image from user's mobile camera and give the 
solution instantly.

## Try yourself at
https://sudoku-solv.herokuapp.com/

### Why this project is important?
This project is good enough to be in someone's resume because it comprises of algorithms(backtracking), Image processing(extraction of sudoku and numbers) 
machine learning (CNN) for digit recognition and finally GUI.

### Methodology
* Algorithm for solving the sudoku - we have used backtracking with recursive function concept in order to solve the given sudoku.
* Extraction the sudoku from given image - opencv is used in order to detect sudoku and extract it.
* Extracting numbers image from sudoku - grid is sliced in order to get image of each number and then enhanced for furthur work.
* Predicting each image - CNN model is trained on mnist daatset of handwritten digits and 98% acracy is achieved on validation set but somehow
the model is not giving perfect predictions. Hence,project is not completed yet.

### IN Process Images
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

#### Output
![1](https://user-images.githubusercontent.com/46081301/92573329-446ff380-f2a3-11ea-8cc3-88fe927e270d.jpeg)


## Web App
![Screenshot from 2020-09-09 13-50-24](https://user-images.githubusercontent.com/46081301/92573520-8ac55280-f2a3-11ea-94ba-e3faed5733c6.png)
![Screenshot from 2020-09-09 13-50-48](https://user-images.githubusercontent.com/46081301/92573530-8d27ac80-f2a3-11ea-991a-cda0d67075ad.png)
![Screenshot from 2020-09-09 13-51-07](https://user-images.githubusercontent.com/46081301/92573542-9153ca00-f2a3-11ea-9346-07d6729ffdcb.png)

## Video Demo 
[<img src="https://img.youtube.com/vi/r8ZjVVI6AtU/maxresdefault.jpg" width="50%">](https://youtu.be/r8ZjVVI6AtU)

#### Docker Image Pull Command
docker pull pushkarasharma11/sudoku_solver:1.0


