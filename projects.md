Below you can find some curated (open-source and proprietary) projects that give you a good overview of my strengths.
You can also view a list of my most successful open-source projects [here](https://github.com/Osiris-Team?tab=repositories&q=&type=&language=&sort=stargazers) if you are interested.

Take a look at some client reviews (average 4.8/5 stars), all of them can be found here on [Fiverr](https://www.fiverr.com/osiristeam):

> Really enjoyed working with him, put alot of effort into the work and solved all my issues. Really recommend working with him and would love to work with him again in the future! - l_12346, Australia

> I had hired several developers from Fiverr, however everyone failed except this developer. He was the only one able to identify my problem and solve it. - domenicherge649, Germany

> Great communication and fast replies, delivered what was asked for. Before any important decision, always asked which approach was in my best interest. - mani_monti, Portugal

#### Extension of a CRM Web-Panel

I expanded the functionality of an existing CRM Web-Panel by developing a new, separate Web-Panel that operates on the same machine and connects to the same SQL database as the original CRM.
This approach was necessary due to the closed-source nature of the original CRM; however, the original developers provided access to the database, allowing for the integration of additional features through my external software.

The new functionalities included advanced filtering and enhancement of client customer data through web scraping and integration with the Google Maps/Places API. Furthermore, I implemented a phone number validation feature by leveraging the Twilio API to ensure data accuracy and improve the overall quality of the CRM system.

<div align="center">
    <img src="https://github.com/user-attachments/assets/b2ca8901-68ac-4e1f-84a3-b578c7d7ede8"></img>

</div>

#### Custom ERP Web-Panel

I developed a fully customized ERP Web-Panel designed to meet the specific requirements of the client, incorporating a variety of advanced and tailored features. Among these was an integrated web-based PDF editor, which included customizable preset templates and the capability for automatic data population, significantly streamlining document creation. Additionally, the system featured a robust product database for managing inventory and a secure customer information storage solution, enabling efficient data retrieval and management.

To enhance collaboration and user experience, the ERP solution also supported multi-user functionality, allowing seamless teamwork across departments. This was complemented by integrated real-time chat features for instant communication and a Google-synced calendar for managing schedules and appointments. Together, these features created a comprehensive, user-friendly platform that improved both operational efficiency and team coordination.

<div align="center">
    <img src="https://github.com/user-attachments/assets/bdeb2ea4-2835-4d88-94d5-315e51758709"></img>
</div>

#### Airport Camera Control Web-Panel 

The system enables live video streaming from multiple airport cameras, with full control over their feeds, and includes an advanced feature for tracking incoming airplanes using AI-powered object detection. This was a particularly complex challenge, as it required processing individual frames from the video stream in real-time while ensuring high performance despite the computational demands of object detection, which led to occasional processing spikes. To address this, several performance optimizations were implemented to ensure smooth operation and minimize latency.

Additionally, the solution had to interface with the airport cameras using a proprietary, legacy SDK, which introduced additional complexity in terms of compatibility and integration. Despite these challenges, the system successfully delivered a robust, real-time video surveillance and tracking solution, providing accurate airplane monitoring and seamless camera control for airport operations.

<div align="center">
    <img src="https://github.com/user-attachments/assets/9ce4dd85-a8e4-4862-bb70-ede1b5a1bb6d"></img>
</div>

#### AutoPlug-Web and Client
AutoPlug is my largest personal and monetized project. Its goal is to simplify/automate maintenance tasks of server admins.
Its made of 2 parts which optionally can communicate with each other.

AutoPlug-Web can be accessed at [autoplug.one](https://autoplug.one/) and is more of a centralized admin panel to manage servers
and collaborate with server staff easily.
It communicates with the AutoPlug-Client and is responsible for critical/sensitive operations like showing/adding/updating/removing files based on user permissions
and providing access to terminals. This requires a high level of security and trust from its users, which is given by using a backend and security focused framework
called [Vaadin](https://vaadin.com/). Developing this part of the software taught me about handling the complexity of larger applications, webservers in general, SSL,
HTML/CSS/JavaScript, payment systems like PayPal/Stripe integrated via my [PayHook](https://github.com/Osiris-Team/PayHook) library, SQL databases and code generation with my [jSQL-Gen](https://github.com/Osiris-Team/jSQL-Gen) tool. The File-Manager looks like this (outdated):

<div align="center">
    <img src="https://github.com/Osiris-Team/AutoPlug-Client/blob/master/docs/file-manager.gif?raw=true"></img>
</div>


This is accompanied by the AutoPlug-Client, which contains most of the automation features. Developing it taught me a lot about Java in general, Server-Client communication, the TCP protocol, REST-APIs, web-scraping, JSON,
and even made me consider very interesting alternatives like [Netty](https://netty.io/), which finally was not implemented due to the release of Virtual-Threads and the comparatively simpler Java Sockets-API. This is what it looks like when running some tasks (outdated):

<div>
    <img src="https://github.com/Osiris-Team/AutoPlug-Client/blob/master/docs/tasks.gif?raw=true"></img>
</div>



#### Desku
[Desku](https://github.com/Osiris-Team/Desku) is a low-code, developer-first Java framework with UI components, for developing cross-platform desktop, web, android/ios apps in one codebase.
I like the Java language, however its GUI libraries feel outdated and something like this doesn't really exist, thus this project. Under the hood it's based on Webviews, meaning it uses HTML/CSS/JS to
display the frontend, which theoretically makes it compatible with all frontend frameworks out there. The focus here is to provide a developer-friendly, simple API and
handle the more complex things in Desku. This project expanded my knowledge of webserver internals and made me discover some annoyances of the Java language
(which you can find over at [my-jsrs](https://github.com/Osiris-Team/my-jsrs)).


<div align="center">
    <img src="https://github.com/user-attachments/assets/8e9641ad-ae03-4413-babe-4eb0094a08fc"></img>
</div>



#### PayHook
PayHook is a lightweight and efficient Java library designed to simplify payment processing by unifying PayPal and Stripe into a single API. It eliminates the need for developers to manually handle JSON, API requests, or database storage, streamlining the integration of both one-time and subscription-based payments. Built with simplicity in mind, PayHook consists of just three core classes—PayHook, Product, and Payment—making it easy to adopt while maintaining flexibility for various use cases. By leveraging webhooks, it ensures secure and verified transactions, automatically managing missed payments and cancellations to reduce operational overhead.

Developing PayHook has deepened my expertise in Java development, API integration, Webhooks/REST, and payment processing systems. I designed the library to unify PayPal and Stripe under a single, developer-friendly API, eliminating the need for direct JSON handling, API calls, and manual database management. Through this project, I honed my skills in designing scalable architectures, implementing secure webhook-based transactions, and optimizing database performance with low-level SQL queries. Additionally, working with real-time payment events reinforced my understanding of concurrency, data integrity, and error handling in mission-critical applications.


#### Android Apps
I worked on multiple Open-Source Android apps like [OpenLauncher](https://github.com/Osiris-Team/openlauncher),
[Simple-Calendar](https://github.com/Osiris-Team/Simple-Calendar), 
[Notally](https://github.com/Osiris-Team/Notally),
[VinylMusicPlayer](https://github.com/Osiris-Team/VinylMusicPlayer), etc. where I fixed bugs and implemented new features for clients.
This taught me how to interact with existing code, fight the need of changing everything and focus on adding the requested changes only.
I also achieved a basic understanding of the Android API and the Kotlin language, plus these projects also made me better at debugging/navigating 
other developers code.
