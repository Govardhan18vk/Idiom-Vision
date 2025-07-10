#  Idiom Vision

**Idiom Vision** is a AI project that interprets visual representations of idioms. It takes images as input, generates meaningful captions using a vision-language model, and determines whether the interpretation of an idiom is **idiomatic**, **literal**, or **irrelevant**. The application is built with an intuitive Streamlit UI for ease of use and interactivity.

---

##  What It Does

The application performs **two core subtasks**:

###  Subtask A: Image Captioning & Idiom Matching
- Upload **5 candidate images**.
- Enter an **idiom**.
- The system:
  - Generates captions for all images.
  - Queries a local LLM (e.g., `LLaMA 2`) to get the idiom's meaning.
  - Compares each image caption with the idiom's meaning using semantic similarity (SBERT).
  - Ranks images by their relevance to the idiom.

###  Subtask B: Idiomatic vs Literal vs Irrelevant Classification
- Upload:
  - **2 sequence images** (to set context),
  - **4 candidate images**.
- Enter an idiom.
- The system:
  - Generates captions for all images.
  - Predicts which image best continues the sequence.
  - Uses average similarity to classify the overall image representation as:
    - **Literal**
    -**Idiomatic**
    -**Irrelevant**

---

## Demo

> **Screenshots.**  
![image](https://github.com/user-attachments/assets/8ecd43da-e388-490c-9092-557d4a825594)


![image](https://github.com/user-attachments/assets/23ee0101-3d41-4d21-9928-754cd387151a)


![image](https://github.com/user-attachments/assets/d6dc185e-40b7-4403-858e-9f954d7a6b0d)


## ⚙️ Tech Stack

| Task | Technology |
|------|------------|
| UI | Streamlit |
| Image Captioning | BLIP (`Salesforce/blip-image-captioning`) |
| Semantic Embedding | SentenceTransformers (MiniLM-L6-v2) |
| Similarity Metric | Cosine Similarity |
| LLM Backend | LLaMA 2 (local API call) |
| Image Handling | Pillow (PIL), base64 |

---

## 🛠️ Installation Instructions

> Just run the commands 


### Clone the repository
```bash
git clone https://github.com/your-username/idiom-vision.git
cd idiom-vision
```
### Creating a Python Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### Installing Required Libraries
```bash
pip install streamlit
pip install torch torchvision torchaudio
pip install transformers
pip install sentence-transformers
pip install scikit-learn
pip install pillow
pip install requests
```
### Running the App
```bash
streamlit run app.py

```
From the home page, you’ll be able to access both subtasks.

### Project Structure
```bash
idiom-vision/
├── app.py                         # Home page of the Streamlit app
├── landing pages for Subtasks/                # Subtask modules
│   ├── subtask_A.py              # 5-image captioning & idiom similarity
│   └── subtask_B.py              # Sequence prediction & idiom classification
├── README.md                     # This file
├── #And some backround image files
```
### How It Works
*BLIP Model generates textual captions for input images.

*SentenceTransformer creates vector embeddings for the captions and idiom meanings.

*Cosine Similarity is used to measure how close the image meaning is to the idiom and also the image caption embeddings.

*Threshold value is kept to determine whether the visual representation is idiomatic, literal, or irrelevant.

### Future Enhancements
*Fine-tune BLIP on idiom-specific datasets

*Replace thresholds with a trained classifier (e.g., SVM or neural net)

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request. Ensure your code follows the existing structure and includes appropriate documentation.


## Contact

For questions or support, contact **me** at [medikurthisaigovardhanrao@gmail.com](mailto:medikurthisaigovardhanrao@gmail.com)


