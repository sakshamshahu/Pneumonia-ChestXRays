# Pneumonia Chest X-Rays
### The Model

The model is based on a CNN built through  the libraries Keras and TensorFLow. The CNN consists of 2 dense and convolutional layers of size 64 each.
The dataset has been ran through the model 40 times with batch size of 100 for each interation. The loss function used is the binary-cross entropy function, which is primary used in instances where the class division is binary.

The metrics generated for the model are: 
```loss: 0.0024 - accuracy: 1.0000 - val_loss: 0.2683 - val_accuracy: 0.9251```

