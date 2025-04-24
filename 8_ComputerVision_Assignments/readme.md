# Assignment 8: Computer Vision Modules

## Overview
This assignment covers a broad set of computer vision tasks using deep learning with TensorFlow and Keras, including:
- Supervised contrastive learning
- Transfer learning across image, audio, video modalities
- Zero-shot classification using CLIP
- State-of-the-art models like EfficientNet, BiT, MLP-Mixer, ConvNeXt v2
- Vision classifier development using datasets like MNIST, Fashion MNIST, CIFAR-10
- Medical imaging tasks such as X-ray pneumonia and 3D CT scan classification

Each section below references a self-contained Colab notebook implementing the concepts with complete visualizations.

---

## ✅ Part 1: Supervised Contrastive Learning
- Implemented a custom loss function for supervised contrastive learning
- Compared with traditional softmax-based cross-entropy
- Used Fashion MNIST dataset
- t-SNE visualization of learned embeddings and confusion matrix comparison
- **Colab**: https://colab.research.google.com/drive/1AbWJhsIBsX977ium_t4nGPfauDsILv2Z?usp=sharing 

**🎥Video**: https://youtu.be/VKeK-9RVR28 

---

## ✅ Part 2: Transfer Learning Across Modalities

### Images
- Transfer learning with EfficientNet and fine-tuning
- BiT used for SOTA baseline
- Used Dogs vs Cats or Flower classification as reference
- **Colab**: https://colab.research.google.com/drive/1fwBqqVI7OMOi8GSY5kQJFmWFFwcRFDLT?usp=sharing

### Audio
- Used YAMNet for feature extraction
- Classifier built using Logistic Regression on audio embeddings
- t-SNE and confusion matrix visualized
- **Colab**: https://colab.research.google.com/drive/1Za8VoSJl5fXUMEA89_lFoVknOmqqIyMT?usp=sharing 

### Video
- Used TFHub's I3D model on preprocessed UCF101 data
- Demonstrated feature extraction and fine-tuning
- Simulated setup with synthetic data for reliability
- **Colab**: https://colab.research.google.com/drive/1Wz69TXXt4hKg58prBEgI6NE40nh4Qymc?usp=sharing 

**🎥Video**: https://youtu.be/qEBwe5gIFa0 

---

## ✅ Part 3: Zero-Shot Learning + TFHub Transfer Learning
- Used OpenAI's CLIP model for zero-shot classification
- Dataset: real web images and synthetic prompts
- Used BiT + EfficientNet on Flowers dataset from TFHub
- **Colab**: https://colab.research.google.com/drive/1lz_rR4KPKLkxpmokAUEbkd1O5FUsb3y0?usp=sharing 

**🎥Video**: https://youtu.be/XrEt12r-afA 

---

## ✅ Part 4: Vision Classifiers

### MNIST
- Demonstrated EfficientNet and BiT
- MLP-Mixer and ConvNeXt v2 for SOTA comparison
- **Colab**: https://colab.research.google.com/drive/13Oq_N4AP9aSJECelSrcmO8McKgOafF2Z?usp=sharing 

### Fashion MNIST
- Same structure with proper visual evaluation
- **Colab**: https://colab.research.google.com/drive/14O8oW0UQK8u0KwnNPP_uh13g6smPTTSG?usp=sharing 

### CIFAR-10
- Used flattened features for Logistic Regression baseline
- Confusion matrix, per-class accuracy, and image prediction visualization
- **Colab**: https://colab.research.google.com/drive/1r62YG7Q0bi9VQ6Vzz1GHOEU3yxklmTU0?usp=sharing 

**🎥Video**: [Walkthrough Video (YouTube/Drive)](https://your-video-link-here.com)

---

## ✅ Part 5: Medical Image Classification

### a) Pneumonia X-ray Classification
- Real-world dataset loaded via .zip with NORMAL/PNEUMONIA folders
- ConvNet trained on uploaded images
- Class-wise evaluation with color-coded predictions
- **Colab**: https://colab.research.google.com/drive/1i99YP07F7Uu9I_YrRKLilXOgPATfq0D1?usp=sharing 

### b) 3D CT Scan Classification
- Used MosMedData 3D volumes
- Implemented full 3D CNN
- Visualized slices and model performance
- **Colab**: https://colab.research.google.com/drive/1QxrZf8dGv29G1jHjw16QaYbqClFCdoZK?usp=sharing 

**🎥Video**: [Walkthrough Video (YouTube/Drive)](https://your-video-link-here.com)

---

## 🔍 Summary
This assignment demonstrates the application of modern deep learning techniques in:
- Contrastive learning and metric learning
- Multi-modal transfer learning
- Zero-shot classification using foundation models
- Real-world diagnostic use-cases using image classification pipelines

Each Colab is runnable end-to-end with minimal hardware and clear visualizations.

