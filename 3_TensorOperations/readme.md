# 📌 Tensor Operations

This repository explores **basic tensor operations** in both **TensorFlow 2.0** and **PyTorch**. It also demonstrates the use of **einsum operations**, a powerful notation for performing efficient tensor manipulations.

## 🚀 Task

### a) Write a colab exploring various basic tensor operations including demonstrating einsum operations in tensorflow 2.0
### b) Write a colab exploring various basic tensor operations in pytorch

---

## 📌 What are Tensors?  
Tensors are **multi-dimensional arrays** used in **machine learning** and **deep learning**. They generalize **scalars (0D), vectors (1D), matrices (2D), and higher-dimensional data structures**.

---

## 📌 What are Einsum Operations?  
Einstein Summation (`einsum`) is a **powerful notation** for expressing tensor operations concisely. It enables **efficient computations** for **matrix multiplication, dot products, transpositions, summation, outer products**, and more.

---

## 📌 Tensor Operations in TensorFlow
TensorFlow provides **efficient handling of tensors**, allowing operations like:
- ✅ **Creating tensors** (Scalars, Vectors, Matrices, and Higher-dimensional tensors).  
- ✅ **Basic tensor manipulations** – Indexing, Slicing, Reshaping, and Broadcasting.  
- ✅ **Math operations** – Addition, Multiplication, Dot Product, Matrix Multiplication.  
- ✅ **Advanced operations** – Softmax, Argmax, Reduce operations.  
- ✅ **Einsum operations** – Efficient matrix multiplications, element-wise operations, and batch processing.  

---

## 📌 Tensor Operations in PyTorch
PyTorch provides **dynamic computation graphs** and efficient tensor operations, including:
- ✅ **Creating tensors** (Scalars, Vectors, Matrices, Higher-dimensional tensors).  
- ✅ **Basic operations** – Addition, Multiplication, Dot Product, Matrix Multiplication.  
- ✅ **Indexing and slicing** – Accessing tensor elements efficiently.  
- ✅ **Broadcasting** – Enabling operations between tensors of different shapes.  
- ✅ **Reshaping and transposing** – Changing tensor shapes dynamically.  
- ✅ **Conversion between NumPy & PyTorch tensors**.  
- ✅ **Reduction operations** – Max, Argmax, Sum, Mean.  

---

## 📌 Summary of Covered Topics
| Concept | Key Function |
|---------|-------------|
| **Shapes** | `tensor.shape` |
| **Indexing** | `tensor[row, col]` |
| **Math Operations** | `+`, `*`, `tf.matmul()` |
| **Math Functions** | `tf.reduce_max()`, `tf.argmax()`, `tf.nn.softmax()` |
| **Manipulating Shapes** | `tf.reshape()`, `tf.expand_dims()`, `tf.squeeze()` |
| **DTypes** | `tf.cast()` |
| **Broadcasting** | Arithmetic on different shapes |
| **Convert to Tensor** | `tf.convert_to_tensor()` |
| **Ragged Tensors** | `tf.ragged.constant()` |
| **String Tensors** | `tf.strings.join()` |
| **Sparse Tensors** | `tf.sparse.SparseTensor()`, `tf.sparse.to_dense()` |

---

## 📌 Artifacts:
### 🚀 **1. PyTorch Basics: Tensor Operations**
📂 **Notebook**:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo-name/pytorch-tensor-basics.ipynb)

📺 **YouTube Video**: _(Add link here)_

---

### 🚀 **2. Tensor Operations in TensorFlow**
📂 **Notebook**:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo-name/tensorflow-tensor-basics.ipynb)

📺 **YouTube Video**: _(Add link here)_

## 📌 Features Covered
- ✅ Creating **Scalars, Vectors, Matrices, and Tensors**  
- ✅ **Tensor Properties** – Shape, Data Type, Device (CPU/GPU)  
- ✅ **Basic Math Operations** – Addition, Multiplication, Matrix Multiplication  
- ✅ **Indexing & Slicing** – Single & Multi-Dimensional Indexing  
- ✅ **Reshaping & Transposing** – `view()`, `reshape()`, `T`  
- ✅ **Broadcasting** – Operations on Different Shapes  
- ✅ **Conversion between NumPy & PyTorch Tensors**  
- ✅ **Reduction Operations** – `max`, `argmax`, `sum`, `mean`  
- ✅ **Element-wise & Matrix Operations**  

---

### 🚀 **3. Einsum Operations**
📂 **Notebook**:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo-name/einsum-operations.ipynb)

📺 **YouTube Video**: _(Add link here)_
