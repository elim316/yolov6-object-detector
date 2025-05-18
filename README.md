# YOLOv6 Object Detection 
This project runs real-time object detection on webcam video using a YOLOv6 model.

## Features

- Real-time object detection from webcam input
- Preprocessing with letterbox resizing for YOLOv6
- Non-Maximum Suppression (NMS) for filtering overlapping detections
- Bounding box drawing with class labels and confidence scores
- Supports loading custom YOLOv6 models and class names from YAML

---

## Setup Instructions

### 1. Clone the YOLOv6 repository (if not done)

```bash
git clone https://github.com/meituan/YOLOv6.git
cd YOLOv6

```

---

### 2. Install dependencies
Make sure you have Python 3.8+ and install required packages:

```
pip install -r requirements.txt
```

Dependencies include:

<li> torch

<li> torchvision

<li> opencv-python

<li> pyyaml

<li> numpy

---

### 3. Prepare Model and Config Files
Model weights: Download or place your .pt YOLOv6 model file, e.g., yolov6m_mbla.pt

Dataset YAML: Provide a dataset YAML file containing class names, e.g., data/dataset.yaml

Config file (if needed): For loading weights-only checkpoints, you need the model config .py file (e.g., ```configs/yolov6m.py```).

--- 

### 4. Running the Detection Script
Modify paths in the script:
```
model_path = '/path/to/yolov6m_mbla.pt'
yaml_path = '/path/to/data/dataset.yaml'
```
Run the script:
```
python your_script.py
```
Press q to quit the webcam window.

---

<h2>Troubleshooting</h2>
  <ul>
    <li><strong>No config file error:</strong>
      <ul>
        <li>YOLOv6 requires a config file to build model architecture when loading weights-only checkpoints.</li>
        <li><strong>Solution:</strong> Download the corresponding config file from the YOLOv6 repo</li>
        <li>Or use a full model checkpoint to skip building from config.</li>
      </ul>
    </li>
    <li><strong>Model not defined / UnpicklingError:</strong>
      <ul>
        <li>This happens if you try to <code>torch.load()</code> a checkpoint without specifying model class context.</li>
        <li>Use <code>safe_globals</code> or load with <code>build_model()</code> + <code>load_checkpoint()</code>.</li>
      </ul>
    </li>
    <li><strong>Webcam not opening:</strong>
      <ul>
        <li>Make sure your webcam is connected and accessible.</li>
        <li>Try <code>cv2.VideoCapture(0)</code> in a separate test script.</li>
      </ul>
    </li>
  </ul>

  <h2>Code Overview</h2>
  <ul>
    <li><code>preprocess_frame(frame, img_size=640)</code>: Resizes and normalizes frames for YOLOv6 input</li>
    <li><code>scale_coords()</code>: Rescales bounding boxes back to original frame size</li>
    <li><code>draw_detections()</code>: Draws bounding boxes and labels on frames</li>
    <li><code>load_class_names()</code>: Loads class names from YAML</li>
    <li><code>main()</code>: Captures webcam frames, runs detection, displays results</li>
  </ul>

  <h2>References</h2>
  <ul>
    <li><a href="https://github.com/meituan/YOLOv6" target="_blank" rel="noopener noreferrer">YOLOv6 official repo</a></li>
    <li><a href="https://pytorch.org" target="_blank" rel="noopener noreferrer">PyTorch</a></li>
    <li><a href="https://opencv.org" target="_blank" rel="noopener noreferrer">OpenCV</a></li>
  </ul>
</body>