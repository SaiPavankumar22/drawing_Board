# Digital Drawing Board

A web application that allows users (e.g., doctors) to draw and submit drawings to a backend server. The drawings are saved in a MongoDB database and can be viewed through a sidebar history feature.

---

## Features

### Frontend:
1. **Canvas Drawing Board**:
   - Users can draw on a canvas using their mouse or stylus.
   - Clear the canvas with the "Clear" button.
2. **Submit Drawings**:
   - Submits the drawing as a Base64-encoded image to the backend.
3. **View History**:
   - Opens a sidebar showing previously saved drawings and their timestamps.
   - Close the sidebar to return to the drawing board.

### Backend:
1. **Save Drawings**:
   - An endpoint (`/api/save`) to save drawings in MongoDB with a timestamp.
2. **Retrieve History**:
   - An endpoint (`/api/history`) to fetch all saved drawings and their metadata (e.g., timestamp).

---

## Technologies Used

### Frontend:
- **HTML**: Structure of the application.
- **CSS**: Styling for the layout, buttons, and sidebar.
- **JavaScript**: Logic for canvas drawing, API interactions, and sidebar functionality.

### Backend:
- **Python (Flask)**: Handles the REST API endpoints for saving and retrieving drawings.
- **MongoDB**: Stores the drawing data.

---

## Setup Instructions

### Prerequisites
1. **Python 3.x**
2. **MongoDB**
3. **Node.js** (optional, for static server testing if required)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start MongoDB service on your system.
5. Run the Flask app:
   ```bash
   python app.py
   ```
   By default, the app runs at `http://127.0.0.1:5000/`.

### Frontend Setup
1. Navigate to the `frontend` folder.
2. Open `draw.html` in a web browser.

---

## API Endpoints

### 1. `/api/save`
- **Method**: POST
- **Description**: Saves a drawing to the database.
- **Request Body**:
  ```json
  {
      "drawing": "data:image/png;base64,<encoded_image_data>"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Drawing saved successfully!",
      "id": "<unique_id>"
  }
  ```

### 2. `/api/history`
- **Method**: GET
- **Description**: Retrieves all saved drawings from the database.
- **Response**:
  ```json
  {
      "drawings": [
          {
              "_id": "<unique_id>",
              "image_data": "data:image/png;base64,<encoded_image_data>",
              "timestamp": "<ISO_timestamp>"
          }
      ]
  }
  ```

---


## Usage
1. Open `draw.html` in a browser.
2. Draw on the canvas and click "Submit" to save the drawing.
3. Click "View History" to open the sidebar and view all saved drawings.
4. Close the sidebar to return to the drawing board.

---

## Notes
- Ensure MongoDB is running before starting the Flask backend.
- You can customize the drawing board dimensions and sidebar styles in the CSS section of `draw.html`.

---

## Future Enhancements
1. **User Authentication**: Add user accounts to manage individual drawing histories.
2. **Search and Filter**: Allow filtering drawings by date or other metadata.
3. **Export Option**: Provide options to download saved drawings as PNG files.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

