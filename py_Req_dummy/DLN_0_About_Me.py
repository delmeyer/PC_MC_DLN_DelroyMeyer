
# coding: utf-8

# # <font color = 'green'>'Delroy Meyer - (Future) Engineer | Materials Characterization Group at Convergent' <font>
# 
# #### *<font color = 'blue'> An Interactive Notebook to showcase how I can add value to the Materials Characterizaton team and 'nudge' your decision to interview (and hopefully hire) me!<font>*<a class="tocSkip">
# 
# * Press ```Alt+r``` to start the slideshow
# * Press ```Spacebar``` to toggle the slides forward
# * Press ```Shift``` + ```Spacebar``` to toggle the slides backwards

# # DLN Contents
# 
# 0. [Materials Characterization Laboratory DLN | A Showcase for Convergent Manufacturing Group Ltd](DLN_0_About_Me.ipynb) - An 'Welcome' message to the Convergent Manufacturing - Materials Characterization Group, explaining the concept of these DLN entries, why I made them out of interest for the team's *Characterization Lab Technician/Scientist* opening, and presenting a brief 'About Me' StoryMap
# <br>
# 
# 1. [§1: Structural durability analyses of carbon fibre & epoxy-based composites - Introduction](DLN_1_Introduction.ipynb) - An introduction to the quasi-fatigue experiments performed on carbon fibre/epoxy composite specimens.
# <br>
# 
# 2. [§2: Structural durability analyses of carbon fibre & epoxy-based composites - Laminate mechanics theory](DLN_2_Theory.ipynb) - A discussion of composite laminate theory, as a basis for performing stress-strain-deformation calculations to characterize the structural durability of composite laminate layups.
# <br>
# 
# 3. [§3: Structural durability analyses of carbon fibre & epoxy-based composites - Experimental results](DLN_3_Experimental.ipynb) - Using Python scientific programming libraries to explore and visualize quasi-fatigue tensile & compressive loading experiments on carbon fibre/epoxy composite test coupons.
# <br>
# 
# 4. [§4: Structural durability analyses of carbon fibre & epoxy-based composites - Matrix calculations](DLN_4_Calculations.ipynb) - Using MATLAB to perform structural durability matrix calculations from carbon fibre/epoxy composite test coupon experimental data.

# # Purpose of this interactive notebook
# Hi Alastair, Martin, Convergent & Co.! I've created this digital notebook as a supplement to my application package for the [Characterization Lab Technician/Scientist](https://www.indeed.ca/cmp/Convergent-Manufacturing-Techn/jobs/Characterization-Lab-Technician-Scientist-196df99b0a902fca?q=materials+engineer&vjs=3) opening. 
# 
# I wanted a fun way to show you, and the Materials Characterization Group at Convergent, that I'm the type of self-motivated, hands-on, detail oriented individual that would add value to your group and to the Convergent business; moreover, I believe that this particular role is one in which I can make a strong impact in.

# # The 'Interactive DLN' concept
# This 'notebook concept' is a spin-off idea from a (proprietary) digital laboratory notebook (DLN) that I created for my master thesis project with [nanoleq AG](www.nanoleq.com), the [ETH Zürich Laboratory of Biosensors and Bioelectronics](http://www.lbb.ethz.ch/research.html) and the [JKU Linz Institute for Polymer Materials and Testing](https://www.jku.at/en/institute-of-polymeric-materials-and-testing/research/).

# # The 'Interactive DLN' concept <a class="tocSkip">
# About a week into my thesis project work, I quickly abandoned recording experimental data and observations in the paper laboratory notebook given to me. 
# 
# Under the mentorship of my principle thesis advisor, who had performed extensive experimental data recording, observation archiving and subsequent data analytics/visualization computing in Python/R programming environments during his PhD, I quickly adopted a similar method to manage my experiments.

# # The 'Interactive DLN' concept <a class="tocSkip">
# I created an interactive digital laboratory notebook, where I could: 
# 
# **1. Effectively archive my experimental data, observations and procedures**

# * Import standardized test procedures and record how I executed the test procedures (reproducibility) 
# * Ensure the systematic archival and organization of all experimental runs performed
# * Assign and apply data-type attributes to independent/dependent physico-chemical variables, to apply object oriented programming routines thereafter

