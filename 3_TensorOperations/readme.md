# 🧠 Tensor Operations Guide

This repository explores **basic tensor operations** in both **TensorFlow 2.0** and **PyTorch**. It also demonstrates the use of **einsum operations**, a powerful notation for performing efficient tensor manipulations.

### 📝 Task

a) Write a colab exploring various basic tensor operations including demonstrating einsum operations in tensorflow 2.0

b) Write a colab exploring various basic tensor operations in pytorch

### 📘 Solution

## 🔍 What are Tensors?  
Tensors are **multi-dimensional arrays** used in **machine learning** and **deep learning**. They generalize **scalars (0D), vectors (1D), matrices (2D), and higher-dimensional data structures**.


## 🔍 What are Einsum Operations?  
Einstein Summation (`einsum`) is a **powerful notation** for expressing tensor operations concisely. It enables **efficient computations** for **matrix multiplication, dot products, transpositions, summation, outer products**, and more.

## 🔍 Tensor Operations in TensorFlow
TensorFlow provides **efficient handling of tensors**, allowing operations like:
- **Creating tensors** (Scalars, Vectors, Matrices, and Higher-dimensional tensors).  
- **Basic tensor manipulations** – Indexing, Slicing, Reshaping, and Broadcasting.  
- **Math operations** – Addition, Multiplication, Dot Product, Matrix Multiplication.  
- **Advanced operations** – Softmax, Argmax, Reduce operations.  
- **Einsum operations** – Efficient matrix multiplications, element-wise operations, and batch processing.  

## 🔍 Tensor Operations in PyTorch
PyTorch provides **dynamic computation graphs** and efficient tensor operations, including:
- **Creating tensors** (Scalars, Vectors, Matrices, Higher-dimensional tensors).  
- **Basic operations** – Addition, Multiplication, Dot Product, Matrix Multiplication.  
- **Indexing and slicing** – Accessing tensor elements efficiently.  
- **Broadcasting** – Enabling operations between tensors of different shapes.  
- **Reshaping and transposing** – Changing tensor shapes dynamically.  
- **Conversion between NumPy & PyTorch tensors**.  
- **Reduction operations** – Max, Argmax, Sum, Mean.  

---

## 📊 Artifacts:
### 🚀 **1. Basic Tensor Operations (TensorFlow)**
📂 **Colab Notebook**:  https://colab.research.google.com/drive/1bN3_DkvYlSJpe6kYWxN0YO9YsBX1jkFY?usp=sharing 

🎥 Youtube Video:

## 📌 Features Covered

- ✅ Creating **Scalars, Vectors, Matrices, and Tensors**  
- ✅ **Tensor Properties**: tensor's shape, data type, and the computing device.
- ✅ **Basic Tensor Manipulations** :Operations such as indexing, slicing, reshaping, and broadcasting tensors to fit required dimensions.
- ✅ **Math Operations**: Basic mathematical operations including addition, multiplication, and matrix multiplication.
- ✅ **Advanced Tensor Algebra with Einsum**: Use of Einstein summation (einsum) to perform complex tensor algebra.
- ✅ **Visualizing Tensors**: Visualization of tensor structures and values using matplotlib.
- ✅ **Ragged and Sparse Tensors**  
- ✅ **Interactive Tensor Manipulation**: Using IPython widgets for interactive reshaping and manipulation of tensors.
- ✅ **Tensor Reshaping and Slicing**: Detailed examples of reshaping and slicing tensors.
- ✅ **Tensor Transformations**: Complex tensor transformations like transpose and roll, providing insights into data manipulation techniques.

---

### 🚀 **2. PyTorch Basics: Tensor Operations**
📂 **Colab Notebook**: https://colab.research.google.com/drive/1RcqjxZw77FBzJo8AjQsmB7o2PG_OyV8i?usp=sharing 

🎥 Youtube Video:

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
- ✅ **Advanced Indexing and Slicing** – Operations on Different Shapes  
- ✅ **Visualizations** : Visualize operations like tensor addition and multiplication using matplotlib.
- ✅ **Tensor Transformations and Manipulations** – Tensor flattening and concatenation using torch.roll and torch.flip.
- ✅ **Dynamic Computation**  

---

### 🚀 **3. Einsum Operations**
📂 **Colab Notebook**: https://colab.research.google.com/drive/1saWvnT_SmBMyTw91Ue019AdHeDpM1qld?usp=sharing 

🎥 Youtube Video: https://youtu.be/dflRGnTSpWQ 

## 📌 Features Covered
- ✅ **Transpose** – Swaps rows & columns using `"ij->ji"`.
- ✅ **Sum of elements** – Collapses all dimensions using `"ij->"`.
- ✅ **Column Sum** – Sums across rows using `"ij->j"`.
- ✅ **Row Sum** – Sums across columns using `"ij->i"`.
- ✅ **Matrix-Vector Multiplication** – `"ij,j->i"`.
- ✅ **Matrix-Matrix Multiplication** – Standard matrix multiplication `"ik,kj->ij"`.
- ✅ **Dot Product (First row)** – Row-wise dot product `"i,i->"`.
- ✅ **Dot Product with Matrix** – Matrix-wise dot product `"ij,ij->"`.
- ✅ **Hadamard Product** – Element-wise multiplication `"ij,ij->ij"`.
- ✅ **Outer Product** – Computes the outer product `"i,j->ij"`.
- ✅ **Matrix Diagonal** – Extracts diagonal elements `"ii->i"`.
- ✅ **Matrix Trace** – Sum of diagonal elements `"ii->"`.
