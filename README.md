<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/ful1e5/apple_cursor">Apple Cursors</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>
<p align="center">
    <a href="https://github.com/Syndrizzle/apple-cursor-catppuccin/stargazers"><img alt="Stargazers" src="https://img.shields.io/github/stars/Syndrizzle/apple-cursor-catppuccin?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/Syndrizzle/apple-cursor-catppuccin/issues"><img src="https://img.shields.io/github/issues/Syndrizzle/apple-cursor-catppuccin?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/Syndrizzle/apple-cursor-catppuccin/contributors"><img src="https://img.shields.io/github/contributors/Syndrizzle/apple-cursor-catppuccin?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
This cursor theme is unofficial and is not affiliated with catppuccin.
</p>

## Acknowledgement

This project is a modification of [Apple Cursors by ful1e5](https://github.com/ful1e5/apple_cursor).

## Installation

### GitHub Release

<!-- x-release-please-start-version -->

1. Download your preferred flavor for your system from the [latest GitHub release](https://github.com/Syndrizzle/apple-cursor-catppuccin/releases/latest).

2. Extract the downloaded files.

3. Follow the steps below for installing on windows or linux:
   - **For Linux:**
     - Move the extracted theme directories to one of the following locations:
     - **For the local user:** `$HOME/.icons`
     - **For all users**: `/usr/share/icons`
	 - Choose the theme in your settings.
   - **For Windows**
     - Open the extracted directory.
     - Right click on `install.inf` and click `Install`.
     - Click on `Apply` in the popped up window and exit.


## Manual Installation

### Prerequisites

- Python version 3.7 or higher
- zip
- [clickgen](https://github.com/ful1e5/clickgen) (See below)
- [catppuccin-python](https://github.com/catppuccin/python) (See below)
- [yarn](https://classic.yarnpkg.com/)

### Steps

1. Clone this repository and go to downloaded directory:

   ```bash
   git clone https://github.com/Syndrizzle/apple-cursor-catppuccin.git
   cd apple-cursor-catppuccin
   ```

2. Install the dependencies:

   ```bash
   # Install Yarn Dependencies
   yarn install
   # Install Python Dependencies
   pip3 install -r requirements.txt
   ```

3. **(Optional)** Change the accent color:  
   	> **ℹ️ NOTE:**<br>
	> By default, the theme uses `mauve` accent color while building the cursors, keeping all the accent colors is not possible since it results in a lot of files.  
   	> You may wish to change the accent color of the generated cursors.

    - **To do so, edit the `generate_variants.py` file, and change the `ACCENT_COLOR` variable to your desired color.**  
    <br>
    
	```python
	# ... Rest of the code

	"""
	Note: This script generates only Mauve accent variants.
	To generate other accent colors, modify the ACCENT_COLOR const to any of:
	- rosewater, flamingo, pink, mauve, red, maroon, peach, yellow
	- green, teal, sky, sapphire, blue, lavender
	"""

	ACCENT_COLOR = 'mauve' # change it here

	# ... Rest of the code
	```
	- **Regenerate the cursor variants with your applied accent color:**  
	<br>
 
   ```bash
   python3 generate_variants.py
   ```

4. Build the cursors:
   
   ```bash
   yarn generate
   ```

5. Install the cursors:  
   Your built files will be available inside the `bin/` folder. You can install them [the same way as you would install the release files.](https://github.com/Syndrizzle/apple-cursor-catppuccin/edit/main/README.md#github-release)

<br>


## Uninstall

### On Linux

- If you want to uninstall these cursors, you can simply remove the cursor directories from the `~/.icons` directory, or `/usr/share/icons` if you installed them for all users.

### On Windows
- Use the provided `uninstall.bat` script inside the extracted theme folder to remove the installed cursors.  

<br>


## 💝 Thanks to

- [ful1e5](https://github.com/ful1e5/apple_cursor)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center"><a href="https://github.com/Syndrizzle/apple-cursor-catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GNU&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
