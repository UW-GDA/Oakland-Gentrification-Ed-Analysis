# Oakland-Gentrification-Ed-Analysis
MacKenzie Gaddy, Porter Jones, Craig Dittmann

## Summary
The focus of our project is on gentrification's impact on K-12 students in Oakland, California. We hope to take polygon data stating the gentrification risk for a given area from the Urban Displacement Project and analyze various educational markers for that space (e.g. looking at student records that indicate whether the student is on track or not). Student groups of the same areas can be matched based on demographic data. If data is available, we will ideally be able to do this analysis at a few different points in time to analyze the changes over time in neighborhood gentrification impact on school achievement as well.

## Background
Gentrification is defined by the Urban Displacement Project as:
> "A process of neighborhood change that includes economic change in a historically disinvested neighborhood —by means of real estate investment and new higher-income residents moving in - as well as demographic change - not only in terms of income level, but also in terms of changes in the education level or racial make-up of residents."


The Bay Area has experienced rapid gentrification in the past decade,
with 1/3 of poor neighborhoods experiencing some form of gentrification between 2013 and 2017, the highest rate in the country.

Gentrification is difficult to measure, as there are a lot of factors that could be used to classify a neighborhood as being "gentrified" some easier to track than others. The Urban Displacement Project has produced a system for classifying neighborhoods in varying stages of gentrification, which we will use for this project.

Since gentrification is a powerful transformation of a space, we wanted to explore any trends in schools/students related to that transformation. Oakland Unified School District has some public facing datasets which we will analyze in the context of our gentrification data.


Oakland Unified School District (OUSD) is a highly diverse school district serving 35,000 students across a mosaic of campuses, including public and charter schools. The majority of the students OUSD attend “Title 1” schools and receive free and reduced lunch. 

## Questions we will explore

### PROBLEM STATEMENT



While gentrification has provided a mixed bag of outcomes, the changes have been real. Students, teachers and administrators have been forced to confront and grapple with low enrollment, budget cuts and a declining quality of education. While gentrification may bring money and resources into communities and change cities rapidly, schools have largely remained unchanged, outdated and underfunded. 

One of the major determinants of resource supply and demand is OUSD’s school choice policy. Students can theoretically apply to any school in the district, creating a fairly fluid network of choices within the district. This policy has been studied extensively and has been shown to create segregation across the district further exacerbating issues around funding and equity.

Our research will examine three different comprehensive district high schools. We chose these schools due to their gentrification categorization (Urban Displacement Project) while controlling for relative school size.


### QUESTIONS

Our research hopes to examine the relationship between three key relationships:
* 1: How has school enrollment demand changed across our study area over the last five years?
* 2: What community resources help create communities that are resilient to gentrification?
* 3: How has the increase in average home value across our study areas impacted standardized test scores (CAASPP MAth and English) across five years?

### OBJECTIVES

Create compelling geospatial visual representations of data that accurately show how our study areas have changed over time. 

Conduct statistical analysis that can give insight into how gentrification can be identified and studied.

Use a mixture of qualitative and quantitative data to contextualize and provide nuance for our analysis.

## Datasets we will use
A few datasets we may use:
* [Urban Displacement Project](https://www.urbandisplacement.org/)
* [Oakland School Locations](https://data.oaklandca.gov/Education/Map-of-Oakland-Public-Schools/trbj-7f28)
* [Oakland School Educational Data](http://www.ousddata.org/)
* [American Community Survey Data](https://www.census.gov/programs-surveys/acs/data.html)

## Tools/packages we will use
A few tools and packages we are considering using:
* [geopandas](https://geopandas.org/)
* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [matplotlib](https://matplotlib.org/stable/index.html)

## Planned methodology/approach
Below we have defined our inital steps with possible types of analyis. 

* Merge school location data w/gentrification classifications to determine what stage of gentrification schools are classified as.

* Determine a dataset of educational data that we wish to explore in the context of gentrification.
* Merge our educational dataset with the school/gentrification dataset.
* Analyze the data in an exploratory manner. This would involve making plots, calculating aggregate statistics, and maybe some other simple statistical methods for seeing if there are any interesting trends in the data.
* If an interesting trend is found, further explore that trend using more involved methods. Maybe related to linear regression, clustering, removing outliers, etc. 

* Determine the type of tests we will use for our analysis. 
- Probabliity Density Function
- Quantile Plot
- Linear Regression
- Kernal Density Estimator 
- Interactive Plot
* [Analysis Tools](https://docs.google.com/document/d/1hmbMBqoenpnPv53Zm4xFynkerhlspK5lJ_npcwF0iqY/edit?usp=sharing)



## Expected Outcomes
We do not have any strong expected outcomes at the moment.
Our objective is to approach this project with an exploratory mindset.
We will try to see if there are any interesting patterns or correlations,
but given how complicated educational environments are, we will likely not
be able to claim any causations in the scope of this project. 

We do suspect that gentrification interacts with schools and students in a variety of ways,
but we aren't sure if the data will show those interactions or necessarily what they are.

## Other Information
We are currently looking for related research on gentrification's impact on schools
and will update our outline as we find things.

## References
* [Oakland, S.F. neighborhoods fastest gentrifying in U.S.](https://www.mercurynews.com/2020/06/18/oakland-s-f-neighborhoods-fastest-gentrifying-in-u-s/)
* [Gentrification and Displacement in the San Francisco Bay Area: A Comparison of Measurement Approaches](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6616964/)
* [Urban Displacement Project: Gentrification Explained](https://www.urbandisplacement.org/gentrification-explained)
