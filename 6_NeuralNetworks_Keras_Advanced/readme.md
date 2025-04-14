# 🧠 Assignment 6: Advanced Neural Network Training with Keras

This repository contains a comprehensive suite of Google Colab notebooks that demonstrate **advanced neural network training techniques using TensorFlow/Keras**. The focus is on regularization, data augmentation, tuning, and custom model components. This hands-on implementation helps build strong foundations and practical know-how in deep learning workflows.

---

## 🎯 Assignment Objective

✔️ Showcase various data augmentation and generalization techniques  
✔️ Implement and compare Keras regularization methods (L1, L2, Dropout, EarlyStopping, etc.)  
✔️ Experiment with initializations, normalization, callbacks, and customizations  
✔️ Demonstrate advanced topics like custom layers, metrics, losses, schedulers, training loops  
✔️ Record and explain every notebook via a detailed walkthrough video  
📘 Part 1: Data Augmentation & Generalization Techniques
Each notebook in this section illustrates one or more techniques in-depth, with A/B testing where applicable.

Notebook	Techniques Demonstrated
01_L1_L2_Regularization	tf.keras.regularizers.l1, l2, l1_l2
02_Dropout_Regularization	Dropout, impact on overfitting
03_EarlyStopping	EarlyStopping callback w/ patience tuning
04_MonteCarlo_Dropout	MC-Dropout for uncertainty modeling
05_Weight_Initializations	He, Glorot, RandomNormal, etc.
06_BatchNormalization	Batch norm placement strategies
07_Custom_Dropout_Regularization	AlphaDropout, SpatialDropout
08_Callbacks_TensorBoard	TensorBoard, ModelCheckpoint, ReduceLROnPlateau
09_Keras_Tuner_Optimization	Hyperparameter search (Random, Bayesian, Hyperband)
10_KerasCV_Augmentation	keras_cv.layers.RandomFlip, CutMix, RandAugment
11_Augmentation_MultiModal	Using AugLy & nlpaug for image, video, text, etc.
12_FastAI_DataAugmentation	FastAI Transforms, TTA
📗 Part 2: Advanced Keras Constructs
These notebooks demonstrate advanced custom implementations.

Notebook	Concepts Implemented
01_Custom_LearningRateScheduler	OneCycle Scheduler
02_Custom_Dropout_Layers	MCAlphaDropout, custom noise dropout
03_Custom_Normalization_Layers	MaxNormDense, LayerNorm, etc.
04_TensorBoard_Tracking	Scalars, Histograms, Embeddings logging
05_Custom_Loss_Functions	HuberLoss, TweedieLoss, etc.
06_Custom_Activations_Initializers	LeakyReLU, my_glorot_initializer, MyL1Regularizer
07_Custom_Metrics	HuberMetric, Accuracy with thresholds
08_Custom_Layers	ExponentialLayer, MyDense, GaussianNoiseLayer
09_Custom_Models	ResidualRegressor, ResidualBlock
10_Custom_Optimizers	MyMomentumOptimizer, Lookahead
11_Custom_Training_Loops	From scratch loop with gradient tape
🎥 Walkthrough Video
📺 Watch the detailed walkthrough:
🔗 Video Link (Google Drive / YouTube)

In this video:

I demonstrate execution of all notebooks

Explain architecture, tuning strategy, visualizations

Show live TensorBoard dashboards and metrics

📚 References & Inspiration
Hands-On ML by Aurélien Géron

KerasCV

AugLy by Meta AI

nlpaug Library

FastAI Book & Notebooks

🛠 Requirements
Python 3.10+

TensorFlow 2.12+

Colab with GPU acceleration

pip install keras keras-tuner tensorflow-addons keras-cv fastai nlpaug AugLy

🧑‍💻 Author
Submitted by: [Your Name]
Course: Advanced Deep Learning with Keras
University: [Your Institution]