# # The 'Interactive DLN' concept <a class="tocSkip">
# I created an interactive digital laboratory notebook, where I could: 
# 
# **2. Make use of powerful Python, R and MATLAB libraries, in an interactive computing environment to:**

# * Perform data analyses on my experimental observations
# * Create powerful data visualization graphics (both static and interactive)
# * Conduct interactive presentations with my thesis supervisors and company team members

# # Polymer and composite materials testing & characterization 'Portfolio'
# I've gone ahead and created a small 'portfolio of sorts' of select material characterization projects that I've conducted during my graduate education. Use the 'DLN Contents' navigation cell (*at the beginning of each DLN Jupyter Notebook*), to access specific projects.

# # Getting to know more about me
# I've created a 'StoryMap' of my professional, academic and cultural development over the past 5 years, so you can get a better sense of who I am and how my personality might fit in with your team's personalities. Navigate the StoryMap to find out a bit more about me and invite me for an interview to meet me in person 
# 
# (*Exit the SlideShow to get a better view of the StoryMap in the Jupyter DLN, or click [here](https://uploads.knightlab.com/storymapjs/2e0e49870f3e1b20bcc6405a8e568761/a-journey-through-the-progression-of-my-profession/index.html) to view it in your browser*)

# In[5]:


from IPython.display import IFrame

IFrame(src='https://uploads.knightlab.com/storymapjs/2e0e49870f3e1b20bcc6405a8e568761/a-journey-through-the-progression-of-my-profession/index.html', width=800, height=600)


# # Maintaining a laboratory notebook - Why go digital? <a class="tocSkip">

# ## Open-Source (Python & Jupyter Notebook) DLN vs. Proprietary DLN Software? <a class="tocSkip">
# 
# * Jupyter - Interactive omputer programming environment, compatible with many programming languages including Python, R, Julia, PHP, MATLAB, Mathematica | [Jupyter Kernels for Programming Languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
# 
# ### Pros and Cons of OS-DLN vs. P-DLN <a class="tocSkip">
# 
# | DLN Attribute | OS-DLN | P-DLN |
# | ----------- | ----------- | ----------- |
# | Security | Title | Title |
# | Price | Text | Text |
# | Build Effort | Text | Text |
# | Customization | Text | Text |
# | Data Storage | Text | Text |
# | Server requirements | Text | Text |
# | Search functionality | Text | Text |
# 
# 
# ## The 'Experiment Reproducibility' Problem <a class="tocSkip">
# 
# * Retrieval of experimental data - 
# * Archiving of experimental data:
#     * Electronic archival (document control) system to store DLN, relevant experimental data files in centralized server (Cloud computing options, local server options)
# * 'Standardized' recording of experimental results & observations
# * Quick reference links to electronic resources:
#     * Experimental E-SOPs
#     * Academic papers
#     * Simulation results in  ABAQUS (Python Scripting), COMPRO, RAVEN
#     * Material models
# * Knowledge transfer and record keeping
# 
# ## Data visualization <a class="tocSkip">
# 
# * *'Reporting results to engineers and management using Microsoft Word and Excel'* - is there a better way?
# * Data visualization + presentation of experimental results, all done from DLN platform
# 
# ## *Continue* <a class="tocSkip">

# # Data Creation & Retrieval with OS-DLN <a class="tocSkip">

