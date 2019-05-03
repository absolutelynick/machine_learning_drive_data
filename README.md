# Machine Learning using Behavioural Cloning

This was a test of concept flowing a Udemy tutorial [Applied Deep Learning - The complete self-driving car course](https://www.udemy.com/applied-deep-learningtm-the-complete-self-driving-car-course). The goal was to gather data driving a car around a track and then using Keras (a wrapper for Tensorflow) teach the car how to drive itself.

Keras and Tensorflow and can be run on [Googles Collaboratory](https://colab.research.google.com) saving on GPU and computational power locally. Otherwise your local Anaconda shell using Python3 will work just fine.

## My Google Collaboratory Created Notebook

This was the code that was used to make my machine learning model.

[Behavioural_Cloning.ipynb](https://github.com/absolutelynick/machine_learning_drive_data/blob/master/Behavioural_Cloning.ipynb)

## Research

[Nvidia Developer Blog](https://devblogs.nvidia.com/deep-learning-self-driving-cars/)

[End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)

## Simulator

Download For [Windows](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58983318_beta-simulator-windows/beta-simulator-windows.zip) or [Linux](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58983558_beta-simulator-linux/beta-simulator-linux.zip) or [Mac](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58983385_beta-simulator-mac/beta-simulator-mac.zip)

Extract the zip file anywhere you like and you can fire the simulator from **beta_simulator.exe**

## Dependencies Locally

To run locally with Anaconda run these commands in your Terminal.

```bash
conda install imgaug

conda install openCV

conda install tensorflow

conda install keras
```


## Dependencies on Colab

Image augment will be the only item that isn't provided as standard.

```
!pip3 install imgaug
```

## Testing my model

Open your Anaconda shell and type in the following commands after navigating to and saving the files in a folder:

```bash
git clone https://github.com/absolutelynick/machine_learning_drive_data

cd machine_learning_drive_data

python3 drive.py
```

And run the simulator in the Autonomous mode and Enjoy!

![](/image_data/prediction.PNG "The Prediction from my model")
