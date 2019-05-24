
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
