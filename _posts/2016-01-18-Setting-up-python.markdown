---
layout: post
title:  "Setting up IPython Notebook" 
date:   2016-01-18 14:00:00
categories: Lecture notes
---

The lecture is written in IPython Notebook format. You will quickly see that you can edit these notebooks yourself to add your own notes and do the exercises. You can view the first lecture's notebook directly using [nbviewer](http://nbviewer.ipython.org/github/ggorman/Numerical-methods-1/blob/master/notebook/interpolation.ipynb) or [download the notebook here](http://raw.githubusercontent.com/ggorman/Numerical-methods-1/master/notebook/interpolation.ipynb) (Note: you may need to right-click and use *Save Link As...*).

### Initial setup
We recommend that you download the notebooks for the lecture and store them in the H: drive. 

1. Create a folder on the H: drive called `notebooks` (or any other sensible name) in the file explorer:
![Create a new folder](https://raw.githubusercontent.com/ggorman/Numerical-methods-1/gh-pages/images/new_folder_on_h_drive.jpg "Create a new folder called 'notebooks' on your H: drive.")

2. At the beginning of each lecture, download the relevant `.ipynb` file and place it in this folder. Once you've saved the notebook, you can open it using Anaconda.
This is already installed in the computer lab. You can also installed it on your personal computer for free - see instructions below:

### [Continuum Analytics - Anaconda](https://store.continuum.io/cshop/anaconda/)
1. First, we strongly recommend setting your default browser to Google Chrome or Firefox. In Firefox, go to *Tools* > *Options* > *Advanced* tab, and click the *Make Firefox the default browser* button. In Chrome, go to the *Settings* window and click *Make Google Chrome the default browser*.

2. From the Windows Start menu, search for and open the `cmd` command line tool:
![cmd](https://raw.githubusercontent.com/ggorman/Introduction-to-programming-for-geoscientists/gh-pages/images/cmd_menu_item.jpg "The cmd command line tool.")

3. At the command line, type the following 3 commands, pressing Enter after each one:<br>
```
H:
```<br>
```
cd notebooks
```<br>
```
ipython notebook
```<br>
This will start up IPython Notebook in your default web browser. From there you should see the `.ipynb` files that you have saved in the `notebooks` folder.

