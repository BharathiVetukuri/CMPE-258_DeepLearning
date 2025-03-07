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

```
## Project Structure
The repository consists of three main folders:

### **Numpy Implementation** (`numpy/`)
- [`numpy_nn.ipynb`](numpy/numpy_nn.ipynb): A 3-layer neural network built from scratch using NumPy, implementing manual backpropagation with chain rule-based gradient propagation.

### **PyTorch Implementations** (`pytorch/`)
- [`pytorch_scratch.ipynb`](pytorch/pytorch_scratch.ipynb): PyTorch version without built-in layers, defining a fully custom network.
- [`pytorch_classes.ipynb`](pytorch/pytorch_classes.ipynb): Using PyTorch's built-in modules for a cleaner and more scalable model.
- [`pytorch_lightning.ipynb`](pytorch/pytorch_lightning.ipynb): Implementation using PyTorch Lightning for structured training.

### **TensorFlow Implementations** (`tensorflow/`)
- [`tensorflow_scratch.ipynb`](tensorflow/tensorflow_scratch.ipynb): TensorFlow implementation without high-level APIs, using `einsum` instead of matrix multiplication.
- [`tensorflow_builtin.ipynb`](tensorflow/tensorflow_builtin.ipynb): Using TensorFlow’s built-in layers.
- [`tensorflow_functional.ipynb`](tensorflow/tensorflow_functional.ipynb): Implementation using the Functional API.
- [`tensorflow_highlevel.ipynb`](tensorflow/tensorflow_highlevel.ipynb): High-level API implementation.
```

---

## Implementations Overview

### **1. Numpy Implementation (From Scratch)**
- Implements a **3-layer neural network** for non-linear regression.
- Uses **manual backpropagation** and **chain rule-based gradient propagation**.
- Includes non-linear activation functions.
- Displays loss over epochs and final output.
- Uses synthetic 3-variable data visualization in **4D plot**.

[Notebook Link](notebooks/numpy_nn.ipynb)

### **2. PyTorch Implementations**
- **From Scratch:** No built-in PyTorch layers, manual tensor operations.
- **Class-Based:** Uses `torch.nn.Module` for structured implementation.
- **Lightning Version:** More modular and scalable approach.

[Notebook Links]
- [PyTorch From Scratch](notebooks/pytorch_nn.ipynb)
- [PyTorch Class-Based](notebooks/pytorch_nn_classes.ipynb)
- [PyTorch Lightning](notebooks/pytorch_lightning_nn.ipynb)

### **3. TensorFlow Implementations**
- **Low-Level API:** No built-in layers, manual operations using TensorFlow.
- **Built-in Layers:** Uses `tf.keras.layers` for structured design.
- **Functional API:** Implements the model in a more modular way.
- **High-Level API:** Uses `tf.keras.Model` for efficient design.

[Notebook Links]
- [TensorFlow Low-Level API](notebooks/tensorflow_lowlevel.ipynb)
- [TensorFlow Built-in Layers](notebooks/tensorflow_builtin.ipynb)
- [TensorFlow Functional API](notebooks/tensorflow_functional.ipynb)
- [TensorFlow High-Level API](notebooks/tensorflow_highlevel.ipynb)

### **4. JAX Implementation**
- Uses JAX for automatic differentiation and high-performance computation.
- Implements the **3-layer deep neural network** with JAX’s functional paradigm.

[Notebook Link](notebooks/jax_nn.ipynb)

---

## Video

