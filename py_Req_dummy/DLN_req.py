
# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
#
# ## §1: Introduction

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

# # 0. DLN Introduction
#
# This digital laboratory notebook (DLN) is comprised of four linked entries that are listed in the DLN contents section above. The DLN provides a comprehensive platform that:
#
# * Discuss composite fatigue and pertinent composite mechanics theory
# * Provide an overview of tensile and compression quasi-static fatigue tests performed on carbon fibre/epoxy composite laminate coupons with varying fibre orientations and ply layers
# * Provides a scientific computing platform to utilize tensile & compressive quasi-static fatigue experiment data for:
#     * Stress-strain data visualization
#     * Statistical data analyses
#     * Store empirically-determined elastic properties of the tested composite coupons for structural durability calculations
#     * Perform matrix calculations to quantify the structural durability of the tested composite laminate coupons materials

# ## I. Experiment log
# * **Date of experiment**: 10.14.2017
# * **Principle investigator**: Delroy Meyer, EIT, BASc
# * **Test operators**: Jürgen Müller, Delroy Meyer, Cintia Oliveria
# * **Lead investigator**: Prof. Dr-mont. Zoltan Major
# * **Course**: LVA Nr. 378.029 - 480ADPTPPBV17 - Polymer Product Design and Engineering III - Graduate Seminar
# * **Location**: Institute of Polymer Materials and Testing (IPMT), JKU Linz - Linz, Austria
#     * Compounding and specimen preparation Lab: *Composite coupon specimen preparation*
#     * Mechanical Lab: *Tensile & compression testing*
#
# ### i. Experiment test (lab) environment conditions
# *Measurement taken: 10-14-2017 08:45:07*
# <b>
#
# $T_{test} (°C) = 21.23$ (*within* $ 23 ± 3 °C$ *standard laboratory atmosphere range as per ASTM D5229*)
# <br>
# $RH (\%) = 55.7$ (*within* $ 50 ± 10 \%$ *standard laboratory atmosphere range as per ASTM D5229*)

# # 1. Purpose of experiment and data analyses
# These experiments were conducted to investigate the dependency of the structural durability of (high fibre volume fraction) carbon fibre/epoxy laminate composites on fibre orientation. Quasi-static tensile and compressive fatigue tests were performed with unidirectional (UD) carbon/epoxy laminates at angles of 0°, 45° and 90°.
#
# ## 1.1 Why these investigations are needed
# 1. Short and long-fibre reinforced composites offer advantages over conventional metallic materials for the manufacture of components across many different manufacturing industries (*common examples: aerospace/automotive component manufacture, building materials, sports equipment, chemical process industry components*)
#     * Polymeric laminated composites, like carbon-fibre/epoxy laminates, present high strength-to-weight and stiffness-to-weight ratios when compared with metallic materials
# <br>
#
# 2. To dimension parts undergoing sustained tensile or compressive forces in application, and the material's consequent deformation response, the quasi-fatigue tensile & compressive characterization testing is necessary
# <br>
#
# 3. *My personal opinion*: Composite materials design offers, for all practical intents and purposes, virtually limitless options for component design, processing and application-use. Consequently, this mean that, for the foreseeable future, there will be an ongoing need to conduct testing for both existing and novel composite materials design and structural analyses; the evolution of innovation in composite materials development and processing technologies will further expand the scope of testing needed.

# ## 1.2 Fatigue mechanics of composite materials - conceptual theory
#
# * Due to their inner structure consisting of continuous fibres and matrix material the macroscopic properties of composite materials are anisotropic
#     * UD-lamina layers, themselves, are considered to be transversely isotropic; on planes parallel with the fibre direction they behave orthotropically and on an imaginary plane perpendicular to the fibre direction they behave isotropically
#
# * The interface between the fibre and the matrix resin and its properties influence the performance of the composite as well
#
# * When mechanical quasi-static or fatigue loads are applied, a variety of complex damage mechanisms such as matrix microcracking, interfacial fibre/matrix debonding, transverse rupture, fibre rupture or delamination occur on microscopic scale
#
# * The properties of unidirectional (UD) composites transverse to fibre direction are generally low. Under fatigue loads, the matrix is subjected to strain-controlled fatigue due to the constraint provided by the fibres
#
# * Higher fibre volume fractions increase mechanical properties such as tensile strength and stiffness in fibre direction
#
# * The fibres of an CFRPs are what “deliver” its excellent properties but the resin (the matrix) is still required in order to:
#     * provide a cohesive component
#     * direct loads into the fibres
#     * protect the fibres against environmental influences
#     * prevent the fibres from buckling when subjected to compressive stress
#     * *However, this means that*: unfortunately stresses will of necessity now arise in the matrix as well, and also at the interface of the fibres and matrix
#

# ## 1.3 Structural durability calculations as part of composite fatigue-life prediction
# Structural durability calculations constitute 'one piece in the puzzle' of forming a complete fatigue-life prediction model for composite materials. These calculations rely on the following studies:
#
# 1. An evaluation of the **load-time-history** of the material
# <br>
#
# 2. Analyses of the **local anisotropic behaviour** of the material:
# <br>
#
# 3. Analyses of the **macroscopic behaviour** of the material:
#     * quasi-static stress/time investigations:
#         * data for stress-strain behaviour and strength (elasticity and strength properties)
#     * cyclic stress/cycle investigations (S-N curves)
# <br>
#
# 4. Consideration of **Lamina input variables**:
#     * lamina thickness
#     * fibre content
#     * type and orientation of reinforcement
#
# A visual representation of the full workflow for creating a composite fatigue-life prediction model, provided by Mösenbacher et. al. [1], shows how these studies contribute to the workflow.
#
# ![Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)](0.Images/CFRP_Fatigue_Predict_Wrkflw.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
#
# *<center> Fig. 1 - Complete workflow for developing a composite fatigue-life prediction model (Mösenbacher, ECCM16, 2016)</center>*

# ## 1.4 Data analysis & calculations to be determined from this investigation
#
# This DLN will focus on the ***load-time history*** and ***stress-strain*** analysis segments of the **composite fatigue-life prediction model workflow** shown in Figure 1 above.
#
# The following results will be presented from the tensile and compressive quasi-static fatigue loading experiment runs performed on carbon fibre/epoxy laminate coupons of various fibre orientations and ply layers:
#
# 1. Empirical determination of tensile/compressive moduli of elasticity
# <br>
#
# 2. Calculation of stress-strain elastic engineering constants to characterize the structural durability of composite materials undergoing long-term static (force) loading in application
# <br>

###########################################################################################################################################################################
#==========================================================================================================================================================================
###########################################################################################################################################################################



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

###########################################################################################################################################################################
#==========================================================================================================================================================================
###########################################################################################################################################################################



# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
#
# ## §2 Composite laminate theory (*based on LEFM*)
#
# Principles of linear elastic composite laminate theory, pertinent to calculating the elastic engineering constants required to characterize the elastic structural durability of various tested carbon fibre/epoxy laminate coupons, are discussed here.

# # DLN Contents
#
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

# ## 2.1 Structural mechanics theory of UD composite laminates subject to plane stress
# All of the coupons prepared and tested for this investigation were UD composite laminates; the coupons were subjected to either tensile or compressive plane stress in the 1-2 plane of the composite geometry, as shown below. This is to say that the coupons were only subjected to *in-plane* stress loads (i.e. tensile and compressive loading in the fibre direction):
#
# ![Image](0.Images/UD_lamina_1-2_plane.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
#
# *<center> Fig. X - Unidirectional fibre-reinforced lamina (Jones, 1999)</center>*
#

# ### 2.1.1 A brief overview of linear elastic strain-stress theory (*relevant to the 2-D in-plane stress fields*)
# A comprehensive overview of linear elastic approximations of stress-strain relationships for anisotropic materials can be found in many resources that focus on solid mechanics [(Tuttle, 2004), (Pilkey, 1999)]. A simplification of (linear elastic) stress-strain theory[<sup>1</sup>](#fn1), applied to UD-laminate composites subjected to in-plane stress, is briefly described here. These equations provide the basis for the structural durability calculations of stress-strain effects on the carbon fibre/epoxy coupons.
#
# **Generalized Hooke's Law**
# The generalized Hooke's law relating a stress field (induced by an applied force) to strain (deformation) response, of a particular material, can be written in the following simple notation notation :
#
# $$ \mathbf{\sigma_{i}} = \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# Where:
# * $\mathbf{\sigma_{i}}$ are the stress components
# * $\mathbf{C_{ij}}$ is the stiffness matrix
# * $\mathbf{\varepsilon_{j}}$ are the strain components
#
# The normal and shear stress fields, induced by an applied force, are pictured in Cartesian coordinates below:
#
# ![Image](0.Images/Stress_Element_Cartesian.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
#
# *<center> Fig. X - Stresses on a material element (Jones, 1999)</center>*
#
# **The stain (deformation) response**
# Deformation of the material, responding to the induced stress field, is characterized by *tensor shear strain* ($\mathbf{\varepsilon_{ij}}$) and *engineering shear strain* ($\mathbf{\gamma_{ij}}$). Considering a material element being deformed, the tensor and engineering shear strains are defined, respectively, as:
#
# $$ \mathbf{\varepsilon_{1}} = \frac{\partial u}{\partial x}, \qquad \mathbf{\varepsilon_{2}} = \frac{\partial v}{\partial y}, \qquad \mathbf{\varepsilon_{3}} = \frac{\partial w}{\partial z}$$
#
# $$ \mathbf{\gamma_{23}} = \frac{\partial v}{\partial z} + \frac{\partial w}{\partial y}, \qquad \mathbf{\gamma_{31}} = \frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}, \qquad \mathbf{\gamma_{12}} = \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}$$
#
# **Stress-strain relationships - Stiffness and compliance elasticity constants**
# The integral of the incremental work done (per unit volume) on a material (subjected to an applied force that induces a stress field and subsequent strain (deformation) response to the load, yields a relation between work done on the material and the resultant tensor shear strain:
#
# $$ \mathbf{W} = \frac{1}{2} \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{i}} \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# This result relates The second order differentiation of Hooke's Law shows that the stiffness matrix ($\mathbf{C_{ij}}$) is symmetric (*i.e* $\mathbf{C_{ij}} = \mathbf{C_{ji}}$). Similarly, by examining the inverse of the stress-strain relations, the work done on the material can be related to the induced stress field:
#
# $$ \mathbf{W} = \frac{1}{2} \mathbf{S_{ij}} \cdot \mathbf{\sigma_{i}} \mathbf{\sigma_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# Where:
# * $\mathbf{S_{ij}}$ is the compliance matrix
#
# ***Here it's important to note that hygrothermal effects on the deformation of the material are not being considered.*** *This is valid if experimental testing is done with test environment controls and neglecting material temperature changes during tensile/compressive loading.*
#
# The stiffness and compliance matrices have 36 constants, owing to the six degrees of freedom for considering the (linear elastic) deformation response of a material element. The generalized matrices are as follows:
#
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# **Significance of coupled stress-strain elements (*described with the compliance matrix*)**
# For anisotropic materials, significant coupling occurs between the applied stress and the various strain responses. Examing the compliance matrix, the following stress-strain responses are coupled:
#
# * The $ S_{11}, S_{22}$ and $S_{33} $ terms each represent extensional response to their respective applied stress components ($ \sigma_{1}, \sigma_{2}, \sigma_{3} $) in the same direction.
#
# * The $ S_{44}, S_{55}$ and  $S_{66} $ terms represent shear strain response to an applied shear stress in the same plane
#
# * The $ S_{12}, S_{13}$ and  $S_{23} $ terms represent coupling between dissimilar normal stresses and normal strains (extension-extension coupling more commonly known as the Poisson effect)
#
# * The $ S_{14}, S_{15}, S_{16}, S_{24}, S_{25}, S_{26}, S_{34}, S_{35}$ and $S_{36} $ terms represent normal strain response to applied shear stress in a more complex manner than for the preceding compliances (shear-extension coupling)
#
# * Finally, the $ S_{45}, S_{46}$ and $S_{56} $ terms represent shear strain response to shear stress applied in another plane (shear-shear coupling)
#
# * However, less than 36 of the constants can be shown to actually be independent for elastic materials when important characteristics of the strain energy are considered, such as whether the material behaves anisotropically, orthotropically, monoclinically or traversely isotropically when undergoing deformation.
#
# [comment]: <> (------------------------------§2.3.2 Footnotes------------------------------)
# __________________________________
#
# <span id="fn1"> 1. Linear elasticity theory makes a number of assumptions about the elastic/plastic deformation response to stress fields induced by applied force loads, namely that strain responses are infinitesimally small, and that relationships between the components of stress and strain are approximately. Additionally, the theory is valid only for stress states that do not produce yielding.</span>

# ### 2.1.2 UD laminae strain-stress relationships
# The fibre arrangements, of the laminate coupons prepared for these experimental investigations, were classified as orthotropic or transversely isotropic bodies. In UD laminae, all planes whose perpendicular vector is transverse with respect to the fibre direction are planes of symmetry. The UD laminae are transversely isotropic. On planes parallel with the fibre direction it behaves orthotropically (*material properties that differ along three mutually-orthogonal twofold axes of rotational symmetry - a subset of anisotropic materials*)and on an imaginary plane perpendicular to the fibre direction it behaves isotropically (*material properties remain constant in all directions*).
#
#  **3-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
#  <br>
#
# With the application of tensile or compressive force loading, parallel to the fibre direction of the UD laminae (in-plane loading), shear-extension and shear-shear coupling can be neglected. As such, the stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\
# C_{21} & C_{22} & C_{23} & 0 & 0 & 0 \\
# C_{31} & C_{32} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\
# S_{21} & S_{22} & S_{23} & 0 & 0 & 0 \\
# S_{31} & S_{32} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# **3-D Isotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# The stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting isotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\
# C_{12} & C_{11} & C_{13} & 0 & 0 & 0 \\
# C_{13} & C_{13} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\
# S_{12} & S_{11} & S_{13} & 0 & 0 & 0 \\
# S_{13} & S_{13} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & 2(S_{11} - S_{12})  \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$

# ### 2.1.3 2-D UD laminae strain-stress relationships
# Since the test coupons for this investigation are all UD laminate samples, and tensile/compressive loadings during experiment runs were applied in the 1-2 plane of the samples, the remaining theory discussion will focus on 2-D laminae stress-strain relationships.
#
# The plane-stress state of the UD composite, in the 1-2 plan, is defined by setting:
#
# $$ \sigma_{3} = 0, \tau_{23} = 0, \tau_{31} = 0$$
#
# such that:
#
# $$ \sigma_{1} ≠ 0, \sigma_{2} ≠ 0, \tau_{21} ≠ 0$$
# <br>
#
# where $ \sigma_{1}$ and $ \sigma_{2}$ represent the stress components normal to the 1-2 plane of a UD laminate material, w.r.t to the 1 and 2 directions respectively, and $ \tau_{21}$ represents the intralaminar shear stress w.r.t. the 1-2 plane of a UD laminae material.
#
# **2-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# As such, the 2-D stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & 0 \\
# C_{12} & C_{22} & 0 \\
# 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & 0 \\
# S_{12} & S_{22} & 0 \\
# 0 & 0 & 2(S_{11} - S_{12}) \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right)$$
#
# These equations effectively describe the deformation response (described by tensor and engineered shear strain components) of the UD laminae in the 1-2 plane, w.r.t. a shear stress field (described by stress components normal to the 1-2 plane and in-plane shear stress components).
#
# The tensile and compressive tests, performed for the purposes of this investigation, will be conducted with preset force loads. The resulting displacement (strain) measured will determine the engineering constants required to solve the stress-strain equations discussed above.

