# 🧠 Assignment 6: Advanced Neural Network Training with Keras

This repository contains a comprehensive suite of Google Colab notebooks that demonstrate **advanced neural network training techniques using TensorFlow/Keras**. The focus is on regularization, data augmentation, tuning, and custom model components. This hands-on implementation helps build strong foundations and practical know-how in deep learning workflows.


## 🎯 Assignment Objective

✔️ Showcase various data augmentation and generalization techniques  
✔️ Implement and compare Keras regularization methods (L1, L2, Dropout, EarlyStopping, etc.)  
✔️ Experiment with initializations, normalization, callbacks, and customizations  
✔️ Demonstrate advanced topics like custom layers, metrics, losses, schedulers, training loops  
✔️ Record and explain every notebook via a detailed walkthrough video  

## 📘 Part 1: Data Augmentation & Generalization Techniques

Each notebook in this section illustrates one or more techniques in-depth, with A/B testing where applicable.

| 📒 Notebook                          | 🧪 Techniques Demonstrated                                                                 |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| `01_L1_L2_Regularization.ipynb`     | `tf.keras.regularizers.l1`, `l2`, and `l1_l2` penalties for weight regularization         |
| `02_Dropout_Regularization.ipynb`   | `Dropout` layers and their effect on overfitting                                           |
| `03_EarlyStopping.ipynb`            | `EarlyStopping` callback with patience and restore_best_weights                           |
| `04_MonteCarlo_Dropout.ipynb`       | `MC-Dropout` during inference for uncertainty estimation                                   |
| `05_Weight_Initializations.ipynb`   | Initializers like `He`, `Glorot`, `RandomNormal`, and their optimal usage                 |
| `06_BatchNormalization.ipynb`       | `BatchNormalization` before and after activations – effects on convergence                |
| `07_Custom_Dropout_Regularization.ipynb` | `AlphaDropout`, `SpatialDropout`, and custom implementations                            |
| `08_Callbacks_TensorBoard.ipynb`    | `TensorBoard`, `ModelCheckpoint`, `ReduceLROnPlateau`, and `EarlyStopping` callbacks      |
| `09_Keras_Tuner_Optimization.ipynb` | Hyperparameter optimization using `Keras Tuner` (RandomSearch, Hyperband, Bayesian)       |
| `10_KerasCV_Augmentation.ipynb`     | `keras_cv.layers` like `RandomFlip`, `CutMix`, `RandAugment`, `MixUp`                    |
| `11_Augmentation_MultiModal.ipynb`  | Data augmentation for image, video, text, time series using `AugLy` and `nlpaug`          |
| `12_FastAI_DataAugmentation.ipynb`  | Augmentation and test-time augmentation (`TTA`) using FastAI transforms                   |

## 📗 Part 2: Advanced Keras Constructs

These notebooks demonstrate advanced Keras and TensorFlow customization techniques including custom layers, models, losses, metrics, and training workflows.

| 📒 Notebook                              | 🔍 Concepts Implemented                                                                    |
|-----------------------------------------|---------------------------------------------------------------------------------------------|
| `01_Custom_LearningRateScheduler.ipynb` | `OneCycleScheduler`, cosine annealing, and warm restarts                                   |
| `02_Custom_Dropout_Layers.ipynb`        | `MCAlphaDropout`, custom noise-based dropout layers                                        |
| `03_Custom_Normalization_Layers.ipynb`  | Custom `MaxNormDense`, `LayerNormalization`, and scaling layers                            |
| `04_TensorBoard_Tracking.ipynb`         | TensorBoard logging of scalars, histograms, and embeddings                                 |
| `05_Custom_Loss_Functions.ipynb`        | Custom loss classes like `HuberLoss`, `TweedieLoss`, etc.                                  |
| `06_Custom_Activations_Initializers.ipynb` | Custom `LeakyReLU`, `my_glorot_initializer`, `MyL1Regularizer`, weight constraints       |
| `07_Custom_Metrics.ipynb`               | `HuberMetric`, precision/recall-based accuracy metrics                                     |
| `08_Custom_Layers.ipynb`                | Layers like `ExponentialLayer`, `MyDense`, `AddGaussianNoise`, custom `LayerNorm`         |
| `09_Custom_Models.ipynb`                | Full model architectures: `ResidualBlock`, `ResidualRegressor`, subclassed models         |
| `10_Custom_Optimizers.ipynb`            | Implementing `MyMomentumOptimizer`, extending base optimizer behavior                      |
| `11_Custom_Training_Loops.ipynb`        | From-scratch training loop using `tf.GradientTape` on `FashionMNIST`                      |

# Colab Links

📝 All notebooks are executed in Colab, thoroughly annotated, and explained in the walkthrough video. Please find the links to individual Colabs in the readme.md files of Part-1 and Part-2.


# 🎥 Walkthrough Video

Watch the detailed walkthrough:

🔗 Video Link (Google Drive / YouTube): Please find all the Video Links in the readme.md files of Part-1 and Part-2


# 🛠 Requirements

- Python 3.10+

- TensorFlow 2.12+

- Colab with GPU acceleration

