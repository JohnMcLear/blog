# Workspace & User Profile: John McLear

## About the User: John McLear
John is a senior software engineer and open-source advocate born and raised in Bradford, UK. He has been deeply involved in ICT since age 18, transitioning from technical support to managing large-scale teams and contributing to global software projects.

### Core Passion
John is dedicated to creating ICT services that are accessible worldwide, 24/7. He thrives on the challenge of building robust, scalable systems and managing the teams that bring them to life.

### Technical Expertise & Interests
- **Open Source:** A key contributor to **Etherpad** and **Etherpad Lite**, and involved in projects like **Primary Games Arena**, **My School Closures**, and **School Email**.
- **Hardware & Embedded Systems:** Highly specialized in **ESPHome**, **ESP32-C6**, and **ST25R NFC** technology. He maintains strict hardware pinout standards (e.g., SDA=21, SCL=22) and favors the `esp-idf` framework.
- **Web & Infrastructure:** Extensive experience with high-performance web stacks, including **Varnish Cache**, **WordPress (MU)**, **Shibboleth (SP/IDP)**, **Microsoft Exchange**, and **Linux/CentOS** administration.
- **Languages:** Proficient in **PHP**, **Perl**, **Javascript**, **HTML/CSS**, **Powershell**, and **C++** (for embedded).
- **Security:** Passionate about child protection in ICT, e-safety, and secure authentication (SSO).

### Writing & Engineering Style
- **Pragmatic & Technical:** His blog posts are often deep dives into specific technical fixes, tutorials, or industry critiques.
- **Engineering Rigor:** Adheres to high standards, such as non-blocking logic (avoiding `delay()`), PascalCase for types in ESPHome, and rigorous compile-testing before committing.
- **Direct & Transparent:** Prefers concise, high-signal communication. Focuses on the "why" and practical application rather than conversational filler.
- **Security-First:** Never logs or commits sensitive credentials and always uses placeholders (e.g., 00-00-00-00) for UIDs in documentation.

---

## About this Workspace (https://mclear.co.uk)
This repository is the source for John's personal blog and technical knowledge base.

### Structure
- **Root Folders:** `contact-me`, `more`, `privacy`, `sites`, `thanks`.
- **`posts/`**: A vast archive of technical tutorials, reviews, and updates dating back to 2008.
- **`index.html`**: The main entry point, providing a clean directory-style listing (with `.git` hidden).
- **`index.gmi`**: The root index for visitors using the **Gemini protocol**.
- **`markdown-viewer.html`**: A custom-built client-side renderer for viewing the blog's `.md` files in a standard web browser.
- **`CNAME`**: Configured for `mclear.co.uk`.
- **`.nojekyll`**: Ensures GitHub Pages serves all files (including `.md` and `.gmi`) without Jekyll processing.