# ### 2.1.4 Overview of engineering constants for solving strain-stress equations
# A brief overview of the engineering constants required to solve the 2-D UD laminae stress-strain equations is presented below:
#
# 1. The slope of (tensile/compressive) stress-strain curve:
#     * $ E = \frac{\sigma}{\varepsilon} $
#     * $ E_{i}$ represents the Young's (extension) moduli in the $ i^{th}$ directions, describing the elastic extension of the material in a specific direction
#
# 2. The slope of strain-strain curves (Poisson's ratio):
#     * the negative of the ratio of (signed) transverse strain to (signed) axial strain (i.e. extension-extension coupling coefficient)
#     * $ \nu_{ij} = \frac{-\varepsilon_{i}}{\varepsilon_{j}} $
#
# 3. The shear modulus, $ G_{ij}$, defining the ratio of shear stress to the shear strain in the (i-j) plane, or rather the material's response to shear stress
#
# **The orthotropic UD laminae case**
# <br>
#
# From these definitions, the **compliance matrix** can be expressed in terms of these engineering constants as follows:
#
# $$S =
# \begin{bmatrix} \frac{1}{E_{11}} & - \frac{\nu_{21}}{E_{22}} & 0 \\
# - \frac{\nu_{12}}{E_{11}} & \frac{1}{E_{22}} & 0 \\
# 0 & 0 & \frac{1}{G_{12}} \\
# \end{bmatrix} $$
#
# Since the stiffness and compliance matrices are mutually inverse, it follows by matrix algebra that their components are related as follows for orthotropic materials (*limited to the 2-D case*):
#
# $$ C_{11} = \frac{S_{22}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{1}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ C_{22} = \frac{S_{11}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{2}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ C_{12} = \frac{S_{12}}{S_{11} S_{22} - S^{2}_{12}} = \frac{\nu_{12}E_{1}}{1 - \nu_{12} \nu_{21}} =
# \frac{\nu_{21}E_{1}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ \frac{C_{11} - C_{12}}{2} = G_{12} $$
#
# **The isotropic UD laminae case**
# <br>
#
# Note that for orthotropic UD laminae, there are four independent variables, namely $ E_{1}, E_{2}, \nu_{12} $ and $ G_{12} $. For the isotropic case, we note that:
# * $ S_{11} = \frac{1}{E_{1}} = \frac{1}{E_{2}} = \frac{1}{E} =  S_{22} $, such that $ E_{1} = E_{2} = E $
# * $ S_{12} = - \frac{\nu_{12}}{E_{1}} = - \frac{\nu_{21}}{E_{2}} = - \frac{\nu}{E} $
# * $ \frac{1}{G_{12}} = \frac{1}{G} = \frac{2(1 + \nu)}{E} $

# ## 2.2 UD laminae in-plane strain-stress relationships

# For in-plane stresses of composite plies we assume that stresses and strains to not vary in certain directions, depending on how the ply is force-loaded. When the aforementioned plane-strain condition exists, the three-dimensional analysis simplifies considerably.
#
# The UD laminate test coupons, from the experimental trials, were subjected to in-plane stresses (via 1-2 plane tensile and compressive force loading. The fibre arrangements, of the experiment laminate coupons, were classified as orthotropic or (symmetric) transversely isotropic bodies.
#
# From the general, anisotropic stress-strain systems of equationss,  defined in Eq. [6] and [7] with the stiffness and compliance matrices respectively:
#
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# These equations reduce to the following for in-plane (*plane-stress*) loading of orthotropic composite plies:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\
# Q_{12} & Q_{22} & Q_{26} \\
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
#
# Where:
#
# $Q_{ij}$ represent the **in-plane** elements of the stiffness matrix subject to the **plane-stress condition** (*differentiated from the general stiffness matrix elements $C_{ij}$*)
#
# The plane-stress conditioned compliance matrix is the inverse of the plane-stress conditioned stiffness matrix:
#
# $$ \begin{bmatrix} S'_{11} & S'_{12} & S'_{16} \\
# S'_{12} & S'_{22} & S'_{26} \\
# S'_{16} & S'_{26} & S'_{66} \\
# \end{bmatrix}^{-1}  =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\
# Q_{12} & Q_{22} & Q_{26} \\
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix} $$
#
# Where:
#
# $S'_{ij}$ represent the **in-plane** elements of the compliance matrix subject to the **plane-stress condition** (*differentiated from the general compliance matrix elements $S_{ij}$*)

# ## 2.3 Stress and strain transformations

# Axes transformations are important in stress-strain of materials. Such transformations are required to compute critical values of these (stress-strain) characteristics, as well as to be able to understand the tensorial nature of stress and strain. Other entities, such as moment of inertia and curvature, also transform in a manner similar to stress and strain.
#
# For the purposes of this DLN the relevant theory related to transformations of stress and strain from a local coordinate system to a global coordinate system will briefly be discussed. Further resources on (stress-strain) tensor transformation theory can be found in [Roylance, 2001].
#
# ### 2.3.1 Stress and strain transformations for laminate plies
#
# Stress can be transformed from a local cartesian coordinate system **L(p,q,r)** to a global cartesian coordinate system **G(p,q,r)** via:
#
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \sigma_{G,r} \\ \tau_{G,qr} \\ \tau_{G,pr} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} T_{\sigma11} & \cdots & T_{\sigma16} \\
# \vdots & \ddots & \vdots \\
# T_{\sigma61} & \cdots & T_{\sigma66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \sigma_{L,r} \\ \tau_{L,qr} \\ \tau_{L,pr} \\ \tau_{L,pq} \\  \end{array} \right)$$
#
# Which can be written in the form:
#
# $$ \mathbf{\sigma_{G}} = [\mathbf{\hat{T}_{\sigma}}] \mathbf{\sigma_{L}} $$
#
# For composite laminate plies subjected to plane-strain and plane-stress conditions, one is only interested stresses manifested in the G(p-q) and L(p-q) planes; for UD laminate plies this would mean the planes that characterize stresses occurring only in the fibre direction and transverse to the fibre direction. Then the stresses in the **G(p,q,r)** coordinate system are arrived at by rotation about the 'r' axis of the **L(p,q,r)** coordinate system, namely:
#
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\
# s^{2} & c^{2} & -2cs \\
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \tau_{L,pq} \\  \end{array} \right)$$
#
# Where:
# <br>
#
# $ c = cos\Theta \qquad\quad s = sin\Theta $
#
# And can be written in the form:
#
# $$ \mathbf{\sigma_{G}} = [\mathbf{T_{\sigma}}] \mathbf{\sigma_{L}} $$
#
# Meaning that only the three in-plane strain components are transformed.
#
# A similar treatment of the strain tensor, relating strains (on a composite laminate ply material) in the local coordinate system to the global coordinate system, yields:
#
# $$ \left( \begin{array}{c} \varepsilon_{G,p} \\ \varepsilon_{G,q} \\ \gamma_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & cs \\
# s^{2} & c^{2} & -cs \\
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{L,p} \\ \varepsilon_{L,q} \\ \gamma_{L,pq} \\  \end{array} \right)$$
#
# Where c and s are as previously defined, and can be written alternatively as:
#
# $$ \mathbf{\varepsilon_{G}} = [\mathbf{T_{\varepsilon}}] \mathbf{\varepsilon_{L}} $$
#
# The stiffness and compliance matrices, $[\mathbf{C}]$ and $[\mathbf{S}]$ respectively, can be transformed accordingly (*see [Roylance, 2001] for matrix inversion steps*) to yield:
#
# $$ [\mathbf{C'}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{C}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
#
# $$ [\mathbf{S'}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
#
# Thus the transformed stiffness matrix can be computed for composites with fibres of varying orientations, from a reference local coordinate system and using laminate ply material stiffness constants to a global coordinate system, with the stress and strain transforms being:
#
# $$ [\mathbf{T_{\sigma}}] =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\
# s^{2} & c^{2} & -2cs \\
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
#
# $$ [\mathbf{T_{\varepsilon}}] =
# \begin{bmatrix} c^{2} & s^{2} & cs \\
# s^{2} & c^{2} & -cs \\
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
#
# ### 2.3.2 In-plane transformed stiffness and compliance matrices
#
# It follows that, for composite plies subjected to plane-stress conditions, the transformed in-plane stress and strain systems of equations can be derived by substituting the plane-stress conditioned stiffness and compliance matrices (Eqn. [23], [24]) into Eqns. [31] and [32]:
#
# $$ [\mathbf{\bar{Q}}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{Q}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
#
# $$ [\mathbf{\bar{S}}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
#
#
# ### 2.3.3 References
#
# 1. Roylance, D. (2001). Transformation of stresses and strains. Lecture Notes for Mechanics of Materials.

# ## 2.4 Laminate structural durability calculations

# ### 2.4.1 Stiffness matrices for in-plane stress conditioned laminates
#
# Eqn.s [35] and [36] represent the plane-stressed conditioned stiffness and compliance matrices for individual plies. To approximate the stress-strain relationships of entire laminates (multi-layer manufactured plies), we define the [A], [B] and [D] stiffness matrices:
#
# $$ [\mathbf{A}] = \int_{-h_{b}}^{h_{t}} [\bar{\mathbf{Q}}]dz $$, and each $[A_{ij}]$ element defined by:
#
# $$ A_{ij} = \int_{-h_{b}}^{h_{t}} \bar{Q_{ij}}dz $$
#
# Where:
#
# * $h_{b}$ represents the distance of the laminate plies from the reference plane to the bottom surface of the entire laminate structure
# * $h_{t}$ represents the distance of the laminate plies from the reference plane to the top surface of the entire laminate structure
# * Recall that $[\bar{Q}]$ represents the in-plane stress conditioned, transformed stiffness matrix of each ply
#
# The variable '$\mathbf{z}$' in Eqn. [37] defines the distance of the '$\mathbf{z^{th}}$' ply from the reference plane
#
# $$ [\mathbf{B}] = \int_{-h_{b}}^{h_{t}} z[\bar{\mathbf{Q}}]dz $$, and each $[B_{ij}]$ element defined by:
#
# $$B_{ij}] = \int_{-h_{b}}^{h_{t}} z\bar{Q_{ij}}dz $$
#
# and
#
# $$ [\mathbf{D}] = \int_{-h_{b}}^{h_{t}} z^{2}[\bar{\mathbf{Q}}]dz $$, and each $[D_{ij}]$ element defined by:
#
# $$ D_{ij} = \int_{-h_{b}}^{h_{t}} z^{2}\bar{Q_{ij}}dz $$
#
# From the assumption that the composite plies and laminates, tested for the quasi-static fatigue loading investigations, exhibit linear elastic behaviour, it is assumed that $[\bar{Q}]$ is constant across each ply. Thus, the laminate stiffness and compliance integrals above can be replaced by the summations:
#
# $$ A_{ij} = \sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z_{k}-z_{k-1}) $$
#
# $$ B_{ij} = \frac{1}{2}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{2}_{k}-z^{2}_{k-1}) $$
#
# $$ D_{ij} = \frac{1}{3}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{3}_{k}-z^{3}_{k-1}) $$

# ## 2.5 Mechanics of in-plane stress-conditioned composite laminates

# ### 2.5.1 In-plane forces and moments
#
# From the [A], [B] and [D] in-plane stiffness matrix elements described in Eqns. [43] through [45], the in-plane forces and moments of the laminate can be related to the in-plane strain and curvature response of the laminate. For a laminate subject to the in-plane stress condition in the 1-2 plane, this relationship is:
#
# $$ \left( \begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right) =
# \begin{bmatrix} A_{11} & A_{12} & A_{16} & B_{11} & B_{12} & B_{16} \\
# A_{21} & A_{22} & A_{26} & B_{21} & B_{22} & B_{26} \\
# A_{61} & A_{62} & A_{66} & B_{61} & B_{62} & B_{66} \\
# B_{11} & B_{12} & B_{16} & D_{11} & D_{12} & D_{16} \\
# B_{21} & B_{22} & B_{26} & D_{21} & D_{22} & D_{26} \\
# B_{61} & B_{62} & B_{66} & D_{61} & D_{62} & D_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) $$
#
# Inversion of Eqn. [46] defines the strain and curvature of the laminate in terms of the in-plane force loading and moments of the laminate. For a laminate force-loaded in the 1-2 plane:
#
# $$ \left(\begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) =
# \begin{bmatrix} \alpha_{11} & \alpha_{12} & \alpha_{16} & \beta_{11} & \beta_{12} & \beta_{16} \\
# \alpha_{21} & \alpha_{22} & \alpha_{26} & \beta_{21} & \beta_{22} & \beta_{26} \\
# \alpha_{61} & \alpha_{62} & \alpha_{66} & \beta_{61} & \beta_{62} & \beta_{66} \\
# \beta_{11} & \beta_{12} & \beta_{16} & \delta_{11} & \delta_{12} & \delta_{16} \\
# \beta_{21} & \beta_{22} & \beta_{26} & \delta_{21} & \delta_{22} & \delta_{26} \\
# \beta_{61} & \beta_{62} & \beta_{66} & \delta_{61} & \delta_{62} & \delta_{66} \\
# \end{bmatrix}
# \cdot
# \left(\begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right)
#  $$
#
#  ### 2.5.2 Importance of the [A], [B] and [D] matrices to laminate structural durability analyses
#
#  The [A], [B] and [D] matrices characterize the stiffness of the laminates, the degree to which the composite laminate will elastically deform, when subjected to certain force-loading conditions.
#
#  For the purposes of the quasi-static fatigue (tensile and compressive) in-plane force-loading of carbon fibre/epoxy laminate composite coupons (the experiments designed to investigate the *linear* elastic structural durability of these composite materials), the significance of these matrices are as follows:
#
#  1. The $A_{ij}$ stiffness matrix elements relate the in-plane forces, imposed on the laminate coupons, to the in-plane (*elastic*) deformations manifested in the laminates (*under tensile or compressive force-loading*)
#
#  2. The $B_{ij}$ stiffness matrix elements are the in-plane–out-of-plane coupling stiffnesses that relate the:
#      * in-plane forces, imposed on the laminate coupons, to the resultant curvatures of the laminate
#      * moments, imposed on the laminate, to the resultant in-plane deformation of the laminate
#
#  3. The $D_{ij}$ stiffness matrix elements are the bending stiffnesses that relate the moments, imposed on the laminate, to the resultant curvatures of the laminate
#
# Examination of the [A], [B], and [D] matrices show that different types of couplings may occur. For the experimental (tensile and compressive force-loading) of the composite laminate coupons in the 1-2 plane, the following important force-moment-curvature-deformation couplings are worth noting:
#
# 1. **Extension–shear coupling**
#     * When the elements $A_{16}$, $A_{26}$ (of the $A_{ij}$ elements) are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause shear deformation ($\gamma^o_{1-2}$), and a twist force ($N_{1-2}$) causes elongations in the 1 and 2 directions
#
# 2. **Bending–twist coupling**
#     * When the elements $D_{16}$, $D_{26}$ are not zero, bending moments ($M_{1}, M_{2}$) may cause a twisting of the laminate ($\kappa_{1-2}$), and a twist moment ($M_{1-2}$) causes curvatures in the 1–3 and 2–3 planes
#
# 3. **Extension–twist and bending–shear coupling**
#     * When the elements $B_{16}$, $B_{26}$ are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause twist ($\kappa_{1-2}$), and bending moments ($M_{1}, M_{2}$) result in shear deformation ($\gamma^o_{1-2}$)
#
# 4. **In-plane–out-of-plane coupling**
#     * When the $B_{ij}$ stiffness matrix elements are not zero, in-plane forces ($N_{1}, N_{2}, N_{1-2}$) cause out-of-plane deformations (curvatures) of the laminate, and moments ($M_{1}, M_{2}, M_{1-2}$) cause in-plane deformations in the 1-2 plane.
#
# It is worth noting that these four types of coupling are characteristic of composite materials and do not occur in homogeneous isotropic materials. The following two couplings occur in both composite and isotropic materials:
#
# 5. **Extension–extension coupling**
#     * When the element $A_{12}$ is not zero, a normal force $N_{1}$ causes elongation in the 2 direction ($\varepsilon^o_{2}$), and a normal force $N_{2}$ causes elongation in the 1 direction ($\varepsilon^o_{1}$)
#
# 6. **Bending–bending coupling**
#     * When the element $D_{12}$ is not zero, a bending moment $M_{1}$ causes curvature of the laminate in the 2-3 plane ($\kappa_{2}$), and a bending moment $M_{2}$ causes curvature of the laminate in the 1–3 plane ($\kappa_{1}$)

