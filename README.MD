# 🏂 Digital Snowboarding 🏂
![Static Badge](https://img.shields.io/badge/python-3.12-green)
![Static Badge](https://img.shields.io/badge/django-5.0.6-blue)
<img alt="GitHub" src="https://img.shields.io/github/license/n1ce7ry/digital-snowboarding">

## Table of Contents

  - [About](#about)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Deploy](#deploy)
  - [Contributing](#contributing)
  - [License](#license)

## About

Digital Snowboarding is an innovative platform created to support and promote snowboarding as a sport and culture. The site offers comprehensive information coverage and commercial support for snowboarding events.

## Features

- Create profile and login.
- Publication of the current list of participating teams.
- Display current results and statistics.
- Detailed profiles of each competitor.
- A rich collection of event photos and videos.
- Live streaming of the event in real time.
- Easily purchase tickets for upcoming events.
- Exclusive merchandise with competition symbols.

## Getting Started

Follow these steps to get started:

1. Clone the project: 
```bash
git clone https://github.com/n1ce7ry/digital-snowboarding`
```
2. Install the dependencies 
```bash
pip install -r requirements.txt
```
3. Edit env.example, rename it to env.sh, and run it: 
```bash
vim env.example
mv env.example env.sh
source env.sh
```
4. Apply database migrations
```bash
python manage.py migrate
```
5. Create a superuser account: 
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

Once you start your local server, you can log in to it through your web browser.

## Deploy

### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`

## Contributing

We welcome contributions from the community! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test them.
4. Commit your changes: `git commit -m "Add your brief commit message"`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Create a pull request to the `main` branch of this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.