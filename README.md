# AirCanvas

**A real-time, gesture-controlled drawing application using computer vision.**

AirCanvas is a Python-based application that enables touchless drawing through hand tracking and finger gestures. It uses a webcam to detect hand landmarks and translates index-finger movement into strokes on a virtual canvas.

## Overview

The application combines real-time hand tracking with gesture-based input to create an interactive drawing experience. Users can select colors, draw using finger movements, and erase portions of the canvas without using a mouse or touchscreen.

## Features

- **Real-time hand tracking:** Detects hand landmarks using MediaPipe.
- **Gesture-based drawing:** Draws when the thumb and index finger are sufficiently apart.
- **Color selection:** Supports red, green, blue, and yellow drawing colors.
- **Eraser mode:** Erases strokes using a circular eraser.
- **Smooth drawing:** Applies position smoothing to reduce abrupt cursor movement.
- **Live visualization:** Displays the camera feed, hand landmarks, toolbar, and drawing canvas.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| OpenCV | Camera input, image processing, drawing, and display |
| MediaPipe | Hand landmark detection |
| NumPy | Canvas creation and image arrays |
| Math | Distance calculation between landmarks |

## How It Works

1. **Capture:** OpenCV reads frames from the webcam.
2. **Preprocess:** Each frame is horizontally flipped and converted from BGR to RGB for hand tracking.
3. **Detect:** MediaPipe identifies hand landmarks.
4. **Interpret:** The index fingertip controls the cursor, while thumb-to-index distance determines whether drawing is active.
5. **Render:** Finger movement generates strokes on a separate canvas. Toolbar gestures select colors or activate the eraser.
6. **Display:** The drawing is combined with the camera frame and displayed in real time.

## Project Structure

```text
AirCanvas/
├── main.py
├── check_mp.py
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python installed on your system
- A working webcam
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/bytebelle-ai/AirCanvas.git
cd AirCanvas
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Run the application**

```bash
python main.py
```

A window titled `Air Canvas` should open when the webcam and required dependencies are available.

### Controls

| Interaction | Action |
|---|---|
| Move index fingertip | Control the drawing cursor |
| Separate thumb and index finger | Draw |
| Move fingertip to a color circle | Select a drawing color |
| Move fingertip to the eraser control | Activate eraser mode |
| Press `Esc` | Exit the application |

## Limitations

- Requires a working webcam and suitable lighting.
- Hand tracking accuracy depends on camera quality and visibility.
- The current implementation tracks one hand at a time.
- Drawings are maintained in memory and are not automatically saved to an image file.

## Future Improvements

- Add controls for brush size and additional colors.
- Implement an option to save and export drawings.
- Improve gesture recognition and cursor stability.
- Add a dedicated clear-canvas control.

## Repository

Source code: [github.com/bytebelle-ai/AirCanvas](https://github.com/bytebelle-ai/AirCanvas)