# MedVision – AI Medical Image Analyzer
<img width="1058" height="535" alt="image" src="https://github.com/user-attachments/assets/4ab77bf0-eb98-4f77-83fc-d15ea65238b4" />
<strong>Medvision Homepage</strong>

## Project Overview

MedVision is an AI-powered medical image diagnostic system designed to assist healthcare professionals in detecting pneumonia from medical imaging ie., chest X-rays.

The system integrates Deep Learning, Explainable AI (Grad-CAM), Spring Boot Backend, Angular Frontend, and FastAPI AI services to provide accurate and interpretable predictions.

---

## Problem Statement

Traditional medical diagnosis using imaging can be time-consuming and dependent on specialist availability.

MedVision helps improve:
- diagnostic speed
- prediction accuracy
- clinical decision support
- AI explainability for trust in predictions

---

## Key Features

- AI-based disease prediction from medical images
- Grad-CAM visualization for explainable AI
- Angular modern dashboard UI
- Spring Boot backend management
- FastAPI model inference API
- PostgreSQL database integration
- Prediction history tracking

##  How MedVision Works

1. User uploads X-ray image  
2. Image sent to FastAPI AI service  
3. Model (DenseNet121) predicts result  
4. Grad-CAM generates heatmap  
5. Spring Boot stores results  
6. Angular displays output  

## Screenshots

<img width="1091" height="548" alt="image" src="https://github.com/user-attachments/assets/28dc2d83-ce13-4149-82d6-751b3716f6d4" />
<strong>Pneumonia Detection Image</strong>

<img width="1079" height="548" alt="image" src="https://github.com/user-attachments/assets/2d9a54f6-3a4c-49ad-87f2-756175803158" />
<strong>Normal Detection Image</strong>

<img width="1080" height="533" alt="image" src="https://github.com/user-attachments/assets/b09de8d6-41b4-433b-82ec-480c33710f38" />
<strong>About Section</strong>

<img width="1065" height="471" alt="image" src="https://github.com/user-attachments/assets/e98915f2-24b8-4a4e-8a0b-4d9ef59ed4ab" />
<strong>Terms and Conditions</strong>

<img width="1088" height="550" alt="image" src="https://github.com/user-attachments/assets/4baf02ec-e952-4c1f-b51a-89a92d0b1044" />
<strong>History Section</strong>

<img width="1077" height="548" alt="image" src="https://github.com/user-attachments/assets/ae2bcfad-801b-4738-9f32-2f59f6f78236" />
<strong>Heatmap History</strong>

## Usage Guide
Follow these steps to run MedVision locally on your system.
---

###  1. Clone the Repository

```bash
git clone https://github.com/BHAVYAA-SINGH/medvision-ai-medical-image-analyzer.git
cd medvision-ai-medical-image-analyzer
```
###  2. Setup Backend (Spring Boot)
```bash
cd medvision-backend
```
<strong>Create Configuration File</strong>
Rename 
```bash
application-example.properties
```
to 
```bash
application.properties
```
Then Update:
```bash
spring.datasource.url=jdbc:postgresql://localhost:5432/your_db
spring.datasource.username=your_username
spring.datasource.password=your_password
```
<strong>Run Backend</strong>
```bash
mvn clean install
mvn spring-boot:run
```
Runs on:
```bash
http://localhost:8080
```
### 3. Setup AI Service (FastAPI)
```bash
cd "AI Microservice"
```
```bash
pip install -r requirements.txt
uvicorn inference.api:app --reload
```
```bash
http://localhost:8000
```
### 4. Setup Frontend(Angular)
```bash
cd medvision-frontend
```
```bash
npm install
ng serve
```
```bash
http://localhost:4200
```
### 5. Access the Application
Open your browser:
```bash
http://localhost:4200
```
### 6. Model Training (Optional)

Open this folder
```bash
model-training-colab/
```
in Google Colab to train or experiment with the model.

Upload a medical image and click Analyze.

## Future Scope 
- Multi-disease detection
- Multi-label classification
- Cloud deployment
- Mobile support
---

## Tech Stack

### Frontend
- Angular
- PrimeNG

### Backend
- Spring Boot
- Java
- PostgreSQL

### AI Service
- FastAPI
- Python
- PyTorch
- DenseNet121
- Grad-CAM

### Model Training
- Google Colab

---

## Project Structure

```text
medvision/
├── medvision-frontend
├── medvision-backend
├── AI Microservice
├── model-training-colab
├── README.md
└── .gitignore
```

## Author 
Developed by: **Bhavya Singh**
