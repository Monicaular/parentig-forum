# Journeying Through Parenthood

## Introduction <a name="introduction"></a>

Journeying Through Parenthood is a vibrant online community tailored for parents navigating the diverse challenges of raising children of varying ages. Whether you're facing the trials of toddlerhood or grappling with the complexities of teenage years, this forum offers a supportive space where parents can seek guidance, share experiences, and find solace in knowing they're not alone on this journey.

From breastfeeding tips for new mothers to strategies for navigating the tumultuous waters of adolescence, this platform covers a spectrum of topics aimed at easing the burdens of parenthood. Whether they are seeking advice on nutrition, managing health concerns, practicing gentle parenting techniques, or simply looking for camaraderie amidst the trials of raising children, Journeying Through Parenthood is here to provide a compassionate ear and a wealth of collective wisdom to help make their parenting journey a little smoother.

![Screenshot of the website's responsive layout on different types of screens](/documentation/images/responsiveness-screenshot.png)

[View the deployed website here](https://parenthood-journey-forum-08676b443434.herokuapp.com/)

# Table of contents 

1. [Introduction](#introduction)
2. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Pallets](#colour-pallets)
    * [Entity Relationship Diagram](#erd)
3. [Features](#features)
    * [Home Page](#home-page)
    * [Navigation](#navigation)
    * [Authentication & Authorization](#authentication-&-authorization)
    * [Search Bar](#search-bar)
    * [Filters](#filters)
    * [CRUD Functionality](#crud)
    * [Resources Page](#resources)
    * [Contact Page](#contact)
    * [Admin Panel](#admin-panel)
    * [Success Messages](#success-messages)
    * [Future Implementations](#future-implementations)
4. [Technologies Used](#technologies-used)
    * [Core Development Technologies](#core-development-technologies)
    * [Libraries, Frameworks and Packages](#libraries-frameworks-packages)
    * [Python/Django Packages](#python-django-packages)
    * [Infrastructural Technologies](#infrastructural-technologies)
5. [Testing](#testing)
    * [Google Lighthouse Performance](#lighthouse)
    * [Browser Compatibility](#browser-compatibility)
    * [Responsiveness](#responsiveness)
    * [Code Validation](#code-validation)
    * [Manual Testing](#manual-testing)

## Design & Planning

### User Stories

**<span style="color: #6371A2ff;">User Story 1</span>**: As a **new visitor**, I can **quickly understand what the forum is about when I land on the homepage**, so that **I can decide if it meets my interests and needs**.

**<span style="color: #6371A2ff;">User Story 2</span>**: As a **user** I can **easily understand and navigate through the website** so that **I can find information quickly and efficiently**.

**<span style="color: #6371A2ff;">User Story 3</span>**: As a **user** I can **create an account** so that **I can actively participate by creating or commenting on posts**

**<span style="color: #6371A2ff;">User Story 4</span>**: As a **forum user**,  I can **log into the forum** so that **I can add posts, view posts, and participate in discussions.**

**<span style="color: #6371A2ff;">User Story 5</span>**: As a **user** I can **select a post** so that **I can effortlessly read its complete text.**

**<span style="color: #6371A2ff;">User Story 6</span>**: As a **user** I can **create, read, update and delete my posts** so that **I can actively engage with the community**.

**<span style="color: #6371A2ff;">User Story 7</span>**: As a **logged-in user** I can **create, read, update, and delete comments on posts** so that **I can engage in discussions effectively.**

**<span style="color: #6371A2ff;">User Story 8</span>**: As a **logged-in user** I can **like both posts and comments** so that **I can contribute to the community by expressing my opinions and preferences.**

**<span style="color: #6371A2ff;">User Story 9</span>**: As a **forum user,** I can **navigate through posts using pagination,** so that **comfortably browse through large numbers of posts without overwhelming load times or scrolling indefinitely.**

**<span style="color: #6371A2ff;">User Story 10</span>**: As a **user** I can **filter posts by different categories** so that **I can more easily find posts that are relevant to my interests or needs.**

**<span style="color: #6371A2ff;">User Story 11</span>**: As a **user** I can **search for posts by inserting one or more keywords** so that **I can quickly find relevant discussions and information.**

**<span style="color: #6371A2ff;">User Story 12</span>**: As a **user** I can **easily access and read the rules and information about the site** so that **I can understand the guidelines and purpose of the platform**.

**<span style="color: #6371A2ff;">User Story 13</span>**: As a **user** I can **easily contact the administrator for any issues that may arise** so that **I can receive prompt resolution and support**.

**<span style="color: #6371A2ff;">User Story 14</span>**: As a **site admin** I can **receive messages regarding potential issues from users** so that **I can address and sort them efficiently.**

**<span style="color: #6371A2ff;">User Story 15</span>**: As a **site admin** I can **review and manage posts that are not relevant to the forum's content** so that **I can maintain the quality and integrity of the platform.**

**<span style="color: #6371A2ff;">User Story 16</span>**: As a **site admin** I can **mark posts as read** so that **I can keep track of the ones I have reviewed**.

**<span style="color: #6371A2ff;">User Story 17</span>**: As a **logged-in user** I can **report another user's comment directly by having a dedicated button** so that **I can bring attention to inappropriate or harmful content.**

**<span style="color: #6371A2ff;">User Story 18</span>**: As a **logged-in user** I can **reply to comments made by other users on posts** so that **I can engage in discussions and provide feedback.**

### Wireframes

Below are wireframe sketches illustrating the proposed layout and design of the forum's user interface. These wireframes serve as a visual guide to showcase the arrangement of key elements and functionality within the forum.

#### Homepage Wireframe

**Description**: This wireframe depicts the layout of the forum's homepage, including navigation menus, featured posts, and search functionality.

<details>
<summary>Homepage Wireframe - Desktop & Mobile</summary>

![Screenshot of desktop homepage wireframe](/documentation/images/desktop-home-page.png)

![Screenshot of mobile homepage wireframe](/documentation/images/mobile-homepage.png)
</details>

#### Posts List Page

**Description**: This wireframe illustrates the layout of the post list page, displaying a collection of posts organized by categories or filters.

<details>
<summary>Posts List Page - Desktop & Mobile</summary>

![Screenshot of desktop posts list wireframe](/documentation/images/desktop-post-list-page.png)

![Screenshot of mobile posts list wireframe](/documentation/images/mobile-posts-list-page.png)
</details>

#### Post Detail Page

**Description**: This wireframe illustrates the layout of a post detail page, showcasing the post content, comments section, and interaction options.

<details>
<summary>Post Detail Page - Desktop & Mobile</summary>

![Screenshot of desktop post detail wireframe](/documentation/images/desktop-post-detail-page.png)

![Screenshot of mobile post detail wireframe](/documentation/images/mobile-post-detail-page.png)
</details>

#### New Post Page

**Description**: This wireframe showcases the layout of the create post form, allowing users to compose new posts.

<details>
<summary>New Post Page - Desktop & Mobile</summary>

![Screenshot of desktop new post wireframe](/documentation/images/desktop-new-post-page.png)

![Screenshot of mobile new post wireframe](/documentation/images/mobile-create-new-post.png)
</details>

#### Edit Post Page

**Description**: This wireframe outlines the layout of the edit post form, allowing users to modify existing posts.

<details>
<summary>Edit Post Page - Desktop & Mobile</summary>

![Screenshot of desktop edit post wireframe](/documentation/images/desktop-edit-post-page.png)

![Screenshot of mobile edit post wireframe](/documentation/images/mobile-edit-post.png)
</details>

#### Edit Comment Page

**Description**: This wireframe illustrates the layout of the edit comment form, enabling users to edit their previously submitted comments.

<details>
<summary>Edit Comment Page - Desktop & Mobile</summary>

![Screenshot of desktop edit comment wireframe](/documentation/images/desktop-edit-comment-page.png)

![Screenshot of mobile edit comment wireframe](/documentation/images/mobile-edit-comment.png)
</details>

#### Rules Page

**Description**: This wireframe showcases the layout of the forum's rules page, providing guidelines and community standards.

<details>
<summary>Rules Page - Desktop & Mobile</summary>

![Screenshot of desktop rules wireframe](/documentation/images/desktop-rules-page.png)

![Screenshot of mobile rules wireframe](/documentation/images/mobile-rules-page.png)
</details>

#### Resources Page

**Description**: This wireframe illustrates the layout of the forum's resources page, offering helpful information and links for users.

<details>
<summary>Resources Page - Desktop & Mobile</summary>

![Screenshot of desktop resources wireframe](/documentation/images/desktop-resources-page.png)

![Screenshot of mobile resources wireframe](/documentation/images/mobile-resources-page.png)
</details>

#### Sign-Up Page

**Description**: This wireframe showcases the layout of the sign-up page, allowing new users to register for a forum account.

<details>
<summary>Sign-Up Page - Desktop & Mobile</summary>

![Screenshot of desktop sign-up wireframe](/documentation/images/desktop-sign-up-page.png)

![Screenshot of mobile sign-up wireframe](/documentation/images/mobile-sign-up.png)
</details>

#### Sign-In Page

**Description**: This wireframe outlines the layout of the sign-in page, enabling registered users to log into their forum accounts.

<details>
<summary>Sign-In Page - Desktop & Mobile</summary>

![Screenshot of desktop sign-in wireframe](/documentation/images/desktop-sign-in-page.png)

![Screenshot of mobile sign-in wireframe](/documentation/images/mobile-sign-in.png)
</details>

#### Sign-Out Page

**Description**: Users can sign out of their forum accounts to securely log out and end their session.

<details>
<summary>Sign-Out Page - Desktop & Mobile</summary>

![Screenshot of desktop sign-out wireframe](/documentation/images/desktop-sign-out-page.png)

![Screenshot of mobile sign-out wireframe](/documentation/images/mobile-sign-out.png)
</details>

### Agile Methodology

#### Definition And Planning:
* Commenced with the creation of a wireframe to visualize the website's layout.
* Crafted user stories to define the functionality of the website.
* Categorized user stories into priority groups: Must Have, Should Have, Could Have, and Won't Have.

![Screenshot of the user stories](/documentation/images/user-stories.png)

#### Iteration Creation:
* Assigned points to each user story based on complexity to facilitate estimation.
* Structured the project into five iterations, each representing distinct periods, typically spanning a few days.
* During each iteration, the focus was on completing user stories selected for that phase.

![Screenshot of the iterations](/documentation/images/iterations.png)

#### Kanban Board Implementation
* Employed a Kanban board to visually manage the workflow and track progress.
* Allowed for the seamless movement of user stories across various stages, from 'To Do' to 'In Progress' and finally 'Done'.
* This visual representation ensured transparency and clarity regarding the status of each task, fostering effective collaboration and informed decision-making throughout the project.

![Screenshot of the Knaban Board](/documentation/images/kanban-board.png)

#### Regular Reviews and Retrospectives:

At the conclusion of each iteration, I conducted an assessment of completed tasks and facilitated a retrospective session to pinpoint areas for process enhancement.

#### Reiteration:

For subsequent iterations, I revisited newly acquired user stories, reassessing their priority and significance to sustain the project's advancement.

This methodology enabled me to adeptly prioritize tasks and concentrate on pivotal objectives throughout each iteration, thus propelling the project forward according to predetermined objectives.

### Colour Pallete

For this website, I've selected specific colors to enhance different sections:

* The navbar features a deep purple (#634188ff) for a touch of elegance.
* Titles are in a paler purple (#DED2E3ff) to create a calm atmosphere.
* The background adopts a soft pinkish-beige (#CCB9B5ff) for comfort and nostalgia.
* Buttons are in a muted blue-grey (#6371A2ff) to convey reliability.
* Lastly, the footer and hovered buttons sport a rich orange-brown (#D87C3Cff) to stand out and add vitality.

![Screenshot of the website's colours pallete](/documentation/images/forum-pallete.png)

### Entity Relationship Diagram

The ERD for this forum represents the various entities and their relationships within the system. It illustrates how users, posts, comments, categories, and tags are interconnected. Users can create posts and comments, which are associated with specific categories and can be tagged with relevant keywords. Additionally, users can engage with posts by liking or commenting them. The ERD provides a clear visual representation of the data model underlying this forum, facilitating understanding and effective database design.

A visual representaion of the ERD is presented below:
![Screenshot of the entity relationship diagram within the forum's database](/documentation/images/erd.png)

## Features

### Home Page:
* Reassuring Quotes and Featured Posts
    * The home page displays inspiring and reassuring quotes to uplift users.
    * Featured posts are showcased on the home page to highlight important or popular content.

![Screenshot illustrating the forum's home page](/documentation/images/home-page.png)

### Navigation
* Navigation menu:
    * A navigation menu is present on all pages, allowing users to easily navigate between different sections of the website.
    * The navbar features dropdown icons to ensure a clean and organized appearance.
    * The hamburger menu appears on mobile devices and expands to display the primary navigation links.

![Screenshot illustrating the forum's navigation bar with the menu icons](/documentation/images/navigation-bar-menu.png)

### Authentication & Authorization
* Create Account:
    * Users can register for an account by providing necessary information such as username, email, and password.
    * It includes a sign in link for the users that may have forgotten they already have an account.

![Screenshot with the sign-up page](/documentation/images/sign-up-page-corrected.png)

* Login Page:
    * A login page is provided for users to securely log into their accounts using their credentials.
    * A login requirement condition has been incorporated into the views, ensuring that users are redirected to this page when attempting to view post details.

![Screenshot with the sign in page](/documentation/images/sign-in-page.png)

* Log Out Page:
    * Users can log out of their accounts with the option to cancel if they have pressed this option by mistake or changed their mind.

![Screenshot with the log out page](/documentation/images/sign-out-page.png)

### Search Bar
* Search Functionality:
    * A search bar is available on the posts list page, enabling users to search for specific posts by entering keywords.

### Filters
* Filter By Age And Category:
    * Users can filter posts on the posts list page by age and category to find relevant content more efficiently.

![Screenshot with the search bar and the filtering options](/documentation/images/search-and-filter-posts.png)

### CRUD Functionality
* Create, Read, Update, Delete Posts:
    * Users can create new posts, providing a title, content, category and optionally selecting adding tags.
    * Users can view their own posts along with the posts of other users.
    * Users have the ability to edit their own posts, modifying the title, content, categories, and tags.
    * Users can delete their own posts, removing them from public view and the database.

<details>
<summary>Create Post</summary>

![Screenshot with create new post](/documentation/images/new-post-form.png)

</details>

<details>
<summary>Read Post</summary>

![Screenshot with accessing post detail](/documentation/images/post-detail-access.png)

![Screenshot with post detail](/documentation/images/post-detail.png)
</details>

<details>

<summary>Update Post</summary>

![Screenshot with edit post form](/documentation/images/edit-post-form.png)
</details>

<details>

<summary>Delete Post</summary>

![Screenshot with delete post message](/documentation/images/delete-post.png)
</details>

* Create, Read, Update, Delete Comments:
    * Users can create comments on posts, providing their feedback or thoughts.
    * Users can view comments made by themselves and others on posts.
    * Users have the ability to edit their own comments, modifying the content and the photo.
    * Users can delete their own comments, removing them from public view and the database.

<details>
<summary>Create Comment</summary>

![Screenshot with create new comment form](/documentation/images/new-comment-form.png)

</details>

<details>
<summary>Read Comment</summary>

![Screenshot with comments on a post](/documentation/images/comments.png)
</details>

<details>

<summary>Update Comment</summary>

![Screenshot with edit comment form](/documentation/images/edit-comment-form.png)
</details>

<details>

<summary>Delete Comment</summary>

![Screenshot with delete comment message](/documentation/images/delete-comment.png)
</details>

### Resources Page

* Users can download files that admins upload on this page.
![Alt Text](/documentation/images/download-resources.png)

### Contact Page
* Users can submit a contact form to the admins
![Alt Text](/documentation/images/user-contact-page.png)


### Admin Panel

<details>

<summary>Control Featured Posts:</summary>

![Screenshot with admin panel](/documentation/images/is-featured-admin.png)
</details>

* Admins can select and manage featured posts, determining which posts are displayed prominently on the homepage.

<details>

<summary>Update Rules and Resources:</summary>

![Screenshot with admin panel](/documentation/images/add-rules.png)

![Screenshot with admin panel](/documentation/images/add-downloading-resource.png)

![Screenshot with admin panel](/documentation/images/add-resource-link.png)
</details>

* Admins have the ability to update rules and resources, ensuring that users are informed of any policy changes or new resources available.

<details>
<summary>Delete, Add, Update Posts:</summary>

![Screenshot with admin panel](/documentation/images/admin-delete-posts.png)

![Screenshot with admin panel](/documentation/images/admin-add-post.png)

![Screenshot with admin panel](/documentation/images/admin-edit-posts.png)
</details>

* Admins can delete, add, and update posts on the website, giving them control over the content displayed to users.

<details>
<summary>Manage Users:</summary>

![Screenshot with admin panel](/documentation/images/admin-add-user.png)

![Screenshot with admin panel](/documentation/images/admin-delete-users.png)

![Screenshot with admin panel](/documentation/images/user-authorization.png)
</details>

* Admins can manage users, including adding new users, deleting existing users, and modifying user permissions.

<details>

<summary>Contact Requests Management:</summary>

![Screenshot with admin panel](/documentation/images/contact-requests-read.png)
![Screenshot with admin panel](/documentation/images/contact-requests-delete.png)
</details>

* Admins can manage contact requests by marking them as read or deleteing them.

### Success Messages

<details>

<summary> Success message displayed upon adding, editing, or deleting posts/comments.</summary>

![Alt text](/documentation/images/post-submitted.png)
![Alt text](/documentation/images/post-updated.png)
![Alt text](/documentation/images/post-deleted.png)
![Alt text](/documentation/images/comment-submitted.png)
![Alt text](/documentation/images/comment-updated.png)
![Alt text](/documentation/images/comment-deleted.png)

</details>

<details>

<summary> Confirmation message shown upon liking posts/comments.</summary>

![Alt text](/documentation/images/post-like.png)
![Alt text](/documentation/images/comment-like.png)
![Alt text](/documentation/images/comment-unlike.png)

</details>

<details>

<summary>Notification upon successful login/logout.</summary>

![Alt text](/documentation/images/succesful-login.png)

![Alt text](/documentation/images/succesfully-loggedout.png)

</details>

### Future Implementations

#### Admin Review and Pending Status:

* Introduce a review process where all user-submitted reviews undergo evaluation by an admin.
* Upon submission, reviews are marked with a "Pending Review" status.
Admins have access to a dedicated dashboard where they can review pending reviews.
* After review, admins can either approve or reject the review. If rejected, they can provide feedback to the user.
* Users receive notifications about the status of their reviews, informing them whether it's approved or rejected.

#### User Profile with Profile Photo:

* Enhance user profiles to include personal details such as name, email, bio, and a profile photo.
* Users can upload a profile photo from their device or select one from a predefined set of avatars.
* Ensure the profile page is customizable, allowing users to manage their personal information easily.

#### Video Uploading by Users:

* Implement a feature enabling users to upload videos related to the platform's content.
* Integrate video uploading functionality with the platform's existing infrastructure.
* Apply appropriate file size and format restrictions, and provide feedback to users during the upload process.

#### Reply to Comments with Infinite Replies:

* Enable users to reply to comments on posts/videos, fostering interactive discussions.
* Implement a nested commenting system that supports unlimited levels of replies.
* Ensure clear visual indicators for nested replies to maintain readability.


#### Tagging Usernames in Replies:

* Allow users to tag other users by their usernames when replying to comments.
* Implement autocomplete functionality to assist users in selecting the correct username.

#### Reporting Comments and Users:
* Introduce a reporting feature that allows users to flag inappropriate comments or user behavior.
* Include options for reporting individual comments or entire user profiles.
* Admins can review reported content and take appropriate actions, such as removing comments or suspending user accounts.

## Technologies Used

### Core Development Technologies

* Django (Python) for building the backend application.
* JavaScript and Python (Django) for server-side logic.
* HTML, CSS, JavaScript (ES6) for building the user interface.

### Libraries, Frameworks and Packages

* **[Crispy-Bootstrap5](https://django-crispy-forms.readthedocs.io/en/latest/)** and django-crispy-forms (Version 2.1) for integrating Bootstrap 5 with Django forms, providing easy-to-use, crispy forms with Bootstrap styling.
* **[Django-Allauth](https://allauth.org/)** to provide a set of authentication and account management functionalities.


### Python/Django Packages
* **[Gunicorn](https://pypi.org/project/gunicorn/)**, a Python WSGI HTTP server for Unix, used to deploy the application in production environment.
* **[Psycopg2](https://pypi.org/project/psycopg2/)**, a PostgreSQL adapter for Python, allows Django to interact with the PostgreSQL database.
* **[Pillow](https://pypi.org/project/pillow/)**, a Python Imaging Library (PIL) fork, used for image processing in the application.
* **[Whitenoise](https://pypi.org/project/whitenoise/)** used to serve static files efficiently in production.
* **[Sqlparse](https://pypi.org/project/sqlparse/)** used for SQL query formatting and debugging.

### Infrastructural Technologies

* **[Git](https://git-scm.com/)** - A tool for version control, managing changes to source code files.
* **[GitHub](https://github.com/)** - A platform where all website files are stored and organized within repositories.
* **[Gitpod](https://gitpod.io/)** - An Integrated Development Environment (IDE) utilized for coding and editing project files.
* **[Figma](https://www.figma.com/)** - A collaborative interface design tool utilized for designing and creating database models for the project.
* **[Heroku](https://www.heroku.com/)** - A platform utilized for deploying and hosting the project.
* **[ElephantSQL](https://www.elephantsql.com/)** - A managed PostgreSQL database service used for storing project data.
* **[Cloudinary](https://cloudinary.com/)** for managing multimedia content in this Django application.

## Testing

### Google's Lighthouse Performance

#### Home Page

<details>

<summary>Home Page</summary>

![Alt text](/documentation/images/lighthouse-home-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-home-mobile.png)

</details>

#### Posts Page

<details>

<summary>Desktop</summary>

![Alt text](/documentation/images/lighthouse-posts-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-posts-mobile.png)

</details>

#### Post Detail Page

<details>

<summary>Desktop</summary>

![Alt text](/documentation/images/lighthouse-post-detail-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-post-detail-mobile.png)

</details>

#### New Post Page

<details>

<summary>Desktop</summary>

![Alt text](/documentation/images/lighthouse-add-post-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-create-post-mobile.png)

</details>

#### Rules Page

<details>

<summary>Desktop</summary>

![Alt text](/documentation/images/lighthouse-rules-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-rules-mobile.png)

</details>

#### Resources Page

<details>

<summary>Desktop</summary>

![Alt text](/documentation/images/lighthouse-resources-desktop.png)

</details>

<details>

<summary>Mobile</summary>

![Alt text](/documentation/images/lighthouse-resources-mobile.png)

</details>

## Browser Compatibility

### Responsiveness

Utilizing Google Dev Tools during development and subsequently verifying with the Responsivity app, it has been confirmed that the forum website demonstrates commendable responsiveness across a range of devices, encompassing mobile phones, tablets, laptops, and desktop computers.

![Screenshot of the forum posts page on iPhone 12 Pro](/documentation/images/iphone-12-pro-390x844.jpeg)
![Screenshot of the forum posts page on iPad Pro](/documentation/images/ipad-768x1024.jpeg)
![Screenshot of the forum posts page on McBook Pro](/documentation/images/mcbook-pro-1440x900.jpeg)

| Device | iPhone SE | iPhone X | iPhone 12 Pro | iPhone 13 Pro Max | iPhone 14 Pro Max | iPad | iPad Air | iPad Pro | Macbook Pro |
| ---------| ----------- | ------| -------| ----------| ---------- | ------------ | ---------- | ------------- | ------------ |
| **Resolution** | **375x667** | **375x812** | **390x844** | **414x76** | **414x896** | **768x1024** | **820x1180** | **1024x1366** | **1440x900** |
| **Render** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| **Layout** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| **Functionality** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass|
| **Links** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| **Images** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |
| **Portrait/Landscape** | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass |

### Code Validation

Every HTML page underwent examination with the [W3C Markup Validation Service](https://validator.w3.org/), revealing no significant errors.

#### Home Page

![Home Page html validation results](/documentation/images/home-html.png)

#### Posts Page

![Posts Page html validation results](/documentation/images/post-list-html.png)

#### Posts Page

![Posts Page html validation results](/documentation/images/post-list-html.png)

#### Add Post Page

![Add Post Page html validation results](/documentation/images/add-post-html.png)

#### Edit Post Page

![Edit Post Page html validation results](/documentation/images/edit-post-html.png)

#### Rules Page

![Rules Page html validation results](/documentation/images/rules-html.png)

#### Resources Page

![Resources Page html validation results](/documentation/images/resources-html.png)

#### CSS

The CSS page was checked using the [W3C Markup Validation Service](https://validator.w3.org/), and no errors were found.

![Styling file validation results](/documentation/images/style-css.png)


### JavaScript

Both JavaScript files successfully passed through [JSHint](https://jshint.com/) without encountering any errors.

![Messages js validation results](/documentation/images/messages-js.png)

![Script js validation results](/documentation/images/script-js.png)

### Python

All custom Python code files were formatted according to the PEP8 standards using the [Black](https://pypi.org/project/black/) formatter.

## Manual Testing

### Notifications and feedback testing for submitting a post
| Action | Notifications and feedback for posting | Result |
| ------- | ------- | ---------|
| Add a post | Your post has been submitted succesfully! | Pass |
| Edit post | You post has been updated succesfully | Pass |
| Delete post | Your post has been succesfully deleted! | Pass |
| Cancel delete post | Returns to the post detail | Pass |

### Notifications and feedback testing for comments

| Action | Notifications and feedback for commenting | Result |
| ------- | ------- | ---------|
| Add a comment |  Your comment has been posted successfully! | Pass |
| Edit a comment | Comment updated successfully! | Pass |
| Delete a comment | Comment deleted successfully! | Pass |
| Cancel delete comment | Returns to the post detail | Pass |

### Notifications and feedback testing for contact form

| Action | Notifications and feedback for contact request | Result |
| ------- | ------- | ---------|
| Submit contact form with details |  Your contact request has been submitted successfully! | Pass |

### Notifications and feedback testing for sign up, sign in and sign out

| Action | Notifications and feedback for contact request | Result |
| ------- | ------- | ---------|
| Sign Up |  You have successfully logged in. | Pass |
| Sign In | You have successfully logged in. | Pass |
| Sign Out |  You have successfully logged out. | Pass |

### Notifications and feedback testing for the admin panel

| Action | Notifications and feedback for action | Result |
| ------- | ------- | ---------|
| Contact form submitted | Message displayed in the contact requests section | Pass |
| <details><summary>Contact form marked as read</summary> ![Alt text](/documentation/images/mark-as-read-1.png)</details> | <details><summary>Read column changes from red "x" to green tick</summary> ![Alt text](/documentation/images/mark-as-read-2.png)</details> | Pass |
| <details><summary>Delete a post or more</summary> ![Alt text](/documentation/images/delete-a-post.png)</details>| <details><summary>Successfully deleted {number} post(s).</summary> ![Alt text](/documentation/images/succesfully-deleted-post.png)</details> | Pass |
| <details><summary>Delete a comment or more </summary> ![Alt text](/documentation/images/delete-a-comment.png)</details>|<details><summary> Successfully deleted {number} comment(1). </summary> ![Alt text](/documentation/images/successfully-deleted-comment.png)</details> | Pass |
|<details><summary> Mark a post as featured  </summary> ![Alt text](/documentation/images/featured-posts.png)</details>| <details><summary>Tick the 'is featured' column  </summary> ![Alt text](/documentation/images/mark-as-featured.png)</details>| Pass |
| <details><summary>Ad a new rule </summary> ![Alt text](/documentation/images/add-a-new-rule.png)</details>| <details><summary>Submit rule</summary> ![Alt text](/documentation/images/submit-a-new-rule.png)</details> | Pass |
| <details><summary>Add a downloading resource </summary> ![Alt text](/documentation/images/add-new-resources.png)</details> | <details><summary>Submit resource </summary> ![Alt text](/documentation/images/submit-new-resource.png)</details> | Pass |

### Testing all links and buttons on website

| Link/Button | Purpose | Result |
| ------- | ------- | ---------|
| Navbar Brand | Returns to Home Page | Pass |
| Navbar Home Link | Returns to Home Page | Pass |
| Navbar Posts Link | Takes user to the posts list | Pass |
| Navbar About/Rules Link | Takes user to rules page | Pass |
| Navbar About/Resources Link | Takes user to the resources page | Pass |
| Navbar user icon link | Shows and takes user to sign in/sign up page when not registered | Pass |
| Navbar user name link | Takes user to the sign out page when logged in | Pass |
| "here" link in introduction | Takes user to add post page if logged in | Pass |
| "here" link in introduction | Takes user to sign in page if not registered | Pass |
| Clickable featured post title | Takes user to the post detail page if logged in | Pass |
| Clickable featured post title | Takes user to the sign in page if logged out | Pass |
| Read More Button in featured posts | Takes user to the post detail page if logged in | Pass |
| Read More Button in featured posts | Takes user to the sign in page if logged out | Pass |
| Footer Contact Us | Takes the user to the contact form page | Pass |
| Contact form submit button | Submits the request form to admin | Pass |
| Add Post button on posts page | Opens a new post form | Pass |
| Create post button on new post page | Submits a new post | Pass |
| Choose file button on new post page | Opens a window to choose a photo from user's computer | Pass |
| Search button on posts page | Brings up posts that contain the word(s) inserted by the user | Pass |
| Apply Filter button on posts page | Brings up posts that apply to the filter(s) chosen by the user | Pass |
| Clear Filter button on posts page | Brings up the whole posts list | Pass |
| Clickable post title | Takes user to the post detail page if logged in | Pass |
| Clickable post title | Takes user to the sign in page if logged out | Pass |
| Read More Button in posts content | Takes user to the post detail page if logged in | Pass |
| Read More Button in posts content | Takes user to the sign in page if logged out | Pass |
| Submit button on post detail page | Submits a new comment | Pass |
| Choose file button on post detail page | Opens a window to choose a photo from user's computer | Pass |
| Edit button on post detail | Opens the post in an editable format | Pass |
| Save Changes button on edit post page | Saves the updated post | Pass |
| Cancel button on edit post page | Returns the user to the post detail page | Pass |
| Delete button on post detail | Opens a window for the user to confirm deletion | Pass |
| Delete button on the delete modal | Removes the post and returns the user to the posts list | Pass |
| Cancel button on delete modal | Returns the user to the post detail page | Pass |
| Heart shaped button on the post detail | Counts the number of likes (clicks) a post has | Pass |
| Edit button on comment | Opens the comment in an editable format | Pass |
| Update button on edit comment page | Saves the updated comment | Pass |
| Cancel button on edit comment page | Returns the user to the post detail page | Pass |
| Delete button on comment| Opens a window for the user to confirm deletion | Pass |
| Delete button on the delete modal | Removes the comment and returns the user to the posts list | Pass |
| Cancel button on delete modal | Returns the user to the post detail page | Pass |
| Heart shaped button on the comment | Counts the number of likes (clicks) a comment has | Pass |
| Next button on posts list | Takes the user to the next page of posts | Pass |
| Number buttons between Next and Prev | Takes the user to that page number of posts | Pass |
| Prev button on posts page | Takes the user to the previous page of posts | Pass |
| Sign Out button | Logs out user and takes them to the home page | Pass |
| Cancel button on the sign out page | Return the user to the previous page | Pass |
| Sign In button | Logs the user in and takes him to the home page if selected from the navbar or to the post detail if redirected to it | Pass |
| Sign Up button | Takes the user to the register form, logs them in and direct them to the home page | Pass |

## Bugs

| Bug | Fix
|:-------:|:--------|
| After standardizing the style of all the buttons, I changed the class of the delete comment button, causing it to stop working when clicked. | Upon reviewing the JavaScript file, I realized that I had removed the class targeted by the event listener and corrected it. 

| Bug | Fix
|:-------:|:--------|
Success messages were not appearing on the right side of the page and were not visible to the user. | After extensive research without finding a solution, I decided to use a modal for better visibility.

![Example of the sussces message](/documentation/images/comment-updated.png)

| Bug | Fix
|:-------:|:--------|
After introducing the modal for messages, I have noticed that they showed twice when there were no search results and when submitting a contact form. | I fixed this by removing the html code that was displaying them initially.


| Bug | Fix
|:-------:|:--------|
To allow users to edit a comment, I used a prefilled form that appeared in the new comment section. However, the page didn't scroll to the form automatically, making it seem like the edit button wasn't working because the form wasn't immediately visible to the user. | I decided to create a new html file for editing the comment, similar to editing the post.

![Edit comment form](/documentation/images/edit-comment-form.png)