# ## 2.6 Applications of [A], [B], [D] ( [$\alpha$], [$\beta$], [$\delta$] ) matrices to the (*elastic*) structural durability characterization of experiment carbon fibre/epoxy composite coupons

# * [§3: Structural durability analyses of carbon fibre & epoxy-based composites - Experimental results](DLN - §3 - Structural durability analyses of carbon fibre & epoxy-based composites - Experimental.ipynb) is the DLN entry that uses Python scientific programming libraries to explore and visualize quasi-fatigue tensile & compressive loading experiments on carbon fibre/epoxy composite test coupons. From analyses of the experiments, the elastic properties of the test coupons are determined.
# <br>
#
# * [§4: Structural durability analyses of carbon fibre & epoxy-based composites - Matrix calculations](DLN - §2 - Structural durability analyses of carbon fibre & epoxy-based composites - Calculations.ipynb) is the DLN entry that uses MATLAB to perform structural durability matrix calculations from carbon fibre/epoxy composite test coupon experimental data. The $[A], [B], [D]$ $([\alpha], [\beta], [\delta])$ matrices are calculated for each of the test laminate coupons.
#


###########################################################################################################################################################################
#==========================================================================================================================================================================
###########################################################################################################################################################################


# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
#
# ## §2 Composite laminate theory (*based on LEFM*)
#
# Principles of linear elastic composite laminate theory, pertinent to calculating the elastic engineering constants required to characterize the elastic structural durability of various tested carbon fibre/epoxy laminate coupons, are discussed here.

# # DLN Contents
#
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

# ## 2.1 Structural mechanics theory of UD composite laminates subject to plane stress
# All of the coupons prepared and tested for this investigation were UD composite laminates; the coupons were subjected to either tensile or compressive plane stress in the 1-2 plane of the composite geometry, as shown below. This is to say that the coupons were only subjected to *in-plane* stress loads (i.e. tensile and compressive loading in the fibre direction):
#
# ![Image](0.Images/UD_lamina_1-2_plane.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
#
# *<center> Fig. X - Unidirectional fibre-reinforced lamina (Jones, 1999)</center>*
#

# ### 2.1.1 A brief overview of linear elastic strain-stress theory (*relevant to the 2-D in-plane stress fields*)
# A comprehensive overview of linear elastic approximations of stress-strain relationships for anisotropic materials can be found in many resources that focus on solid mechanics [(Tuttle, 2004), (Pilkey, 1999)]. A simplification of (linear elastic) stress-strain theory[<sup>1</sup>](#fn1), applied to UD-laminate composites subjected to in-plane stress, is briefly described here. These equations provide the basis for the structural durability calculations of stress-strain effects on the carbon fibre/epoxy coupons.
#
# **Generalized Hooke's Law**
# The generalized Hooke's law relating a stress field (induced by an applied force) to strain (deformation) response, of a particular material, can be written in the following simple notation notation :
#
# $$ \mathbf{\sigma_{i}} = \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# Where:
# * $\mathbf{\sigma_{i}}$ are the stress components
# * $\mathbf{C_{ij}}$ is the stiffness matrix
# * $\mathbf{\varepsilon_{j}}$ are the strain components
#
# The normal and shear stress fields, induced by an applied force, are pictured in Cartesian coordinates below:
#
# ![Image](0.Images/Stress_Element_Cartesian.jpg "Fig.X - Composite material fatigue-life prediction workflow. Ref: Mösenbacher, ECCM16 (2016)")
#
# *<center> Fig. X - Stresses on a material element (Jones, 1999)</center>*
#
# **The stain (deformation) response**
# Deformation of the material, responding to the induced stress field, is characterized by *tensor shear strain* ($\mathbf{\varepsilon_{ij}}$) and *engineering shear strain* ($\mathbf{\gamma_{ij}}$). Considering a material element being deformed, the tensor and engineering shear strains are defined, respectively, as:
#
# $$ \mathbf{\varepsilon_{1}} = \frac{\partial u}{\partial x}, \qquad \mathbf{\varepsilon_{2}} = \frac{\partial v}{\partial y}, \qquad \mathbf{\varepsilon_{3}} = \frac{\partial w}{\partial z}$$
#
# $$ \mathbf{\gamma_{23}} = \frac{\partial v}{\partial z} + \frac{\partial w}{\partial y}, \qquad \mathbf{\gamma_{31}} = \frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}, \qquad \mathbf{\gamma_{12}} = \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}$$
#
# **Stress-strain relationships - Stiffness and compliance elasticity constants**
# The integral of the incremental work done (per unit volume) on a material (subjected to an applied force that induces a stress field and subsequent strain (deformation) response to the load, yields a relation between work done on the material and the resultant tensor shear strain:
#
# $$ \mathbf{W} = \frac{1}{2} \mathbf{C_{ij}} \cdot \mathbf{\varepsilon_{i}} \mathbf{\varepsilon_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# This result relates The second order differentiation of Hooke's Law shows that the stiffness matrix ($\mathbf{C_{ij}}$) is symmetric (*i.e* $\mathbf{C_{ij}} = \mathbf{C_{ji}}$). Similarly, by examining the inverse of the stress-strain relations, the work done on the material can be related to the induced stress field:
#
# $$ \mathbf{W} = \frac{1}{2} \mathbf{S_{ij}} \cdot \mathbf{\sigma_{i}} \mathbf{\sigma_{j}}, \qquad\quad i,j = 1, ..., 6 $$
#
# Where:
# * $\mathbf{S_{ij}}$ is the compliance matrix
#
# ***Here it's important to note that hygrothermal effects on the deformation of the material are not being considered.*** *This is valid if experimental testing is done with test environment controls and neglecting material temperature changes during tensile/compressive loading.*
#
# The stiffness and compliance matrices have 36 constants, owing to the six degrees of freedom for considering the (linear elastic) deformation response of a material element. The generalized matrices are as follows:
#
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# **Significance of coupled stress-strain elements (*described with the compliance matrix*)**
# For anisotropic materials, significant coupling occurs between the applied stress and the various strain responses. Examing the compliance matrix, the following stress-strain responses are coupled:
#
# * The $ S_{11}, S_{22}$ and $S_{33} $ terms each represent extensional response to their respective applied stress components ($ \sigma_{1}, \sigma_{2}, \sigma_{3} $) in the same direction.
#
# * The $ S_{44}, S_{55}$ and  $S_{66} $ terms represent shear strain response to an applied shear stress in the same plane
#
# * The $ S_{12}, S_{13}$ and  $S_{23} $ terms represent coupling between dissimilar normal stresses and normal strains (extension-extension coupling more commonly known as the Poisson effect)
#
# * The $ S_{14}, S_{15}, S_{16}, S_{24}, S_{25}, S_{26}, S_{34}, S_{35}$ and $S_{36} $ terms represent normal strain response to applied shear stress in a more complex manner than for the preceding compliances (shear-extension coupling)
#
# * Finally, the $ S_{45}, S_{46}$ and $S_{56} $ terms represent shear strain response to shear stress applied in another plane (shear-shear coupling)
#
# * However, less than 36 of the constants can be shown to actually be independent for elastic materials when important characteristics of the strain energy are considered, such as whether the material behaves anisotropically, orthotropically, monoclinically or traversely isotropically when undergoing deformation.
#
# [comment]: <> (------------------------------§2.3.2 Footnotes------------------------------)
# __________________________________
#
# <span id="fn1"> 1. Linear elasticity theory makes a number of assumptions about the elastic/plastic deformation response to stress fields induced by applied force loads, namely that strain responses are infinitesimally small, and that relationships between the components of stress and strain are approximately. Additionally, the theory is valid only for stress states that do not produce yielding.</span>

# ### 2.1.2 UD laminae strain-stress relationships
# The fibre arrangements, of the laminate coupons prepared for these experimental investigations, were classified as orthotropic or transversely isotropic bodies. In UD laminae, all planes whose perpendicular vector is transverse with respect to the fibre direction are planes of symmetry. The UD laminae are transversely isotropic. On planes parallel with the fibre direction it behaves orthotropically (*material properties that differ along three mutually-orthogonal twofold axes of rotational symmetry - a subset of anisotropic materials*)and on an imaginary plane perpendicular to the fibre direction it behaves isotropically (*material properties remain constant in all directions*).
#
#  **3-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
#  <br>
#
# With the application of tensile or compressive force loading, parallel to the fibre direction of the UD laminae (in-plane loading), shear-extension and shear-shear coupling can be neglected. As such, the stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\
# C_{21} & C_{22} & C_{23} & 0 & 0 & 0 \\
# C_{31} & C_{32} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\
# S_{21} & S_{22} & S_{23} & 0 & 0 & 0 \\
# S_{31} & S_{32} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{55} & 0 \\
# 0 & 0 & 0 & 0 & 0 & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# **3-D Isotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# The stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting isotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & 0 & 0 & 0 \\
# C_{12} & C_{11} & C_{13} & 0 & 0 & 0 \\
# C_{13} & C_{13} & C_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & C_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & C_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & 0 & 0 & 0 \\
# S_{12} & S_{11} & S_{13} & 0 & 0 & 0 \\
# S_{13} & S_{13} & S_{33} & 0 & 0 & 0 \\
# 0 & 0 & 0 & S_{44} & 0 & 0 \\
# 0 & 0 & 0 & 0 & S_{44} & 0 \\
# 0 & 0 & 0 & 0 & 0 & 2(S_{11} - S_{12})  \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$

# ### 2.1.3 2-D UD laminae strain-stress relationships
# Since the test coupons for this investigation are all UD laminate samples, and tensile/compressive loadings during experiment runs were applied in the 1-2 plane of the samples, the remaining theory discussion will focus on 2-D laminae stress-strain relationships.
#
# The plane-stress state of the UD composite, in the 1-2 plan, is defined by setting:
#
# $$ \sigma_{3} = 0, \tau_{23} = 0, \tau_{31} = 0$$
#
# such that:
#
# $$ \sigma_{1} ≠ 0, \sigma_{2} ≠ 0, \tau_{21} ≠ 0$$
# <br>
#
# where $ \sigma_{1}$ and $ \sigma_{2}$ represent the stress components normal to the 1-2 plane of a UD laminate material, w.r.t to the 1 and 2 directions respectively, and $ \tau_{21}$ represents the intralaminar shear stress w.r.t. the 1-2 plane of a UD laminae material.
#
# **2-D Orthotropic $\mathbf{\sigma} - \mathbf{\varepsilon}$ relationship**
# As such, the 2-D stress-strain relationship, w.r.t the ***stiffness matrix***, for UD laminae exhibiting orthotropic behaviour is simplified to:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & 0 \\
# C_{12} & C_{22} & 0 \\
# 0 & 0 & (C_{11} - C_{12})/2 \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
#
# and w.r.t. to the ***compliance matrix***:
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & 0 \\
# S_{12} & S_{22} & 0 \\
# 0 & 0 & 2(S_{11} - S_{12}) \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right)$$
#
# These equations effectively describe the deformation response (described by tensor and engineered shear strain components) of the UD laminae in the 1-2 plane, w.r.t. a shear stress field (described by stress components normal to the 1-2 plane and in-plane shear stress components).
#
# The tensile and compressive tests, performed for the purposes of this investigation, will be conducted with preset force loads. The resulting displacement (strain) measured will determine the engineering constants required to solve the stress-strain equations discussed above.

# ### 2.1.4 Overview of engineering constants for solving strain-stress equations
# A brief overview of the engineering constants required to solve the 2-D UD laminae stress-strain equations is presented below:
#
# 1. The slope of (tensile/compressive) stress-strain curve:
#     * $ E = \frac{\sigma}{\varepsilon} $
#     * $ E_{i}$ represents the Young's (extension) moduli in the $ i^{th}$ directions, describing the elastic extension of the material in a specific direction
#
# 2. The slope of strain-strain curves (Poisson's ratio):
#     * the negative of the ratio of (signed) transverse strain to (signed) axial strain (i.e. extension-extension coupling coefficient)
#     * $ \nu_{ij} = \frac{-\varepsilon_{i}}{\varepsilon_{j}} $
#
# 3. The shear modulus, $ G_{ij}$, defining the ratio of shear stress to the shear strain in the (i-j) plane, or rather the material's response to shear stress
#
# **The orthotropic UD laminae case**
# <br>
#
# From these definitions, the **compliance matrix** can be expressed in terms of these engineering constants as follows:
#
# $$S =
# \begin{bmatrix} \frac{1}{E_{11}} & - \frac{\nu_{21}}{E_{22}} & 0 \\
# - \frac{\nu_{12}}{E_{11}} & \frac{1}{E_{22}} & 0 \\
# 0 & 0 & \frac{1}{G_{12}} \\
# \end{bmatrix} $$
#
# Since the stiffness and compliance matrices are mutually inverse, it follows by matrix algebra that their components are related as follows for orthotropic materials (*limited to the 2-D case*):
#
# $$ C_{11} = \frac{S_{22}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{1}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ C_{22} = \frac{S_{11}}{S_{11} S_{22} - S^{2}_{12}} = \frac{E_{2}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ C_{12} = \frac{S_{12}}{S_{11} S_{22} - S^{2}_{12}} = \frac{\nu_{12}E_{1}}{1 - \nu_{12} \nu_{21}} =
# \frac{\nu_{21}E_{1}}{1 - \nu_{12} \nu_{21}} $$
#
# $$ \frac{C_{11} - C_{12}}{2} = G_{12} $$
#
# **The isotropic UD laminae case**
# <br>
#
# Note that for orthotropic UD laminae, there are four independent variables, namely $ E_{1}, E_{2}, \nu_{12} $ and $ G_{12} $. For the isotropic case, we note that:
# * $ S_{11} = \frac{1}{E_{1}} = \frac{1}{E_{2}} = \frac{1}{E} =  S_{22} $, such that $ E_{1} = E_{2} = E $
# * $ S_{12} = - \frac{\nu_{12}}{E_{1}} = - \frac{\nu_{21}}{E_{2}} = - \frac{\nu}{E} $
# * $ \frac{1}{G_{12}} = \frac{1}{G} = \frac{2(1 + \nu)}{E} $

# ## 2.2 UD laminae in-plane strain-stress relationships

