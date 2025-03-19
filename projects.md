Below you can find some curated (open-source and proprietary) projects that give you a good overview of my strengths.
You can also view a list of my most successful open-source projects [here](https://github.com/Osiris-Team?tab=repositories&q=&type=&language=&sort=stargazers) if you are interested.

Take a look at some client reviews (average 4.8/5 stars), all of them can be found here on [Fiverr](https://www.fiverr.com/osiristeam):

> Really enjoyed working with him, put alot of effort into the work and solved all my issues. Really recommend working with him and would love to work with him again in the future! - l_12346, Australia

> I had hired several developers from Fiverr, however everyone failed except this developer. He was the only one able to identify my problem and solve it. - domenicherge649, Germany

> Great communication and fast replies, delivered what was asked for. Before any important decision, always asked which approach was in my best interest. - mani_monti, Portugal

#### Custom ERP Web-Panel

A fully custom ERP Web-Panel with individual features requested by the client like an integrated web-based pdf-editor with presets and automatic data filling, a products database and customer information data storage, as well as multi-user collaboration capabalities and integrated chat and google synchronized calendar.

<div align="center">
    <img src="https://github.com/user-attachments/assets/bdeb2ea4-2835-4d88-94d5-315e51758709"></img>
</div>

#### Airport Camera Control Web-Panel 

Allows live video streaming of different airport cameras and controlling them, with an option to track incoming airplanes by using AI (object detection).
This was a challenging request since it required handling the individual images of the video stream and several performance optimizations due to object detection causing spikes in processing.
Besides it also had to communicate with the cameras via a proprietary, older SDK.

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

#### Android Apps
I worked on multiple Open-Source Android apps like [OpenLauncher](https://github.com/Osiris-Team/openlauncher),
[Simple-Calendar](https://github.com/Osiris-Team/Simple-Calendar), 
[Notally](https://github.com/Osiris-Team/Notally),
[VinylMusicPlayer](https://github.com/Osiris-Team/VinylMusicPlayer), etc. where I fixed bugs and implemented new features for clients.
This taught me how to interact with existing code, fight the need of changing everything and focus on adding the requested changes only.
I also achieved a basic understanding of the Android API and the Kotlin language, plus these projects also made me better at debugging/navigating 
other developers code.
