# P-climate
Project Name: AI for Climate Reconstruction through Proxy Data
Project Manager: Hannah Mandell, PO ’23

## ABSTRACT
### Background & Motivation 
Earth’s climate has been studied since the earliest age of humankind. Even still, this multi-factored system of geologic, hydrologic, and atmospheric interactions remains one of the most nuanced and important fields of study today – particularly in the wake of a rapidly changing climate system. 

An important factor in understanding Earth’s climatic future is understanding Earth’s climatic past. Many fields of study have developed under this one notion. For example, dendroclimatology is the science of determining past climates from the annual properties of tree rings. Similar processes can be completed by examining annual aspects of ice cores, sediment cores, and even the skeletal rings of oceanic organisms. Thanks to these processes, science has gained the famous ‘hockey stick’ diagram that allows us to see the dramatic effect of anthropogenic global warming. 

Each of these items are described as ‘proxies’ since the measured aspects of the physical, biological, or isotopic records stored in their annual markers directly relate to measurements of the climate system at the time of creation, thus providing paleo-climatologists with proxies to the temperature, salinity, precipitation, or atmospheric composition of the period without physically having to measure them. Proxies are the key to looking into Earth’s climate past. 

Many linear regression models have been scientifically developed between the markers in the proxies and physical measurements of a climate system. However, with the climate system being so notably complex and the samples often having considerate ‘noise’ in their data, it is only reasonable to explore the role of machine learning in improving these models and their subsequent climate reconstructions. 

### Project Goals & Description
The PAGES (Past Global Change) 2k consortium is one of the most comprehensive sources of information and data related to global temperature over the past couple thousand years. It pulls from a plethora of temperature proxies from many distinct sources. Using the diverse proxy datasets for temperature from PAGES this project aims to construct a temperature-focused climate reconstruction by means of Neural Network computing, a relatively novel approach. Although PAGES datasets contain different organisms and proxies, the aim of the project is to use artificial intelligence to identify an overall signal in the measurements despite the various sources of ‘noise’. 
With the input data being multiple proxy measurements all dated by time, the final output signal will be a constructed temperature time series of the previous couple hundred or thousand years.

 


The project’s neural network model will be constructed and tested extensively against existing climate reconstructions from leading scientific organizations (NOAA Extended Reconstructed Sea Surface Temperature (ErSST), NCAR Hadley Centre Global Sea Ice and Sea Surface Temperature (HadISST), NOAA Optimum Interpolation Sea Surface Temperature (OISST)) that were created using many different factors, including proxies, and are considered to be the most robust temperature reconstructions known to the scientific community. The goal of this project is to recreate similar time series but with machine learning and only temperature proxies. 

## PROJECT TIMELINE
1.	(1-2 weeks) Setup and Broad Research
a.	Install necessary programs, packages, libraries.
b.	Configure appropriate working environments.
c.	Formulate group understanding of the science of proxies and their relationship to climate reconstruction. 
d.	Describe existing paleoclimatology methods (linear regression models) and their results.
e.	Meet with existing experts in the field of climate models and paleoclimatology. 
f.	Determine group member individual strengths and goals within this project.
2.	(2-3 weeks) Narrower Research
a.	Discuss and explore the nature of a neural network. Build understanding as to why it could provide a more efficient model than existing methods.
b.	Explore different types of neural networks. 
c.	Consider the limitations of machine learning methods.
3.	(2-3 weeks) Data Processing
a.	Configure the PAGES data such that it can be put into our future model in a consistent method.
b.	Exploratory analysis of the data.
4.	(3-4 weeks) Model Development
a.	 Model selection and implementation.
5.	(1-2 weeks) Model Tweaking
a.	Time permitting. Investigate model parameters. 

## PROJECT MEMBER REQUIREMENTS
- Team member mindset.
- Working knowledge of Python or R.
 - Have at least completed a computer science or statistical programming class.
- Eagerness to learn and contribute to a rapidly growing field of environmental science.
 - Excited to be at the intersection of AI and environmental topics.
- Background in chemistry, biology, physics, or environmental science (desired, but not necessary!).

## SOURCES & INSPIRATION
Fang, M., & Li, X. (2019). An artificial neural networks‐based tree ring width proxy system \	model 
 for paleoclimate data assimilation. Journal of Advances in Modeling Earth 
 Systems, 11, 892–904. https://doi.org/10.1029/2018MS001525 

Goosse, H., Crespin, E., Montety, A. D., Mann, M. E., Renssen, H., & Timmermann, A. (2010). 
 Reconstructing surface temperature changes over the past 600 years using climate model 
 simulations with data assimilation. Journal of Geophysical Research, 115, D09108. https://doi.org/10.1029/2009JD012737 Graybill, D. A., & Idso, S. B. (1993).

Jevšenak, Jernej, and Tom Levanič. “Should Artificial Neural Networks Replace Linear Models 
 in Tree Ring Based Climate Reconstructions?” Dendrochronologia 40 (December 1, 
 2016): 102–9. https://doi.org/10.1016/j.dendro.2016.08.002.

Kadow, C., Hall, D.M. & Ulbrich, U. Artificial intelligence reconstructs missing climate 
 information. Nat. Geosci. 13, 408–413 (2020). 
 https://doiorg.ccl.idm.oclc.org/10.1038/s41561-020-0582-5 

Mannila, Heikki, Hannu Toivonen, Atte Korhola, and Heikki Ol. “Learning, Mining, or 
 Modeling? - A Case Study from Paleoecology.” Discovery Science 1532 (March 15, 1999).
 PAGESk Consortium (2017). A global multiproxy database for temperature reconstructions of 
 the common era. Scientific Data, 4, 170088. https://doi.org/10.1038/sdata.2017.88

Read “Surface Temperature Reconstructions for the Last 2,000 Years” at NAP.Edu. Accessed 
 September 1, 2021. https://doi.org/10.17226/11676.

Tahmasebi, Pejman, Serveh Kamrava, Tao Bai, and Muhammad Sahimi. “Machine Learning in 
 Geo- and Environmental Sciences: From Small to Large Scale.” Advances in Water 
 Resources 142 (August 2020): 103619. https://doi.org/10.1016/j.advwatres.2020.103619.

