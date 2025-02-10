# MyRecipe - Project Overview

## Problem Statement

Many people struggle to find reliable and practical recipes that actually work. Additionally, they often do not know where to seek help for culinary questions. Due to a lack of cooking knowledge and skills, many individuals rely on processed and ultra-processed foods, leading to an imbalanced diet full of preservatives and harmful ingredients.

MyRecipe aims to bridge this gap by offering a structured and interactive platform where users can:

Access tested and verified recipes
Engage with a community of home cooks and professional chefs
Improve their culinary skills with step-by-step guidance
Reduce reliance on processed foods by promoting homemade meals
By making reliable recipes and expert advice easily accessible, MyRecipe helps users build confidence in the kitchen and make healthier food choices.


## Purpose

The purpose of MyRecipe is to create a collaborative and user-friendly platform where chefs and home cooks can share tested and trustworthy recipes while enabling others to engage, learn, and ask questions.

The platform aims to:

✅ Improve Cooking Skills – Offer step-by-step guidance, culinary tips, and best practices.

✅ Promote Healthier Eating – Encourage homemade meals using fresh, natural ingredients.

✅ Foster a Cooking Community – Enable interaction through comments, Q&A, and recipe sharing.

✅ Ensure Accessibility & Simplicity – Provide an intuitive interface optimized for all devices.

Through MyRecipe, users can connect, share experiences, and adopt healthier eating habits, ultimately shifting towards wholesome, home-cooked meals that benefit overall well-being.


## Target Audience

MyRecipe is designed for a wide range of users who have an interest in cooking and healthy eating. The platform accommodates:

👤 Guest Users – Visitors who can browse recipes but have limited interaction.

👥 Registered Users – Users with an account who can save, comment, and engage with the community.

👨‍🍳 Chefs & Home Cooks – Contributors who submit their own recipes and share expertise.

🛠 Administrators – Moderators responsible for managing content, reviewing recipe submissions, and monitoring user engagement.


## Core Features

🚀 We're building something great! 🎉 Check out the key features of MyRecipe:

Recipe Management

:heavy_check_mark: Save Favourite Recipes – Bookmark recipes for quick access.

:heavy_check_mark: Recipe Submission – Users can submit detailed recipes with images and instructions.

:heavy_check_mark: Recipe Search & Browsing – Filter by categories (e.g., desserts, main courses) or search by ingredients.

User Interaction

:heavy_check_mark: User Registration & Login – Create accounts to unlock interactive features.

:heavy_check_mark: Comment Section – Ask questions, share tips, and interact with other cooks.

:heavy_check_mark: Direct Chef Contact – Get culinary advice from professional chefs.

:heavy_check_mark: Recipe Rating System – Rate recipes from 1 to 5 stars to help others choose the best ones.

User Experience & Accessibility

:heavy_check_mark: Recipe Details Page – A dedicated page with full ingredients, steps, and user feedback.

:heavy_check_mark: User-Friendly Interface – Intuitive design for seamless navigation.

:heavy_check_mark: Mobile & Desktop Optimisation – A fully responsive layout for all devices.

:heavy_check_mark: Social Sharing – Share your favourite recipes on social media with one click.

Admin & Moderation Tools

:heavy_check_mark: Complete Admin Panel – Manage recipes, users, and comments efficiently.

:heavy_check_mark: Content Review System – Ensure recipe quality and prevent spam.

:heavy_check_mark: User Reports & Moderation – Maintain a respectful and helpful community.

✨ And more exciting features coming soon! Stay tuned! 🚀


## Why MyRecipe?

:one: Reliable Recipes: Every recipe is tested and reviewed.

:two: Community-Driven: Engage with a network of passionate cooks.

:three: Health-Focused: Encourages home cooking with wholesome ingredients.

:four: Intuitive & Accessible: Easy-to-use platform with a clean interface.


## USER STORIES

