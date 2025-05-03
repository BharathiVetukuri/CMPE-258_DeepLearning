# Assignment: Transformers and NLP

## 📚 Overview
This project demonstrates three key tasks using Transformers for Natural Language Processing (NLP):
- **Inference with a Pretrained Transformer** (Text Generation and Sentiment Classification)
- **Fine-tuning a Pretrained Transformer** (Sentiment Classification)
- **Building a Transformer Model from Scratch** (Text Classification)

All work has been implemented in separate, clean Colab notebooks for maximum clarity and reproducibility.

---

## 📚 Key Concepts

### 🔹 Inference with a Pretrained Transformer
> Inference with a pretrained transformer means using a model that has already been trained on a large dataset — without modifying its weights — to make predictions on new data.  
> Example: Using a pretrained BERT or Gemma model to classify sentiment or generate new text without retraining.

### 🔹 Fine-Tuning a Pretrained Transformer
> Fine-tuning a pretrained transformer means taking a model that has already learned general language patterns and training it further on a specific, smaller dataset to adapt it to a new task.  
> Example: Fine-tuning BERT on movie reviews for better sentiment analysis.

### 🔹 Building a Transformer from Scratch
> Building a transformer from scratch means manually creating the layers and architecture (like attention, embeddings, feed-forward) without using pre-trained models.  
> It provides full control and deeper understanding of how transformers function internally.

---

## 📝 Assignment Breakdown

| Notebook | Description |
|:--|:--|
| `9A_Inference_Pretrained_Classifier.ipynb` | Inference with pretrained transformer using **KerasHub** and **Hugging Face** models (Gemma2 text generation + DistilBERT sentiment analysis). |
| `9B_Finetune_Transformer.ipynb` | Fine-tuning pretrained models: (a) KerasHub TextClassifier on IMDB dataset, and (b) Hugging Face BERT-base-cased model on Rotten Tomatoes dataset. |
| `9C_Build_Transformer.ipynb` | Build and train a Transformer model manually from scratch on the IMDB reviews dataset. |

---

## 🔗 Colab Notebooks

| Task | Colab Link |
|:--|:--|
| Inference with Pretrained Transformer | [Open Colab 1]() |
| Fine-tuning Pretrained Transformer | [Open Colab 2]() |
| Build Transformer from Scratch | [Open Colab 3]() |

---

## 📺 YouTube Walkthrough Videos

| Task | Video Link |
|:--|:--|
| Inference Walkthrough | [Watch on YouTube]() |
| Fine-tuning Walkthrough | [Watch on YouTube](#) |
| Build Transformer Walkthrough | [Watch on YouTube](#) |

---

## ⚙️ Libraries and Tools Used
- TensorFlow / Keras 3
- Keras Hub (`keras-hub`)
- Hugging Face Transformers
- Datasets (Hugging Face Hub)
- Evaluate (for metrics like F1 Score)
- Matplotlib (for visualizations)

---

## 🚀 How to Run
1. Open each `.ipynb` Colab notebook individually.
2. Install necessary packages if not already installed:
   ```bash
   !pip install keras keras-hub transformers datasets evaluate
