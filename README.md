# StarWarsFirestore

# Overview

In my journey as a software engineer, I've embarked on a fascinating project: developing a Star Wars-themed application integrated with a Firestore cloud database. This web application serves as a rich platform for fans and users to explore and manage a collection of Star Wars characters, allowing operations such as adding, viewing, updating, and deleting character records.

The primary goal behind creating this software was to dive deeper into the realms of cloud database integration and RESTful API development while crafting an engaging user experience centered around the beloved Star Wars universe. Through this project, I aimed to solidify my skills in full-stack development and learn how to efficiently manage and present dynamic data in a web application.

[Software Demo Video](https://youtu.be/sm7RtQlf49Y)

# Cloud Database

The backbone of this application is Firebase Firestore, a flexible, scalable NoSQL cloud database from Google. Firestore's real-time data syncing capabilities and straightforward setup made it an ideal choice for this project. It enables the application to instantly reflect updates, providing an interactive and up-to-date experience for users.

I designed the Firestore database with a structure that mirrors the rich lore of the Star Wars universe. The database comprises two collections named people and planet, with each document representing a unique character or planet in the Star Wars galaxy. 


# Development Environment

- Visual Studio Code: My go-to code editor for its robust features, extensions, and integrated terminal, facilitating coding, debugging, and version control in one place.
- Flask: A Python micro-framework used to construct the backend logic, including the API endpoints for interacting with the Firestore database.
- Firebase Admin SDK for Python: This server-side library connects the Flask backend with Firebase Firestore, enabling seamless data operations.
- Postman: Essential for testing the API, ensuring each endpoint accurately performs the expected operations before integrating with the frontend.

# Useful Websites

- [Firebase Documentation](https://firebase.google.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [Firestore Tutorial](https://firebase.google.com/docs/firestore)
- [Firebase Console](https://firebase.google.com/docs/firestore)

# Future Work

- User Authentication and Profiles: Introduce user authentication to allow fans to create their profiles, save favorite characters, and possibly interact with other users.
- Advanced Searching and Filtering: Implement advanced search and filtering capabilities, enabling users to find characters based on specific criteria such as species, or homeworld.
- UI/UX Enhancements: Continue to refine the user interface and experience, incorporating feedback from users and adding animations or interactive elements that immerse users in the Star Wars theme

