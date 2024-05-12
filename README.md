# Journeying Through Parenthood

## Introduction <a name="introduction"></a>

Navigating Parenthood Together is a vibrant online community tailored for parents navigating the diverse challenges of raising children of varying ages. Whether you're facing the trials of toddlerhood or grappling with the complexities of teenage years, this forum offers a supportive space where parents can seek guidance, share experiences, and find solace in knowing they're not alone on this journey.

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

