# W.B.I.P
### A Graphical User Interface using tkinter module in python.
### Project Features:

  -> W - Wordle
      Wordle is a word guessing game, in which you have to guess the 5 letter word in 6 tries. After every attempt, the letters are color coded. (green - the letter exists in the word and is in the right position, yellow - the letter exists in the word but is in the wrong position)
      
  -> B - Bank
      Here we have used the concept of Classes and objects and the "with open()" method in python to simulate a banking experience and to save the log history.
      
  -> I - Image Compressor
      Image Compressor solves the hassles of looking for ways to compress image size or even the dimensions of an image. In this part, we have created an easy way to download an image of desired dimensions.
      
  -> P - Pokemon Battle
      This is a game, an attempt to recreate the pokemon cards game, where 2 players battle against each other with a pokemon, and the winner is decided according to a few stats of the pokemon.
      Libraries/Concepts covered:
      - API fetching
      In terminal:<br>
      
  ```python
  pip install requests
  ```
    
  <br>Import:<br>
      
  ```python
  import requests
  ```
      
  <br>To fetch API (assuming that you have the api link):<br>
  
  ```python
  data = requests.get("the api link which you have")
  data.json()
  ```
