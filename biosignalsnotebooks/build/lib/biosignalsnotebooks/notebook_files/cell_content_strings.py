"""
File with the set of strings that contain a markdown or code cell content for general application
in the notebooks.

"""

HEADER = """<table width="100%">
    <tr style="border-bottom:solid 2pt #009EE3">
        <td style="text-align:left" width="10%">
            <a href="FILENAME" download><img src="../../images/icons/download.png"></a>
        </td>
        <td style="text-align:left" width="10%">
            <a href="SOURCE" target="_blank"><img src="../../images/icons/program.png" title="Be creative and test your solutions !"></a>
        </td>
        <td></td>
        <td style="text-align:left" width="5%">
            <a href="../MainFiles/biosignalsnotebooks.ipynb"><img src="../../images/icons/home.png"></a>
        </td>
        <td style="text-align:left" width="5%">
            <a href="../MainFiles/contacts.ipynb"><img src="../../images/icons/contacts.png"></a>
        </td>
        <td style="text-align:left" width="5%">
            <a href="https://github.com/biosignalsnotebooks/biosignalsnotebooks" target="_blank"><img src="../../images/icons/github.png"></a>
        </td>
        <td style="border-left:solid 2pt #009EE3" width="15%">
            <img src="../../images/ost_logo.png">
        </td>
    </tr>
</table>"""

# FOOTER = """<hr>
# <table width="100%">
#     <tr>
#         <td style="border-right:solid 3px #009EE3" width="20%">
#             <img src="../../images/ost_logo.png">
#         </td>
#         <td width="40%" style="text-align:left">
#             <a href="https://github.com/biosignalsnotebooks/biosignalsnotebooks">&#9740; GitHub Repository</a>
#             <br>
#             <a href="../MainFiles/biosignalsnotebooks.ipynb">&#9740; Notebook Categories</a>
#             <br>
#             <a href="https://pypi.org/project/biosignalsnotebooks/">&#9740; How to install biosignalsnotebooks Python package ?</a>
#             <br>
#             <a href="../MainFiles/signal_samples.ipynb">&#9740; Signal Library</a>
#         </td>
#         <td width="40%" style="text-align:left">
#             <a href="../MainFiles/by_diff.ipynb">&#9740; Notebooks by Difficulty</a>
#             <br>
#             <a href="../MainFiles/by_signal_type.ipynb">&#9740; Notebooks by Signal Type</a>
#             <br>
#             <a href="../MainFiles/by_tag.ipynb">&#9740; Notebooks by Tag</a>
#             <br>
#             <br>
#         </td>
#     </tr>
# </table>"""

DESCRIPTION_SIGNAL_SAMPLES = """With *Plux* acquisition systems, a vast set of physiological signals can be acquired.

All the signals that were used in **<span style="color:#009EE3">biosignalsnotebooks</span>** notebooks have been collected with **bitalino** or **biosignalsplux**, being this page a resource where relevant characteristics of each acquisition are presented, together with a temporal segment of the signal."""

DESCRIPTION_GROUP_BY = """Each Notebook content is summarized in his header through a quantitative scale ('"Difficulty" between 1 and 5 stars) and some keywords (Group of "tags").

Grouping Notebooks by difficulty level, by signal type to which it applies or by tags is an extremelly important task, in order to ensure that the **<span style="color:#009EE3">biosignalsnotebooks</span>** user could navigate efficiently in this learning environment.
"""

HEADER_ALL_CATEGORIES = """<link rel="stylesheet" href="../../styles/theme_style.css">
<!--link rel="stylesheet" href="../../styles/header_style.css"-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<table width="100%">
    <tr>
        <td id="image_td" width="15%" class="header_image_color_i"><div id="image_img"
        class="header_image_i"></div></td>
        <td class="header_text"> Notebook Title </td>
    </tr>
</table>"""

HEADER_MAIN_FILES = """<link rel="stylesheet" href="../../styles/theme_style.css">
<!--link rel="stylesheet" href="../../styles/header_style.css"-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<table width="100%">
    <tr>
        <td id="image_td" width="20%" class="header_image_color_2">
            <img id="image_img" src="../../images/ost_logo.png"></td>
        <td class="header_text"> Notebook Title </td>
    </tr>
</table>"""

OPEN_IMAGE = """<link rel="stylesheet" href="../../styles/theme_style.css">
<img src="../../images/OS_logo_title_slim.png">
<div class="title"><h2 class="color11"> Available Notebooks </h2></div>"""

