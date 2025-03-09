# Neural Network Implementations in Numpy, PyTorch and TensorFlow

## Assignment Overview
This repository contains implementations of a **3-layer deep neural network** for **non-linear regression** using various frameworks, including:

- **Numpy (from scratch with manual backpropagation)**
- **PyTorch (both from scratch and using class-based implementation)**
- **PyTorch Lightning**
- **TensorFlow (multiple approaches: low-level API, functional API, built-in layers, and high-level API)**

Additionally, the project follows the constraints and requirements specified in the assignment:
- **Using TensorFlow einsum instead of matrix multiplication**
- **Generating synthetic data using a 3-variable non-linear equation**
- **Visualizing data using a 4D plot**

---

## Repository Structure

The repository consists of three main folders:

### **Numpy Implementation** (`1_NeuralNetworks_NumPy/`)
- A 3-layer neural network built from scratch using NumPy, implementing manual backpropagation with chain rule-based gradient propagation.

### **PyTorch Implementations** (`2_NeuralNetworks_PyTorch/`)
- PyTorch version without built-in layers, defining a fully custom network.
- Using PyTorch's built-in modules for a cleaner and more scalable model.
- Implementation using PyTorch Lightning for structured training.

### **TensorFlow Implementations** (`3_NeuralNetworks_TensorFlow/`)
- TensorFlow implementation without high-level APIs, using `einsum` instead of matrix multiplication.
- Using TensorFlow’s built-in layers.
- Implementation using the Functional API.
- High-level API implementation.

---

## Implementations Overview

### **1. Numpy Implementation (From Scratch)**
- Implements a **3-layer neural network** for non-linear regression.
- Uses **manual backpropagation** and **chain rule-based gradient propagation**.
- Includes non-linear activation functions.
- Displays loss over epochs and final output.
- Uses synthetic 3-variable data visualization in **4D plot**.

[Notebook Links]
- [Neural Networks - NumPy](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/1_NeuralNetworks_NumPy/A_NumPy_3LayerNN_Non_LinearRegression.ipynb)

### **2. PyTorch Implementations**
- **From Scratch:** No built-in PyTorch layers, manual tensor operations.
- **Class-Based:** Uses `torch.nn.Module` for structured implementation.
- **Lightning Version:** More modular and scalable approach.

[Notebook Links]
- [PyTorch From Scratch]([notebooks/pytorch_nn.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/2_NeuralNetworks_PyTorch/B_PyTorch_3LayerNN.ipynb))
- [PyTorch Class-Based]([notebooks/pytorch_nn_classes.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/2_NeuralNetworks_PyTorch/C_PyTorch_Class_Based_3LayerDNN.ipynb))
- [PyTorch Lightning]([notebooks/pytorch_lightning_nn.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/2_NeuralNetworks_PyTorch/D_PyTprchLightning_3NN.ipynb))

### **3. TensorFlow Implementations**
- **Low-Level API:** No built-in layers, manual operations using TensorFlow.
- **Built-in Layers:** Uses `tf.keras.layers` for structured design.
- **Functional API:** Implements the model in a more modular way.
- **High-Level API:** Uses `tf.keras.Model` for efficient design.

[Notebook Links]
- [TensorFlow Variations]([notebooks/tensorflow_lowlevel.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/3_NeuralNetworks_TensorFlow/E_TensorFlow_Variants.ipynb))
- [TensorFlow Low-Level API]([notebooks/tensorflow_lowlevel.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/3_NeuralNetworks_TensorFlow/F_TensorFlow_WithoutHighLevelAPIs.ipynb))
- [TensorFlow Built-in Layers]([notebooks/tensorflow_builtin.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/3_NeuralNetworks_TensorFlow/G_TensorFlow_BuiltIn.ipynb))
- [TensorFlow Functional API]([notebooks/tensorflow_functional.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/3_NeuralNetworks_TensorFlow/H_TensorFlow_FunctionalAPI.ipynb))
- [TensorFlow High-Level API]([notebooks/tensorflow_highlevel.ipynb](https://github.com/BharathiVetukuri/CMPE-258_DeepLearning/blob/main/4_NeuralNetworks_Frameworks/3_NeuralNetworks_TensorFlow/I_TensorFlow_HighLevelAPI.ipynb))

---

## Video

Each Folder readme.md contains its respective Youtube Video Links.
