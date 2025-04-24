# Assignment 8: Computer Vision Modules

## Overview
This assignment covers a broad set of computer vision tasks using deep learning with TensorFlow and Keras, including:
- Supervised contrastive learning
- Transfer learning across image, audio, video modalities
- Zero-shot classification using CLIP
- State-of-the-art models like EfficientNet, BiT, MLP-Mixer, ConvNeXt v2
- Vision classifier development using datasets like MNIST, Fashion MNIST, CIFAR-10
- Medical imaging tasks such as X-ray pneumonia and 3D CT scan classification

Each section below references a self-contained Colab notebook implementing the concepts in a failproof, CPU/GPU-safe manner with complete visualizations.

---

## ✅ Part 1: Supervised Contrastive Learning
- Implemented a custom loss function for supervised contrastive learning
- Compared with traditional softmax-based cross-entropy
- Used Fashion MNIST dataset
- t-SNE visualization of learned embeddings and confusion matrix comparison
- Colab: `fashionmnist_supervised_contrastive.ipynb`

## ✅ Part 2: Transfer Learning Across Modalities

### Images
- Transfer learning with EfficientNet and fine-tuning
- BiT used for SOTA baseline
- Used Dogs vs Cats or Flower classification as reference
- Colab: `image_transfer_learning_dogs.ipynb`

### Audio
- Used YAMNet for feature extraction
- Classifier built using Logistic Regression on audio embeddings
- t-SNE and confusion matrix visualized
- Colab: `audio_transfer_learning_yamnet.ipynb`

### Video
- Used TFHub's I3D model on preprocessed UCF101 data
- Demonstrated feature extraction and fine-tuning
- Simulated setup with synthetic data for reliability
- Colab: `video_transfer_learning_ucf101.ipynb`

---

## ✅ Part 3: Zero-Shot Learning + TFHub Transfer Learning
- Used OpenAI's CLIP model for zero-shot classification
- Dataset: real web images and synthetic prompts
- Used BiT + EfficientNet on Flowers dataset from TFHub
- Colab: `zeroshot_clip_tfhub_bit.ipynb`

---

## ✅ Part 4: Vision Classifiers

### MNIST
- Demonstrated EfficientNet and BiT
- MLP-Mixer and ConvNeXt v2 for SOTA comparison
- Colab: `mnist_transfer_learning.ipynb`

### Fashion MNIST
- Same structure with proper visual evaluation
- Colab: `fashionmnist_transfer_learning.ipynb`

### CIFAR-10
- Used flattened features for Logistic Regression baseline
- Confusion matrix, per-class accuracy, and image prediction visualization
- Colab: `cifar10_transfer_learning.ipynb`

---

## ✅ Part 5: Medical Image Classification

### a) Pneumonia X-ray Classification
- Real-world dataset loaded via .zip with NORMAL/PNEUMONIA folders
- ConvNet trained on uploaded images
- Class-wise evaluation with color-coded predictions
- Colab: `xray_convnet_classification.ipynb`

### b) 3D CT Scan Classification
- Used MosMedData 3D volumes
- Implemented full 3D CNN
- Visualized slices and model performance
- Colab: `ctscan_3d_classification.ipynb`

---

## 🔍 Summary
This assignment demonstrates the application of modern deep learning techniques in:
- Contrastive learning and metric learning
- Multi-modal transfer learning
- Zero-shot classification using foundation models
- Real-world diagnostic use-cases using image classification pipelines

Each Colab is runnable end-to-end with minimal hardware and clear visualizations.