DESCRIPTION_CATEGORY = """<br>**<span style="color:#009EE3">biosignalsnotebooks</span>** (<a href="../MainFiles/aux_files/biosignalsnotebooks_presentation.pdf">see project presentation<img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a>) is a set of documents and a **<span class="color1">Python</span>** library to provide programming examples in the form of **<span class="color5">Jupyter Notebooks</span>**, as companion to the **<span style="color:#009EE3">OpenSignals</span>** biosignals acquisition tools.

This collection of code samples has the purpose to help users of PLUX Wireless Biosignals systems, such as **bitalino** or **biosignalsplux**, and to the researcher or student interested on recording processing and classifying biosignals. The examples are set on a level of complexity to inspire the users and programmers on how easy some tasks are and that more complex ones can also be achieved, by reusing and recreating some of the examples presented here.

A **<span class="color1">Python</span>** library (entitled **<span style="color:#009EE3">biosignalsnotebooks</span>** ) is the base toolbox to support the notebooks and to provide some useful functionalities. It can be installed through pip command, like demonstrated in a <a href="https://pypi.org/project/biosignalsnotebooks/" target="_blank">PyPI <img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a> dedicated page.

In many cases we also point and illustrate with code the usage of other python toolboxes dedicated to biosignal processing.

The notebooks will cover the full topics pipeline of working with biosignals, such as: **<span class="color1">Load</span>** a file; **<span class="color3">Visualise</span>** the data online and offline, **<span class="color4">Pre-Process</span>** a one channel signal or a multi-channel acquisition, **<span class="color5">Detect</span>** relevant events in the signals, **<span class="color6">Extract</span>** features from many different type of sensors and domains, **<span class="color7">Train and Classify</span>** among a set of classes with several machine learning approaches, **<span class="color8">Understand</span>** the obtained results with metrics and validations techniques.

These examples are carried in a multitude of biosignals , from ECG, EDA, EMG, Accelerometer, Respiration among many others.
The notebooks have a set of labels to help navigate among topics <a href="../MainFiles/by_tag.ipynb"><img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a>, types of signals <a href="../MainFiles/by_signal_type.ipynb"><img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a>, application area <a href="../MainFiles/biosignalsnotebooks.ipynb"><img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a> and complexity <a href="../MainFiles/by_diff.ipynb"><img src="../../images/icons/link.png" width="10px" height="10px" style="display:inline"></a> level to support the search for particular solutions.

We encourage you to share new example ideas, to pose questions info@plux.info, and to make improvements or suggestion to this set of notebooks.

**Be inspired on how to make the most of your biosignals!**

<br>
"""

HEADER_TAGS = """<div id="flex-container">
    <div id="diff_level" class="flex-item">
        <strong>Difficulty Level:</strong>   <span class="fa fa-star 1"></span>
                                <span class="fa fa-star 2"></span>
                                <span class="fa fa-star 3"></span>
                                <span class="fa fa-star 4"></span>
                                <span class="fa fa-star 5"></span>
    </div>
    <div id="tag" class="flex-item-tag">
        <span id="tag_list">
            <table id="tag_list_table">
                <tr>
                    <td class="shield_left">Tags</td>
                    <td class="shield_right" id="tags">tags</td>
                </tr>
            </table>
        </span>
        <!-- [OR] Visit https://img.shields.io in order to create a tag badge-->
    </div>
</div>"""

SEPARATOR = """<hr>"""

AUX_CODE_MESSAGE = """<span class="color6">**Auxiliary Code Segment (should not be replicated by
the user)**</span>"""

CSS_STYLE_CODE = """from biosignalsnotebooks.__notebook_support__ import css_style_apply
css_style_apply()"""

JS_CODE_AUTO_PLAY = """%%html
<script>
    // AUTORUN ALL CELLS ON NOTEBOOK-LOAD!
    require(
        ['base/js/namespace', 'jquery'],
        function(jupyter, $) {
            $(jupyter.events).on("kernel_ready.Kernel", function () {
                console.log("Auto-running all cells-below...");
                jupyter.actions.call('jupyter-notebook:run-all-cells-below');
                jupyter.actions.call('jupyter-notebook:save-notebook');
            });
        }
    );
</script>"""

FOOTER = """<hr>
<table width="100%">
    <tr>
        <td style="border-right:solid 3px #009EE3" width="20%">
            <img src="../../images/ost_logo.png">
        </td>
        <td width="40%" style="text-align:left">
            <a href="../MainFiles/aux_files/biosignalsnotebooks_presentation.pdf" target="_blank">&#9740; Project Presentation</a>
            <br>
            <a href="https://github.com/biosignalsnotebooks/biosignalsnotebooks" target="_blank">&#9740; GitHub Repository</a>
            <br>
            <a href="https://pypi.org/project/biosignalsnotebooks/" target="_blank">&#9740; How to install biosignalsnotebooks Python package ?</a>
            <br>
            <a href="../MainFiles/signal_samples.ipynb">&#9740; Signal Library</a>
        </td>
        <td width="40%" style="text-align:left">
            <a href="../MainFiles/biosignalsnotebooks.ipynb">&#9740; Notebook Categories</a>
            <br>
            <a href="../MainFiles/by_diff.ipynb">&#9740; Notebooks by Difficulty</a>
            <br>
            <a href="../MainFiles/by_signal_type.ipynb">&#9740; Notebooks by Signal Type</a>
            <br>
            <a href="../MainFiles/by_tag.ipynb">&#9740; Notebooks by Tag</a>
        </td>
    </tr>
</table>"""

MD_EXAMPLES = """<p class="steps">1 - Description of the first instruction</p>
<strong><span class="color1">Example of a Markdown cell (supports HTML and some LaTex syntax)</span></strong>"""

CODE_EXAMPLES = """# Code cell where Python instructions can be applied
print("Hello and Welcome to biosignalsnotebooks environment !")"""

# 07/11/2018  00h02m :)