# For in-plane stresses of composite plies we assume that stresses and strains to not vary in certain directions, depending on how the ply is force-loaded. When the aforementioned plane-strain condition exists, the three-dimensional analysis simplifies considerably.
#
# The UD laminate test coupons, from the experimental trials, were subjected to in-plane stresses (via 1-2 plane tensile and compressive force loading. The fibre arrangements, of the experiment laminate coupons, were classified as orthotropic or (symmetric) transversely isotropic bodies.
#
# From the general, anisotropic stress-strain systems of equationss,  defined in Eq. [6] and [7] with the stiffness and compliance matrices respectively:
#
# *Stiffness matrix* ($\mathbf{C_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} C_{11} & C_{12} & C_{13} & C_{14} & C_{15} & C_{16} \\
# C_{21} & C_{22} & C_{23} & C_{24} & C_{25} & C_{26} \\
# C_{31} & C_{32} & C_{33} & C_{34} & C_{35} & C_{36} \\
# C_{41} & C_{42} & C_{43} & C_{44} & C_{45} & C_{46} \\
# C_{51} & C_{52} & C_{53} & C_{54} & C_{55} & C_{56} \\
# C_{61} & C_{62} & C_{63} & C_{64} & C_{65} & C_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) $$
#
# *Compliance matrix* ($\mathbf{S_{ij}}$):
# <br>
#
# $$ \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \\ \gamma_{23} \\ \gamma_{31} \\ \gamma_{12} \\  \end{array} \right) =
# \begin{bmatrix} S_{11} & S_{12} & S_{13} & S_{14} & S_{15} & S_{16} \\
# S_{21} & S_{22} & S_{23} & S_{24} & S_{25} & S_{26} \\
# S_{31} & S_{32} & S_{33} & S_{34} & S_{35} & S_{36} \\
# S_{41} & S_{42} & S_{43} & S_{44} & S_{45} & S_{46} \\
# S_{51} & S_{52} & S_{53} & S_{54} & S_{55} & S_{56} \\
# S_{61} & S_{62} & S_{63} & S_{64} & S_{65} & S_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \\ \tau_{23} \\ \tau_{31} \\ \tau_{12} \\  \end{array} \right)$$
#
# These equations reduce to the following for in-plane (*plane-stress*) loading of orthotropic composite plies:
#
# $$ \left( \begin{array}{c} \sigma_{1} \\ \sigma_{2} \\ \tau_{12} \\  \end{array} \right) =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\
# Q_{12} & Q_{22} & Q_{26} \\
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{1} \\ \varepsilon_{2} \\ \gamma_{12} \\  \end{array} \right) $$
#
# Where:
#
# $Q_{ij}$ represent the **in-plane** elements of the stiffness matrix subject to the **plane-stress condition** (*differentiated from the general stiffness matrix elements $C_{ij}$*)
#
# The plane-stress conditioned compliance matrix is the inverse of the plane-stress conditioned stiffness matrix:
#
# $$ \begin{bmatrix} S'_{11} & S'_{12} & S'_{16} \\
# S'_{12} & S'_{22} & S'_{26} \\
# S'_{16} & S'_{26} & S'_{66} \\
# \end{bmatrix}^{-1}  =
# \begin{bmatrix} Q_{11} & Q_{12} & Q_{16} \\
# Q_{12} & Q_{22} & Q_{26} \\
# Q_{16} & Q_{26} & Q_{66} \\
# \end{bmatrix} $$
#
# Where:
#
# $S'_{ij}$ represent the **in-plane** elements of the compliance matrix subject to the **plane-stress condition** (*differentiated from the general compliance matrix elements $S_{ij}$*)

# ## 2.3 Stress and strain transformations

# Axes transformations are important in stress-strain of materials. Such transformations are required to compute critical values of these (stress-strain) characteristics, as well as to be able to understand the tensorial nature of stress and strain. Other entities, such as moment of inertia and curvature, also transform in a manner similar to stress and strain.
#
# For the purposes of this DLN the relevant theory related to transformations of stress and strain from a local coordinate system to a global coordinate system will briefly be discussed. Further resources on (stress-strain) tensor transformation theory can be found in [Roylance, 2001].
#
# ### 2.3.1 Stress and strain transformations for laminate plies
#
# Stress can be transformed from a local cartesian coordinate system **L(p,q,r)** to a global cartesian coordinate system **G(p,q,r)** via:
#
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \sigma_{G,r} \\ \tau_{G,qr} \\ \tau_{G,pr} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} T_{\sigma11} & \cdots & T_{\sigma16} \\
# \vdots & \ddots & \vdots \\
# T_{\sigma61} & \cdots & T_{\sigma66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \sigma_{L,r} \\ \tau_{L,qr} \\ \tau_{L,pr} \\ \tau_{L,pq} \\  \end{array} \right)$$
#
# Which can be written in the form:
#
# $$ \mathbf{\sigma_{G}} = [\mathbf{\hat{T}_{\sigma}}] \mathbf{\sigma_{L}} $$
#
# For composite laminate plies subjected to plane-strain and plane-stress conditions, one is only interested stresses manifested in the G(p-q) and L(p-q) planes; for UD laminate plies this would mean the planes that characterize stresses occurring only in the fibre direction and transverse to the fibre direction. Then the stresses in the **G(p,q,r)** coordinate system are arrived at by rotation about the 'r' axis of the **L(p,q,r)** coordinate system, namely:
#
# $$ \left( \begin{array}{c} \sigma_{G,p} \\ \sigma_{G,q} \\ \tau_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\
# s^{2} & c^{2} & -2cs \\
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \sigma_{L,p} \\ \sigma_{L,q} \\ \tau_{L,pq} \\  \end{array} \right)$$
#
# Where:
# <br>
#
# $ c = cos\Theta \qquad\quad s = sin\Theta $
#
# And can be written in the form:
#
# $$ \mathbf{\sigma_{G}} = [\mathbf{T_{\sigma}}] \mathbf{\sigma_{L}} $$
#
# Meaning that only the three in-plane strain components are transformed.
#
# A similar treatment of the strain tensor, relating strains (on a composite laminate ply material) in the local coordinate system to the global coordinate system, yields:
#
# $$ \left( \begin{array}{c} \varepsilon_{G,p} \\ \varepsilon_{G,q} \\ \gamma_{G,pq} \\  \end{array} \right) =
# \begin{bmatrix} c^{2} & s^{2} & cs \\
# s^{2} & c^{2} & -cs \\
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon_{L,p} \\ \varepsilon_{L,q} \\ \gamma_{L,pq} \\  \end{array} \right)$$
#
# Where c and s are as previously defined, and can be written alternatively as:
#
# $$ \mathbf{\varepsilon_{G}} = [\mathbf{T_{\varepsilon}}] \mathbf{\varepsilon_{L}} $$
#
# The stiffness and compliance matrices, $[\mathbf{C}]$ and $[\mathbf{S}]$ respectively, can be transformed accordingly (*see [Roylance, 2001] for matrix inversion steps*) to yield:
#
# $$ [\mathbf{C'}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{C}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
#
# $$ [\mathbf{S'}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
#
# Thus the transformed stiffness matrix can be computed for composites with fibres of varying orientations, from a reference local coordinate system and using laminate ply material stiffness constants to a global coordinate system, with the stress and strain transforms being:
#
# $$ [\mathbf{T_{\sigma}}] =
# \begin{bmatrix} c^{2} & s^{2} & 2cs \\
# s^{2} & c^{2} & -2cs \\
# -cs & cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
#
# $$ [\mathbf{T_{\varepsilon}}] =
# \begin{bmatrix} c^{2} & s^{2} & cs \\
# s^{2} & c^{2} & -cs \\
# -2cs & 2cs & c^{2}-s^{2} \\
# \end{bmatrix} $$
#
# ### 2.3.2 In-plane transformed stiffness and compliance matrices
#
# It follows that, for composite plies subjected to plane-stress conditions, the transformed in-plane stress and strain systems of equations can be derived by substituting the plane-stress conditioned stiffness and compliance matrices (Eqn. [23], [24]) into Eqns. [31] and [32]:
#
# $$ [\mathbf{\bar{Q}}] = [\mathbf{\hat{T}_{\sigma}}][\mathbf{Q}][\mathbf{\hat{T}_{\varepsilon}}]^{-1} $$
#
# $$ [\mathbf{\bar{S}}] = [\mathbf{\hat{T}_{\varepsilon}}][\mathbf{S}][\mathbf{\hat{T}_{\sigma}}]^{-1} $$
#
#
# ### 2.3.3 References
#
# 1. Roylance, D. (2001). Transformation of stresses and strains. Lecture Notes for Mechanics of Materials.

# ## 2.4 Laminate structural durability calculations

# ### 2.4.1 Stiffness matrices for in-plane stress conditioned laminates
#
# Eqn.s [35] and [36] represent the plane-stressed conditioned stiffness and compliance matrices for individual plies. To approximate the stress-strain relationships of entire laminates (multi-layer manufactured plies), we define the [A], [B] and [D] stiffness matrices:
#
# $$ [\mathbf{A}] = \int_{-h_{b}}^{h_{t}} [\bar{\mathbf{Q}}]dz $$, and each $[A_{ij}]$ element defined by:
#
# $$ A_{ij} = \int_{-h_{b}}^{h_{t}} \bar{Q_{ij}}dz $$
#
# Where:
#
# * $h_{b}$ represents the distance of the laminate plies from the reference plane to the bottom surface of the entire laminate structure
# * $h_{t}$ represents the distance of the laminate plies from the reference plane to the top surface of the entire laminate structure
# * Recall that $[\bar{Q}]$ represents the in-plane stress conditioned, transformed stiffness matrix of each ply
#
# The variable '$\mathbf{z}$' in Eqn. [37] defines the distance of the '$\mathbf{z^{th}}$' ply from the reference plane
#
# $$ [\mathbf{B}] = \int_{-h_{b}}^{h_{t}} z[\bar{\mathbf{Q}}]dz $$, and each $[B_{ij}]$ element defined by:
#
# $$B_{ij}] = \int_{-h_{b}}^{h_{t}} z\bar{Q_{ij}}dz $$
#
# and
#
# $$ [\mathbf{D}] = \int_{-h_{b}}^{h_{t}} z^{2}[\bar{\mathbf{Q}}]dz $$, and each $[D_{ij}]$ element defined by:
#
# $$ D_{ij} = \int_{-h_{b}}^{h_{t}} z^{2}\bar{Q_{ij}}dz $$
#
# From the assumption that the composite plies and laminates, tested for the quasi-static fatigue loading investigations, exhibit linear elastic behaviour, it is assumed that $[\bar{Q}]$ is constant across each ply. Thus, the laminate stiffness and compliance integrals above can be replaced by the summations:
#
# $$ A_{ij} = \sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z_{k}-z_{k-1}) $$
#
# $$ B_{ij} = \frac{1}{2}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{2}_{k}-z^{2}_{k-1}) $$
#
# $$ D_{ij} = \frac{1}{3}\sum_{k=1}^{K} (\bar{Q_{ij}})_{k}(z^{3}_{k}-z^{3}_{k-1}) $$

# ## 2.5 Mechanics of in-plane stress-conditioned composite laminates

# ### 2.5.1 In-plane forces and moments
#
# From the [A], [B] and [D] in-plane stiffness matrix elements described in Eqns. [43] through [45], the in-plane forces and moments of the laminate can be related to the in-plane strain and curvature response of the laminate. For a laminate subject to the in-plane stress condition in the 1-2 plane, this relationship is:
#
# $$ \left( \begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right) =
# \begin{bmatrix} A_{11} & A_{12} & A_{16} & B_{11} & B_{12} & B_{16} \\
# A_{21} & A_{22} & A_{26} & B_{21} & B_{22} & B_{26} \\
# A_{61} & A_{62} & A_{66} & B_{61} & B_{62} & B_{66} \\
# B_{11} & B_{12} & B_{16} & D_{11} & D_{12} & D_{16} \\
# B_{21} & B_{22} & B_{26} & D_{21} & D_{22} & D_{26} \\
# B_{61} & B_{62} & B_{66} & D_{61} & D_{62} & D_{66} \\
# \end{bmatrix}
# \cdot
# \left( \begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) $$
#
# Inversion of Eqn. [46] defines the strain and curvature of the laminate in terms of the in-plane force loading and moments of the laminate. For a laminate force-loaded in the 1-2 plane:
#
# $$ \left(\begin{array}{c} \varepsilon^o_{1} \\ \varepsilon^o_{2} \\ \gamma^o_{1-2} \\ \kappa_{1} \\ \kappa_{2} \\ \kappa_{12} \\  \end{array} \right) =
# \begin{bmatrix} \alpha_{11} & \alpha_{12} & \alpha_{16} & \beta_{11} & \beta_{12} & \beta_{16} \\
# \alpha_{21} & \alpha_{22} & \alpha_{26} & \beta_{21} & \beta_{22} & \beta_{26} \\
# \alpha_{61} & \alpha_{62} & \alpha_{66} & \beta_{61} & \beta_{62} & \beta_{66} \\
# \beta_{11} & \beta_{12} & \beta_{16} & \delta_{11} & \delta_{12} & \delta_{16} \\
# \beta_{21} & \beta_{22} & \beta_{26} & \delta_{21} & \delta_{22} & \delta_{26} \\
# \beta_{61} & \beta_{62} & \beta_{66} & \delta_{61} & \delta_{62} & \delta_{66} \\
# \end{bmatrix}
# \cdot
# \left(\begin{array}{c} N_{1} \\ N_{2} \\ N_{1-2} \\ M_{1} \\ M_{2} \\ M_{1-2} \\  \end{array} \right)
#  $$
#
#  ### 2.5.2 Importance of the [A], [B] and [D] matrices to laminate structural durability analyses
#
#  The [A], [B] and [D] matrices characterize the stiffness of the laminates, the degree to which the composite laminate will elastically deform, when subjected to certain force-loading conditions.
#
#  For the purposes of the quasi-static fatigue (tensile and compressive) in-plane force-loading of carbon fibre/epoxy laminate composite coupons (the experiments designed to investigate the *linear* elastic structural durability of these composite materials), the significance of these matrices are as follows:
#
#  1. The $A_{ij}$ stiffness matrix elements relate the in-plane forces, imposed on the laminate coupons, to the in-plane (*elastic*) deformations manifested in the laminates (*under tensile or compressive force-loading*)
#
#  2. The $B_{ij}$ stiffness matrix elements are the in-plane–out-of-plane coupling stiffnesses that relate the:
#      * in-plane forces, imposed on the laminate coupons, to the resultant curvatures of the laminate
#      * moments, imposed on the laminate, to the resultant in-plane deformation of the laminate
#
#  3. The $D_{ij}$ stiffness matrix elements are the bending stiffnesses that relate the moments, imposed on the laminate, to the resultant curvatures of the laminate
#
# Examination of the [A], [B], and [D] matrices show that different types of couplings may occur. For the experimental (tensile and compressive force-loading) of the composite laminate coupons in the 1-2 plane, the following important force-moment-curvature-deformation couplings are worth noting:
#
# 1. **Extension–shear coupling**
#     * When the elements $A_{16}$, $A_{26}$ (of the $A_{ij}$ elements) are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause shear deformation ($\gamma^o_{1-2}$), and a twist force ($N_{1-2}$) causes elongations in the 1 and 2 directions
#
# 2. **Bending–twist coupling**
#     * When the elements $D_{16}$, $D_{26}$ are not zero, bending moments ($M_{1}, M_{2}$) may cause a twisting of the laminate ($\kappa_{1-2}$), and a twist moment ($M_{1-2}$) causes curvatures in the 1–3 and 2–3 planes
#
# 3. **Extension–twist and bending–shear coupling**
#     * When the elements $B_{16}$, $B_{26}$ are not zero, in-plane normal forces ($N_{1}, N_{2}$) cause twist ($\kappa_{1-2}$), and bending moments ($M_{1}, M_{2}$) result in shear deformation ($\gamma^o_{1-2}$)
#
# 4. **In-plane–out-of-plane coupling**
#     * When the $B_{ij}$ stiffness matrix elements are not zero, in-plane forces ($N_{1}, N_{2}, N_{1-2}$) cause out-of-plane deformations (curvatures) of the laminate, and moments ($M_{1}, M_{2}, M_{1-2}$) cause in-plane deformations in the 1-2 plane.
#
# It is worth noting that these four types of coupling are characteristic of composite materials and do not occur in homogeneous isotropic materials. The following two couplings occur in both composite and isotropic materials:
#
# 5. **Extension–extension coupling**
#     * When the element $A_{12}$ is not zero, a normal force $N_{1}$ causes elongation in the 2 direction ($\varepsilon^o_{2}$), and a normal force $N_{2}$ causes elongation in the 1 direction ($\varepsilon^o_{1}$)
#
# 6. **Bending–bending coupling**
#     * When the element $D_{12}$ is not zero, a bending moment $M_{1}$ causes curvature of the laminate in the 2-3 plane ($\kappa_{2}$), and a bending moment $M_{2}$ causes curvature of the laminate in the 1–3 plane ($\kappa_{1}$)

