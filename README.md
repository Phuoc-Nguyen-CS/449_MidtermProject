# CPSC 449 Midterm Project

## Table of Contents
1. [Demonstration](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#demonstration)
2. [POSTMAN](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#postman)
- [Register](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#register)
- [Login](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#login)
- [Upload](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#upload)
- [Uploaded](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#uploaded)
3. [Objective](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#objective)
4. [Members](https://github.com/Phuoc-Nguyen-CS/449_MidtermProject#members)


## Submission Checklist:
 - [ ] Include a requirement.txt file with all the necessary packages.
 - [ ] Include one screenshot including all the endpoints listed in POSTMAN.
 - [ ] Your submission should include a video demonstrating the working of authentication and file handling endpoints


## Demonstration:

Uploading File Demo Video:
[![](https://i0.wp.com/css-tricks.com/wp-content/uploads/2015/11/drag-drop-upload-1.gif?ssl=1)](https://www.youtube.com/watch?v=dz6Oh0MD9Ds&ab_channel=PhuocNguyen)

## POSTMAN:
### Register
![Register](./pictures/register.png)

### Login
![Login](./pictures/login.png)

### Upload
![Upload](./pictures/upload.png)

### Uploaded
![Uploaded](./pictures/uploaded.png)
 
## Objective:
### Task 1: Setting up the Flask application
* Create a **new Flask application** and set up the **necessary packages and modules.**
* **Create a virtual environment** for the application.
* **Connect your Flask application** with the Database (MySQL preferably.)
### Task 2: Error Handling
* **Implement error handling** for your API to ensure that it returns proper error messages and status codes.
* **Create error handlers*** for ex. 400, 401, 404, 500, and any other errors that you feel
are necessary.
* Make sure that error messages are **returned in a consistent format.**
### Task 3: Authentication
* Implement **authentication** for your **API** using **JWT.**
* **Create a user model** with username and password fields.
* **Implement a login endpoint** that authenticates the user and **returns a JWT token.**
* **Implement a protected endpoint** that requires a valid JWT token to access.
### Task 4: File Handling
* **Implement file handling** for your API to allow users to upload files.
* **Create an endpoint** that allows users to upload files. 
* **Implement file validation** to ensure that files are uploading within the allowed file size limit.
* **Store uploaded files** in a secure location. (A folder in your project's folder structure.)
### Task 5: Public Route
* **Create a public route** that allows users to view public information.
* **Implement an endpoint** that returns a list of items that can be **viewed publicly.**
* Ensure that this **endpoint does not require authentication.**

## Members:
* Phuoc Nguyen
* Christian Verry
* Linh Nguyen