USER STORY: User Login [#1](https://github.com/gerasoa/MyRecipeBook/issues/2#issue-2811824467)

USER STORY: Browse and Search Recipes [#2](https://github.com/gerasoa/MyRecipeBook/issues/1#issue-2810909751)

USER STORY: Leave Comments on Recipes [#3](https://github.com/gerasoa/MyRecipeBook/issues/3#issue-2811829264)

USER STORY: Submit Recipes [#4](https://github.com/gerasoa/MyRecipeBook/issues/4#issue-2811830286)

USER STORY: Filter Recipes by Dietary Preferences [#5](https://github.com/gerasoa/MyRecipeBook/issues/5#issue-2811831905)

USER STORY: Save Recipes to Favourites [#6](https://github.com/gerasoa/MyRecipeBook/issues/6#issue-2811838753)

USER STORY: View Ratings and Reviews [#7](https://github.com/gerasoa/MyRecipeBook/issues/7#issue-2811840169)

USER STORY: Moderate Recipe Submissions and Comments [#8](https://github.com/gerasoa/MyRecipeBook/issues/8#issue-2811841297)

USER STORY: Recipe Rating [#9](https://github.com/gerasoa/MyRecipeBook/issues/9#issue-2811842049)


## WIREFRAMES

![wireframe browser](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/wf-browser.png)

![wireframe mobile](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/wf-mobile.png)

![wireframe tablet](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/wf-tablet.png)



## Future Enhancements

💡 AI-Powered Recommendations – Suggest recipes based on user preferences and available ingredients.

💡 Video Tutorials – Step-by-step cooking guides from professional chefs.

💡 Recipe Collections – Themed lists like "Beginner Recipes" and "Quick & Easy Meals".

💡 Meal Planning Tools – Generate weekly meal plans based on dietary preferences.


## Data Model

Overview

The MyRecipe platform uses a structured PostgreSQL database to store and manage crucial data for recipes, users, and comments. Django migrations are employed to efficiently manage schema changes and keep the database updated as the project evolves.

Data Model

The main tables in the MyRecipe database are:

📋 Users

Stores all user information, including their name, email, and password. This table handles user authentication and permissions.

🍽 Recipes

Contains recipe details such as title, ingredients, instructions, and the user who created the recipe. It also stores metadata related to the recipe's category and preparation time.

💬 Comments

Allows users to comment on recipes, sharing their feedback, questions, and tips. Each comment is tied to a specific recipe and user, fostering interaction.

📊 Database Relationships

Users ↔ Recipes: A user can create multiple recipes, but each recipe is tied to a single user.
Recipes ↔ Comments: Each recipe can have multiple comments, but each comment is linked to one recipe.

Database Diagram

Below is the diagram that illustrates the relationships between the tables in the MyRecipe database:

![Data model](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/database-model.png)


## Authentication, Authorization & Access Control

MyRecipe implements role-based authentication with specific roles for users:

👤 Logged-in Users – Can browse, save, and comment on recipes.

👨‍🍳 Chefs – Can submit and manage their own recipes.

👑 Admin – Has full access to manage content, users, and the platform.

Users can log in or register via email and password. When not logged in, the Login and Register options are available. Once logged in, the Logout option appears. Admins and Chefs have exclusive access to their dedicated admin areas, while regular users can only access the public website interface.

## Testing

Test Procedures

🚀 Python Tests: Manual tests were conducted to validate the functionality, usability, and responsiveness of the application, ensuring all key features function as expected.

⚙️ W3C Validation: W3C validators were used to check the compliance of HTML and CSS with web standards, ensuring accessibility and cross-browser compatibility.

Testing Documentation
📋 Test Cases: Manual tests were performed based on specific use cases of the application, covering functionalities such as login, registration, navigation, and recipe submission.

✅ Results: All tests passed successfully, with positive validation of HTML and CSS using W3C validators, and no critical errors found.

<details>
  <summary>Show/Hide Test Validator Images</summary>


![CSS Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-css-style.png)

![Html Index Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-html-index.png)

![Html Recipe Detail Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-html-recipe_detail.png)

![Html Chefs Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-html-chefs.png)

![Html Chefs Detail Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-html-chef_detail.png)

![Html Favorites Validation](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/validator-html-favorites.png)

</details>

<details>
  <summary>Show/Hide Lighthouse Images</summary>

![Recipe List](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/lighthouse-recipe-list.png)

![Recipe Detail](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/lighthouse-recipe-detail.png)

![favorites](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/lighthouse-favorites.png)

![Chefs Detail](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/lighthouse-chefs-detail.png)

![Search](https://github.com/gerasoa/MyRecipeBook/blob/main/docs/lighthouse-search.png)

</details>

## Version Control & Secure Code Management

This project utilizes Git for version control and is hosted on GitHub. The repository can be accessed here:

📌 [GitHub Repository](https://github.com/gerasoa/MyRecipeBook)

🛠️ Git Workflow

✅ Feature-Based Commits: Commits are made after implementing new features, bug fixes, or complex adjustments.

✅ Main Branch Usage: The project is maintained on the main branch for stability.

✅ Descriptive Commit Messages: Each commit follows a meaningful and structured format.

✅ Secure Code Management

✅ No sensitive data is committed: Credentials and private keys are stored securely.

✅ .env and .gitignore: Used to prevent sensitive files from being included in the repository.

✅ Security Review: The repository is regularly checked to ensure compliance with best security practices.


## Deployment

The application is deployed on Heroku and is accessible at:

[My Recipes Book](https://github.com/gerasoa/MyRecipeBook)

### 🛠 Deployment Process

The deployment was carried out using Heroku with the following steps:

1 - Prepare the application

 - Install dependencies: `pip install -r requirements.txt`

 - Set `DEBUG = False` for production.

 - Configure `ALLOWED_HOSTS` to include the Heroku app domain.

2 - Set up environment variables

The following variables were added to Heroku:

- CLOUDINARY_URL – For media storage

- DATABASE_URL – For database connection

- DISABLE_COLLECTSTATIC=1 – To prevent static file collection issues

- SECRET_KEY – To ensure application security

3 - Deploy to Heroku

- Create a new Heroku app: heroku create my-recipes-book

- Set environment variables: heroku config:set VAR_NAME=value

- Push the project:

```bash
git add .
git commit -m "Prepare for deployment"
git push heroku main
```

- Run database migrations: `heroku run python manage.py migrate`


## 🔒 Security Measures

✔ `SECRET_KEY` and other sensitive credentials are stored securely as environment variables.

✔ `.gitignore` is configured to exclude sensitive files.

✔ `DEBUG = False` in production to enhance security.


## ✅ Deployment Verification

After deployment, the application was tested to ensure:

- The functionality matches the local development version.

- Database connections and media storage work correctly.

- The UI and interactive features operate as expected.


## AI Assistance in Development 🤖

During the development of this project, I strategically used GitHub Copilot to assist in various aspects of the code creation process. Here’s how AI contributed:

1 - Code Creation & Refinement:

Copilot helped generate parts of the code, especially in complex areas, and suggested improvements for better code structure and readability. It also assisted in refining classes and optimizing the CSS for better organization.

Bug Detection & Fixing:

2 -  I encountered several bugs in the code, which were identified and corrected with the help of AI. Copilot played a crucial role in pinpointing semantic errors and suggesting corrections, ensuring smoother functionality.

3 - Content Creation & Testing:

AI also contributed to generating content for the site and testing core functionalities. This was particularly valuable in ensuring that key features were working as expected.

4 - Productivity & Efficiency Gains:

The use of AI drastically reduced development time, allowing for quicker debugging, content generation, and code optimization. The overall impact on productivity was significant, and I was able to focus on higher-level tasks with improved efficiency.

## TECHNOLOGIES USED

**HTML5**: The standard markup language for creating web pages, providing the structure and content of the site.

**CSS3**: A style sheet language used for describing the presentation of a document written in HTML, enabling responsive and visually appealing designs.

**JavaScript**: A programming language that enables interactive web pages, enhancing user experience with dynamic content and features.

**GitHub**: A platform for version control and collaboration, allowing multiple developers to work on projects simultaneously and manage code changes.

**Heroku**: A cloud platform as a service (PaaS) supporting several programming languages, used for deploying, managing, and scaling web applications.

**Pexels**: A free stock photo and video website, providing high-quality images used within the application for visual enhancement.

**Cloudinary**: Media management service that allows uploading, storing, manipulating, and delivering images and videos.

**Crispy-bootstrap5**: Django package that integrates Django forms with Bootstrap 5, allowing for easy and consistent form rendering.

**Dj-database-url**: Utility for configuring database URLs in Django.

**Dj3-cloudinary-storage**: Django package that integrates Django media storage with the Cloudinary service.

**Django**: High-level web framework for Python that enables rapid and clean development of web applications.

**Django-crispy-forms**: Django package that makes it easy to create elegant and reusable forms.

**Django-allauth**: Django application for authentication, registration, and account management.

**Django-summernote**: WYSIWYG editor based on Summernote for integration with Django.

**Gunicorn**: WSGI HTTP server for Python applications, used to deploy Django applications.

**Pillow**: Image processing library for Python.

**Psycopg2**: PostgreSQL database adapter for Python.

**Python3-openid**: Library for supporting the OpenID protocol.

**Tzdata**: Time zone database.

**Whitenoise**: Library for serving static files in Django applications.

## CREDITS

- Project developed by the "My Recipes" team.
- Images provided by [Pexels](https://www.pexels.com/).
- Diagrams created using [Lucidchart](https://lucid.app/) and [dbdiagram.io](https://dbdiagram.io/).
- Hosted on [Heroku](https://www.heroku.com/).
- Source code managed on [GitHub](https://github.com/).
- https://getemoji.com



## IMAGES

Chefs - 160x160 pixels
Chefs detail - 300x300 pixels 
https://www.pexels.com/photo/fish-salad-dish-262959/
https://www.pexels.com/search/food/



