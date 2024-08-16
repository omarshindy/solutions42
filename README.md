
# Solutions42

## Project Overview

Solutions42 is a web-based application built using Wagtail CMS, designed to support multi-language content management with ease. The project provides a framework for creating and managing content in multiple languages, ensuring that administrators can efficiently handle localization requirements within the Wagtail admin interface.

## Setup Instructions

### Running Locally

To run the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/omarshindy/solutions42.git
   cd solutions42
   ```

2. **Create a `.env` File**

   At the root level of the project, create a `.env` file containing the following keys (this is required for both local and Docker environments):

   ```bash
   DB_HOST=db
   DB_PORT=5432
   POSTGRES_DB=solutions
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   ```

3. **Create and Activate a Virtual Environment**

   Ensure you have Python 3.9 installed. Create and activate a virtual environment using the following commands:

   ```bash
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

4. **Install Project Dependencies**

   With the virtual environment activated, install the project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**

   To set up the database, apply the migrations using the following command:

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   Once the migrations are complete, start the development server by running:

   ```bash
   python manage.py runserver
   ```

   You can now access the project in your web browser at `http://127.0.0.1:8000`.

### Running with Docker

To run the project using Docker, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/omarshindy/solutions42.git
   cd solutions42
   ```

2. **Create a `.env` File**

   As mentioned in the local setup, ensure you have a `.env` file at the root level with the following keys:

   ```bash
   DB_HOST=db
   DB_PORT=5432
   POSTGRES_DB=solutions
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   ```

3. **Build and Start the Containers**

   Use Docker Compose to build and start the containers:

   ```bash
   docker-compose up --build
   ```

4. **Apply Database Migrations**

   Once the containers are up and running, apply the database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Access the Application**

   The application will be accessible at `http://localhost:8000`.

## Language Support

### Adding or Switching Languages

To add or switch languages in the Wagtail admin:

1. Go to the Wagtail admin panel.
2. Navigate to the "Settings" menu and select "Languages."
3. Add a new language or edit an existing one to switch between languages.
4. Use Wagtail's localization features to manage translations for pages and other content.

Make sure to use the Wagtail Localize package to handle translations seamlessly.

## Linting

### 1. Running Ruff Linting

To maintain code quality, run Ruff linting using the following command:

```bash
ruff .
```

### 2. Ruff Configuration

The Ruff configuration is managed through a `.ruff.toml` file located in the root of the project. It includes specific rules tailored to this project. Ensure that the configurations in the `.ruff.toml` file align with the team's coding standards.

## Page Setup and Snippets

### HomePage Sections

The `HomePage` is the main landing page of the site. It contains several sections that can be customized via the Wagtail admin interface. Common sections include:

- **NewsBlock**: Getting Maximun 5 instances from News Created under NewsIndexPage
- **ImageSliderBlock**: Choose targeted images to appear in HomePage and it's orderable
- **VisionBlock**: To Add Title and Image for the Vision

Each of these sections can be edited through the Wagtail admin by navigating to the `HomePage` and adding or modifying blocks in the relevant section.

### Creating NewsIndexPage and NewsPage

The `NewsIndexPage` serves as a listing page for all `NewsPage` entries. To create and manage these pages:

1. **Create a NewsIndexPage**
   - Go to the Wagtail admin and add a new page under the desired parent page.
   - Choose `NewsIndexPage` from the list of available page types.
   - Fill out the relevant fields, such as title, intro text, and any other custom fields provided.

2. **Create NewsPage**
   - Navigate to your `NewsIndexPage` in the admin.
   - Add a child page and select `NewsPage` from the list of page types.
   - Fill out the fields such as title, publish date, content, and any other fields provided.

### Adding Header and Footer Snippets

To add header and footer snippets that can be reused across the site:

1. **Create Snippets from NavBar**
   - In the Wagtail admin, navigate to the "Snippets" section.
   - Add a new navbar snippet to either header or footer to be selected from nabar type .

2. **Select Pages for Redirection Titles in Header or Footer**
   - When creating a header or footer snippet, you can choose specific pages that will serve as redirection titles.
   - In the snippet form, use the page chooser widget to select the pages you want to appear as links in the header or footer.
   - This allows users to click on the header or footer items and be redirected to the chosen page.
