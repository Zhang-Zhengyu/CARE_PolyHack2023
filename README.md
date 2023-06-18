# CARE_PolyHack2023

Project Name:
CARE(Cyberbullying Assessment and Response Engine)

Group Name:
Forward Roll

Proof of Concept

Forward Roll
Technical Implementation
•	Describe the core technical implementation of the proof of concept
CARE: Cyberbullying Assessment and Response Engine is a Social Media Violence Detection and Mental Health Care System that uses crawling tools to crawl publicly available information on social media. This information is processed by a pre-trained model and an OpenAI GPT model to detect the social media violence component. The system then provides relevant psychological advice to give mental health care to potential victims of social media violence.
•	Explain the technologies, frameworks, programming languages, or tools utilized in the development process
o	Social media crawlers: Python based scripts, the webcrawlers.py in our source code is an example of a "Zhihu" website crawler that will crawl the web for potentially violent content in questions and answers. Users can write their own crawlers to crawl other social media feeds.
o	Language violence detection and psychological care model: We pre-trained the OpenAI GPT3.5 model for violence detection by calling its API. For example, the source code contains statements with the keywords "system" and "agent". The information entered by the user is processed by the language model.
o	Framework: A local server is built using the Python based Flask backend (see app.py for details). With this backend running, the user's browser will pop up (currently only supported for Windows) to a front-end page written in HTML. The page will have a good user interface.
o	Programming Languages：Python, HTML, CSS, JavaScript
o	Tool：Anaconda
•	Provide an overview of the architecture or system design that supports the proof of concept
See our demonstration video on YouTube (https://youtu.be/a8w6ul61KLA) for more details. In this video the final system is able to determine social media violence more accurately and give psychological advice with some feasibility.
Running the Code
•	For source code: Please make sure that the Python 3 runtime environment is installed on your system. The code calls the OpenAI API Please make sure that the user has obtained the OpenAI API Key. The user can add the API Key to app.py to get support for the language model. The user can add the relevant value to openai.api_key = "sk-xxxxxxxxxxxxxxxxxxx" or to the system environment variable. Please run launcher.py with the Python 3 interpreter and the system will then pip install the necessary libraries before running app.py with the interpreter.
•	For releases: Please ensure that the Python 3 runtime environment is installed on your system. Users should also add the OpenAI API Key to app.py to get support for the language model. The user interface can then be accessed by running launcher.exe.
Sources and Claims
Alzahrani, S., Alzahrani, N., & Alzahrani, A. (2019). Cyberbullying and its influence on academic, social, and emotional development among school students in Saudi Arabia: cross-sectional study. Journal of Medical Internet Research, 21(3), e12435. 
 
Australian Human Rights Commission. (n.d.). Cyberbullying, Human rights and bystanders. Retrieved from https://humanrights.gov.au/our-work/commission-general/cyberbullying-human-rights-and-bystanders-0 
 
Chen, A., Ng, A., Xi, Y., & Hu, Y. (2022). What makes an online help-seeking message go far during the COVID-19 crisis in mainland China? A multilevel regression analysis. Digital Health, 8. https://doi.org/10.1177/20552076221085061 
 
European Parliament. (n.d.). Combating gender-based violence: Cyber violence wide range of negative impacts on individuals and society. Retrieved from https://www.europarl.europa.eu/EPRS/graphs/2021-Cyberviolence_EN.pdf  
 
Hanu, L., Thewlis, J., & Haco, S. (2021). How AI Is Learning to Identify Toxic Online Content. Scientific American. Retrieved from https://www.scientificamerican.com/article/can-ai-identify-toxic-online-content/  
 
Kim J., Lee J., Park E., & Han J. (2020). A deep learning model for detecting mental illness from user content on social media. Scientific Reports 10(1), 11846. https://doi.org/10.1038/s41598-020-68764-y 
 
Karim F., Oyewande A.A., Abdalla L.F., Ehsanullah R.C., & Khan S. (2020). Social media use and its connection to mental health: A systematic review. Cureus 12(6), e8627. https://doi.org/10.7759/cureus.8627 
 
Marr, B. (2023). How Dangerous Are ChatGPT And Natural Language Technology For Cybersecurity? Forbes. Retrieved from https://www.forbes.com/sites/bernardmarr/2023/01/25/how-dangerous-are-chatgpt-and-natural-language-technology-for-cybersecurity/ 
 
Naslund J.A., Bondre A., Torous J., & Aschbrenner K.A. (2020). Social media and mental health: Benefits, risks, and opportunities for research and practice. Journal of Technology in Behavioral Science 5(3), 245–257. https://doi.org/10.1007/s41347-020-00134-x 
 
Orben A., & Przybylski A.K. (2019). The association between adolescent well-being and digital technology use. Nature Human Behaviour 3(2), 173–182. https://doi.org/10.1038/s41562-018-0506-1 
 
Perspective API. (n.d.). Perspective API - A tool for detecting toxic comments online. https://www.perspectiveapi.com/ 
 
ReThink. (n.d.). ReThink - Stop cyberbullying before the damage is done. https://www.rethinkwords.com/ 
 
Statista. (2020). Number of social media users worldwide from 2010 to 2025. https://www.statista.com/statistics/278414/number-of-worldwide-social-network-users/ 
 
TalkLife. (n.d.). TalkLife - You’re not alone. https://talklife.co/ 
 
UNICEF. (n.d.). Cyberbullying: What is it and how to stop it. Retrieved from https://www.unicef.org/end-violence/how-to-stop-cyberbullying  
 
United Nations Office on Drugs and Crime. (n.d.). Obstacles to Cybercrime Investigations. Retrieved from https://www.unodc.org/e4j/en/cybercrime/module-5/key-issues/obstacles-to-cybercrime-investigations.html 
 
Vinney C. (2020). What is the impact of violent media on mental health? Verywell Mind. Retrieved from https://www.verywellmind.com/what-is-the-impact-of-violent-media-on-mental-health-5270512 

Testing Methodologies
Our tests are presented in our video: https://youtu.be/a8w6ul61KLA.

Limitations and Future Enhancements
•	Limitations: 
o	Scalability: Because CARE relies on text crawling and mining technology, its scalability may be limited. As the number of web users increases, CARE may require more computing resources to process large amounts of text data.
o	Performance: CARE uses natural language processing techniques to explore the help-seeking behaviour of web users, which may affect its performance. Natural language processing is a computationally intensive task that may require significant computational resources to complete quickly.
o	Known issues: CARE applies care to users who have experienced violence by calling GPT's API, but GPT does not fully understand human emotions and needs. As a result, CARE may not be able to fully meet the needs of users who have experienced violence.
•	Future Enhancements:
o	To improve scalability, consider using more advanced text crawling and mining techniques to process large amounts of data more quickly.
o	To improve performance, consider using faster natural language processing algorithms or more computational resources.
o	To solve known problems, consider developing more advanced artificial intelligence techniques to better understand human emotions and needs.
Supporting Materials:
Demonstration: https://youtu.be/a8w6ul61KLA