# The OS-DLN must be able to create, import, store and retrieve all important data types in digital format, such as:
# 
# ## 1. Text processors <a class="tocSkip">
# * WYSIWYG - MS Word | [Jupyter notebook extension for exporting notebook as MS Word doc](https://github.com/innovationOUtside/nb_extension_wordexport)
#     * Import MS Word documents to P-DLN | [extract data from MS Word Documents using Python](https://towardsdatascience.com/how-to-extract-data-from-ms-word-documents-using-python-ed3fbb48c122)
#     
# ## 2. Spreadsheet tool <a class="tocSkip">
# 
# Allows you to create tables, enter and format data, perform calculations and create graphs within the ELN, as well as import from and export to Excel:
# 
# * Import Excel and CSV Formats (.xls, .xlsx, .csv) to DLN | [Python Excel Tutorial: The Definitive Guide](https://www.datacamp.com/community/tutorials/python-excel-tutorial)
# * Import Google Sheets to DLN | [Google Sheets + Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
# 
# ## 3. Images <a class="tocSkip">
# 
# The OS-DLN requires the capability to import images and add annotations, keeping in mind the following:
# * Large file sizes: SEM/TEM microscopic images require large storage space in the OS-DLN and robust computing power to render the images in the OS-DLN for all use-cases (DLN editing, presentations)
# * Images must not effect/impact data recording and data analyses
# 
# ## 4. Mobile/tablet Apps (nice to have) <a class="tocSkip">
# 
# Mobile and tablet apps, as well as responsive design, allowing researchers to use their preferred device to record their experiment notes
# 
# ## 5. Search functionality <a class="tocSkip">
# 
# The OS-DLN requires simple, effective and sophisticated search functionality, allowing you to retrieve your data by author, tag, unique ID, textual content, timestamp, and/or structured data query (fast keyword search capabillities, Experimental tag ID fast retrieval, etc.). One should be able to find the desired research data in seconds. Archival documentation system should allow 'Quick Reference' to pin-point search 'keywords'.

# # Data storage <a class="tocSkip">

# The OS-DLN must have a secure, robust, well-resourced data storage system in-place. There are basically two categories of solutions:
# 
# 1. Cloud-computing solutions
# 2. On-premises, self-hosted servers
# 
# For materials characterization purposes, the data storage warehousing of DLNs must also be able to securely and efficiently store all related/integrated data files of different types, such as:
# 
# * Simulation models (ex. experimental validation models: ABAQUS/SolidWorks, COMPRO, RAVEN, COMSOL)
# * Experimental data records (Excel, CSV, Google Sheets, Plain Text)
# * Text processing records (MS Word, Plain Text)
# * Literature review (PDF, EPUB, interactive HTML)
# * Material models (MATLAB, Python, React JS, R)
# 
# ## Cloud-hosted data storage <a class="tocSkip">
# 
# * Store all DLN entries and related related/integrated data files on cloud server
# * Common (secure) cloud server options:
#     * Amazon Web Services
#     * Microsoft Azure
# 
# ### Advantages of cloud-based solutions <a class="tocSkip">
# 
# * No setup costs
# * No (on-going) maintenance costs or resources required
# * No administration costs
# * Integrated cloud-computing environment - access content anywhere/anytime a functional Internet connection is available
# * Solution providers work to ensure minimal 'down time'
# 
# ### Disadvantages of cloud-based solutions <a class="tocSkip">
# 
# * Control of data security and privacy is ultimately handled by the service provider
#     * Need to be aware of security controls, encryption capabilities, authentication processes
# * Service depends on fast, reliable LAN/WLAN connectivity
#  
# 
# ## On-premises, self-hosted data storage <a class="tocSkip">
# 
# * Store all DLN entries and related related/integrated data files on own server
# 
# ### Advantages <a class="tocSkip">
# 
# * IT-Admin has full control over settings, security protocols, encryption, authentication and document control of all content hosted on server
# * Server is dedicated solely to own organization and is accessible offline
# 
# ### Disadvantages <a class="tocSkip">
# 
# * Higher cost of IT resources to setup, maintain and continuously update/improve server hosting
#     * IT is responsible for reliability, speed, security, service performance, software updates, bug fixes and version control of server
#     * IT is responsible for document control of all server content
#  
# 
# ## Cloud solution of self-hosting? <a class="tocSkip">
# The organization’s policy regarding data storage will be the key decision maker here. Large organizations with a big IT department often prefer to have an on-premise solution to be in full control, and are willing to pay extra for that reassurance. Smaller companies and research institutions are generally more willing to take advantage of the capabilities offered by cloud computing, especially those provided by Amazon or Microsoft.
# 
# ## Free cloud solution <a class="tocSkip">
# 
# * [LabFolder - Free for up to 3 Team Members](https://www.labfolder.com/pricing/industry/)
# * [LabFolder - The Electronic Lab Notebook in 2019: A comprehensive guide](https://www.labfolder.com/electronic-lab-notebook-eln-research-guide/)
