# Quakers and Mental Health

http://qmh.haverford.edu/

The Quakers & Mental Health portal launched in the summer of 2015 as an interactive website to hold scholarship about the history of mental health in Philadelphia, in the 19th and 20 centuries, and in particular of Friends Hospital, the first private mental health institution in the United States. This multi-year project combines archival research and writing with digital scholarship to create and support scholarship on the history of mental health, to analyze data and create visualizations from that research. The Friends Hospital records, which are on loan to Haverford College Quaker & Special Collections, offer a wealth of information on Quakerism, the treatment of the mentally ill, and the development of American psychiatric hospitals in the 19th and 20th centuries.

This project consists of basic static pages built on Django, and uses Plotly to create interactive data visualizations.

## Local Development with Docker

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Clone the project and point Docker Desktop to the project directory.
3. Visit `http://localhost:8000` in your browser.

## Deploying

See [Deploying Docker Projects](https://github.com/HCDigitalScholarship/ds-cookbook/blob/master/docker/containerizing.md#2-deploying-the-project).

## Adding new images

In the repo, add images to this directory [/myAsylum/qmh/static/images](https://github.com/HCDigitalScholarship/qmh-v2/tree/master/myAsylum/qmh/static/images). The static image mounting does not appear to be correctly set up. This needs to be fixed in the future. In the meantime, you can manually copy the image from the upload directly to the static folder it wants to be in:

Example:
`cd /srv/qmh-v2/myAsylum/static/images`

`cp /srv/qmh-v2/myAsylum/qmh/static/images/GenderDeath.png GenderDeath.png`

## Adding New Essays

1. Upload the PDF to [this static folder](https://github.com/HCDigitalScholarship/qmh-v2/tree/master/myAsylum/static/essays) (note: there are two static folders, we don't know why. `/myAsylum/static/essays` in the correct one)* 

* - I(Mike) think it actually should go in qmh/myAsylum/qmh/static/essays, it seems that after branching from commit f05dfea, 22_Bratt.pdf was present in the qmh/myAsylum/static/essays folder, but not the qmh/myAsylum/qmh/static/essays folder, and the locally hosted site showed no pdf.  After cp-ing 22_Bratt.pdf over to the more nested essays dictionary, the site is now hosting this essay file correctly, indicating that the latter folder location is the correct one.
TLDR: use /qmh/myAsylum/qmh/static/essays/ for the location


2. Create the html template in `/myAsylum/qmh/templates/` (you can mostly duplicate an existing essay template)

* - duplicate essay_23Roark.html for reference

3. Add the page to the `views.py` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/views.py)
4. Add the page in `urls.py` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/urls.py)
5. Update the table in `essays.html` [here](https://github.com/HCDigitalScholarship/qmh-v2/blob/master/myAsylum/qmh/templates/essays.html) to include the link to your new essay page
6. Commit & merge your changes 
7. Deploy your changes to the server and restart the server (see above)