# ## 2.6 Applications of [A], [B], [D] ( [$\alpha$], [$\beta$], [$\delta$] ) matrices to the (*elastic*) structural durability characterization of experiment carbon fibre/epoxy composite coupons

# * [§3: Structural durability analyses of carbon fibre & epoxy-based composites - Experimental results](DLN - §3 - Structural durability analyses of carbon fibre & epoxy-based composites - Experimental.ipynb) is the DLN entry that uses Python scientific programming libraries to explore and visualize quasi-fatigue tensile & compressive loading experiments on carbon fibre/epoxy composite test coupons. From analyses of the experiments, the elastic properties of the test coupons are determined.
# <br>
#
# * [§4: Structural durability analyses of carbon fibre & epoxy-based composites - Matrix calculations](DLN - §2 - Structural durability analyses of carbon fibre & epoxy-based composites - Calculations.ipynb) is the DLN entry that uses MATLAB to perform structural durability matrix calculations from carbon fibre/epoxy composite test coupon experimental data. The $[A], [B], [D]$ $([\alpha], [\beta], [\delta])$ matrices are calculated for each of the test laminate coupons.
#


# coding: utf-8

# # Structural durability analyses for carbon/epoxy laminates
#
# ## §3: Experimental

# In[39]:


#Preamble to hide inputs so that massive code scripts are not cluttering the data visualization output
from IPython.display import HTML

