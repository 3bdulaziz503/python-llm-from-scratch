# Lesson 01: Environment Setup

## 1. Project Overview

This project aims to build a small GPT-style language model from scratch using Python and PyTorch.

The project starts with English text data and will later explore Arabic text processing.

## 2. Development Environment

| Component | Version / Details |
|---|---|
| Operating System | Windows 11 |
| Python | 3.14.4 |
| PyTorch | 2.15.0+cpu |
| NumPy | 2.5.5 |
| Matplotlib | 3.11.2 |
| Code Editor | Visual Studio Code |
| Virtual Environment | .venv |
| Version Control | Git |
| Remote Repository | GitHub |

## 3. Hardware Information

- Local graphics device: AMD Radeon Graphics.
- PyTorch CUDA availability: False.
- Local development and initial experiments will use the CPU.
- Google Colab GPU will be used for larger training experiments.

## 4. Project Structure

```text
python-llm-from-scratch/
│
├── checkpoints/
├── configs/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── lessons/
│   └── reports/
├── notebooks/
├── src/
│   ├── data/
│   ├── tokenizer/
│   ├── model/
│   ├── training/
│   └── evaluation/
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── test_pytorch.py
```

## 5. PyTorch Verification

A test script was executed successfully.

The test verified:
- PyTorch installation.
- NumPy installation.
- Matplotlib installation.
- Tensor creation.
- Tensor arithmetic operations.

CUDA was not available in the local environment, so CPU execution was confirmed.

## 6. Git and GitHub

The project was initialized as a local Git repository.

The main branch was created and the initial commit was completed.

The remote GitHub repository was configured successfully.

The initial project files were pushed to GitHub.

## 7. Lesson Status

- [x] Python environment created.
- [x] Required libraries installed.
- [x] PyTorch tested.
- [x] Project folders created.
- [x] Git initialized.
- [x] Initial commit created.
- [x] GitHub remote configured.
- [x] Initial push completed.
- [ ] Lesson documentation committed and pushed.

## 8. Next Lesson

**Lesson 02: Reading, Exploring, and Cleaning Text Data.**