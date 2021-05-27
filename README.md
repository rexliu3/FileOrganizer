[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Python program that organizes different file types into different folders.
* For example, all .docx files are moved into a "Documents" folder

### Built With
* [Python](https://www.python.org/)
* [watchdog](https://pypi.org/project/watchdog/)


## Getting Started
### Prerequisites
* Python
  ```sh
  https://www.python.org/downloads/
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/rexliu3/FileOrganizer.git
   ```
2. Enter the folder path in `Main.py`
   ```py
   folder_to_track = "ENTER FOLDER PATH HERE"
   ```


<!-- USAGE EXAMPLES -->
## Usage
Run `Main.py`: ``` python3 Main.py ```
* The program will then begin monitoring the specified folder and organize documents into their appropriate folders
* Note: you may need to create the following folders in the specified folder: "PDFs", "Images", "Program Downloads exe", "Videos", "Documents", "Unknown File Type"


<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/rexliu3/FileOrganizer/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact
Rex Liu - rexliu3@berkeley.edu

Project Link: [https://github.com/rexliu3/FileOrganizer](https://github.com/rexliu3/FileOrganizer)


[contributors-shield]: https://img.shields.io/github/contributors/rexliu3/FileOrganizer?style=for-the-badge
[contributors-url]: https://github.com/rexliu3/FileOrganizer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rexliu3/FileOrganizer?style=for-the-badge
[forks-url]: https://github.com/rexliu3/FileOrganizer/network/members
[stars-shield]: https://img.shields.io/github/stars/rexliu3/FileOrganizer?style=for-the-badge
[stars-url]: https://github.com/rexliu3/FileOrganizer/stargazers
[issues-shield]: https://img.shields.io/github/issues/rexliu3/FileOrganizer?style=for-the-badge
[issues-url]: https://github.com/rexliu3/FileOrganizer/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/rexliu3/FileOrganizer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rexliu3