HTML('''<script>
code_show=true;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# # DLN Contents
#
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

# ## I. Experiment log
# * **Date of experiment**: 10.14.2017
# * **Principle investigator**: Delroy Meyer, EIT, BASc
# * **Test operators**: Jürgen Müller, Delroy Meyer, Cintia Oliveria
# * **Lead investigator**: Prof. Dr-mont. Zoltan Major
# * **Course**: LVA Nr. 378.029 - 480ADPTPPBV17 - Polymer Product Design and Engineering III - Graduate Seminar
# * **Location**: Institute of Polymer Materials and Testing (IPMT), JKU Linz - Linz, Austria
#     * Compounding and specimen preparation Lab: *Composite coupon specimen preparation*
#     * Mechanical Lab: *Tensile & compression testing*
#
# ### i. Experiment test (lab) environment conditions
# *Measurement taken: 10-14-2017 08:45:07*
# <b>
#
# $T_{test} (°C) = 21.23$ (*within* $ 23 ± 3 °C$ *standard laboratory atmosphere range as per ASTM D5229*)
# <br>
# $RH (\%) = 55.7$ (*within* $ 50 ± 10 \%$ *standard laboratory atmosphere range as per ASTM D5229*)

# ## 3.1 Composite specimens to be tested for structural durability analyses

# ### 3.1.1 Properties applicable to all test coupons
# * **Composite type**: CFRP - carbon/epoxy laminates
#     * Carbon fibre ply:
#         * Unidirectional 0°:
#         * Unidirectional 90°:
#         * Unidirectional 45°:
#         * Unidirectional ±45°: [HiMax™ FCIM151](https://www.hexcel.com/user_area/content_media/raw/FCIM151.pdf)
#     * Epoxy resin system: [HexPly® M35-4](https://www.hexcel.com/user_area/content_media/raw/HexPly_M354_DataSheet.pdf)
# * **Void fraction ($v_{f}$, %)**: 55
# * **Test speed (mm/min)**: 1
# * **No. of samples per test**: 3
#
# ### 3.1.2 Properties applicable to all specimens
# The following table details the specimens to be tested for the investigation:
#
# **<center>Table 1. Set of carbon fibre/epoxy laminate coupons for quasi-static fatigue testing</center>**
#
# | Coupon tag | Direction | Orientation [°] | Loading | No. of Layers | Avg. Coupon Width [mm] | Avg. Coupon Thickness [mm] |
# |:----------:|:---------:|:---------------:|:-----------:|:-------------:|:----------------------:|:--------------------------:|
# | UD_0_4_T | UD | 0 | Tension | 4 | 9.98 | 1.02 |
# | UD_90_8_T | UD | 90 | Tension | 8 | 20.02 | 1.98 |
# | BD_±45_8_T | BD | ±45 | Tension | 8 | 20.1 | 1.95 |
# | UD_45_8_T | UD | 45 | Tension | 8 | 20.06 | 2.01 |
# | UD_0_4_C | UD | 0 | Compression | 4 | 9.98 | 1.01 |
# | UD_90_8_C | UD | 90 | Compression | 8 | 19.98 | 2.02 |
#
# As a reference, ply (laminate) layers were layed-up according to the following convention:
#
# ![Image](0.Images/UD_laminate_orientation_ref.jpg)
#
# *<center> Fig. Y - UD lamina lay-up orientations (JKU Linz - IPPE, 2017)</center>*
#
#
# ### 3.1.3 References
# [1] *Mosenbacher, A., Brunbauer, J., Pichler, P. F., Guster, C., & Pinter, G. (2014). Modelling and validation of fatigue life calculation method for short fiber reinforced injection molded parts. In 16th European conference of composite materials.* [Link](http://www.escm.eu.org/eccm16/assets/0329.pdf)
#
# [2] *Jones, R. M. (1999). Mechanics of composite materials. 2nd Ed. CRC press.*

# ## 3.2 Carbon fibre/epoxy test coupon fabrication

# 1. Carbon/epoxy specimens with 55% fibre volume fraction were produced with the following materials:
#
#     * **Epoxy resin and system**: HexPly® M35-4
#     * **Carbon fibres**: HiMax™ FCIM151
#     * **Other**: Epoxy-compatible binder was used to make handling the layup of carbon fibre sheets easier and to prevent distortion during the layup manufacturing
# <br>
#
#
# 2. The specimen laminates were produced according to the cure cycle protocol indicated in the HexPly® M35-4 technical specification, with:
#     * the cure temperature set at $100 \pm 2.5°C$
#     * cure processing time set at 4.5 hours
#     * heat-up and cool-down rates set at 1°C/minute, vacuum applied at -0.85 bar
#     * autoclave pressure set to 7.5 bar-g.
# <br>
#
# 3. Unidirectional (UD) carbon/epoxy specimens were milled from plates with diamond blades at angles of 0°, 45°/±45° and 90°
# <br>
#
# 4. Specimen geometries for mechanical tests with carbon/epoxy specimens were chosen according to the following specifications:
#     * Rectangular specimens (especially for UD)
#     * Tabs for load introduction
#     * Tab material had to possess a lower stiffness than tested materials; testing CF/epoxy composite coupons - aluminum tabs were used for fabrication
# <br>
#
# The following figure shows the dimensions used to prepare the composite coupons for testing:
#
# ![Image](0.Images/CF-Epoxy_Coupon_Dim.jpg)
#
# *<center> Fig. 3.1 - Test coupon geometries for UD quasi-isotropic and 0°  (JKU Linz - IPPE, 2017)</center>*
#
# 4-ply UD specimens had the following geometry:
# * $200 \pm 0.1 mm \quad\quad x \quad\quad 10 \pm 0.025 mm \quad\quad x \quad\quad 1 \pm 0.025 mm$ for UD 0° specimens
#
# 8-ply UD specimens had the following geometry:
# * $200 \pm 0.1 mm \quad\quad x \quad\quad 20 \pm 0.1 mm \quad\quad x \quad\quad 2 \pm 0.025 mm$ for 8-ply/off-axis specimens
#
# * Aluminium tabs with 1.5 mm thickness were adhered on both sides of all carbon/epoxy specimens( For tensile loads, usually 1 mm thickness is chosen for specimens tested in fibre direction)

# ## 3.3 Experimental equipment and data reduction process

# ### 3.3.1 Data analysis
# For data evaluation, all moduli and strengths were calculated with the real cross-sections of the respective tested specimens. Moduli were evaluated between 0.001 and 0.003 absolute strain, as per:
# * ASTM D3039/D3039M: Standard test method for tensile properties of polymer matrix composite materials
#
# * ASTM D3410 / D3410M: Standard Test Method for Compressive Properties of Polymer Matrix Composite Materials
#
# * ASTM_E111-04: Standard Test Method for Young’s Modulus, Tangent Modulus, and Chord Modulus
#
# ### 3.3.2 Equipment
# * All mechanical tests were performed on a Zwick-Roell HA 100 kN servo-hydraulic fatigue test machine designed for loads up to 100 kN at room temperature
#
# ### 3.3.3 Quasi-static tension and compression tests
# * In quasi-static tension and compression tests, specimens were loaded in a displacement controlled way with a test speed of 1 mm/min
# * End-tabs were clamped completely between the Zwick-Roell HA system grips
# * Strains in longitudinal direction were recorded by means of a proprietary digital sensor setup (JKU Linz IPMT)
# * The experiment runs were designed to investigate the in-plane tensile and compressive properties of polymer matrix composite materials reinforced by high-modulus fibers (in this case, carbon fibre/epoxy laminate composites). The applicability of the ASTM test method are limited to continuous fiber or discontinuous fiber-reinforced composite material forms, in which the laminate is balanced and/or symmetric with respect to the test direction

# ## 3.4 Experimental data analyses - Python Preamble

# ### 3.4.1 Premable for python object-oriented programming

# In[40]:


##===============================IMAGES============================================================

#Image import preamble
import IPython
from IPython.display import display, Image, SVG, Math, YouTubeVideo
Image_PATH = "/Users/delroy_m/Desktop/(CMT) Materials Characterization ELN/0.Images/"

# Use 'image drag & drop' IPython Notebook Extension
#IPython.html.nbextensions.install_nbextension('https://raw.github.com/ipython-contrib/IPython-notebook-extensions/master/nbextensions/usability/dragdrop/main.js')

#Load 'image drag & drop' extension
#%javascript
#IPython.load_extensions('usability/dragdrop/main');

#NOTE about 'image drag & drop' extension handling of images
# The image will be uploaded to the server into the directory where your notebook resides. This means, the image is not copied into the notebook itself, it will only be linked to.

##===============================DATA ANALYSES=====================================================

#import PANDAS - A library providing high-performance, easy-to-use data structures and data analysis tools
import pandas as pd
#print("Current Pandas version:", pd.__version__)
# print("plotly version:", __version__)

#import SciPy - A Python-based ecosystem of open-source software for mathematics, science, and engineering
import scipy
from scipy import *
#Import Gaussian distribution STATS package to validate whether experimental data is randomly (normally)
#distributed
from scipy.stats import *
#from scipy.stats import norm
# if using a Jupyter notebook, include:
#%matplotlib inline

#import NumPy - A fundamental package for scientific computing with Python
import numpy as np

#import qgrid - Allows querying of DataFrames with intuitive scrolling, sorting, and filtering controls,
#as well as editing features, for the DataFrames, by double clicking cells
import qgrid

##===============================DATA VISUALIZATION================================================

#import matplotlib - A Python 2D plotting library
#import matplotlib.pyplot as plt

#import Pygal - A Python SVG Charts Creator
import pygal

#import Plotly for online or offline interactive plot rendering
#
#If using Plotly with online server:
#import plotly.plotly as py
#
#If using Plotly offline and saving code/graphs/images locally:
import plotly.graph_objs as go
import plotly as py
from plotly import __version__ #ensures that most up-to-date plotly pckg is being used
from plotly.offline import init_notebook_mode, plot, download_plotlyjs, iplot
import plotly.figure_factory as ff
from plotly import tools
#Improve Plotly figure render responsiveness
import plotly.io as pio
pio.renderers.default = 'iframe'
# #import cufflinks as cf


#import Seaborn - Statistical data visualization using Matplotlib
import seaborn as sns
#from matplotlylib import fig_to_plotly

#import Plotly express - A terse, consistent, high-level wrapper around Plotly.py for rapid data exploration and figure generation
#import plotly_express as px

#Put plotly environment in 'offline mode'
py.offline.init_notebook_mode(connected=True)

#Reinitialize Jupyter Notebook mode
init_notebook_mode()

#For 'online' plotting:
# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api

#Do I have the most up-to-date plotly package?
#print("Current Plotly version:", __version__)

##===============================SYSTEM COMMANDS====================================================
import glob
import sys
import datetime
import os

##===============================EXCEPTION HANDLING=================================================
#Ignore dataframe slicing copying warnings --> these are annoying, and issue is acknowledged
pd.options.mode.chained_assignment = None  # default='warn'

#Mute any annoying compiling warnings that arise when running code
#import warnings
#warnings.filterwarnings("ignore")


# ### 3.4.2 Setup framework for parsing quasi-static fatigue experimental data into Python (Pandas) dataframes

# In[41]:


##===============================Create dataframe from experiment data================================
#Coupon cyclic fatigue testing datasets - formatted according to "Hadley Wickham - Tidy Data"
#"Hadley Wickham - Tidy Data" - http://vita.had.co.nz/papers/tidy-data.pdf

#1. Each variable forms a column
#2. Each observation forms a row
#3. Each type of observational unit forms a table

##----------------------------------------------------------------------------------------------------
##-Naming convention for experiment files-##
#
#[Fiber_direction]-[Orientation_degree]-[Tension/Compression]-[Fibre_type]-[Test_speed (mm/min)]-[Test_temp]...
#-[Strain_in_load_direction]-[#_of_specimens_tested]-[specimen_avg_width (mm)]-[specimen_avg_thickness (mm)].xlsx

#"Experiment data attribute tags
####----------------------------------------------------------------------------------------------------
#   1. Fiber_direction:
#      - Unidirectional (UD): 0°, 90° --> Provides longitudinal stiffness
#      - Bidirectional (BD): ±45° --> Provides torsional stiffness
#      * Attribute_type = [Alpha]
#
#   2. Orientation (°): 0°, ±45°, 90°
#      * Attribute_type = [Alphanumeric]
#
#   3. Tension/compression loading:
#      - T: Tension
#      - C: Compression
#      * Attribute_type = [Alpha]
#
#   8. Strain-in-load direction (x, y, x &/OR y):
#      - UD: ε,y
#      - BD: ε,y &/OR ε,x
#      * Attribute_type = [Alphanumeric]
#
#   9. No. of specimens tested (#):
#      * Attribute_type = [Numeric]
#
#   10. Specimens avg. width (mm):
#      * Attribute_type = [Numeric]
#
#   11. Specimens avg. thickness (mm):
#      * Attribute_type = [Numeric]
#
#
#"Experiment data variables
####----------------------------------------------------------------------------------------------------
#Column 1:
#      - Tension or compression load [N]
#
##Column 2:
#      - Strain [%]

#Custom color palette for plotting
####----------------------------------------------------------------------------------------------------
#Column 1:
dark_turquoise = '#00CED1'
turquoise = '#40E0D0'
medium_turquoise = '#48D1CC'
pale_turquoise = '#AFEEEE'
aqua_marine = '#7FFFD4'
powder_blue = '#B0E0E6'
cadet_blue = '#5F9EA0'
steel_blue = '#4682B4'
corn_flower_blue = '#6495ED'
deep_sky_blue = '#00BFFF'
dodger_blue = '#1E90FF'
light_blue = '#ADD8E6'
sky_blue = '#87CEEB'
light_sky_blue = '#87CEFA'
midnight_blue = '#191970'
navy = '#000080'
dark_blue = '#00008B'
medium_blue = '#0000CD'
blue = '#0000FF'
royal_blue = '#4169E1'


# ### 3.4.3 Parse quasi-static fatigue experimental data into data frame

# In[42]:


#Upload all 'cleaned' experimental data sets for composite coupon fatigue testing

##===============================DEFINE DATA DIRECTORY=============================================
#Data import from local server
#Used so that data files & code are not mixed together + makes it easy to change working
#directory to where data is stored

#Set desired directory path here
desired_dir = r"/Users/delroy_m/Desktop/(CMT) Materials Characterization ELN/2. Cleaned data/Quasi_static_data"

work_dirPath = os.chdir(desired_dir) #Set the current directory to the desired working directory path

verify_cwd_path = os.getcwd()
print("CWD: " + verify_cwd_path)

##===============================Import cleaned experiment data======================================
qsf_expt_data = glob.glob('*.xlsx') # Get all files from all subfolders.
qsf_expt_data

#Define DataFrame to store quasi-static fatigue .xlsx experiment files
qsf_df = pd.DataFrame()

#Enter test (lab) environment measurements for completeness of data parsing
T_test = 21.23
RH_test = 55.7

#Pandas 'read_excel' syntax
#pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, parse_cols=None,
#                  true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None,
#                  keep_default_na=True, verbose=False, parse_dates=False, date_parser=None,
#                  thousands=None, comment=None, skip_footer=0, skipfooter=0, convert_float=True,
#                  mangle_dupe_cols=True, **kwds)

#loop to establish columns for DataFrame
for i, P in enumerate(qsf_expt_data):                                      #i: counter, P: place holder
    #print(P)
    eqsf_df = pd.read_excel(P, header=None)                                #read .xlsx experiment data
#    if i == 0:
    try:
        eqsf_df.columns = ['Force load [N]','ε,y [%]','ε,x [%]', 'σ,qs [MPa]']
    except:
        #print('Data in old format!')
        eqsf_df.columns = ['Static load [N]','ε,y [%]','ε,x [%]', 'σ,qsf [MPa]']
    file_info = P.split("_")                                  # Extract info from filename
    eqsf_df['Coupon tag'] = file_info[len(file_info)-5] + "_" + file_info[len(file_info)-4] +                             "_" + file_info[len(file_info)-3] + "_" + file_info[len(file_info)-2]
    eqsf_df['Fibre direction'] = file_info[0]
    #sample_info = file_info[len(file_info)-1].split("_")
    eqsf_df['Orientation (°)'] = file_info[1]
    eqsf_df['# of plys'] = file_info[2]
    eqsf_df['Loading'] = file_info[3]
    if file_info[3] == "T":
        eqsf_df['Loading'] = "Tension"
    else:
        eqsf_df['Loading'] = "Compression"
    qsf_df = pd.concat([eqsf_df, qsf_df])

#Label index column as 'Measurement data point'
qsf_df.index.name = 'Data point'

#View entire DataFrame
#qsf_df

#Quick view of head of DataFrame
#qsf_df.head()

#Quick view of tail-end of DataFrame
#qsf_df.tail()

#Create Qgrid query DataFrame to enable me to explore the entire contents of a DataFrame
#using intuitive sorting and filtering controls (and DataFrame won't crash like Excel!)
#
#Qgrid allows editing of the data - let's lock it so users can't accidently change the data
col_opts = { 'editable': False }
#
#col_defs = { 'Fibre-type': { 'editable': False },'Test speed [mm/min]': { 'editable': False },
#           'T (°C)': { 'editable': False }, 'RH (%)': { 'editable': False } }
qsf_qgrid_df = qgrid.show_grid(qsf_df, column_options = col_opts, show_toolbar = True) #, column_definitions=col_defs)
qsf_qgrid_df


# ### 3.4.4 Tensile and compression modulus of elasticity (ASTM E111) data import

# In[43]:


##===============================Data import for modulus calcs =====================================
#Set desired directory path here
desired_dir = r"/Users/delroy_m/Desktop/(CMT) Materials Characterization ELN/2. Cleaned data/QS_elastic_mod_data"

work_dirPath = os.chdir(desired_dir) #Set the current directory to the desired working directory path

verify_cwd_path = os.getcwd()
print("CWD: " + verify_cwd_path)

##===============================Import cleaned experiment data======================================
qsf_mod_data = glob.glob('*.xlsx') # Get all files from all subfolders.
qsf_mod_data

##===============================Data parsing========================================================
#loop to establish columns for DataFrame
for i, P in enumerate(qsf_mod_data):                                      #i: counter, P: place holder
    #print(P)
    eqsf_mod_df = pd.read_excel(P, header=None)                           #read .xlsx experiment data
#    if i == 0:
    try:
        eqsf_mod_df.columns = ['Coupon tag','Avg. Width [mm]','Avg. Thickness [mm]', 'XS Area [mm^2]',                               'σ @ 1000 με [MPa]', 'σ @ 3000 με [MPa]', 'E, chord [MPa]', 'E, chord [GPa]',                               'Loading']
    except:
        #print('Data in old format!')
        eqsf_mod_df.columns = ['Static load [N]','ε,y [%]','ε,x [%]', 'σ,qsf [MPa]']

# Use DataFrame.insert() to add a column of composite coupon descriptors
#
#Custom identifiers for coupon specimens
cols=['UD 0°, 4-Ply, Tension', 'UD 90°, 8-Ply, Tension', 'BD ±45°, 8-Ply, Tension', 'UD 45° 8-Ply, Tension',
     'UD 0°, 4-Ply, Compression', 'UD 90°, 8-Ply, Compression']
eqsf_mod_df.insert(0, 'Coupon type', cols, True)

#Label index column as 'Measurement data point'
#qsf_mod_df.index.name = 'Data point'

#View entire DataFrame
eqsf_mod_df

#Quick view of head of DataFrame
#eqsf_mod_df.head()

#Quick view of tail-end of DataFrame
#eqsf_mod_df.tail()

#Create Qgrid query DataFrame to enable me to explore the entire contents of a DataFrame
#using intuitive sorting and filtering controls (and DataFrame won't crash like Excel!)
#
#Qgrid allows editing of the data - let's lock it so users can't accidently change the data
#col_opts = { 'editable': False }
#
#col_defs = { 'Fibre-type': { 'editable': False },'Test speed [mm/min]': { 'editable': False },
#           'T (°C)': { 'editable': False }, 'RH (%)': { 'editable': False } }
#qsf_mod_df_qgrid_df = qgrid.show_grid(eqsf_mod_df, column_options = col_opts, show_toolbar = True) #, column_definitions=col_defs)
#qsf_mod_df_qgrid_df


# ## 3.5 Data reduction results - Data visualization

# ### 3.5.1 Tensile modulus of elasticity for quasi-static fatigue tests

# In[44]:


##=============================== Quasi-static fatigue tests =====================================
#                                 Elastic moduli plotting for
#                                 carbon fibre/epoxy composites
#=================================================================================================

#Custom identifiers for coupon specimens
cols =  ['UD 0° Tension', 'UD 90° Tension', 'BD ±45° Tension', 'UD 45° Tension',
         'UD 0° Compression', 'UD 90° Compression']
Tcols = ['UD 0° Tension', 'UD 90° Tension', 'BD ±45° Tension', 'UD 45° Tension']
Ccols = ['UD 0° Compression', 'UD 90° Compression']

#Plot titles
plt_title = 'Moduli of elasticity for carbon fibre/epoxy composites'
y_axis_title = 'Modulus of elasticity [MPa]'

#Filter the elastic modulus DataFrame for 'Tensile' loading experiments
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

#Filter the tensile modulus DataFrame for 'Compression' loading experiments
eqsf_Cmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Compression']

#Create data structures for plotting calculated tensile and compressive elastic moduli values
#NOTE: THIS CODE DOES NOT RUN, SEEMS TO BE A PROBLEM PASSING VARIABLE SIZED DATA STRUCTURES
#      TO PLOTLY 'GO.FIGURE' FUNCTION
data1 = [go.Bar(x = Tcols,
                y = eqsf_Tmod_df['E, chord [MPa]'],
                name = 'Tensile test'
               )]
data2 = [go.Bar(x = Ccols,
                y = eqsf_Cmod_df['E, chord [MPa]'],
                name = 'Compression test'
               )]

#Create framework for bar plot
#mod_data = [data1, data2]
mod_data = [go.Bar(x = cols,
                y = eqsf_mod_df['E, chord [MPa]'])]

#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Plot figure layout
layout = go.Layout(title='Elastic moduli of carbon fibre/epoxy test coupons',
                   font=font_pkg0,
                   hovermode='closest',
                   xaxis=dict(
                       title='Test coupons',
                       titlefont=dict(font_pkg1),
                       showticklabels=True,
                       tickangle=25,
                       tickfont=dict(font_pkg2),
                   ),
                   yaxis=dict(
                       title='Calculated modulus [MPa]',
                       titlefont=dict(font_pkg1),
                       showticklabels=True,
                       tickangle=0,
                       tickfont=dict(font_pkg2),
                       type='log',
                       autorange=False,
                       range=[0.0001,5.5],
                       showexponent = 'all', exponentformat = 'power'
                   )
                  )

#Render plot
fig = go.Figure(data=mod_data, layout=layout)
py.offline.iplot(fig, filename='qsf_elastic_modulus')


# ### 3.5.2 Quasi-static fatigue experiments - Force & strain measurement statistics data import

# In[45]:


##===============================Data import for STAT calcs import ==================================
#Set desired directory path here
desired_dir = r"/Users/delroy_m/Desktop/(CMT) Materials Characterization ELN/2. Cleaned data/STAT_data"

work_dirPath = os.chdir(desired_dir) #Set the current directory to the desired working directory path

verify_cwd_path = os.getcwd()
print("CWD: " + verify_cwd_path)

##===============================Import cleaned experiment data======================================
qsf_STAT_data = glob.glob('*.xlsx') # Get all files from all subfolders.
qsf_STAT_data

##===============================Data parsing========================================================
#loop to establish columns for DataFrame
for i, P in enumerate(qsf_STAT_data):                                      #i: counter, P: place holder
    #print(P)
    eqsf_STAT_df = pd.read_excel(P, header=None)                           #read .xlsx experiment data
#    if i == 0:
    try:
        eqsf_STAT_df.columns = ['Coupon tag','μ ± 3σ','Intervals', 'Force data',                               'φ(x) - F', 'Strain y-data', 'φ(x) - ε,y', 'Strain x-data',                               'φ(x) - ε,x']
    except:
        #print('Data in old format!')
        eqsf_STAT_df.columns = ['Static load [N]','ε,y [%]','ε,x [%]', 'σ,qsf [MPa]']

#View entire DataFrame
eqsf_STAT_df

#Quick view of head of DataFrame
#eqsf_STAT_df.head()

#Quick view of tail-end of DataFrame
#eqsf_STAT_df.tail()

#Create Qgrid query DataFrame to enable me to explore the entire contents of a DataFrame
#using intuitive sorting and filtering controls (and DataFrame won't crash like Excel!)
##
#eqsf_STAT_df_qgrid_df = qgrid.show_grid(eqsf_STAT_df, column_options = col_opts, show_toolbar = True)


# ## 3.5.3  σ-ε quasi-static fatigue analyses

# ### 3.5.3.1 - UD 0°, 4-Ply, Tension: σ-ε plot

# In[46]:


##====================Create sub-DataFrame for UD 0° CFRE Tension QSF experiment=========================

#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
UD_0_4_T_df = qsf_df[qsf_df['Coupon tag'] == 'UD_0_4_T']

#Import experimental/calculated data values
Force = UD_0_4_T_df['Force load [N]']
Stress = UD_0_4_T_df['σ,qs [MPa]']
Strain = UD_0_4_T_df['ε,y [%]']
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain = Strain.tolist()

#True Stress calculation
Stress_True = [ x * (1+y) for y,x in zip(Strain,Stress)]
#True Strain calculation
Strain_True = [math.log(1+x) for x in Strain]
##-----------------+++++++++++++++++++++++-----------------+++++++++++++++++++++++----------------


#Composite durability calculations from expt. data
#---------------------------------------------------------------------------------
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame

### in MPa
Emod_UD_0_4_T_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == 'UD_0_4_T']['E, chord [MPa]'].values[0]
### in GPa
Emod_UD_0_4_T_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == 'UD_0_4_T']['E, chord [GPa]'].values[0]

#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)

#Ultimate in-plane shear strength (S)
# S =

#E,11 calculation:






#Call plotly 'Scattergl' function and assign plot data
σvsε_UD04T = go.Scattergl(x = Strain, y = Stress, mode = 'markers',
                          marker = dict(
                              line = dict(
                                  width = 0.5, color = '#1E90FF'),size=2
                          )
                         )

#Assign to 'data' variable for plot initialization
σvsε_UD04T_data = [σvsε_UD04T]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']
E_mod_mpa = "Emod = " + "%.3f" % Emod_UD_0_4_T_MPa + " MPa\n"
E_mod_gpa = "Emod = " + "%.3f" % Emod_UD_0_4_T_GPa + " GPa\n"
UTS = "UTS = " + "%.3f" % UTS + " MPa\n"



plc_hldr_title = 'σ vs. ε - UD 0° 4-Ply Coupon, tensile loaded (in-fibre direction)'
plc_hldr_title_2 = '&sigma vs. &epsilon - UD 0° 4-Ply Coupon, tensile loaded (in-fibre direction)'

def_layout = go.Layout(title=plc_hldr_title,
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )


fig = go.Figure(data=σvsε_UD04T_data, layout=def_layout)
#py.offline.iplot(fig, filename='σvsε_UD04T_data')
pio.show(fig, filename='σvsε_UD04T_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD04T_stress_strain.svg')
# #.PDF
pio.write_image(fig, im_Path + 'UD04T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD04T_stress_strain.eps')
# #.jpeg
pio.write_image(fig, im_Path + 'UD04T_stress_strain.jpg')



# ##### UD 0° 4-Ply Coupon - Tension-loaded: Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Tensile modulus of elasticity ($E_{t}$, *ASTM D3039*): 113.088 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): GAT

# ![Image](0.Images/UD04T_stress_strain.svg)

# ### 3.5.3.2 - UD 0°, 4-Ply, Tension Coupon - Experiment statistical analyses

# In[47]:


##=============================== UD 0° 4-Ply Tension-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'UD_0_4_T'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS
ε_stat = df['Strain y-data']                   #strain statistic data
ε_prob = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std = exp_df['ε,y [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
color_map1 = [data1_paint, data2_paint]
color_map2 = [data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data1_paint),
                               size=5
                           )
                          )

#Call plotly 'Scattergl' function and plot Strain statistical data
ε_prob_plot = go.Scattergl(x = intval2, y = ε_prob, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data2_paint),
                               size=5
                           )
                          )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
ε_prob_plt_data = [ε_prob_plot]
prob_plot_data = [F_prob_plot, ε_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='UD 0° 4-Ply Coupon - Tensile force measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

def_layout_ε = go.Layout(title='UD 0° 4-Ply Coupon - Strain measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)


#Force probability distribution
fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD04T_F_prob_data')
pio.show(fig_F, filename='UD04T_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + 'UD04T_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + 'UD04T_F_prob_distn.eps')


fig_ε = go.Figure(data=ε_prob_plt_data, layout=def_layout_ε)
#py.offline.iplot(fig_ε, filename='UD04T_ε_prob_data')
pio.show(fig_ε, filename='UD04T_ε_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_ε, im_Path + 'UD04T_ε_prob_distn.svg')
pio.write_image(fig_ε, im_Path + 'UD04T_ε_prob_distn.eps')


# ##### UD 0° 4-Ply Coupon - Tension-loaded:  Experiment statistics summary

# ![Image](0.Images/UD04T_F_prob_distn.svg)
#
# ![Image](0.Images/UD04T_ε_prob_distn.svg)

# ### 3.5.3.3 - UD 90°, 8-Ply, Tension: σ-ε plot

# In[48]:


##====================Create sub-DataFrame for UD 90° CFRE Tension QSF experiment=========================

#Slice CFRE coupon quasi-fatigue loading experiment data from DataFrame
UD_90_8_T_df = qsf_df[qsf_df['Coupon tag'] == 'UD_90_8_T']

#Define DataFrame I.D. tag
df = UD_90_8_T_df

#Define coupon I.D. tag
c_tag = 'UD_90_8_T'

#Import experimental/calculated data values
Force = df['Force load [N]']
Stress = df['σ,qs [MPa]']
Strain = df['ε,y [%]']
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain = Strain.tolist()

#df_list = df['STYNAME'].tolist()

#True Stress calculation
Stress_True = [ x * (1+y) for y,x in zip(Strain,Stress)]
#True Strain calculation
Strain_True = [math.log(1+x) for x in Strain]

#Composite strength characteristics
##
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame
##
### in MPa
Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [MPa]'].values[0]
### in GPa
Emod_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [GPa]'].values[0]
##
#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)
##
#Ultimate in-plane shear strength (S)
# S =

#Call plotly 'Scattergl' function and assign plot data
σvsε = go.Scattergl(x = Strain, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = '#1E90FF'),size=2
                    )
                   )

#Assign to 'data' variable for plot initialization
σvsε_data = [σvsε]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout = go.Layout(title='σ vs. ε - UD 90° 8-Ply Coupon, tensile loaded (⟂ to fibre direction)',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

# anchored_text = AnchoredText("Tensile Modulus of Elasticity = " +"%.3f" % Emod_GPa + " GPa\n" +
#                              "UTS = "+ "%.3f" % UTS +" MPa\n"+
#                              "Failure Stress = " + "%.5f" % failure_stress +" MPa\n"+
#                              "Max Strain = "+ "%.5f" % Strain[8], loc='right')
# ax.add_artist(anchored_text)



fig = go.Figure(data=σvsε_data, layout=def_layout)
#py.offline.iplot(fig, filename='σvsε_UD908T_data')
pio.show(fig, filename='σvsε_UD908T_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD908T_stress_strain.svg')
# #.PDF
#pio.write_image(fig, im_Path + 'UD908T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD908T_stress_strain.eps')
# #.jpeg
#pio.write_image(fig, im_Path + 'UD908T_stress_strain.jpg')


# ##### UD 90° 8-Ply Coupon - Tension-loaded:  Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Tensile modulus of elasticity ($E_{t}$, *ASTM D3039*): 3.074 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): LIT

# ![Image](0.Images/UD908T_stress_strain.svg)

# ### 3.5.3.4 - UD 90°, 8-Ply, Tension Coupon - Experiment statistical analyses

# In[49]:


##=============================== UD 90° 8-Ply Tension-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'UD_90_8_T'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS
ε_stat = df['Strain y-data']                   #strain statistic data
ε_prob = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std = exp_df['ε,y [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
color_map1 = [data1_paint, data2_paint]
color_map2 = [data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data1_paint),
                               size=5
                           )
                          )

#Call plotly 'Scattergl' function and plot Strain statistical data
ε_prob_plot = go.Scattergl(x = intval2, y = ε_prob, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data2_paint),
                               size=5
                           )
                          )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
ε_prob_plt_data = [ε_prob_plot]
prob_plot_data = [F_prob_plot, ε_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='UD 90° 8-Ply Coupon - Tensile force measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

def_layout_ε = go.Layout(title='UD 90° 8-Ply Coupon - Strain measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)



fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD908T_F_prob_data')
pio.show(fig_F, filename='UD908T_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + 'UD908T_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + 'UD908T_F_prob_distn.eps')


fig_ε = go.Figure(data=ε_prob_plt_data, layout=def_layout_ε)
#py.offline.iplot(fig_ε, filename='UD908T_ε_prob_data')
pio.show(fig_ε, filename='UD908T_ε_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_ε, im_Path + 'UD908T_ε_prob_distn.svg')
pio.write_image(fig_ε, im_Path + 'UD908T_ε_prob_distn.eps')


# ##### UD 90° 8-Ply Coupon - Tension-loaded:  Experiment statistics summary

# ![Image](0.Images/UD908T_F_prob_distn.svg)
#
# ![Image](0.Images/UD908T_ε_prob_distn.svg)

# ### 3.5.3.5 - ±45°, 8-Ply, Tension: σ-ε plot

# In[50]:


##====================Create sub-DataFrame for BD ±45° CFRE Tension QSF experiment=========================

#Slice CFRE coupon quasi-fatigue loading experiment data from DataFrame
BD_pm45_8_T_df = qsf_df[qsf_df['Coupon tag'] == 'BD_±45_8_T']

#Define DataFrame I.D. tag
df = BD_pm45_8_T_df

#Define coupon I.D. tag
c_tag = 'BD_±45_8_T'        #For some unknown reason the '± symbol was interrupting the code compile'
                            #Added 'c_tag_alt' as alternative coupon I.D. term

c_tag_alt = 'BD ±45°, 8-Ply, Tension'

#Import experimental/calculated data values
Force = df['Force load [N]']
Stress = df['σ,qs [MPa]']
Strain_y = df['ε,y [%]']       #Strain in 1-direction (y-axis reference - in fibre direction)
Strain_x = df['ε,x [%]']       #Strain in 2-direction (x-axis reference - perpendicular to fibre direction)
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain_y = Strain_y.tolist()
plt_Strain_x = Strain_x.tolist()

#df_list = df['STYNAME'].tolist()

#True Stress calculation
Stress_y_True = [ x * (1+y) for y,x in zip(Strain_y,Stress)]
Stress_x_True = [ x * (1+y) for y,x in zip(Strain_x,Stress)]
#True Strain calculation
Strain_y_True = [math.log(1+x) for x in Strain_y]
Strain_x_True = [math.log(1+x) for x in Strain_x]

#Composite strength characteristics
##
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame
##
### in MPa
Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [MPa]'].values[0]
#Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon type'] == c_tag]['E, chord [MPa]'].values[0]
### in GPa
Emod_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [GPa]'].values[0]
##
#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)
##
#Ultimate in-plane shear strength (S)
# S =


#Call plotly 'Scattergl' function and assign plot data
##
#Plot stress-strain response in 1-direction (y-direction)
σvsε_y = go.Scattergl(x = Strain_y, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = '#1E90FF'),size=2
                    )
                   )

#Plot stress-strain response in 1-direction (x-direction)
σvsε_x = go.Scattergl(x = Strain_x, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = corn_flower_blue),size=2
                    )
                   )

#Assign to 'data' variable for plot initialization
σvsε_y_data = σvsε_y
σvsε_x_data = σvsε_x

plt_data_y = [σvsε_y]                    #plot  y-direction tensile σvsε
plt_data_x = [σvsε_x]                    #plot  x-direction tensile σvsε
plt_data = [σvsε_y_data, σvsε_x_data]    #plot in-fibre and perpendicular=to=fibre direction tensile σvsε

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


# # #Define y-axis tickvals
# # #y_tick_vals = [ 0.7, 1, 5, 10, 30]
# # #tickvals=y_tick_vals

#Describe plot layout for y-direction stress-strain response
def_layout_y = go.Layout(title='σ vs. ε - BD ±45° 8-Ply Coupon, y-direction tensile loading',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

#Describe plot layout for x-direction stress-strain response
def_layout_x = go.Layout(title='σ vs. ε - BD ±45° 8-Ply Coupon, x-direction tensile loading',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )


#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

# anchored_text = AnchoredText("Tensile Modulus of Elasticity = " +"%.3f" % Emod_GPa + " GPa\n" +
#                              "UTS = "+ "%.3f" % UTS +" MPa\n"+
#                              "Failure Stress = " + "%.5f" % failure_stress +" MPa\n"+
#                              "Max Strain = "+ "%.5f" % Strain[8], loc='right')
# ax.add_artist(anchored_text)



fig_y = go.Figure(data=plt_data_y, layout=def_layout_y)
#py.offline.iplot(fig_y, filename='σvsε_UD±458T_y_data')
pio.show(fig_y, filename='σvsε_UD±458T_y_data')

fig_x = go.Figure(data=plt_data_x, layout=def_layout_x)
#py.offline.iplot(fig_x, filename='σvsε_UD±458T_x_data')
pio.show(fig_x, filename='σvsε_UD±458T_x_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD±458T_stress_strain.svg')
# #.PDF
#pio.write_image(fig, im_Path + 'UD±458T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD±458T_stress_strain.eps')
# #.jpeg
#pio.write_image(fig, im_Path + 'UD±458T_stress_strain.jpg')


# ##### ±45° 8-Ply Coupon - Tension-loaded: Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Tensile modulus of elasticity ($E_{t}$, *ASTM D3039*): 12.467 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): LAT

# ![Image](0.Images/UD±458T_stress_strain.svg)

# ### 3.5.3.5 - ±45°, 8-Ply, Tension Coupon - Experiment statistical analyses

# In[51]:


##=============================== ±45° 8-Ply Tension-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'BD_±45_8_T'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS - y-direction (2-direction)
ε_stat_y = df['Strain y-data']                   #strain statistic data
ε_prob_y = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean_y = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std_y = exp_df['ε,y [%]'].std()                #st. dev of force measurement values

#Tensile strain measurements STATS - y-direction (2-direction)
ε_stat_x = df['Strain x-data']                   #strain statistic data
ε_prob_x = df['φ(x) - ε,x']                      #strain statistic probability computation
ε_mean_x = exp_df['ε,x [%]'].mean()              #mean of force measurement values
ε_std_x = exp_df['ε,x [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
data3_paint = '#6A5ACD'    #slate blue
color_map1 = [data1_paint, data2_paint, data3_paint]
color_map2 = [data3_paint, data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data1_paint),
                               size=5
                           )
                          )

#Call plotly 'Scattergl' function and plot Strain statistical data
εy_prob_plot = go.Scattergl(x = intval2, y = ε_prob_y, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data2_paint),
                               size=5
                           )
                          )

#Call plotly 'Scattergl' function and plot Strain statistical data
εx_prob_plot = go.Scattergl(x = intval2, y = ε_prob_x, mode = 'markers',
                     marker = dict(
                         line = dict(
                                   width = 0.5, color = data3_paint),
                               size=5
                           )
                          )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
εy_prob_plt_data = [εy_prob_plot]
εx_prob_plt_data = [εx_prob_plot]
prob_plot_data = [F_prob_plot, εy_prob_plot, εx_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='±45° 8-Ply Coupon - Tensile force measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

def_layout_εy = go.Layout(title='±45° 8-Ply Coupon - Strain (1-direction) measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

def_layout_εx = go.Layout(title='±45° 8-Ply Coupon - Strain (2-direction) measurement statistical probability distribution',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)



fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD908T_F_prob_data')
pio.show(fig_F, filename='±458T_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + '±458T_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + '±458T_F_prob_distn.eps')


fig_εy = go.Figure(data=εy_prob_plt_data, layout=def_layout_εy)
#py.offline.iplot(fig_εy, filename='±458T_εy_prob_data')
pio.show(fig_εy, filename='±458T_εy_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_εy, im_Path + '±458T_εy_prob_distn.svg')
pio.write_image(fig_εy, im_Path + '±458T_εy_prob_distn.eps')

fig_εx = go.Figure(data=εx_prob_plt_data, layout=def_layout_εx)
#py.offline.iplot(fig_εx, filename='±458T_εx_prob_data')
pio.show(fig_εx, filename='±458T_εx_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_εx, im_Path + '±458T_εx_prob_distn.svg')
pio.write_image(fig_εx, im_Path + '±458T_εx_prob_distn.eps')


# ##### ±45° 8-Ply Coupon - Tension-loaded:  Experiment statistics summary

# ![Image](0.Images/±458T_F_prob_distn.svg)
#
# ![Image](0.Images/±458T_εy_prob_distn.svg)
#
# ![Image](0.Images/±458T_εx_prob_distn.svg)

# ### 3.5.3.6 - UD 45°, 8-Ply, Tension: σ-ε plot

# In[52]:


##====================Create sub-DataFrame for UD 90° CFRE Tension QSF experiment=========================

#Slice CFRE coupon quasi-fatigue loading experiment data from DataFrame
UD_45_8_T_df = qsf_df[qsf_df['Coupon tag'] == 'UD_45_8_T']

#Define DataFrame I.D. tag
df = UD_45_8_T_df

#Define coupon I.D. tag
c_tag = 'UD_45_8_T'

#Import experimental/calculated data values
Force = df['Force load [N]']
Stress = df['σ,qs [MPa]']
Strain = df['ε,y [%]']
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain = Strain.tolist()

#df_list = df['STYNAME'].tolist()

#True Stress calculation
Stress_True = [ x * (1+y) for y,x in zip(Strain,Stress)]
#True Strain calculation
Strain_True = [math.log(1+x) for x in Strain]

#Composite strength characteristics
##
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame
##
### in MPa
Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [MPa]'].values[0]
### in GPa
Emod_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [GPa]'].values[0]
##
#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)
##
#Ultimate in-plane shear strength (S)
# S =

#Call plotly 'Scattergl' function and assign plot data
σvsε = go.Scattergl(x = Strain, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = '#1E90FF'),size=2
                    )
                   )

#Assign to 'data' variable for plot initialization
σvsε_data = [σvsε]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout = go.Layout(title='σ vs. ε - UD 45° 8-Ply Coupon, tensile loaded',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

# anchored_text = AnchoredText("Tensile Modulus of Elasticity = " +"%.3f" % Emod_GPa + " GPa\n" +
#                              "UTS = "+ "%.3f" % UTS +" MPa\n"+
#                              "Failure Stress = " + "%.5f" % failure_stress +" MPa\n"+
#                              "Max Strain = "+ "%.5f" % Strain[8], loc='right')
# ax.add_artist(anchored_text)



fig = go.Figure(data=σvsε_data, layout=def_layout)
#py.offline.iplot(fig, filename='σvsε_UD458T_data')
pio.show(fig, filename='σvsε_UD458T_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD458T_stress_strain.svg')
# #.PDF
#pio.write_image(fig, im_Path + 'UD458T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD458T_stress_strain.eps')
# #.jpeg
#pio.write_image(fig, im_Path + 'UD458T_stress_strain.jpg')


# ##### UD 45° 8-Ply Coupon - Tension-loaded: Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Tensile modulus of elasticity ($E_{t}$, *ASTM D3039*): 8.990 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): LIT

# ![Image](0.Images/UD458T_stress_strain.svg)

# ### 3.5.3.7 - UD 45°, 8-Ply, Tension Coupon - Experiment statistical analyses

# In[53]:


##=============================== UD 45° 8-Ply Tension-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'UD_45_8_T'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS
ε_stat = df['Strain y-data']                   #strain statistic data
ε_prob = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std = exp_df['ε,y [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
color_map1 = [data1_paint, data2_paint]
color_map2 = [data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data1_paint),
                              size=5
                          )
                         )

#Call plotly 'Scattergl' function and plot Strain statistical data
ε_prob_plot = go.Scattergl(x = intval2, y = ε_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data2_paint),
                              size=5
                          )
                         )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
ε_prob_plt_data = [ε_prob_plot]
prob_plot_data = [F_prob_plot, ε_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='UD 45° 8-Ply Coupon - Tensile force measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

def_layout_ε = go.Layout(title='UD 45° 8-Ply Coupon - Strain measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)



fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD458T_F_prob_data')
pio.show(fig_F, filename='UD458T_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + 'UD458T_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + 'UD458T_F_prob_distn.eps')


fig_ε = go.Figure(data=ε_prob_plt_data, layout=def_layout_ε)
#py.offline.iplot(fig_ε, filename='UD458T_ε_prob_data')
pio.show(fig_ε, filename='UD458T_ε_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_ε, im_Path + 'UD458T_ε_prob_distn.svg')
pio.write_image(fig_ε, im_Path + 'UD458T_ε_prob_distn.eps')


# ##### UD 45° 8-Ply Coupon - Tension-loaded:  Experiment statistics summary

# ![Image](0.Images/UD458T_F_prob_distn.svg)
#
# ![Image](0.Images/UD458T_ε_prob_distn.svg)

# ### 3.5.3.8 - UD 0°, 4-Ply, Compression: σ-ε plot

# In[54]:


##====================Create sub-DataFrame for UD 90° CFRE Tension QSF experiment=========================

#Slice CFRE coupon quasi-fatigue loading experiment data from DataFrame
UD_0_4_C_df = qsf_df[qsf_df['Coupon tag'] == 'UD_0_4_C']

#Define DataFrame I.D. tag
df = UD_0_4_C_df

#Define coupon I.D. tag
c_tag = 'UD_0_4_C'

#Import experimental/calculated data values
Force = df['Force load [N]']
Stress = df['σ,qs [MPa]']
Strain = df['ε,y [%]']
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain = Strain.tolist()

#df_list = df['STYNAME'].tolist()

#True Stress calculation
Stress_True = [ x * (1+y) for y,x in zip(Strain,Stress)]
#True Strain calculation
Strain_True = [math.log(1+x) for x in Strain]

#Composite strength characteristics
##
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame
##
### in MPa
Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [MPa]'].values[0]
### in GPa
Emod_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [GPa]'].values[0]
##
#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)
##
#Ultimate in-plane shear strength (S)
# S =

#Call plotly 'Scattergl' function and assign plot data
σvsε = go.Scattergl(x = Strain, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = '#1E90FF'),size=2
                    )
                   )

#Assign to 'data' variable for plot initialization
σvsε_data = [σvsε]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout = go.Layout(title='σ vs. ε - UD 0° 4-Ply Coupon, compression loaded',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

# anchored_text = AnchoredText("Tensile Modulus of Elasticity = " +"%.3f" % Emod_GPa + " GPa\n" +
#                              "UTS = "+ "%.3f" % UTS +" MPa\n"+
#                              "Failure Stress = " + "%.5f" % failure_stress +" MPa\n"+
#                              "Max Strain = "+ "%.5f" % Strain[8], loc='right')
# ax.add_artist(anchored_text)



fig = go.Figure(data=σvsε_data, layout=def_layout)
#py.offline.iplot(fig, filename='σvsε_UD04C_data')
pio.show(fig, filename='σvsε_UD04C_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD04C_stress_strain.svg')
# #.PDF
#pio.write_image(fig, im_Path + 'UD04T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD04C_stress_strain.eps')
# #.jpeg
#pio.write_image(fig, im_Path + 'UD04T_stress_strain.jpg')


# ##### UD 0° 4-Ply Coupon - Compression-loaded: Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Compressive modulus of elasticity ($E_{t}$, *ASTM D3039*): 99.226 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): DGM

# ![Image](0.Images/UD04C_stress_strain.svg)

# ### 3.5.3.8 - UD 0°, 4-Ply, Compression Coupon - Experiment statistical analyses

# In[55]:


##=============================== UD 0° 4-Ply Compression-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'UD_0_4_C'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS
ε_stat = df['Strain y-data']                   #strain statistic data
ε_prob = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std = exp_df['ε,y [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
color_map1 = [data1_paint, data2_paint]
color_map2 = [data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data1_paint),
                              size=5
                          )
                         )

#Call plotly 'Scattergl' function and plot Strain statistical data
ε_prob_plot = go.Scattergl(x = intval2, y = ε_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data2_paint),
                              size=5
                          )
                         )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
ε_prob_plt_data = [ε_prob_plot]
prob_plot_data = [F_prob_plot, ε_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='UD 0° 4-Ply - Compression force measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

def_layout_ε = go.Layout(title='UD 0° 4-Ply - Strain measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)



fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD04C_F_prob_data')
pio.show(fig_F, filename='UD04C_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + 'UD04C_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + 'UD04C_F_prob_distn.eps')


fig_ε = go.Figure(data=ε_prob_plt_data, layout=def_layout_ε)
#py.offline.iplot(fig_ε, filename='UD04C_ε_prob_data')
pio.show(fig_ε, filename='UD04C_ε_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_ε, im_Path + 'UD04C_ε_prob_distn.svg')
pio.write_image(fig_ε, im_Path + 'UD04C_ε_prob_distn.eps')


# ##### UD 0° 4-Ply Coupon - Compression-loaded:  Experiment statistics summary

# ![Image](0.Images/UD04C_F_prob_distn.svg)
#
# ![Image](0.Images/UD04C_ε_prob_distn.svg)

# ### 3.5.3.9 - UD 90°, 8-Ply, Compression: σ-ε plot

# In[56]:


##================Create sub-DataFrame for UD 90° CFRE Compression QSF experiment======================

#Slice CFRE coupon quasi-fatigue loading experiment data from DataFrame
UD_90_8_C_df = qsf_df[qsf_df['Coupon tag'] == 'UD_90_8_C']

#Define DataFrame I.D. tag
df = UD_90_8_C_df

#Define coupon I.D. tag
c_tag = 'UD_90_8_C'

#Import experimental/calculated data values
Force = df['Force load [N]']
Stress = df['σ,qs [MPa]']
Strain = df['ε,y [%]']
LinearLimit = 1

#NOTE: experimental data is imported as pandas DataFrame; force, stress and strain data are parsed
#      as pandas.Series arrays. These need to be converted to 'list' type data to be plotted with Matplotlib
plt_Force = Force.tolist()
plt_Stress = Stress.tolist()
plt_Strain = Strain.tolist()

#df_list = df['STYNAME'].tolist()

#True Stress calculation
Stress_True = [ x * (1+y) for y,x in zip(Strain,Stress)]
#True Strain calculation
Strain_True = [math.log(1+x) for x in Strain]

#Composite strength characteristics
##
#Extract tensile modulus of elasticity from elastic modulus calculation DataFrame
##
### in MPa
Emod_MPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [MPa]'].values[0]
### in GPa
Emod_GPa = eqsf_mod_df.loc[eqsf_mod_df['Coupon tag'] == c_tag]['E, chord [GPa]'].values[0]
##
#UTS - Ultimate tensiles strength (X,t)
UTS = max(Stress)
##
#Ultimate in-plane shear strength (S)
# S =

#Call plotly 'Scattergl' function and assign plot data
σvsε = go.Scattergl(x = Strain, y = Stress, mode = 'markers',
                    marker = dict(
                        line = dict(
                            width = 0.5, color = '#1E90FF'),size=2
                    )
                   )

#Assign to 'data' variable for plot initialization
σvsε_data = [σvsε]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout = go.Layout(title='σ vs. ε - UD 90° 8-Ply Coupon, compression loaded',
                       titlefont=font_pkg0,
                       yaxis=dict(title='Stress [MPa]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                  tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                  ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                  showexponent = 'all', exponentformat = 'power'),
                       xaxis=dict(title='Measured Strain', showgrid=True, zeroline=False, titlefont=font_pkg1,
                                  tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                  rangemode='tozero')
                      )

#Include quasi-fatigue properties of composite coupon
#
#Modulus
eqsf_Tmod_df = eqsf_mod_df[eqsf_mod_df['Loading'] == 'Tension']

# anchored_text = AnchoredText("Tensile Modulus of Elasticity = " +"%.3f" % Emod_GPa + " GPa\n" +
#                              "UTS = "+ "%.3f" % UTS +" MPa\n"+
#                              "Failure Stress = " + "%.5f" % failure_stress +" MPa\n"+
#                              "Max Strain = "+ "%.5f" % Strain[8], loc='right')
# ax.add_artist(anchored_text)



fig = go.Figure(data=σvsε_data, layout=def_layout)
#py.offline.iplot(fig, filename='σvsε_UD908C_data')
pio.show(fig, filename='σvsε_UD908C_data')

# #Save images in PDF or vector file format for publications (LaTeX)
# #
im_Path = Image_PATH
# #.SVG
pio.write_image(fig, im_Path + 'UD908C_stress_strain.svg')
# #.PDF
#pio.write_image(fig, im_Path + 'UD04T_stress_strain.pdf')
# #.EPS
pio.write_image(fig, im_Path + 'UD908C_stress_strain.eps')
# #.jpeg
#pio.write_image(fig, im_Path + 'UD04T_stress_strain.jpg')


# ##### UD 90° 8-Ply Coupon - Compression-loaded: Stress vs. Strain test summary
#
# * No. of coupons tested: 3
# * Compressive modulus of elasticity ($E_{t}$, *ASTM D3039*): 6.099 GPa
# * Test speed: 1 $\frac{mm}{min}$
# * Failure mode (*ASTM D3039*): GAT

# ![Image](0.Images/UD908C_stress_strain.svg)

# ### 3.5.3.10 - UD 90°, 8-Ply, Compression Coupon - Experiment statistical analyses

# In[57]:


##=============================== UD 90° 8-Ply Compression-loaded coupon =====================================
#                               Statistical analyses of experiment data
#
# This is a custom STAT graphics routine. The SciPy package (namely .distplot(), interfaced with plotly)
# seems to poorly handle statistical probability distributions of the σ/ε quasi-fatigue experimental
# measurement data.
#========================================================================================================

#Define composite coupon tag I.D.
c_tag = 'UD_90_8_C'

#Slice coupon tag data from experiment statistics DataFrame
df = eqsf_STAT_df[eqsf_STAT_df['Coupon tag'] == c_tag]

#Call experimental DataFrame to compute mean & st. dev values
#Slice UD 0° CFRE - 4 Ply - Tension loading experiment data from DataFrame
exp_df = qsf_df[qsf_df['Coupon tag'] == c_tag]

#Tensile force measurements STATS
F_stat = df['Force data']                      #force statistic data
F_prob = df['φ(x) - F']                        #force statistic probability computation
intval1 = df['μ ± 3σ']                         #abscissa values for plot
intval2 = df['Intervals']                      #abscissa values for plot
F_mean = exp_df['Force load [N]'].mean()       #mean of force measurement values
F_std = exp_df['Force load [N]'].std()         #st. dev of force measurement values

#Tensile strain measurements STATS
ε_stat = df['Strain y-data']                   #strain statistic data
ε_prob = df['φ(x) - ε,y']                      #strain statistic probability computation
ε_mean = exp_df['ε,y [%]'].mean()              #mean of force measurement values
ε_std = exp_df['ε,y [%]'].std()                #st. dev of force measurement values


#Standardize data colour
data1_paint = '#1E90FF'    #dodger blue
data2_paint = '#00CED1'    #dark turquoise
color_map1 = [data1_paint, data2_paint]
color_map2 = [data2_paint, data1_paint]


#Call plotly 'Scattergl' function and plot Force statistical data
F_prob_plot = go.Scattergl(x = intval2, y = F_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data1_paint),
                              size=5
                          )
                         )

#Call plotly 'Scattergl' function and plot Strain statistical data
ε_prob_plot = go.Scattergl(x = intval2, y = ε_prob, mode = 'markers',
                    marker = dict(
                        line = dict(
                                  width = 0.5, color = data2_paint),
                              size=5
                          )
                         )


#Assign to 'data' variable for plot initialization
F_prob_plt_data = [F_prob_plot]
ε_prob_plt_data = [ε_prob_plot]
prob_plot_data = [F_prob_plot, ε_prob_plot]

#Define axes title fonts
#
#Type-faces I prefer (all sans-serif): PT Sans, SF Mono, Frutiger, Amplitude, Antique Olive, Avenir, Eurostile
#                                      Optima,
#Font packages for plotting
font_pkg0=dict(family='Optima', size=22, color='black')
font_pkg1=dict(family='Optima', size=16, color='black')
font_pkg2=dict(family='Optima', size=12, color='black')


#Describe plot layout
def_layout_F = go.Layout(title='UD 90° 8-Ply - Compression force measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

def_layout_ε = go.Layout(title='UD 90° 8-Ply - Strain measurement statistical probability distribution',
                      titlefont=font_pkg0,
                      yaxis=dict(title='Probability [φ(x)]', autorange=True, showgrid=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, range=[0, len(Stress)], zeroline=False,
                                 ticks='outside', showline=True, tickwidth=2, rangemode='tozero',
                                 showexponent = 'all', exponentformat = 'power'),
                      xaxis=dict(title='Random variable', showgrid=True, zeroline=True, titlefont=font_pkg1,
                                 tickfont=font_pkg2, ticks='outside', showline=True, tickwidth=2,
                                 rangemode='tozero')
                     )

# anchored_text = AnchoredText("Force measurement mean = " +"%.3f" % F_mean + " N\n" +
#                              "Force measurement st. dev = " +"%.3f" % F_std +
#                              "Strain measurement mean = " +"%.3f" % ε_mean +
#                              "Strain measurement st. dev = " +"%.3f" % ε_std
# ax.add_artist(anchored_text)



fig_F = go.Figure(data=F_prob_plt_data, layout=def_layout_F)
#py.offline.iplot(fig_F, filename='UD908C_F_prob_data')
pio.show(fig_F, filename='UD908C_F_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_F, im_Path + 'UD908C_F_prob_distn.svg')
pio.write_image(fig_F, im_Path + 'UD908C_F_prob_distn.eps')

fig_ε = go.Figure(data=ε_prob_plt_data, layout=def_layout_ε)
#py.offline.iplot(fig_ε, filename='UD908C_ε_prob_data')
pio.show(fig_ε, filename='UD908C_ε_prob_distn')
#Write .svg and .eps plot images to repo
pio.write_image(fig_ε, im_Path + 'UD908C_ε_prob_distn.svg')
pio.write_image(fig_ε, im_Path + 'UD908C_ε_prob_distn.eps')


# ##### UD 90° 8-Ply Coupon - Compression-loaded:  Experiment statistics summary

# ![Image](0.Images/UD908C_F_prob_distn.svg)
#
# ![Image](0.Images/UD908C_ε_prob_distn.svg)
