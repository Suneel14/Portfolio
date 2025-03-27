📝 Description: 
   A modern, responsive portfolio website built with Flask, HTML, CSS, and JavaScript. This portfolio showcases my skills, projects, education, and achievements in an attractive and interactive format with dark/light mode toggle functionality.

✨ Features: 
   Modern UI Design: Clean, professional layout with animations
   Dark/Light Mode: Toggle between color schemes
   Responsive Design: Works on all device sizes
   Interactive Elements: Smooth scrolling, hover effects
   Project Showcase: Highlighted projects with images and links
   Contact Form: Functional form with validation

🛠️ Technologies Used:
   Frontend: HTML5, CSS3, JavaScript
   Backend: Python (Flask)
   Icons: Font Awesome
   Fonts: Google Fonts (Poppins)

🚀 How to Run the Project:
   Prerequisites:
      Python 3.x installed
      pip package manager

Installation Steps:
   Clone the repository:
      git clone https://github.com/Suneel14/portfolio-website.git
      cd portfolio-website
   Create a virtual environment (recommended):
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   Install dependencies:
      pip install flask 
   Run the application:
      python app.py

   Access the website:
      Open your browser and visit: http://localhost:5000

Project Structure:
   portfolio-website/
   ├── static/
   │   ├── styles.css           # Main CSS styles
   │   ├── script.js            # JavaScript functionality
   │   ├── profile.jpg          # Profile picture
   │   ├── projects/            # Project images
   │   │   ├── cowarchaic.jpg
   │   │   ├── chatit.jpg
   │   │   └── bg-remover.jpg
   ├── templates/
   │   ├── index.html           # Main HTML template
   ├── app.py                   # Flask application
   └── README.md                # This file

📂 File Descriptions

app.py -
The Flask backend that serves the portfolio website:
   Defines routes for the main page and contact form
   Handles form submissions
   Serves static files and templates

templates/index.html - 
The main HTML template that contains:
   Navigation sidebar with profile information
   Sections for About, Skills, Education, Projects, Achievements, and Contact
   Responsive layout structure
   Dark/light mode toggle

static/styles.css -
Contains all styling for the portfolio:
   Color variables for dark/light modes
   Responsive design for different screen sizes
   Animations and transitions
   Card layouts for projects and achievements

static/script.js -
Handles all interactive functionality:
   Navigation between sections
   Dark/light mode toggle with localStorage persistence
   Contact form submission handling
   Smooth scrolling animations

🖼️ Adding Your Content :
   Replace static/profile.jpg with your profile picture
   Add your project images to static/projects/
   Update the content in templates/index.html with your information
   Modify the color scheme in static/styles.css if desired

🌐 Deployment Options - 
This portfolio can be deployed to:
   Heroku: Free cloud platform
   PythonAnywhere: Easy Python hosting
   Vercel/Netlify: With some configuration
   AWS/GCP: For production deployments

📄 License
This project is open source and available under the MIT License.
